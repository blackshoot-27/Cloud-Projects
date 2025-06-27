# 📢 AWS S3 Event-Driven Notification System (Lambda + SNS + SQS)

This project demonstrates a **serverless, event-driven architecture on AWS**, where **S3 object events (upload and delete)** trigger a **Lambda function**, which then sends **notifications via Amazon SNS (Email)** and **messages to an Amazon SQS queue**.

---

## ✅ Architecture Diagram:
![Notification system](https://github.com/user-attachments/assets/d626aca2-659f-482f-b2b6-16715cdef7c8)

Amazon S3 → AWS Lambda → SNS (Email Notification)
→ SQS (Message Queue)

Bucket:
![image](https://github.com/user-attachments/assets/71ac394a-7843-4137-bb6a-b8c6a7ed063b)

Lambda-Assigned Role:
![image](https://github.com/user-attachments/assets/cec5f6ce-592f-40b5-b391-67c71ad69e11)


Lambda Function:
![image](https://github.com/user-attachments/assets/28272c00-1542-46ef-80a6-451a768297e6)

SQS Function:

![image](https://github.com/user-attachments/assets/2eb2e721-f864-4b81-9c41-a7daa9f0e49e)

Email Notification:Received
![image](https://github.com/user-attachments/assets/e1182369-703a-4926-a971-84701b5d77c3)

![image](https://github.com/user-attachments/assets/d38c5d38-691a-42ac-b946-40c24a701d24)


## ✅ AWS Services Used:

- **Amazon S3:**  
Triggers events on file creation (PUT) and deletion.

- **AWS Lambda:**  
Event handler written in Python (Boto3). It processes S3 event payloads and triggers notifications.

- **Amazon SNS (Simple Notification Service):**  
Sends email notifications for upload and delete events.

- **Amazon SQS (Simple Queue Service):**  
Receives event metadata messages for later downstream processing.

---

## ✅ Features:

- Detects **file uploads** and **file deletions** in S3
- Sends **email alerts** for each event
- Pushes **structured metadata** (bucket, key, timestamp, event type) into SQS queue
- Fully **event-driven**, **serverless**, and **scalable**


## ✅ Deployment Steps:

1. **Create an S3 bucket** and enable event notifications for PUT and DELETE.
2. **Deploy a Lambda function** using the provided Python code.
3. **Attach necessary IAM roles**:
   - AWSLambdaBasicExecutionRole
   - SNS and SQS full access (or scoped permissions)
4. **Create an SNS topic** and **subscribe your email address**.
5. **Create an SQS queue** and get the queue URL.
6. **Update Lambda environment variables or hard-coded ARNs/URLs** for SNS topic and SQS queue.
7. **Test by uploading and deleting files in S3**.


Lambda.py is available:





