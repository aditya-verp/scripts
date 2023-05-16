import boto3

ec2_resource = boto3.resource('ec2')
TAGS = [
    {
        'Key': 'tag',
        'Value': 'new'

    }
]

taginstance = ec2_resource.instances.filter(
    InstanceIds=[
        'i-00fc3611d46f8cb91','i-0a12fc8e15ef98b54','i-0b60026e2323d7cc6'
    ],
)

for instance in taginstance:
    instance.create_tags(Tags=TAGS)
    print(f'tags sucessfully added to instance {instance.id}')
    print("-----------")
