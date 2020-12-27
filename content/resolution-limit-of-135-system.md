Title: 135系统的分辨率极限 —— CMS 20 II胶片评测
Category: Life
Tags: Photography
Date: 2020-07-03
Slug: resolution-limit-of-135-system

先看一下这张照片，猜猜它是什么画幅的？

![Final result](/images/135-resolution-limit-result.jpg)

这张图的分辨率有7000万像素（70MP），100%放大如下，没有像素或者胶片的颗粒。甚至可以看到乐高颗粒顶上微小的LEGO四个字母（每个字母的宽度是0.8mm）。

![100% crop](/images/135-resolution-limit-100crop-film.jpg)

为了有个对比，我们看一下这个大画幅的照片。

![Large format photo](/images/135-resolution-limit-large-format.jpg)

这个照片的分辨率是170MP，如果我们把它用同样的比例缩放的话，局部是这样的：

![Large format 100% crop](/images/135-resolution-limit-large-format-100crop.jpg)

已经可以看到一些胶片的颗粒了。那么猜猜第一张是什么画幅的呢？4x5？6x9？645数码？还是全幅？

哎还真是全幅135的。。而且不是数码，是胶片。。这张底片翻拍出来的时候我下巴都掉了。100%放大看不见胶片颗粒，8个像素大小的字母勉强可以分辨是什么字母，说明没有过采样，这个70MP真的就是有效分辨率。甚至我觉得稍微再放大一些搞到100MP也仍然可以说是有效分辨率。然鹅一般胶片的分辨率都是被同尺寸的数码爆锤的。一般全幅胶片扫到7MP就差不多了，中画幅一般在50MP也竭像了，也就是继续提升扫描的分辨率并不会榨取更多细节。但相应的全幅传感器的像素一般的在24MP，高像素的有60MP的。所以数码一般是越级锤胶片。全幅数码可以战中幅胶片，中幅数码战4x5胶片。但8x10胶片甚至更大的画幅目前还没有对手。

言归正传，那这个胶片是怎么做到这么高的分辨率的呢？这要从胶片的原理说起。胶片上面有很多银盐颗粒，有的大有的小。大的颗粒对光线敏感，小的颗粒不敏感。所以一束光照过来，大的感光了分解成银变黑了，小的没感光还是透明的，这就形成了不同的灰度。因为银盐实在太多了，所以颗粒大小的分布——也就是灰度的分布——可以近似看成是连续的，而不像数码那样受到ADC的限制只有2^14种可能的取值。所以这就是为什么我们老法师鼓吹胶片影调细腻的原因。但这样也有不好的地方，就是银盐颗粒如果大的话，放大的时候往往会被人注意到，这就是胶片的颗粒的由来。这是阻碍我们提升分辨率的关键因素。

那这个胶片是怎么解决这个问题的呢？很简单，压缩颗粒的大小，把它弄得特别小。这有两个后果，一个是颗粒小了感光度就低了，所以ISO就一下变成了12。基本上只能在室外拍摄或者上架子拍静物了。另一个后果就是银盐颗粒原来有大有小，现在都小，所以大小的分布也被压缩了，也就是灰度的范围变小了。出来的照片容易要么黑，要么白，中间调比以前要少。为了解决这个问题，这个胶片的公司Adox开发了自己的一种特殊的显影液，把ISO提升到了20（好像也没好多少。。），同时降低了对比度，让胶片能够得到接近普通胶片的对比。这个胶片就是Adox CMS 20 II。它需要用Adotech这种显影液来显影。此处吐槽这个公司和卖打印机靠墨盒赚钱一样。。一瓶100ml的显影液卖得比四卷胶卷还贵。。

网上评测来看这个胶片喜欢的人特别喜欢，不喜欢的人特别喜欢。主要槽点就是对比实在是太大了。不过我仔细阅读说明书以后冲洗倒是一遍成功，没感觉对比度放飞自我。里面要注意几个地方，1) 冲洗之前要把显影罐好好刷一遍，不是冲，是刷。把上次残留的定影液洗掉，因为这个显影液特别敏感；2) 不要pre-watering（预浸？），装完片以后直接倒显影液进去就好；3) 不能用清水来停止显影，一定要用正常的（酸性）停止显影液；4) 定影只要30-60秒。根据说明书说，以上任何一个步骤做不到，都有可能导致反差特别大。

那这个胶片的分辨率到底是什么层次呢？首先我们来对比一下同样镜头，同样机位，ISO稍高的数码全幅的效果：

![Full frame digital 100% crop](/images/135-resolution-limit-100crop-digital.jpg)

可以看到像素感相当明显了，而且和上面的胶片对比，明显感觉欠采样，这个圆都不圆。

但如果和数码中画幅相比，就明显体会到底大一级压死人了。。十年前的中画幅后背就用600块的大画幅镜头，轻轻松松打爆135分辨率顶级的50AA。上面LEGO四个字母清晰可见。你大爷还是你大爷。。

![Medium format digital 100% crop](/images/135-resolution-limit-100crop-digital-MF.jpg)

这个胶片的分辨率这么高，扫描也是个很大的问题。传统平扫根本搞不定这么高的DPI。比如爱普生系列平扫，就算用湿扫也只能到3000 DPI，也就是扫到12MP。翻拍的话，用全幅+1:1微距毫无意义，因为瓶颈其实是翻拍的机器。如果用高于1:1来翻拍，且不论全幅镜头很少有这样的微距头，接片也要接死人。所幸我们看到中幅数码的分辨率是足够的，所以我们可以用中幅数码接在大画幅机身上，配合2:1的微距头来进行翻拍：

![Use a MF back to scan the film](/images/135-resolution-limit-gear.jpg)

所以总的来说，要想实现这么高的分辨率，是一个系统工程。不是说装个卷就完了。要有精确的对焦（这里用的还是徕卡旁轴），像差修正良好的镜头，因为光圈不能开太小否则衍射会影响画质，专门的显影液，规范的冲洗，还要有靠谱的翻拍。不论是胶片还是数码，我觉得这个系统应该是当下135画质的极限了。胶片能超过数码我还是非常惊讶的。不过据说今年佳能索尼都要出1亿像素的全幅传感器，我们拭目以待吧。