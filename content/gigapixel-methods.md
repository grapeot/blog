Title: 如何拍出几百亿像素的照片
Date: 2019-01-26 20:30
Category: Life
Tags: Photography, Chinese
Slug: gigapixel-methods

从数码相机的发源开始，我们就一直在问，如何有效提升相机的分辨率。在它的背后其实是一整个（甚至数个）领域的发展。这个文章就从四个部分介绍和超高分辨率数码摄影相关的故事：

1. 什么场景需要几百亿像素的照片？
2. 如果一次性拍摄（非拼接，这样就可以拍摄动态场景），有什么设备和方法可以使用？
3. 如果允许拼接，有什么方法可以使用？
4. 如果只有手头的设备，有什么方法可以拍出高分辨率的图像？

## 几百亿像素的场景

这个场景其实不多见。想想也知道，现在绝大多数的照片浏览都在手机端完成，要那么多像素搞个毛。一般在生活中我们能看到的有以下几个例子：

1. 星球级别的卫星地图，比如NASA的[高分辨率月面图](https://moon.nasa.gov/resources/87/high-resolution-topographic-map-of-the-moon/)，谷歌地球/月球/火星。这种主要是因为星球太大了，即使光学分辨率很低（哪怕100m/像素），乘出来的分辨率也相当可观。因此一般也要求有特殊的浏览手段，一次只下载和浏览一小块区域。受到卫星和飞机设备的限制，这种场景只能使用多次拍摄然后拼接。
2. 文物的保护，比如微软亚洲研究院对敦煌石窟的[高分辨率扫描](https://www.microsoft.com/en-us/research/video/eheritage-program-collaboration-with-dunhuang-academy/)。这个项目在2010年左右就用了10亿像素的机器进行拍摄，用的是单轨大画幅+微距+扫描传感器+景深合成。随着近十年电子传感器的飞速发展，同样的方法在今天达到百亿像素分辨率应该不成问题。
3. 艺术项目，比如微软和西雅图的艺术家们合作做了这个[200亿像素的图像](https://petapixel.com/2014/01/29/microsofts-20-gigapixel-seattle-panorama-includes-fun-surprises/)，里面藏了各种艺术小彩蛋。

## 一次性拍摄

因为现阶段还没有这么高分辨率的的传感器，所谓一次性拍摄，往往指的是多个设备同时拍摄。和多次拍摄拼接相比，这种方法不需要物体是静止的，可以拍摄动态场景。这有土豪的玩法也有一般人的玩法。土豪直接用128个消费级单反（似乎是佳能5D）组成阵列，然后用DSP+FPGA+PC机群现场处理数据：

[http://graphics.stanford.edu/projects/array/](http://graphics.stanford.edu/projects/array/)

这里面很多玩法。拍视频的话可以通过精确控制不同相机的曝光时序，在1/30的曝光时间下实现超高帧率 (3000fps) 超高分辨率 (6k，注意这是04~06年，主流单反还在几百万像素挣扎) 的视频。拍照片的话能得到超精确的光场，超高的信噪比，和/或超高的分辨率。注意因为每个相机的pose是事先知晓的，所以不用估计全景图的几何变换，直接写内存就好。所以按一下快门，全景图的合成是实时的。从这个角度说，也可以看作是一次性拍摄。

Adobe也有类似的技术，但就平民化多了。用的是多个iPhone，朝外拍可以解决动态场景的全景图问题 [arXiv](https://arxiv.org/abs/1507.01147) [video](https://www.youtube.com/watch?v=PwQ6k_ZEQSs)，朝内拍可以生成子弹时间视频 [arXiv](https://arxiv.org/pdf/1507.01148v2.pdf) [video](https://www.youtube.com/watch?v=LgkHcvcyTTM)。通过app来解决多台iphone间同步的问题。当然这个目前没办法达到几百亿像素的程度，只是提供一个技术上的思路——小底+app应该也可以实现的。[https://theblog.adobe.com/bullet-time-in-real-time/](https://theblog.adobe.com/bullet-time-in-real-time/)

## 多次拍摄拼接

这就是大家喜闻乐见的全景图了。当数据量到几百亿像素的时候，系统的主要瓶颈是把所有数据存储在内存里，以及找到一个全局的几何变换。到这个级别，一般来说各家的解决方法都比较类似：用不同的分辨率 分层 局部 合成，然后打散成tile存储。这是因为用户的浏览只会有两种情况：缩小看缩略图（此时用户反正看不见细节，就干脆直接在缩略图上面做全景合成节约内存），放大看细节（此时用户反正看不见全局，就只渲染周边的图像节约内存）。这里最典型的软件就是微软研究院的ICE。特色是没有分辨率限制，同时可以导出成DeepZoom等类似谷歌地球那样无缝放缩平移的格式。之前提到的200亿像素的照片就是用了2000多张图片在ICE里面合成的: [https://www.microsoft.com/en-us/research/product/computational-photography-applications/image-composite-editor/](https://www.microsoft.com/en-us/research/product/computational-photography-applications/image-composite-editor/).

ICE的主要问题在于太自动化了，有时候出现合成上的瑕疵也很难手动调整。因此我也用过其他一些全景合成的软件，推荐两个。一个是[PTGui](http://www.ptgui.com/)，好处是定制性非常高，内存很省，如果是细节控的话不妨使用；坏处是自动算法有点脑残，经常对歪。一个是Photoshop，生成的全景图质量还是蛮高的，就是费内存。Photoshop有个好的地方是可以导出成类似DeepZoom的格式。比如这个86亿像素的照片就是我用PTGui生成，用Photoshop导出的（两年前拍的，现在看技术上有很多瑕疵）：

[https://lab.grapeot.me/gigapixel/Seattle/](https://lab.grapeot.me/gigapixel/Seattle/)

上面提到的敦煌莫高窟的数字化保存项目也可以归为多次拍摄拼接的一种，只是用的是扫描式传感器。他们的设备如下：

![Gigapixel equipment](/images/gigapixel-equipment.png)

图片来自https://www.eecs.yorku.ca/~mbrown/pdf/lu_joch_acm_2012.pdf

## 提升设备的分辨率

分析上面这些这对我们有什么启发呢？如果我们并没有升级设备的打算，有没有可能用算法来增强手头设备的有效分辨率呢？这也是可行的，也许没有几百亿像素这么多，但到两三倍没有问题。大概地说：

* 这种提高分辨率的方法叫drizzle，在天文摄影和医学图像处理中被广泛使用。 
* drizzle要生效的基本要素有：镜头给力传感器不行+抖动 
* 考虑到现代彩色相机的bayer matrix，drizzle有对应的彩色版本叫drizzle debayer。它的基本思路一致，可以提升色彩准确度和有效分辨率。 
* 相关的工具有photoshop，deepskystacker

具体可以参考[这篇教程](https://yage.ai/drizzle.html)。
