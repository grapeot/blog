Title: 黑白相机可以给我们更准确的颜色吗？（二）
Date: 2020-07-06 21:30
Category: Life
Tags: Photography, BlackAndWhite, Color, Chinese
Slug: black-and-white-photo-colorization-2

[上一次](black-and-white-photo-colorization.html)我们提到了黑白相机可以用分光的方法拍摄彩色照片，但是还是有一些问题，一个是彩色的暗角，一个是色彩不准确。这个文章主要介绍一下如何解决这些问题，同时给出一个完整的可操作的拍摄指南。

彩色的暗角可以通过拍摄暗场，或者直接用PS的暗角工具来去除。R，G，B通道拍摄的暗角如图所示：

![Flat fields](/images/blackandwhite-color-flat-field.jpg)

可以看到不同通道暗角的程度是不一样的。就是这个造成了最终合成的彩色图像中的彩色暗角。把这个从图像中扣除掉以后就基本可以解决这个问题。此外，我们还把色卡加入了照片中去，这样在后期就可以用一些自动化的工具进行调色。当然这个色卡可以在同样的光照条件下另外拍摄，这样就不用改变拍摄物体了。这里我们为了简单起见，直接把色卡扔到了我们祖传的辉夜姬乐高前面。

![Raw photos with color checker](/images/blackandwhite-color-film-3-2.jpg)

我用的是爱色丽的色卡。直接用官方的软件，把这个合成的图像（转成的DNG文件）扔进去，就可以得到一个DCP文件（DNG Color Profile）。这里有个坑是，PS和LR都没办法直接应用这个DCP文件，可能因为这个文件一般需要和exif中相机的型号对上才能显示出来。但我们的照片是PS合成的，根本没有相机型号。。所以需要用一些底层一些的软件比如RawTherapee来应用这个DCP文件。然后颜色一下就很正常了：

![Adjusted photo](/images/blackandwhite-color-result-3-2-raw.jpg)

下面就是调调白平衡，拉拉曲线，一个成品就完成了。左边是这次的结果，右边是上次的结果。很明显几个问题都解决了。注意两次拍摄的时间和光照不尽相同，所以有一些明显的差异。虽然色彩还是有点稍微的怪异，比如墙壁偏粉，但是这些可能就需要更多的经验和练习才能解决了。

![Result comparison](/images/blackandwhite-color-result-3-2.jpg)

下面是另一个结果。注意这些都是黑白胶片拍出来的哟：

![Another Result](/images/blackandwhite-color-result-4-2.jpg)

总结一下处理流程：

1. 前期用RGB滤镜分别拍摄，注意在笔记本上记下来每张照片分别是什么滤镜。测光要先注意一下滤镜的filter factor，也就是加几档曝光。摄影滤镜一般都会写，但天文滤镜则不一定，所以需要自己尝试一下。我发现这个加几档和胶片也有关系，比如我的滤镜在Ilford HP5+上面RGB都是加两档，但是在[CMS 20 II](resolution-limit-of-135-system.html)上面RG是两档，B是三挡。
2. 冲洗胶片，扫描或者翻拍。
3. 把得到的raw文件直接反相，除尘。注意这一步不要做非线性的调整。
4. 把三个通道导入PS进行图层对齐，然后分别存成三个文件。注意一定要先存成文件，直接复制粘贴成新图层不知为啥就是不行。。
5. 新建一个PS文件，把RGB通道分别设置成这三个文件。
6. 用LR把这个文件另存为DNG。用爱色丽的软件生成DCP文件。
7. 用RawTherapee对DNG文件应用DCP文件。
8. 进行正常的其他后期。

希望有所启发。下面一步就是用[CMS 20 II](resolution-limit-of-135-system.html)来挑战彩色135摄影的分辨率极限了。。