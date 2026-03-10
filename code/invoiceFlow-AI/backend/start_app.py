#!/usr/bin/env python3
"""
InvoiceFlow AI - Application Launcher with Port Management and HTTPS
"""

# Bandit B404: subprocess import - Safe usage for launching known commands
import subprocess  # nosec B404
import sys
import os
import psutil
import time
import ipaddress
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

def create_self_signed_cert():
    """Create a self-signed certificate for HTTPS."""
    cert_dir = "ssl"
    cert_file = os.path.join(cert_dir, "cert.pem")
    key_file = os.path.join(cert_dir, "key.pem")
    
    # Check if certificates already exist
    if os.path.exists(cert_file) and os.path.exists(key_file):
        print("✅ SSL certificates already exist")
        return cert_file, key_file
    
    # Create ssl directory if it doesn't exist
    os.makedirs(cert_dir, exist_ok=True)
    
    print("🔐 Creating self-signed SSL certificate...")
    
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    
    # Create certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "InvoiceFlow AI"),
        x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
    ])
    
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).add_extension(
        x509.SubjectAlternativeName([
            x509.DNSName("localhost"),
            x509.IPAddress(ipaddress.IPv4Address("127.0.0.1")),
        ]),
        critical=False,
    ).sign(private_key, hashes.SHA256())
    
    # Write certificate to file
    with open(cert_file, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    
    # Write private key to file
    # SECURITY NOTE: Private key is stored unencrypted for local development convenience.
    # This is acceptable for:
    # - Self-signed certificates for local HTTPS
    # - Development/demo environments on localhost
    # - Non-production workloads
    # 
    # For production environments:
    # - Use proper CA-signed certificates
    # - Store private keys in AWS Secrets Manager or AWS Certificate Manager
    # - Use encryption_algorithm=serialization.BestAvailableEncryption(password)
    # 
    # The ssl/ directory is excluded from version control via .gitignore
    # 
    # nosemgrep: unencrypted-private-key
    # checkov:skip=CKV_SECRET_6:Self-signed cert for local development only
    with open(key_file, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    print(f"✅ SSL certificate created: {cert_file}")
    print(f"✅ SSL private key created: {key_file}")
    
    return cert_file, key_file

def kill_process_on_port(port=8501):
    """Kill any process using the specified port."""
    killed = False
    
    # Platform-specific port cleanup
    # NOTE: lsof is Unix-specific. This function uses psutil as fallback for cross-platform support.
    # The lsof approach is attempted first for efficiency on Unix systems.
    
    try:
        # Try lsof command (Unix/Linux/macOS only)
        # Bandit B603, B607: Safe subprocess usage with hardcoded trusted arguments
        result = subprocess.run(['lsof', '-ti', f':{port}'],  # nosec B603 B607
                              capture_output=True, text=True, check=False)
        
        if result.returncode == 0 and result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                try:
                    pid = int(pid.strip())
                    proc = psutil.Process(pid)
                    print(f"🔄 Killing process {pid} ({proc.name()}) using port {port}")
                    proc.kill()
                    proc.wait(timeout=3)
                    killed = True
                except (psutil.NoSuchProcess, psutil.AccessDenied, ValueError):
                    continue
    except FileNotFoundError:
        # lsof not available (Windows or lsof not installed)
        # Fall through to psutil-based approach below
        pass
    except Exception as e:
        print(f"⚠️  Error checking processes with lsof: {e}")
    
    # Cross-platform fallback: Use psutil to find processes by port
    # This works on Windows, Linux, and macOS
    if not killed:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'connections']):
                try:
                    for conn in proc.info['connections'] or []:
                        if conn.laddr.port == port:
                            print(f"🔄 Killing process {proc.info['pid']} ({proc.info['name']}) using port {port}")
                            proc.kill()
                            proc.wait(timeout=3)
                            killed = True
                            break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, AttributeError):
                    continue
        except Exception as e:
            print(f"⚠️  Error checking processes by port: {e}")
    
    # Additional fallback: Kill streamlit processes by name
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if 'streamlit' in proc.info['name'].lower() or \
                   any('streamlit' in arg for arg in proc.info['cmdline']):
                    print(f"🔄 Killing Streamlit process {proc.info['pid']}")
                    proc.kill()
                    proc.wait(timeout=3)
                    killed = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
    except Exception as e:
        print(f"⚠️  Error in fallback process kill: {e}")
    
    if killed:
        print("⏳ Waiting 2 seconds for port to be released...")
        time.sleep(2)
    
    return killed

def main():
    """Main launcher function."""
    print("🚀 InvoiceFlow AI - Starting Application")
    print("=" * 50)
    
    # Kill any existing processes on port 8501
    kill_process_on_port(8501)
    
    # Create SSL certificates
    cert_file, key_file = create_self_signed_cert()
    
    # Start Streamlit app with HTTPS
    print("🌟 Starting Streamlit application with HTTPS...")
    print("🔒 Access at: https://localhost:8501")
    print("⚠️  You may see a security warning - click 'Advanced' and 'Proceed to localhost'")
    
    try:
        # Bandit B603: Safe subprocess usage with trusted arguments from sys.executable
        subprocess.run([  # nosec B603
            sys.executable, "-m", "streamlit", "run", "simplified_app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--server.sslCertFile", cert_file,
            "--server.sslKeyFile", key_file
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()