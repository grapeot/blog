Title: 开箱即用的动漫头像检测包
Category: Computing
Tags: Chinese, AI Technique, Image Processing
Date: 2019-06-20 18:54
Slug: anime-head-detection

虽然人脸检测算法已经相当成熟了，但如果直接把这些人脸检测的包用到动漫数据上的话，基本是啥都检测不出来的。。我们当时在调校人工智障的时候就遇到了这个问题，当时用的是基于小波的传统算法，检测精度虽然高，但漏检的情况真的是惨不忍睹了。。最近终于有时间，标了200张数据，用深度学习训练了一把，效果意外地好，所以把模型和代码开源了。

一个视频例子见[这里](https://www.bilibili.com/video/av56965875)。可以看到在不同的pose下检出率还是可以的。也可以看出这个模型做的其实不是人脸检测，而是头部检测。我们的训练数据就是在辉夜大小姐和小埋上面标的，但意外的是对于其他番，甚至黑白线描也可以检测：

![detection example](/images/anime-head-detection-1.jpg)

对于人脸几乎不看见的背面的情况也可以搞定：

![detection example](/images/anime-head-detection-2.jpg)

对于戴帽子的情况也可以，只是对于比较少见的表情+泳镜的情况就SB了：

![detection example](/images/anime-head-detection-3.jpg)

代码和模型放在了github上：https://github.com/grapeot/AnimeHeadDetector

使用非常简单：
 
* 首先用`git clone --recursive https://github.com/grapeot/AnimeHeadDetector`把代码clone下来。注意这里必须要用`--recursive`，因为我们用了submodule来引用了其他repo。
 
* 然后用`pip install -r requirements.txt`安装依赖。
 
* 因为大小的限制，模型host在其他地方，我们要先用`./downloadWeights.sh`把模型下载下来。
 
* 然后就可以运行`python main.py`跑demo了！这个文件具体的用法可以用`python main.py --help`查看。

目前这个模型还有很多不完美的地方，毕竟只标了200张 23333。内部模型用的是Yolo V3。先放出来，希望能帮到大家