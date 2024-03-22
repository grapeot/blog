Title: 树莓派上的目标检测智能相机
Category: Computing
Tags: Photography, AI, Machine Learning, Object Detection, Raspberry Pi, Chinese
Date: 2020-06-04 22:00
Slug: raspberry-pi-object-detection

故事的缘由是晚上睡觉的时候偶尔会听到外面有响动，总是要起来看一下是怎么回事。所以就想着装一个监控相机。正好手头有一个原来做小项目用的树莓派和相机，就贴在阳台上做了一个小相机用来串流。这下在被窝里也可以暗中观察了。

![Raspberry pi camera](/images/rpi-od-gears-3.jpg)

![Raspberry pi body](/images/rpi-od-gears-2.jpg)

有了平台就有了很多可以折腾的东西。比如我们家有时候会有松鼠，小鸟过来吃东西。于是就顺手加了一个目标检测功能，这样一方面可以自动拍照，一方面也可以手机推送通知提醒我过来吸鼠。时间长了积累的数据还可以用来观察它们的作息等等。效果类似[这个视频](https://www.bilibili.com/video/BV1Af4y1m7hR/)。

从技术的角度来说这里有几个坑。一个是树莓派3的CPU实在是太弱了，换了不少model，最终选择了darknet + EfficientDet B0，才实现8秒一帧的速度。一个是opencv的darknet实现很坑，虽然正常情况下CPU实现比官方darknet快100%左右，但模型加载有问题不会报错，只会出空结果，debug了很长时间。还有一个坑是树莓派在满载的时候散热有问题，芯片常年85度。弄了个散热鳍片可以降到70度左右。

这里从算力的角度说其实有其他选择，比如树莓派4，价格不变还是35美元，性能涨了4倍到了0.14 TFLOPS。如果加点钱买99美元（打折的时候79美元）的nvidia jetson nano的话，可以实现0.5 TFLOPS的性能，里面有一个128核的Maxwell GPU。如果再加钱上399美元的nvidia jetson xavier nx的话，可以拿到3 TFLOPS的性能（整数网络有21 TOPS），功率才15瓦。要知道2060才6.5 TFLOPS，功率可是160W。

回到应用，树莓派的8MP的相机有个问题，拍摄的照片画质实在是太差了。所以还是想把真正的相机接到这个系统里面去。思路很简单，就是把相机架在鸟食旁边，如果树莓派发现这附近有松鼠或者鸟出没，就给相机发一个信号拍摄。这里面的问题是，我的相机是Leica SL，并没有很方便的SDK，怎么办呢？解决方法也很简单，基本上所有相机都支持tethered capture的。这种情况下，拍摄就是在电脑上用鼠标点一个按钮，照片就存下来了。所以我就写了个python脚本，建了一个web service，一旦被ping，就移动鼠标到一个特定的位置，单击一下就搞定。这样虽然土，但非常灵活，而且也是非常可靠的。（记得把电脑定时休眠关掉就好）

![Overall camera config](/images/rpi-od-gears-1.jpg)

然后就是吸鼠时间啦。这个系统非常好，拍了很多有意思的照片。发几张看看：

![Squirrel 1](/images/rpi-od-squirrel-2.jpg)

![Squirrel 2](/images/rpi-od-squirrel-1.jpg)

![Squirrel 3](/images/rpi-od-squirrel-3.jpg)

拍鸟的效果也很震惊：

![Bird 1](/images/rpi-od-bird-1.jpg)

![Bird 2](/images/rpi-od-bird-2.jpg)

上面这个鸟局部放大是这样的：

![Bird 3](/images/rpi-od-bird-3.jpg)

我还是第一次知道原来鸟身上细小的绒毛还有这么精细的结构。真是很有意思了。

其实这个系统还有很多可以思考的地方，比如：

* 为什么不做成云端的系统？比如在电脑上处理，这样速度就不是问题了。这是有可能的，其实我现在就在往这个方向转。当时不这么做有两个原因，一个是开发速度，全在树莓派上完成我就不用做通信，容错，等等奇怪的东西。一个是我的丹炉平时也是在训练其他模型的。
* 为什么不做成大相机+PIR传感器这样的形式？这也是有可能的，实际上就有其他up主已经做出来了。我选择现在目标检测的路线主要是历史原因——就算没有大相机我也是需要这个功能的。

有其他问题欢迎讨论鸭。
