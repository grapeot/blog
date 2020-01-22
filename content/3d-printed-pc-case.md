Title: 关于3D打印机箱的一些实验
Category: Life
Tags: 3D Print, DIY
Date: 2019-10-21 18:54
Slug: 3d-printed-pc-case

我打了一个玩具级别的机箱出来，把经验和踩过的坑总结一下，看看能不能对其他人有所启发。打印组装出来的成品长这样：

![3D printed PC Case](/images/3dprint-pc-case-front.jpg)

我打印机箱的主要动机是1）外形可以自己设计，这样就可以做一些比较灵活少见的外型。比如我这里用的是开放式的设计。2）散热考虑。我的显卡散热/体质不好，放到封闭机箱里面一满负载就100%风扇+温度墙降频。想看看开放机箱是否有改善。3）技术验证，以后还是想做光cpu无显卡带着到处跑的小机箱，但现有的机箱看着又不爽，想先通过这次打印验证一下基本技术。

但我也有自己应用灵活的地方，这是为什么可以选用3D打印+开放设计的原因：1）这个机箱自己用，所以不在乎表面光洁度（省掉后期打磨的步骤了）。2）我在的城市空气很好，所以想先试试看开放式进灰的问题是否严重。3）这个机器主要做服务器ssh上去使用，所以不放在办公桌上，不会出现打翻一杯水一股黑烟冒出来的情况。4）我感兴趣的是mini-itx主板，正好能放到我的FDM打印机里去。要是再大些就不知道怎么弄了。

踩过的坑主要有：

1. 部件的分解。即使是mini-itx的主板，考虑到机箱电源的因素，由于build volume的限制，在绝大多数打印机（包括FDM和SLA）里也不可能一次打出来。所以这里需要考虑如何拼装。我一开始用了类似螺丝的设计，地面电源仓竖起来两根柱子，上面主板仓套上去。但后来发现这样强度不够，把电源乱七八糟一堆线缠到主板仓后面以后会发生弹性形变（把电源线卸了还能恢复原样）。所以后来我把改成了卡扣的设计，强度高了很多，这个问题就解决了。
2. 材料的选择：这个目前还在测试。我用的是最简单的PLA。之前对强度和耐高温有一定的顾虑，主要是显卡一搞就80多度，怕PLA软化。同时电源那一大堆线要缠在竖着的放主板的那块板后面，还是蛮重的。目前看这两点都没什么问题，一方面强度问题我们通过设计解决了，一方面开放机箱非常意外的对散热有奇效，我的显卡核心现在满负载只有50度+，外面感觉凉凉的。目前还没遇到软化问题。
3. 打印：这个是折腾了最久的一步。当打印的部件大小接近整个打印平台大小的时候，之前很多不精确的调整/设置都会暴露出来。比如打印平台的调平。打小东西的时候差一点点根本无所谓，打大东西的时候边角就会翘起来。这里和厂家联系了一段时间，好像还发现了他们固件的一个bug... 后来更新了固件才解决精确调平的问题。
4. 一些细节：主要是打印组装好了准备上电了发现... 诶？开关呢？？？一般的机箱是会有前面板开关的。自己打印的当然没有。所以还得上网买个开关，把开关跳线接出来。跟炸碉堡似的。另外显卡的方向，主板的方向，电源的方向也需要配合。搞不定的时候PCI-e延长线可解。

![Switch of the PC case](/images/3dprint-pc-case-start.jpg)

目前已经跑了三个月了没发现什么问题。感觉FDM还是糙，有钱的话还是Form 3L解千愁。