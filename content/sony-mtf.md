Title: 关于Sony虚标MTF的一些疑问
Date: 2020-01-18 21:30
Category: Life
Tags: Photography, MTF, Chinese
Slug: sony-mtf

最近出了一个Sony镜头，想起来查查sony一些镜头的MTF，直接吓尿了。。画风都是这样的。。这个是135/1.8 @ f/8:  

![135 1.8 MTF claimed](/images/sony-mtf-135-1.8-f8.jpg)

大哥，你的线呢？都和天花板重合在一起了。。其他厂商还怎么活啊。。然后这个是90/2.8:

![90 2.8 MTF claimed](/images/sony-mtf-90-2.8.png)

注意里面红线是f/8，绿线是f/2.8。粗线是10 lp/mm，细线是30 lp/mm。都太夸张了。。就算在最大光圈下，画面边缘，30线的反差也有70%，一代神头啊！

然后我又查了一下我的残幅50/1.8，200美元买的狗头。雾草，红色f/8的MTF也是天花板啊。。

![50 1.8 MTF claimed](/images/sony-mtf-50-1.8.png)

然后就觉得。。哪里不对。。总不能从牛头到狗头，什么镜头的MTF都这么完美吧。。在搜索的过程中发现了一个网站，是镜头租赁网站lensrental开的。他们会测试自家有的这个型号的镜头，然后把平均的MTF贴出来。看了一下他们测出来[Sony 90/2.8在最大光圈下的MTF](https://www.the-digital-picture.com/Reviews/MTF.aspx?Lens=1019&FLI=0&LensComp=0&FLIComp=0)，怎么感觉。。哪里不对啊。。

![90 2.8 MTF measured](/images/sony-mtf-90-2.8-measured.png)

这里我们要看的是左边Sony的MTF下面的两条绿线，和右边实测出来的两条绿线。这样看太麻烦了，我把实测的图只留下绿色，然后把sony的图左右倒过来拼在一起，这样好比较一些：

![90 2.8 MTF comparison](/images/sony-mtf-90-2.8-comparison.jpg)

理想的情况下，我们应该看到完全对称的两条绿线。但这。。差的有点远啊。准确的说是Sony的标称值比实测值高了很多。那会不会是这个网站测量有问题？我们看一下其他品牌，比如Zeiss的55/1.4好了。注意因为蔡司标注的是40lp/mm，我们这里只留下了蓝色的线。这里要和左边最下面的两条线比较：

![Zeiss 55 1.4 MTF comparison](/images/sony-mtf-zeiss-55-1.4-comparison.jpg)

没有任何问题啊！那会不会德系日系品牌测量MTF的方法不一样，这个网站用的是德国的方法而不是日本的方法？那我们来看看佳能的：

![Canon 85 1.2 MTF comparison](/images/sony-mtf-canon-85-1.2-comparison.jpg)

这里要看左边下面的那条线和右边绿色的那条线。可以看到实测的MTF比佳能标称的还高一些。尼康的数据也有类似的观察，吻合得很好。看来也不是品牌的关系。。这时候我突然想起来上面的三个Sony的头其实都是sony自己的，不是索蔡的。那索蔡会如何呢？我看了一下55/1.8 ZA，发现和Sony自己的镜头有很大的区别。一个是标注的是10/20/40 lp/mm，而不是10/30 lp/mm，一个是实测值也和标称值吻合。看来索蔡的MTF是蔡司提供的。

所以基本结论就是，这个测量MTF的网站看起来是可以信赖的，蔡司等德厂和大多数日厂比如佳能尼康的MTF也是可以信赖的，索蔡是可以信赖的，但sony自己设计的头的MTF不能盲信，还是要看第三方评测。