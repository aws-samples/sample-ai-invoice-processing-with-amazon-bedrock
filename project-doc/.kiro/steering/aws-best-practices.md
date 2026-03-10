---
inclusion: manual
---

# AWS Best Practices

This steering file provides guidance on AWS best practices when working with AWS services.

## Security Best Practices

- Always follow the principle of least privilege when creating IAM roles and policies
- Use AWS Secrets Manager or Parameter Store for sensitive information
- Enable encryption for data at rest and in transit
- Implement multi-factor authentication (MFA) for all IAM users
- Use VPC endpoints to access AWS services without traversing the public internet

## Cost Optimization

- Use Auto Scaling to match capacity to demand
- Implement lifecycle policies for S3 objects
- Use Reserved Instances or Savings Plans for predictable workloads
- Monitor and analyze costs using AWS Cost Explorer
- Implement tagging strategy for resource allocation and cost tracking

## Reliability

- Design for failure by implementing redundancy across multiple Availability Zones
- Use health checks and auto-recovery for EC2 instances
- Implement circuit breakers and retries with exponential backoff
- Use managed services when possible to reduce operational overhead
- Implement proper monitoring and alerting using CloudWatch