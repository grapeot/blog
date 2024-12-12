Title: 冲击10亿像素的单张照片
Date: 2020-03-13 15:00
Category: Life
Tags: Photography, Gigapixel, High Resolution, Computational Photography, Chinese
Slug: gigapixel-photo

近半年来，我一直在试图把一张照片的分辨率推到极致。这个分辨率不仅是光学分辨率，也是数码分辨率。一般来说，在一个相机的前提下，提升分辨率主要靠[接片](https://yage.ai/gigapixel-methods.html)或者摇摇乐。接片接出来比较大的照片比较可行，但有一个问题是它往往只能提升数码分辨率而不能提升光学分辨率。所以很多时候还要靠[摇摇乐](https://yage.ai/drizzle.html)。这篇文章主要介绍一下最近做的一个实验。这个实验用中画幅数码后背+中画幅高分辨率微距镜头+摇摇乐实现了10亿像素的分辨率。

我们的场景大致是这样的。

![Overall scene](/images/high_res_scene.jpg)

然后放大单看最中间红色箭头指的那个S字母。因为这个区域非常非常小，所以这其实是个相当难的测试。

首先我们用S1R+50AA拍了一个单张：

![S1R and 50AA](/images/high_res_50aa.jpg)

分辨率的确不咋地。。如果我们开启摇摇乐，连拍8张合成一张187MP的图片：

![S1R and 50AA x8](/images/high_res_50aa_x8.jpg)

可以看到分辨率有明显提升。然后下面这个是[飞思IQ180](https://yage.ai/resolution-limit-of-135-system-3.html)+大画幅镜头（施耐德72/5.6）的结果：

![IQ180 and Schneider x1](/images/high_res_iq180_x1.jpg)

下面是用IQ180+施耐德72/5.6+7张摇摇乐的2.5亿像素的结果：

![IQ180 and Schneider x7](/images/high_res_iq180_x7.jpg)

下面是IQ180+施耐德72/5.6+30张摇摇乐4亿像素的效果：

![IQ180 and Schneider x30](/images/high_res_iq180_x30.jpg)

最后是通过降低离物体的距离来提升放大倍率，然后通过接片来增大视野。但发现在这种情况下相差和色差都崩了。。因为毕竟这个镜头不是为了微距优化的。正好我在ebay上捡漏捡了一个apo-macro-sironar，于是就用这个微距镜头接片，降低摇摇乐的放大倍率，得到了10亿像素的一张照片：

![1000MP Scene](/images/high_res_1000MP_scene.jpg)

哎，看起来平平无奇，不过。。

![File size PSB](/images/high_res_psb.png)

![File size JPG](/images/high_res_jpg.png)

文件大小直接干翻photoshop和opencv。。

![Photoshop Error](/images/high_res_photoshop.jpg)

![OpenCV Error](/images/high_res_opencv.jpg)

然后这个是细节：

![Details](/images/high_res_1000MP.png)

再和4700万像素的S1R+Leica 50APO比比：

![S1R and 50AA](/images/high_res_50aa.jpg)

可能用视频更能体现这个照片里面有多少细节：

https://www.bilibili.com/video/av95861559/

谢谢观赏。