Title: Install DotNetBlogEngine 1.6 on Debian
Date: 2011-12-06 11:06
Category: Computing
Tags: English, Linux, Tutorial
Slug: install-dotnetblogengine-on-debian
Summary: Step-by-step guide to installing DotNetBlogEngine 1.6 on Debian Linux using Apache, Mono, and mod-mono, with notes on version compatibility limitations.

The motivation is, I am trying to move this blog to a linux machine. Anyway, in my old server, Windows Server 2008 is rather slow.
 
The procedures are very simple:
 
1. Install `apache2`, `mono-complete, `and [`libapache2-mod-mono`](http://www.google.com/url?q=http%3A%2F%2Fwww.mono-project.com%2FMod_mono&sa=D&sntz=1&usg=AFQjCNGgO_s-plXvnNr22ff5S1eWgj2vfw).
2. Download [DotNetBlogEngine](http://www.google.com/url?q=http%3A%2F%2Fblogengine.codeplex.com%2Freleases%2Fview%2F39387&sa=D&sntz=1&usg=AFQjCNGKad2J1zk1tOcD12PVVftedFmtjA) 1.6 zip file, extract it, and then copy files into `/var/www/blog` or whatever you like.
Change privilege of `App_Data` into `777`.
3. Generate config file from Mono's [auto config](http://www.google.com/url?q=http%3A%2F%2Fgo-mono.com%2Fconfig-mod-mono%2F&sa=D&sntz=1&usg=AFQjCNFA6wPgSErZjdsXomlaq7cLnZ_uwA) generator.
 Put the generated file in `/etc/apache2/conf.d`.
4. Restart `apache2`.
 
That's it.
Note wget/curl may not get the download file properly from codeplex, therefore downloading the DotNetBlogEngine file elsewhere and then upload it with sftp may be a good solution for machines without GUI.
 
Why not using newer version like 2.0 and 2.5?
Because I haven't figured out how to solve some problems for these versions.
For 2.0, there is an issue reported in [this post](http://blogengine.codeplex.com/workitem/12077), and 2.5 is targeting at ASP.NET 4.0, which Mono doesn't support yet.
There may be solutions, but currently I don't know how.
Seems 1.6 is the version easiest to port to linux.
Fortunately this blog is 1.6. :)
 
Next step of the plan is, to config, deploy and test the overall blog environment in a linux virtual machine.
If it's stable enough, I'll install linux on my server, and use VirtualBox to host the tested virtual image, which avoids reconfiguration, saves time, and makes future deployment more flexible.
 
P.S. But Mono doesn't support ASP.NET 4.0 is really a problem.
I may still need the server to host some demos written in ASP.NET 4.0... 
Need to figure it out. See more discussion in [this post](/running-aspnet-40-applications-in-debianlinux.html).