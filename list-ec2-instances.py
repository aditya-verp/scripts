import boto3

ec2_resource = boto3.resource('ec2')
getinstances = ec2_resource.instances.filter(
Filters=[
    {
        'Name': 'instance-state-name',
         'Values': [
            'stopped'
            ]
    },
    {
        'Name': 'tag:ec2',
        'Values': [
            'prod'
        ]
    },
]
)
#print several parameter of EC2

for instance in getinstances:
    print(f'EC2 instance : {instance.id}')
    print(f'Instance state : {instance.state["Name"]}')
    print(f'instance AMI : {instance.image.id}')
    print(f'instance Platform: {instance.platform}')
    print(f'Instance type: {instance.instance_type}')
    print(f'Private ip : {instance.private_ip_address}')
    print("--------------------------")
