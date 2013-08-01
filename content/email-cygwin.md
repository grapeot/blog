Title: Sending Emails from Cygwin
Date: 2013-03-29 21:28
Category: Computing
Tags: Cygwin, Linux

Googled a lot but couldn't find tutorials about how to send emails from Windows command line. After playing with the mail tools in Cygwin, found it's pretty straightforward and put it up here for future reference.

0. Install cygwin if you don't have it. (It's handy if you are familiar with the linux toolchain!). 
1. Install exim and email. You can both search for it in the searchbox, or expand "mail" item and find them manually.
2. Run exim-config and then email-config in cygwin command line. It's very straightforward to configure. Choose SMTP server, with no authentication, no TLS in the email-config.

And that's it. Try `echo This is a test email | email -s "test" foo@bar.com` to test.
