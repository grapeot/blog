Title: 用Leica 50AA实现200nm/像素的分辨率
Date: 2020-08-03 20:15
Category: Life
Tags: Photography, Chinese
Slug: cmos-pixel-macro

昨天晚上突发奇想，我们一直用CMOS拍照，却没有真的拍出来像素过。有没有可能用相机来拍相机，看看像素到底长什么样呢？

但这不是一件容易的事情。因为就算用1:1的微距，假设两边像素大小一样的话，一个像素对应一个像素，看起来就是一片灰。根据奈奎斯特采样定律，什么都看不见。即使我们用2:1的微距，想象一下也很难看到一个个的像素。因为在4个像素中表示一个框框实在是太难了。不过我手头的微距头也只有Rodenstock Apo-Macro-Sinonar 125mm了。这个头是针对1:5 ~ 2:1的微距范围优化的。一方面超越2:1的范围会让它画质崩坏，一方面我的机身的皮腔也不够长，所以就先用这个配置拍一下吧。效果如图：

![Macro from medium format digital back](/images/cmos-pixel-iq180-raw.jpg)

其实效果已经不错了，可以看到周围集成电路的一些细节。但是像素跟我们之前想象的一样，还是看不见的。但我其实选的困难模式，用来拍摄的cmos的像素是比相机的cmos要小的。那我们开一下摇摇乐试试看：

![Macro from medium format digital back with high rest](/images/cmos-pixel-iq180.jpg)

可以看到分辨率的确有肉眼可感的提升。然鹅受到光学放大倍率的限制，像素还是不可见。

那有没有可能扩大光学放大倍率呢？继续延长皮腔根据之前的解释，是不现实的了。除此之外有几个思路。一个是[使用显微物镜](/microscope-objective-photography.html)。但这种方法的问题在于显微物镜的工作距离（物距）一般特别小，而CMOS往往又是凹在卡口里面的。所以此时打光就会特别困难。另一个思路就是[镜头反接](/reverse-lens-extreme-macro.html)了。这个思路相对靠谱，但上次用的72mm的镜头，一方面焦距略微有点长，就算皮腔拉满也只有4~5倍的放大倍率；一方面也有点担心画质不够好。毕竟这种极端微距的情况下，光圈f值会非常诡异。比如5倍的放大倍率下，即使把镜头的光圈开满开到5.6，实际上的光圈值也只有5x5.6=28。此时其实衍射的干扰已经相当明显了，更别提中大画幅的镜头一般要缩一两档才能用。所以这条路看起来也不太可行。

正在我纠结的时候，突然反应过来，其实用全幅镜头也是可以的。之前一直想着用中幅是因为想用中幅的数码后背，这样就思维定式想要用中幅或者大画幅的镜头。但其实反接的情况下，画幅根本不是个问题——此时光路完全反了，画幅限制的是拍摄范围的大小而不是传感器的大小。当然这样也有局限性，就是因为全幅的镜头没有镜间快门，我的后背又没有电子快门，就没办法用中幅后背，只能用全幅相机。但全幅相机的像素比中幅更大，就从困难模式进入地狱模式了。

没办法，硬着头皮上吧。打印一个镜头板，把50AA反接：

![Equipment 1](/images/cmos-pixel-equip1.jpg)

皮腔拉满，直接干到7倍的放大倍率。光圈开满，到f/2。此时相机看到的光圈其实是f/14。没办法，只能这么弄了。后面加上之前打印的[645D中幅相机](/lower-end-phase-one-xt-1.html)的背板

![Equipment 2](/images/cmos-pixel-equip2.jpg)

![Equipment 3](/images/cmos-pixel-equip3.jpg)

加上补光灯，光强调到最大，外接一个充电宝保证供电，开搞。就在这种情况下，单帧还需要5s曝光时间。继续摇摇乐以后得到了这样的图像：

![Macro from Leica with high res](/images/cmos-pixel-leica.jpg)

卧槽，和之前中画幅的对比，直接打爆。集成电路的小细节都看的清清楚楚。那我们能不能看到像素呢，放大一下：

![Macro from Leica 100% crop](/images/cmos-pixel-SLLocal.jpg)

还是很清楚的。因为我知道这个像素的大小是3.75微米，在100%放大的时候一个像素有18像素宽，所以这张图像的分辨率大约是200nm/像素。这是将近20倍的放大倍率，比之前测试的显微物镜还要大了。真的能看到CMOS上面的像素，还是很兴奋的。

现在的问题是，CMOS上面的这些空的点点是什么？周围的电路又是什么？

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
