import boto3

ssm = boto3.client('ssm', region_name="us-east-2")
parameter = ssm.get_parameter(Name="UserName")
paramValue = parameter['Parameter']['Value']

s3 = boto3.client("s3")
response = s3.put_object(
    Body=paramValue,
    Bucket="dxc-bucket-atreya",
    Key=paramValue

)
print(response)