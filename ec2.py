#!/usr/bin/python  
# Python program to start, stop and check the status of an ec2 instance
import getopt, sys
import boto3
instances = ['i-07643a80fab9a2bef']
  
ec2 = boto3.client('ec2',
                   'ap-south-1',
                   aws_access_key_id='AKIAZRFVU***********',
                   aws_secret_access_key='u7OXfw5CE****************')
try:
	# Parsing argument
	arguments, values = getopt.getopt(sys.argv[1:], "s:", ["Res="])
	
	# checking each argument
	for currentArgument, currentValue in arguments:

		if currentValue == "start":
			result = ec2.start_instances(InstanceIds=instances)
		elif currentValue == "stop":
			result = ec2.stop_instances(InstanceIds=instances)
		elif currentValue == 'status':
			result = ec2.start_instances(InstanceIds=instances)
		else:
			exit ("Pass arguments as start/stop/status")
		print (result)
			
except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
