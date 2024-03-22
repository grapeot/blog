Title: Easy EC2 Sharing (While You Pay the Bill)
Category: Computing
Date: 2014-11-08 20:00
Tags: AWS, github, English

AWS is becoming more and more useful for our research, given its [ease to build clusters](https://grapeot.me/easy-and-cheap-cluster-building-on-aws.html), and the generous sponsor from [people.co](http://blog.people.co/?p=90), we are using it extensively for research.
To save cost, we definitely want to shut the machines down when they are not in use.
However, the fact that I am the "manager" who pays the bill also means only I can turn on the machine through the AWS console.

This is of course not elegant. 
And therefore we wrote a simple system managing all this.
As the following figure shows, we have a web server providing a very simple interface.
Our team members can then hit a button (after authentication) to turn on the machine.

![System framework](https://raw.githubusercontent.com/grapeot/AWSControl/master/framework.png)

What happens behind the scene is, the php accepts the request, and invokes a python script to tell AWS to turn the EC2 instance on via boto (an AWS SDK for python).
After some delay, the script also associate the EC2 instance with a pre-allocated Elastic IP. 
So that the public IP will not bounce and we can still use a single IP/domain name to log on the machine.

The code has been put on [github](https://github.com/grapeot/AWSControl). Enjoy!
