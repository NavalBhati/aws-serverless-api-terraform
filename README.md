# aws-serverless-api-terraform
Serverless REST API using AWS Lambda, API Gateway &amp; DynamoDB managed by Terraform
# 🚀 Serverless REST API using AWS Lambda, API Gateway & DynamoDB (Terraform)
This project deploys a **serverless REST API** using:
- **AWS API Gateway** (Public API)
- **AWS Lambda** (Python Backend)
- **AWS DynamoDB** (NoSQL Database)
- **Terraform** (Infrastructure as Code)

- 🟢 Architecture Diagram
- ![Architecture](docs/screenshots/architecture.png)

- 🟢 Technologies Used
- - Terraform
- AWS Lambda
- AWS API Gateway
- AWS DynamoDB
- Python

- 🟢 How to Deploy
- ### Prerequisites
- Install **Terraform**
- Configure **AWS CLI** (`aws configure`)

### Deploy with Terraform
```sh
terraform init
terraform apply -auto-approve

### **🟢 API Testing**
```md
### Create a User (POST Request)
```sh
curl -X POST "<API-URL>/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com"}'

### **🟢 Clean Up Resources**
```sh
terraform destroy -auto-approve
