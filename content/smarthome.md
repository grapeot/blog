Title: 自己动手改造智能家居生活
Category: Computing
Date: 2016-08-30 16:00
Tags: Chinese, Smart Home, DIY
Slug: diy-smart-home-transformation
Summary: 从睡眠监测、智能闹钟、窗帘控制到安防监控的全套智能家居改造：利用Sleep Cycle、Hue、Wemo、IFTTT等工具打造自动化生活，以及树莓派DIY遥控窗帘。

花了两个月的时间，断断续续做了一些[智能/自动家居的改造](/smart-home-lighting-control.html)。感觉自动家居果然是要成体系才会比较有意思——现在的生活已经有点科幻了。

晚上入睡一小时前，iphone提早把抽湿机打开，让住一楼的穷逼床单能干爽一点。到了入睡的时间，iphone把卧室灯光调暗，色温调低，连上蓝牙音箱播放海浪等声音催眠，慢慢调暗亮度最终关灯。

<img style="max-width: 640px" src="/images/smarthome_1.jpg" / alt="Smart home living room with modern furniture and devices" alt="Smart home living room with modern furniture and devices">

到了早上，手机会根据麦克风的声音判断是不是适合唤醒的浅层睡眠，在适当的时机闹铃，同时慢慢调亮灯光，把窗帘从上往下打开，这样又不会被路人看到羞羞的东西又能被慢慢唤醒。随后会用摄像头和闪光灯测一个心率。

<img style="max-width: 640px" src="/images/smarthome_2.jpg" / alt="A modern smart home living room with automated lights and a voice-activated speaker." alt="A modern smart home living room with automated lights and a voice-activated device.">

洗漱完毕后，siri会问你今天多重（因为穷逼买不起无线体重秤），然后放到apple health中去。

<img style="max-width: 640px" src="/images/smarthome_3.jpg" / alt="A modern smart home living room with sleek devices" alt="Smart home living room with modern furniture and tech gadgets">

吃完早饭，骑车上班，gps定位显示我离开了家，把家里的动作传感器和门窗动作传感器arm上，如果检测到异常会响起警号并且打我电话。而所有数据，比如睡眠质量，心率，体重，骑车的轨迹和速度等等，会被手机记录下来，一方面app自己可以分析（比如天气和睡眠质量的相关性），一方面也被加密起来和医生共享。到了公司以后，ifttt自动记录我到公司的时间，结合trello的时间管理插件在周末自动生成时间利用简报。

<img style="max-width: 640px" src="/images/smarthome_4.jpg" / alt="A modern smart home living room with a couch and a TV." alt="A modern smart home living room with a couch and large window">

港真，五年前完全想不到现在生活是这样信息化，自动化的。但要真问有什么用，我也不知道。。可能就是有了更多的数据，对自己的生活习惯有了更多的了解，从而可以有针对性的优化。同时因为电脑帮你做了很多死的工作，比如每天9点自动开抽湿机，每隔两天扫地机器人自动吸尘，所以脑子更轻松了，也更有了生活质量上的保障。不过对我们不折腾会死星人来说，可能"酷"一个字就够了吧。（笑

如果你们有兴趣[自己装一个系统](/smart-home-air-quality.html)的话，中间涉及的app有：

* sleep cycle：检测睡眠质量，智能闹铃，测心率
* iconnecthue：飞利浦Hue灯泡客户端，带定时功能，需要灯泡配合
* wemo：能用手机遥控的智能开关，需要贝尔金的wemo开关配合
* powerview：亨特道格拉斯百叶窗的app，可以通过无线网控制百叶窗的开合，需要安装亨特道格拉斯的百叶窗
* ismartalarm：ismartalarm DIY安防系统的app，可以通过无线网激活或禁用安防系统，需要安装ismartalarm的硬件设备和传感器
* cyclemeter：记录自行车的速度，路线等，可以存到Apple Health Kit中去
* ifttt：把所有东西整合到一起
* workflow：实现简单的自动化，这里用来实现一个简单的界面，让我可以在通知区域输入体重，然后后台自动存到health里去
* health：苹果的一站式健康平台

此外还有一些DIY的东西。因为能遥控的百叶窗/窗帘实在是太贵了，如果用商业的遥控窗帘（落地窗，三四米的跨度）要两三万人民币，把我卖了也买不起啊。。所以只好用了个rasperberry pi配合舵机控制板，钓鱼线，滑轮组，舵机自己撸了一个土法遥控窗帘，成本500人民币。可惜知乎传不了动图，静态图大概是这个样子的：

<img style="max-width: 640px" src="/images/smarthome_5.jpg" / alt="A modern smart home living room with a robot vacuum." alt="Smart home living room with modern furniture and devices">

原理图是这个样子的：

<img style="max-width: 640px" src="/images/smarthome_6.jpg" / alt="A modern smart home living room with a couch and a TV" alt="A modern smart home living room with a couch and large window">

还用[简单的背景减除](/esp32-cam-1.html)做了个阳台的监控，来看放在外面的豆子到底是谁偷走了。。两天以后发现小偷长这样。。（后来我撒了一把芥末豌豆，整个世界安静了，她再也没来过。。

<img style="max-width: 640px" src="/images/smarthome_7.jpg" / alt="Smarthome device displaying time and temperature" alt="Smart home living room with modern furniture and devices">

未来还是有很多工作的，比如因为房子太老，Nest、EcoBee等先进的温控装置装不上（需要大改电路）。还有之前自己做的行车记录仪等等，以后再介绍吧~