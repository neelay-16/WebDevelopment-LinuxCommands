#!/usr/bin/python3
import subprocess
import cgi
import boto3
print("content-type: text/html")
print()
AWS_SECRET_KEY="wjaapbt3lkLs4/UHVCn/Wy3Lph/RtSTF2By7vDI7"
AWS_ACCESS_KEY="AKIATXKPLAMCGIVSCIPN"
data=cgi.FieldStorage()
cmd=data.getvalue("c")
if "docker ps" in cmd:
        data1=subprocess.getoutput("sudo docker ps")
        output=data1.split("\n")
        for i in output[1:]:
                x=i.split()
                container_id=x[0]
                image_name=x[1]
                container_name=x[-1]
                print("Container ID: "+container_id+" image_name: "+image_name+ "  Container Name: "+container_name)
                print("\n")
elif "date" in cmd:
        data1=subprocess.getoutput("date")
        print(data1)
elif "cal" in cmd:
        data1=subprocess.getoutput("cal")
        print(data1)
elif "ls" in cmd:
        data1=subprocess.getoutput("ls")
        print(data1)
elif "pwd" in cmd:
        data1=subprocess.getoutput("pwd")
        print(data1)
elif "docker images" in cmd:
        data1=subprocess.getoutput("sudo docker images ")
        output=data1.split("\n")
        for i in output[1:]:
                x=i.split()
                REPOSITORY=x[0]
                image_Id=x[2]
                size=x[-1]
                print("Image ID: "+image_Id+" Repository: "+REPOSITORY+ "  Size: "+size)
                print("\n")
elif "aws ec2 launch" in cmd:
        myec2 = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
        response=ec2.run_instances( 
                ImageId='ami-0ded8326293d3201b', 
                InstanceType='t2.micro',
                MaxCount=1,
                MinCount=1)
        print(response)
else :
    data1=subprocess.getoutput("sudo "+cmd)
    print(data1)
