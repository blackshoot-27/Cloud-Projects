📚 Random Quote Generator (Serverless AWS Project)
📌 Project Overview:
This project demonstrates how to build a Serverless Web Application on AWS that fetches and displays random motivational quotes using API Gateway, Lambda (Python), and S3 Static Website Hosting.

For Frontend-Refer Index.html
Backend-Refer lambda function_quote-Generator.py

Architecture Diagram
![archtiecture](https://github.com/user-attachments/assets/4825b487-fb34-40e6-b8c9-cf827e861ea5)


S3 🟠 (Frontend hosting with HTML, CSS, JS)

API Gateway 🟢 (HTTP API - Public endpoint)

Lambda 🔵 (Python function to fetch quotes from external API)

CloudWatch 🟣 (Monitoring Lambda execution and errors)

✅ Features:
Dynamically fetches random quotes from ZenQuotes API

Fully serverless architecture

CORS enabled for browser-to-API calls

Simple, responsive HTML + CSS frontend

User-friendly "Get Random Quote" button

Quotes displayed in bold, italic, with clean formatting

Logs monitored via CloudWatch


💻 Technologies Used:
Python 3.x (Lambda runtime)

HTML + CSS + JavaScript (Frontend)

AWS API Gateway (HTTP API)

S3 (Static website hosting)

External API: ZenQuotes.io




✅ How It Works:
User visits the static HTML site hosted on S3

User clicks "Get Random Quote" button

Frontend JS sends a GET request to API Gateway

API Gateway triggers the Lambda Function

Lambda calls the ZenQuotes API, extracts the quote, formats it as HTML, and returns JSON

Frontend displays the quote in the browser with bold, italic styling


✅ Deployment Steps for AWS Serverless Random Quote Generator
This section explains the exact step-by-step process I followed to build and deploy this project.

✅ Step 1: Frontend (Static Website) - AWS S3
Created an S3 bucket with Static Website Hosting enabled.

Uploaded my HTML, CSS, and JavaScript files.

Configured Bucket Policy to make it publicly readable.

Enabled Static Website Hosting and got the S3 website endpoint URL.

✅ Step 2: Backend (Serverless API) - AWS Lambda (Python)
Created a new Lambda function in Python 3.x runtime.

Wrote a Python script that:

Sends an HTTP GET request to ZenQuotes API.

Parses the JSON response.

Returns only the HTML portion (h) with additional formatting (bold/italic).

Handled CORS by adding this to Lambda response headers:




Tested Lambda from AWS Console using test event.

✅ Step 3: API Exposure - API Gateway (HTTP API)
Created a new HTTP API in API Gateway.

Integrated it with the Lambda function.

Created a GET route /getquote.

Enabled CORS for the route to allow browser calls from S3.

Deployed the API and got the public API endpoint URL.

✅ Step 4: Monitoring - AWS CloudWatch
Verified Lambda execution logs in CloudWatch Logs.

Used logs to debug failed API calls (e.g., missing permissions or syntax errors).

✅ Step 5: Connect Frontend to API
Updated the JavaScript Fetch URL in my HTML to point to the new API Gateway endpoint:


Tested clicking the "Get Random Quote" button from my S3 website.
✔️ Confirmed that the quote appears dynamically.

✅ Step 6: Final Testing
✅ Tested multiple clicks → Each click gives a new quote.

✅ Checked on desktop and mobile browsers.

✅ Verified CORS behavior and browser console for errors.


✅ Screenshots:

Forntend:Refer index.html
![Website Phto](https://github.com/user-attachments/assets/bf22f35e-7435-4230-b649-580e5b49f37b)

![Website 02](https://github.com/user-attachments/assets/4f3efb2c-b857-4326-8dad-cd2af3131d6d)

S3 Bucket:
![s3 bucket](https://github.com/user-attachments/assets/b581f0c2-5a58-48d4-a05a-b1accfdbbb4d)

Lambda:
![lambda](https://github.com/user-attachments/assets/3cc20fd0-1421-4796-9f16-6bc80d0a1d61)


Lambda Logs:

![lambda logs](https://github.com/user-attachments/assets/2cf0f81d-a32d-46ea-a23d-bf72e4c6ca53)





API Gateway:

![API Gateway-Main](https://github.com/user-attachments/assets/d5937cc3-6fc7-4216-9815-b9b0d93bef32)


![API Gateway](https://github.com/user-attachments/assets/9ec40706-dce8-440e-b1d7-feabb764ee14)


![API-Logs](https://github.com/user-attachments/assets/a55a235f-5315-4d44-b6f5-ff0a89d538dd)



API Gateway CORS:

![API Gateway CORS](https://github.com/user-attachments/assets/ecdb13a7-0039-4002-abb6-459a811b85f7)



























