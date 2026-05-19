# InvoiceFlow AI — Textract vs LLM Setup Guide (Windows)

This guide walks you through setting up and running the Invoice Extraction Comparison tool on a Windows machine.

## Prerequisites

- Windows 10/11
- Internet connection
- An AWS account (burner/sandbox account is fine)

---

## Step 1: Install Required Software

### Python 3.10+

1. Open https://www.python.org/downloads/
2. Download the latest Python 3.x installer
3. **Important**: Check ✅ "Add Python to PATH" during installation
4. Verify in PowerShell:
   ```powershell
   python --version
   ```

### AWS CLI

1. Open https://aws.amazon.com/cli/
2. Download and run the Windows MSI installer
3. Verify in PowerShell:
   ```powershell
   aws --version
   ```

### Git

1. Open https://git-scm.com/download/win
2. Download and install (use default options)
3. Verify in PowerShell:
   ```powershell
   git --version
   ```

---

## Step 2: Create an AWS IAM User

1. Sign in to your AWS account at https://console.aws.amazon.com
2. Go to **IAM** → **Users** → **Create user**
3. User name: `invoiceflow-user`
4. Click **Next**
5. Select **Attach policies directly**
6. Search and attach these two policies:
   - `AmazonTextractFullAccess`
   - `AmazonBedrockFullAccess`
7. Click **Next** → **Create user**
8. Click on the newly created user → **Security credentials** tab
9. Under **Access keys**, click **Create access key**
10. Select **Command Line Interface (CLI)**
11. Check the confirmation box → **Next** → **Create access key**
12. **Copy the Access Key ID and Secret Access Key** (you won't see the secret again)

---

## Step 3: Configure AWS Credentials

Open **PowerShell** and run:

```powershell
aws configure
```

Enter the following when prompted:

| Prompt | Value |
|--------|-------|
| AWS Access Key ID | *(paste your access key from Step 2)* |
| AWS Secret Access Key | *(paste your secret key from Step 2)* |
| Default region name | `us-east-1` |
| Default output format | `json` |

Verify it works:

```powershell
aws sts get-caller-identity
```

You should see your account number and user ARN.

---

## Step 4: Clone the Repository

```powershell
git clone -b feat/textract-llm-comparison https://github.com/aws-samples/sample-ai-invoice-processing-with-amazon-bedrock.git
cd sample-ai-invoice-processing-with-amazon-bedrock
```

---

## Step 5: Run the Application

If this is your first time running PowerShell scripts, allow script execution:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then launch:

```powershell
.\run.ps1
```

The script will automatically:
- Create a Python virtual environment
- Install all dependencies
- Start the application

Once you see `Open: http://localhost:8501`, open that URL in your browser.

---

## Step 6: Use the Application

1. **Select a model** from the dropdown (Claude Sonnet 4.6 or Opus 4.5)
2. **Upload an invoice PDF** — sample invoices are in the `docs\` folder:
   - `Sample_Invoice_CloudNova_CN-INV-2026-0042.pdf` (US layout)
   - `Sample_Invoice_Meridian_MDS-2026-1187.pdf` (Indian layout)
3. Click **🚀 Extract & Compare**
4. View the side-by-side comparison of Textract vs LLM extraction

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `python` not recognized | Reinstall Python with "Add to PATH" checked |
| `aws` not recognized | Restart PowerShell after installing AWS CLI |
| "ExpiredToken" error | Re-run `aws configure` with fresh credentials |
| Script execution blocked | Run the `Set-ExecutionPolicy` command from Step 5 |
| Port 8501 already in use | Close other Streamlit apps or change PORT in run.ps1 |

---

## Stopping the Application

Press `Ctrl+C` in the PowerShell window where the app is running.

---

## Cost Estimate

Per invoice processed:
- Textract AnalyzeExpense: ~$0.01
- Bedrock LLM call: ~$0.01–0.03

Total: **~$0.02–0.04 per invoice** (negligible for testing).
