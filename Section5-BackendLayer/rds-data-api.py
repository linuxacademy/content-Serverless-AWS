import boto3

rds_client = boto3.client('rds-data')
database_name = 'information_schema'
db_cluster_arn = '<DB-CLUSTER-ARN>'
db_credentials_secret = '<SECRETS-MANAGER-SECRET-ARN>'

def execute_statement(sql):
    response = rds_client.execute_statement(
            database = database_name,
            resourceArn = db_cluster_arn,
            secretArn = db_credentials_secret,
            sql = sql
            )
    return response

response = execute_statement(f'create database if not exists moosa')
#print(response['records']) Un-comment this if you're runnig a select query and expect rows
print(response)

