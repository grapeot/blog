Title: 能理解聊天记录的微信机器人(三)
Category: Computing
Date: 2017-03-28 9:00
Slug: wechat-bot-3
Tags: Wechat, AI, Bot

花了几个小时用Caffe撸了个最简单的斗图机器人，现在逐渐可以理解聊天的内容了。大概的思路是用随便什么网络把表情库都抽出来一个feature，然后形成一个内容数据库。如果有人在群里发图的话，抽feature，在数据库里面找最近邻，做一些简单的dedup。然后把最像的图发回去。效果意外地好。在一些不知情的群里面跟人直接斗起来了。。

<img src="/images/wechat-bot-image-understanding-1.jpg" alt="Meme fight" style="max-width: 600px">

<img src="/images/wechat-bot-image-understanding-2.png" alt="Meme fight" style="max-width: 600px">

但这个模型也有自己的缺点。一个因素是没有自己训练/fine tune，直接用的是在ImageNet上面训练的模型，所以在一些真实的照片上面表现的很好，尤其是对猫和狗认得神特码准。但在一些二次元鬼畜风的表情上就相当差了。尤其是碰到套图的时候简直惨不忍睹。。

<img src="/images/wechat-bot-image-understanding-3.png" alt="Meme fight" style="max-width: 600px">

代码已经push到github上了：[https://github.com/grapeot/WechatForwardBot](https://github.com/grapeot/WechatForwardBot)。极土。有兴趣的可以看看。