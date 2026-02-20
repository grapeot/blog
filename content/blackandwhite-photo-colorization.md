Title: 黑白相机可以给我们更准确的颜色吗？（一）
Date: 2020-07-02  21:30
Category: Life
Tags: Chinese, Photography, DIY
Slug: black-and-white-photo-colorization

徕卡和飞思都有专门的黑白相机。这些相机去掉了传感器前面的Color Filter Array (CFA)，只能拍摄黑白图像。在带来无比强大的高感的同时，这些相机也给了我们很多灵活性，比如可以在镜头前面加滤镜进行特定波段的摄影，手持拍摄红外等等。这启发我们问一个问题，有没有可能在这个黑白传感器前面套红绿蓝三色滤镜，让黑白传感器也可以拍摄彩色呢？这看起来是个很无聊的事情，人家辛辛苦苦把CFA拿掉，卖这么贵，结果你还又把它变回彩色了。但其实我们看一下普通摄影滤镜的频率响应就会发现相当随意：

![Regular photography filters](/images/blackandwhite-color-filter-photography.JPG)

而对比一下天文摄影里面LRGB的滤镜的频率响应：

![Astrophotography filters](/images/blackandwhite-color-filter-professional.JPG)

可以发现，后者一方面截止频率非常明晰，直上直下；一方面效率也是校准好的，不需要进行亮度调整。所以启发我做一个实验，如果我们用专业的天文摄影的颜色滤镜，加上[黑白相机](/yasselblad.html)，这样有可能得到更准确的颜色吗？于是我买了2英寸的LRGB和。。肯定是买不起8495美元的徕卡M10M的，于是我买了一卷黑白胶卷，装在了[中画幅相机](/full-frame-and-medium-format-1.html)上，用RGB三个滤镜，分别拍摄一个场景，然后把黑白胶片冲洗出来。这样立省8500！

![Mounted](/images/blackandwhite-color-filter-mounted.jpg)

冲出来的胶片很有意思，长这样：

![Raw film](/images/blackandwhite-color-film-3.jpg)

可以看到不同的通道，不同的区域亮度也不一样。最左边的图像是R通道，所以辉夜的红色头巾就很亮。而其他通道头巾就很暗。所以看上去的确有足够的颜色信息呢。下面就是把三张照片进行对齐，分别放到RGB通道里面去，就可以得到这样的结果了：

![Result image Shinomiya](/images/blackandwhite-color-result-3.jpg)

可以看到效果出来了，我们真的可以用纯黑白照片得到一个彩色的照片。但也还是有一些问题的。一个是边角有一些红色的"暗角"，这可能是因为不同滤镜的暗角因为某些原因不尽相同，导致颜色混合之后在边角出现了问题。这也许可以通过拍摄平场进行解决。另一个问题是这个颜色看起来还是有些奇怪，不是特别准确。这也许可以通过拍摄标准色卡进行校色。下面主要就会从这两个方面进行改进。另外，这种方法显然不太适合动态场景，比如有风的树叶hhhh：

![Result image outdoor](/images/blackandwhite-color-result-2.jpg)

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
