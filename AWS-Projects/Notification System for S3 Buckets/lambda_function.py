import json
import boto3

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sqs_client = boto3.client('sqs')


def lambda_handler(event, context):
    sns_topic_arn = 'arn:aws:sns:ap-south-1:637423644989:Default_CloudWatch_Alarms_Topic'

    # Define the SQS queue URL
    sqs_queue_url = 'https://sqs.ap-south-1.amazonaws.com/637423644989/simple-notification_queue'
    
    print(f"Received S3 event: {json.dumps(event)}")
    # Process S3 event records
    for record in event['Records']:

        # Extract S3 bucket and object information
        s3_bucket = record['s3']['bucket']['name']
        s3_key = record['s3']['object']['key']
        captured_event = record['eventName']
        
        # Example: Sending metadata to SQS
        metadata = {
            'bucket': s3_bucket,
            'key': s3_key,
            'timestamp': record['eventTime']
        }
        
        # Send metadata to SQS
        sqs_response = sqs_client.send_message(
            QueueUrl=sqs_queue_url,
            MessageBody=json.dumps(metadata)
        )
        
        # Example: Sending a notification to SNS
        if captured_event == 'ObjectCreated:Put':
            notification_message = f"File created in S3 bucket '{s3_bucket}' with Filename '{s3_key}'"
            sns_response = sns_client.publish(
                 TopicArn=sns_topic_arn,
                 Message=notification_message,
                 Subject="File Uploaded to S3 Bucket Notification"
            )
        elif captured_event == 'ObjectRemoved:Delete':
            notification_message = f"File deleted from S3 bucket '{s3_bucket}' with Filename '{s3_key}'"
            sns_response = sns_client.publish(
                TopicArn=sns_topic_arn,
                Message=notification_message,
                Subject="File Deleted from S3 Bucket Notification"
            )
        

    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }
