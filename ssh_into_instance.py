from fabric import Connection
from subprocess import run
#Connect to the instance using the keypair
c = Connection(
    'ubuntu@23.22.12.129:22', 
    connect_kwargs={
        'key_filename': '/Users/dteimuno/Desktop/keypairforluitccp3.pem'
        },
        )
#Ensure local key is accessible
run(['chmod', '400', '/Users/dteimuno/Desktop/keypairforluitccp3.pem'])
#Transfer the script to the instance
c.put('./apache.sh', '/home/ubuntu/apache.sh')
#Make script executable
c.run('chmod +x /home/ubuntu/apache.sh')
#Run the script on the instance
c.run('sudo /home/ubuntu/apache.sh')