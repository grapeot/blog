Title: Update on the IFTTT Delay API
Category: Computing
Date: 2016-10-30 10:00
Tags: English, Smart Home
Slug: ifttt-delay-api-update

After I released the [IFTTT delay API](/adding-a-delay-to-ifttt-recipes.html), there was some interesting discussion going on in the comments. At the same time, I also found the delay API is still too simple. It still couldn't pass any information other than the event name. And this caused troubles in the applications of "publish a Blogger post 15 minutes after I publish a Wordpress post," or "set my [iSmartAlarm mode](/smart-home-lighting-control.html) to on/off/home." To solve this problem, the API now supports passing extra POST parameters. That is, you can pass in three parameters, named Value1, Value2, Value3, in the POST body (not the capitalization). And then use them accordingly in the Maker channel.

Here is a sample implementation of how to set up the recipes to publish a Blogger post 15 minutes after ublishing a Wordpress post.

<img style="max-width: 640px" src="/images/IFTTT_Wordpress.png" / alt="IFTTT integration with WordPress for automated blogging" alt="IFTTT integration with Wordpress for automated posts">

<img style="max-width: 640px" src="/images/IFTTT_Blogger.png" / alt="A robot博主creating blog posts Automatically" alt="Person using a laptop with IFTTT and Blogger logos">

Now I can dramatically reduce the number of Maker recipes in order to automate my devices.