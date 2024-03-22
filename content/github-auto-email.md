Title: Automatic Email Notification on Github Pushes 
Date: 2013-09-24 17:28
Category: Computing
Tags: github, Linux, English

It would be sweet if we can get auto email notifications whenever someone pushes to our github project.
Unfortunately, the default email service hook of github only supports 2 email addresses at most. 
Although putting everyone into a mailing list is one solution, for small teams like us, it's also convenient to get a quick php script to do this.

The underlying process is, github provides a post-receiving [web hook](https://help.github.com/articles/post-receive-hooks). 
Whenever it receives a push, a URL specified by the user will be hit with a JSON payload about the details.
We then get a php script parsing the payload and send out the summary emails.

[Example code](https://gist.github.com/grapeot/6692145)

Note `mail()` function in php may need extra setup.
Check [here](http://grapeot.me/sending-emails-from-cygwin.html) for a brief introduction about the configuration.  
Of course this can be used to do more such as blog deployment.
[Stephen Zhang](https://github.com/StephenPCG) got his blog deployed [this way](https://github.com/StephenPCG/onebitbug.me/blob/master/cgi-bin/update.cgi).
