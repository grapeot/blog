Title: 佳能VR镜头系统的痛点和解决方法
Date: 2022-04-25 00:11
Category: Computing
Tags: Chinese, Photography, Review
Slug: canon-vr-system-pain-points

最近租了一个佳能的VR镜头用来拍娃，真的是革命性的体验。之前试着用[360全景相机](/images/my_vr_lens.jpg)来拍娃，然后在Quest2上看，已经受了震惊了。但和佳能的[VR镜头系统](/images/my_vr_lens.jpg)出的照片和视频比起来，全景相机就是个弟弟。一方面毕竟是全幅打1/2寸，[画质](/yage.ai/resolution-limit-of-135-system.html)碾压，一方面数码分辨率也更高，4k/180度比6k/360度还是更爽。而且这种立体的感觉，和看3D电影差不多，让人忍不住想去摸摸，或者有狗冲过来的时候会想躲开。我拍了一个松鼠吃东西的视频，youtube链接[在这里](https://www.youtube.com/watch?v=HhlxmclNLVk), Quest2里面可以用app直接看。B站也有一个版本，但我还不清楚怎么在Quest2上面看。

![Canon R5 + VR lens](/images/my_vr_lens.jpg)

但佳能的VR系统也有三个非常蛋痛的地方：

1. 官方的软件EOS VR Utility不支持RAW格式。你说视频跑不动RAW我也理解，图片都不支持是怎么回事小老弟。你不支持RAW本身也就罢了，我理解工期紧任务重，我通过RAW导出来的jpg也不认识，这就有点。。
2. 这个软件本身用起来非常非常痛苦。比如点进一张图，先卡个1分钟算视差，中间啥都干不了。你说我就看一下这张图长什么样，别给我算鸭，不行。然后点个按钮做地平线纠正，又卡个1分钟。最蛋痛的是这个地平线纠正是必须做的一件事情，不做的话在VR眼镜里面就不由自主斗鸡眼。但它默认又没有启用，我就要一张张图点进去，卡一分钟，点一下按钮，卡一分钟，点下一张图，卡一分钟。。。然后比如拍了100张图，要做一百次这个操作。。蛋都碎了好吗佳能！！
3. 然后R5的分辨率也不够高，VR眼镜里面看起来有点糊。别慌喷！听我解释！这个镜头有两组光学结构，每组分别负责一只眼睛。所以虽然R5是8k，分到每个眼睛上就只有4k了。然后这4k还要摊到180度的视角上去，这么看是不是就感觉不太够了？

当然这个文章也不是光抱怨就完了，我写了一个小程序 [[github]](https://github.com/grapeot/EOSVRUtilityUtility)，很大程度上解决了前两个问题。同时第三个问题我发现用Topaz Gigapixel等[神经网络](/yage.ai/ai-it-impact.html)脑补软件可以很好地解决。虽然在100%放大的时候会觉得不太自然，出现了一些原本没有的有些怪异的纹理，但在VR眼镜里面看起来还是非常好的。

所以总体来说我的VR工作流是这样的：

1. 用R5+VR镜头拍娃，得到一坨RAW文件和直出的jpg。
2. 用CaptureOne或者Lightroom处理RAW，得到一坨牛逼jpg。
3. 用这个小工具，给这坨牛逼jpg打补丁，一方面让佳能的软件可以认出来，一方面也默认启用地平线纠正。
4. 用EOS VR Utility把这些牛逼jpg转成VR的格式（3D SBS 180度）。
5. 用Topaz Gigapixel把图片进行放大。
6. 传到VR眼镜里面观看，或者分享。

感觉VR拍娃实在非常革命，尤其是和父母不在一个地方的，可以买一个VR眼镜配好送回去。以后可以直接分享这种VR视频/照片，跟在现场几乎完全一样。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
