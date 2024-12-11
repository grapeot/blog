Title: 知乎人脸的总结
Category: Life
Tags: zhihu, Image Understanding, Research, Chinese
Date: 2016-03-20 18:54

在轮带逛的领导下，知乎的秘密已经被发掘得差不多了。。但是，轮子哥毕竟还要休息，要陪AI，还有年薪百万的工作，不能24小时带领大家逛知乎。所以我们搞了一套头像带逛系统，帮助大家根据头像科学follow高质量的用户。大概地说，给定一个用户，这个系统会告诉你哪些用户和这个用户的头像长得像。那什么，种瓜得瓜，种豆得豆。比如你给它一个严肃的卡通人物，它就会告诉你这些用户可以follow：

![zhihu profile picture example](/images/zhihu-face-example-1.png)

比如你喜欢开封菜，我们有

![zhihu profile picture example](/images/zhihu-face-example-2.png)

如果你比较变态就喜欢小眼睛，可以follow这些用户：

![zhihu profile picture example](/images/zhihu-face-example-3.png)

或者就是刘看山的粉丝

![zhihu profile picture example](/images/zhihu-face-example-4.png)

当然我们也有

![zhihu profile picture example](/images/zhihu-face-example-5.png)

这样的

![zhihu profile picture example](/images/zhihu-face-example-6.png)

和这样的

![zhihu profile picture example](/images/zhihu-face-example-7.png)

哦哦哦是不是突然发现了正确的使用方法。。。呐，这是服用方法：
进入你想要看的人的页面（比如[这个](http://lab.grapeot.me/zhihu/touxiang/simpleprison.html)），就会看到她的主页链接（在页面最上方，Zhihu page那个链接）和与她头像相类似的知乎用户列表。点每个头像就再会进入那个用户的页面。如果你想看某个用户的结果，就进入`http://lab.grapeot.me/zhihu/touxiang/{用户id}.html`。其中这个id是他的主页的zhihu.com/people/后面的部分。比如我的就是grapeot。
现在只收录了8万个用户的头像，所以有的用户会没有结果。
（感觉只要选几个种子用户，再加一个[人脸检测](https://yage.ai/anime-head-detection.html)，就可以批量follow某一类别的用户了呢哦吼吼吼吼吼）
（服用前点个赞撒！）

=====================我是分割线====================

大概一周过去了，我们的知乎头像带逛系统搜集到了8万多个点击。现在带大家来看看你们点的最多的头像有哪些。。

![popular zhihu profile pictures](/images/zhihu-face-attractive-1.png)

![popular zhihu profile pictures](/images/zhihu-face-attractive-2.png)

![popular zhihu profile pictures](/images/zhihu-face-attractive-3.png)

![popular zhihu profile pictures](/images/zhihu-face-attractive-4.png)

里面的bias还是不少的。比如排名第一的头像只是因为在上篇专栏里被选为了入口点。开封菜老爷爷是因为被做了例子。还有可怜的[siyu](http://lab.grapeot.me/zhihu/touxiang/siyu-yang.html)，是因为算法被她弄挂了搜出来的全是墨镜大哥，评论中被盐酥鸡弄出来当反例以后被狂点。。但总的来说，还是能看出来知乎这群禽兽用户的兴趣的。。就是美女美女美女。（有些头像比如那个兔子我也不知道怎么进去的。。）

然后呢，这是你们喜爱的头像的平均脸：

![zhihu profile picture average face](/images/zhihu-face-average.png)

好啦，如果想follow的话，去[这个页面](http://lab.grapeot.me/zhihu/touxiang/most-popular)吧，服用前点个赞撒。

=====================我是分割线====================

我们的知乎头像浏览系统上线来已经搜集到了80余万次点击。一方面这让我们可以做一些简单的统计分析，比如这个你们最喜爱的头像，一方面也让我们可以做一些更深入的探索，比如——做一个[全自动机器人](https://yage.ai/wechat-bot.html)。通过人工智能，我们可以给一个机器人自己的审美，也就是看到一张照片能说出来它有多喜欢这张图。在这个基础上，如果这个机器人能比如一天看100万张图，就可以全天候带逛啦。

幸运的是，在十万级点击的支持下，我们已经可以做出来这样的机器人了！大概地说，我们把点击量在100以上的图给机器人看，告诉它这些是美的。然后随便找几百张男性和动物头像的图给它看，告诉它这是丑的（23333333）。最后经过适当的训练，机器人就可以独立上岗，对纷繁的知乎世界做出自己的判断啦！

机器人觉得最漂亮的头像大概长这样：

![Labeling interface](/images/zhihu-face-label.png)

下面我会给出一个链接，在界面中如果你看到美图，想要follow这个用户的时候，可以直接单击图片直达她的知乎页面。当然这个系统仍然很不完美，尤其往后拖一点的话还是会有一些奇怪的图冒出来。所以我们需要你的帮助！如果你看到自己不喜欢的图，请不要客气，用右键猛击。如果图像的外面出现了红色的外框，就说明你已经成功地把这个图标记成"丑"了。我们的算法后台会每15分钟用最新的输入更新一次模型。所以如果大家积极参与的话，（要么服务器挂掉，要么）很快就能得到非常好的结果了。

传送门：http://lab.grapeot.me/zhihu/autoface

下一步的计划是做成一个24小时全天候智能化无薪无休的带逛机器人。现在我们已经有了1000万张从知乎答案中抓取的图片，但抽取Feature还需要一定的时间。未来如果用户协议许可的话，可能做成一个机器人用户的形式，每小时自动点赞一批答案这样。还可以用类似这样的形式让大家努力调教，甚至实现根据你的口味专门点赞某一类型的图片哟。