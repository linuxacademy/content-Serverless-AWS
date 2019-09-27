import boto3

def lambda_handler(event, context):
#    client = boto3.client('sns')
    
    try:
        size = event['Records'][0]['s3']['object']['size']
    except KeyError:
        pass
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    if event['Records'][0]['eventName'] == "ObjectRemoved:Delete":
        payload_str = "An object with name: " + key + " was deleted from bucket: " + bucket
    else:
        payload_str = "An object with name " + key + " and size "+ str(size) + "B was uploaded to bucket: " + bucket
   
    print(payload_str)

 #Note: You will need to have an SNS topic configured with a valid subscription to publish messages
 #to your e-mail ID to have the code below work.
 #If you are going to use SNS topic, don't forget to un-comment the boto3.client('sns') line right below the 
 #def lambda_handler line

 #   response = client.publish(
 #   TopicArn='<SNS-TOPIC-ARN>',
 #   Message= payload_str,
 #   Subject='My Lambda S3 event')
