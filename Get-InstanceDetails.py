ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    #print("Received event: " + json.dumps(event, indent=2))
    
    
    filters = [{  
        'Name': 'instance-id',
        'Values': ['i-XXXXXXXXXXXX']
    }]
    
    response = ec2.describe_instances(Filters=filters)
