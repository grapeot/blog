Title: Running ASP.NET 4.0 applications in Debian/Linux
Date: 2011-12-23 11:33
Category: Computing

### Introduction

Made some trials to migrate this server to Linux recently. The main reasons are 
1) The Ethernet adapter doesn’t have proper driver for Windows Server 2008, but there are reports saying it’ll work out of the box in Ubuntu 11.04+. (kind of weird) 
2) Windows GUI is consuming much resource, and I suspect Linux without GUI may solve this problem.

After some (actually quite a few) trails, basic conclusion is Windows is still the best place to develop/debug/deploy .NET applications. Pure CLI Linux seems still not suitable to deploy Mono applications, mainly because of lack of debugging capabilities.

But a good thing is, finally I’ve figured out how to run ASP.NET 4.0 applications in Linux environment, and gained some experiences about migrating .NET applications to Linux + Mono. Here let’s see how to do it in Debian. Other distributions should be similar, and even simpler considering we don’t have binaries for latest Mono supporting ASP.NET 4.0 in stable repository of Debian.

### nginx + FastCGI configuration

The basic idea is to use nginx + FastCGI server of Mono to build a dynamic server environment. Considering Debian stable version doesn’t have an up-to-date repository, we need to compile nginx, Mono (2.10+), and xsp from source. The compilation process is rather standard. [This post](http://extralogical.net/articles/howto-compile-nginx-passenger.html) may provide good practices. [Mono website](http://www.mono-project.com/FastCGI_Nginx) provides an example about how to configure nginx and FastCGI. But I’d suggest you to read [this article](http://www.mono-project.com/FastCGI) about basic concepts of FastCGI before making any modifications on the example. Because I wasted quite a lot of time to figure out the parameters feeding fastcgi-mono-server4.

There are also tools written by others to simplify this process. For example, [this script](https://code.google.com/p/nginx-init-ubuntu/) (for Ubuntu, but will also work in Debian with small tweaks) will grant you auto start feature of nginx directly compiled from source. And [this script](https://gist.github.com/philippkueng/1074516) provides some clues about how to use Apache and Mod_mono to establish running environment for Mono 2.10.

### Application configuration

But the problem doesn’t stop here, especially if we are trying to migrate .NET applications to Mono. One serious issue is the difference of file systems of Linux and Windows. Windows simply ignores all the letter cases in the path, while Linux doesn’t, i.e. Bin != bin in Linux. Fortunately, Mono provides a simple solution or switch [IOMap](http://www.mono-project.com/IOMap).

I did succeed in migrating some simple applications. But DotNetBlogEngine seems not that easy. I can make the homepage display normally, but clicking any link will cause a 500 internal error. Don’t know what’s going on inside because I even cannot find error logs (not the logs for nginx, but for FastCGI). For suggestions about more general migration from .NET to Mono, Novell has [a good article](http://www.novell.com/connectionmagazine/2010/02/mono_tools.html) and several useful tools.

### Windows or Linux on this server?

As mentioned before, Linux may (probably) bring better performance and more reliable network. But blog transfer is rather miserable, considering currently there are no perfect ways to transfer from DotNetBlogEngine to WordPress (preserving all the posts, comments, tags, descriptions, links, etc.) and MetaWeblogAPI cannot capture all necessary info either. BlogML may be a solution, but will still drop all the tags and cannot handle links well. And given I also need to host demos written in .NET 4.0 on this server, maybe keeping it as it is is the best solution now.
