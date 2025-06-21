# AWS Deployment Guide for Party Planner

This guide will walk you through deploying your Party Planner app on AWS using Elastic Beanstalk.

## Prerequisites

1. **AWS Account**: You need an active AWS account
2. **AWS CLI**: Install and configure AWS CLI
3. **EB CLI**: Install Elastic Beanstalk CLI
4. **Git**: For version control

## Step 1: Install AWS CLI and EB CLI

### Install AWS CLI
```bash
# macOS (using Homebrew)
brew install awscli

# Or download from AWS website
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

### Install EB CLI
```bash
pip install awsebcli
```

### Configure AWS CLI
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter your default region (e.g., us-east-1)
# Enter your output format (json)
```

## Step 2: Prepare Your Application

Your application is already prepared with the necessary files:
- `application.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `Procfile` - Tells EB how to run the app
- `.ebextensions/01_flask.config` - EB configuration

## Step 3: Initialize Elastic Beanstalk

```bash
# Navigate to your project directory
cd /path/to/your/LinkedInParty

# Initialize EB application
eb init

# Follow the prompts:
# 1. Select your region
# 2. Create new application (enter app name: party-planner)
# 3. Select Python platform
# 4. Select Python version (3.11 or 3.12)
# 5. Set up SSH (optional)
```

## Step 4: Create Environment

```bash
# Create and deploy your environment
eb create party-planner-env

# This will:
# 1. Create an EC2 instance
# 2. Set up load balancer
# 3. Configure security groups
# 4. Deploy your application
# 5. Provide you with a URL
```

## Step 5: Deploy Your Application

```bash
# Deploy your application
eb deploy

# Or if you want to deploy and open in browser
eb deploy --open
```

## Step 6: Monitor Your Application

```bash
# Check application status
eb status

# View application logs
eb logs

# Open application in browser
eb open
```

## Alternative Deployment Methods

### Method 2: AWS Lambda + API Gateway

If you prefer serverless deployment:

1. **Install AWS SAM CLI**
```bash
# macOS
brew install aws-sam-cli
```

2. **Create SAM template** (create `template.yaml`):
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  PartyPlannerFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./
      Handler: application.app
      Runtime: python3.11
      Events:
        Api:
          Type: Api
          Properties:
            Path: /{proxy+}
            Method: ANY
```

3. **Deploy with SAM**
```bash
sam build
sam deploy --guided
```

### Method 3: AWS ECS (Docker)

1. **Create Dockerfile**:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "application:app"]
```

2. **Build and push to ECR**
```bash
aws ecr create-repository --repository-name party-planner
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
docker build -t party-planner .
docker tag party-planner:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/party-planner:latest
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/party-planner:latest
```

## Environment Variables (Optional)

You can set environment variables in the EB console or via CLI:

```bash
eb setenv SECRET_KEY=your-secret-key-here
```

## Custom Domain (Optional)

1. **Register domain in Route 53** or use existing domain
2. **Create SSL certificate** in AWS Certificate Manager
3. **Configure domain** in EB console or via CLI

```bash
eb config
# Add domain configuration
```

## Monitoring and Scaling

### Auto Scaling
```bash
# Configure auto scaling
eb config
# Set min/max instances based on your needs
```

### CloudWatch Monitoring
- Set up CloudWatch alarms
- Monitor application metrics
- Set up log aggregation

## Cost Optimization

### Free Tier
- AWS offers 12 months free tier
- 750 hours/month of t2.micro instances
- 20GB of storage

### Cost Saving Tips
1. Use t3.micro instances for development
2. Set up auto scaling to scale down during low usage
3. Use Spot Instances for non-critical workloads
4. Monitor costs in AWS Cost Explorer

## Troubleshooting

### Common Issues

1. **Deployment Fails**
```bash
eb logs
# Check for specific error messages
```

2. **Application Not Responding**
```bash
eb health
# Check application health
```

3. **Environment Issues**
```bash
eb events
# View recent events
```

### Useful Commands

```bash
# SSH into your instance
eb ssh

# View environment info
eb info

# List all environments
eb list

# Terminate environment
eb terminate party-planner-env

# Clone environment
eb clone party-planner-env --clone_name party-planner-env-2
```

## Security Best Practices

1. **Use IAM roles** instead of access keys
2. **Enable VPC** for network isolation
3. **Set up security groups** to restrict access
4. **Use HTTPS** for all communications
5. **Regular security updates**

## Backup and Recovery

1. **Database backups** (if using RDS)
2. **Application backups** (version control)
3. **Configuration backups** (EB configuration)
4. **Disaster recovery plan**

## Performance Optimization

1. **Enable CloudFront** for static content
2. **Use RDS** for database (if needed)
3. **Implement caching** (Redis/ElastiCache)
4. **Optimize application code**

## Maintenance

### Regular Tasks
1. **Update dependencies** monthly
2. **Monitor costs** weekly
3. **Review logs** for issues
4. **Update SSL certificates** before expiry

### Updates
```bash
# Update application
git add .
git commit -m "Update application"
eb deploy

# Update environment
eb upgrade
```

## Support

- **AWS Documentation**: https://docs.aws.amazon.com/elasticbeanstalk/
- **AWS Support**: Available with paid plans
- **Community Forums**: AWS Developer Forums
- **Stack Overflow**: Tag with aws-elasticbeanstalk

## Estimated Costs

### Small Application (t3.micro)
- **EC2**: ~$8-15/month
- **Load Balancer**: ~$18/month
- **Storage**: ~$1-5/month
- **Data Transfer**: ~$1-10/month
- **Total**: ~$30-50/month

### Free Tier
- **First 12 months**: Free (with limitations)
- **After free tier**: ~$30-50/month

## Next Steps

1. **Set up monitoring** with CloudWatch
2. **Configure custom domain**
3. **Set up CI/CD pipeline**
4. **Implement backup strategy**
5. **Plan for scaling**

Your Party Planner app is now ready for production deployment on AWS! 🚀 