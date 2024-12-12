Title: 乐高拼贴喔卡哇伊阔多
Date: 2020-02-02 15:00
Category: Life
Tags: DIY, Lego, Lego Mosaic, Chinese
Slug: lego-mosaic

最近路过一家乐高店，看到里面有Lego Master用乐高拼了一整面墙的图画，就开始想有没有可能我自己也拼一个呢？放家里当一个照片放着就好，不用一面墙。于是就做了一些实验，拼了一个75x75cm的四宫辉夜出来。下面主要介绍怎么从一张照片得到一个乐高零件的列表，进而购买拼装。很明显，这个分为两步，第一步，从一张照片根据现有的乐高的颜色，得到一个低分辨率的类似8bit的图像；第二步，根据不同颜色的乐高的形状，得到零件的列表和拼接指南。下面我们一个一个讲。

从全彩照片到适合乐高的照片用[3D打印](https://yage.ai/3d-print-faq.html)很容易解决。我做了一些调研，目前已有的方案大都有两个问题，第一没有考虑到乐高本身有什么颜色，只是单纯用系统提供的颜色，所以实际拼的时候还要调整颜色。第二没有禁用Photoshop的仿色（Dither）功能，所以出来有杂点。我从PS操作的角度介绍一个简便易行且效果好的方法。最后再给出一个用程序大幅减少颗粒数量和成本的例子。

首先打开一个图像：

![Original photo](/images/lego-mosaic-original.jpg)

然后用PS缩小到目标大小。这里我用的是64x64像素（拼出来大约50cm x 50cm）：

![Resizing interface](/images/lego-mosaic-figure1-chinese.png)

![Resizing interface](/images/lego-mosaic-figure2-chinese.png)

![Resizing result](/images/lego-mosaic-figure3.jpg)

接下来转换成规定的颜色：

![Color conversion interface](/images/lego-mosaic-figure4-chinese.png)

下面是最重要的部分：
颜色暂时选16，强制选暂时选黑白，仿色选无。这样出来的色彩就会比较自然而且没有噪点：

![Color conversion interface](/images/lego-mosaic-figure5-chinese.png)

![Color conversion result](/images/lego-mosaic-figure6.jpg)

但是，这仍然没有考虑到乐高本身的颜色。乐高本身有多少种颜色呢？如果考虑历史上曾经生产过的颜色，一共有81种（[链接](https://www.bricklink.com/catalogColors.asp)）。但很多现在已经停产了。现在乐高的官网还有18种颜色的1x1 brick可以购买（[链接](https://www.lego.com/en-us/page/static/pick-a-brick?query=1x1%20brick&page=1)）。有人用Pantone色卡一个个和乐高的颜色比对，得到了每种颜色的RGB值（[链接](http://www.bartneck.de/2016/09/09/the-curious-case-of-lego-colors/)）。我把现在乐高网站还在售的型号提取出来，整理如下：

<table><tr><th>Color</th><th>Hex<th><tr>
<tr><td>Brick Yellow          </td><td>D3BC8D</td></tr>
<tr><td>Bright Reddish Violet </td><td>AF1685</td></tr>
<tr><td>Light Purple          </td><td>981D97</td></tr>
<tr><td>Bright Red            </td><td>EF3340</td></tr>
<tr><td>Medium Azur           </td><td>71C5E8</td></tr>
<tr><td>Dark Stone Grey       </td><td>5B6770</td></tr>
<tr><td>New Dark Red          </td><td>9B2743</td></tr>
<tr><td>Medium Lilac          </td><td>330072</td></tr>
<tr><td>Earth Blue            </td><td>003865</td></tr>
<tr><td>Medium Stone Grey     </td><td>A2AAAD</td></tr>
<tr><td>Bright Blue           </td><td>003DA5</td></tr>
<tr><td>Medium Blue           </td><td>6CACE4</td></tr>
<tr><td>Reddish Brown         </td><td>7A3E3A</td></tr>
<tr><td>Bright Yellow         </td><td>FFCD00</td></tr>
<tr><td>Black                 </td><td>27251F</td></tr>
<tr><td>Sand Green            </td><td>789F90</td></tr>
<tr><td>Bright Yellowish Green</td><td>B5BD00 </td></tr>
<tr><td>Bright Orange         </td><td>FF8200</td></tr>
</table>

那这个信息怎么用呢？具体地说，需要在上面索引颜色的界面里把调板换成自定...，然后就会弹出来一个对话框可以选具体颜色：

![Color conversion interface](/images/lego-mosaic-figure7-chinese.png)

![Color conversion interface](/images/lego-mosaic-figure8-chinese.png)

点击其中某个颜色就可以更改RGB值。为了简便起见，我们使用下图中光标高亮的部分（#ffffff）来编辑。

![Color conversion interface](/images/lego-mosaic-figure9-chinese.png)

然后输入上面颜色即可。全部打进去以后PS的颜色应该像这样：

![Color conversion sample](/images/lego-mosaic-figure10-chinese.png)

可以点击...按钮另存为一个ACT文件，这样下次就不用再打啦。但遗憾的是这18个颜色没有足够多的黄色，所以出来的结果非常鬼畜，颜色基本都丢失了：

![Color conversion result](/images/lego-mosaic-figure11.jpg)

但如果我们换一个颜色对比强烈（大红配大绿）的图片，效果就会好很多：

![Color conversion result](/images/lego-mosaic-figure12.jpg)

但是否就意味着对于最开始的蓝毛的例子，我们就没办法了吗？也不是。前面提到我们把仿色给禁用了，这是因为它会引入噪点，非常难看:

![Dither result](/images/lego-mosaic-figure13.jpg)

但仿色到底是干什么的呢？它是一种用有限的颜色来表达更丰富的灰度和颜色的方法。因为64x64的分辨率实在是太低了，所以看起来非常奇怪。如果比如我们想拼一个2m x 2m的乐高墙的话，这个分辨率可以达到256x256。此时dither就非常有效果了（左边是没有Dither的，右边是有Dither的）：

![Dither comparison](/images/lego-mosaic-figure14.jpg)

所以我们也可以看出来，做一个牛逼的乐高像素画，选一个适合能买到的乐高颗粒的照片，是成功的一大半。这个我们也完全可以自动化批量处理，只要用色彩空间中的距离来排序就好。这个就留做家庭作业啦。

几个相对靠谱的例子（长边96像素）：

![Sample result](/images/lego-mosaic-figure15.png)
![Sample result](/images/lego-mosaic-figure16.png)
![Sample result](/images/lego-mosaic-figure17.png)

然后下面怎么办呢？很多网上的教程到这一步就结束了，下面就是去乐高网站买很多1x1的颗粒就好了。但实际上还是有很多优化的空间。比如上面这个96x96的图像，如果全部购买1x1的颗粒需要9216个颗粒，共计645美元。但其实很多颗粒是可以合并的，比如8个1x1的颗粒也许可以合并成一个2x4的颗粒，又省了时间又省了钱。所以我上网手动查询了现在乐高网站上有货的颗粒的尺寸，手工写了个程序生成如何拼贴的方案，得到如下所示的图纸：

![Sample result](/images/lego-mosaic-merged.png)

用这个程序把颗粒的数量从9200+缩减到了2500+，所需费用从650左右缩减到了300左右。在用程序输出了每种颗粒分别要买多少以后在乐高官网上下了单。这个单据客服说要在波兰手工挑出来，然后运到美国，清关啥的搞了好长时间，过了一个月才拿到。。然后就是拼接啦：[b站](https://www.bilibili.com/video/av86261283)

最终的效果如图所示：

![Final result](/images/lego-mosaic-result.jpg)

有感兴趣的小伙伴也可以试试哈！