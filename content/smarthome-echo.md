Title: Amazon Echo在智能家居中的应用
Category: Computing
Date: 2016-09-05 16:00
Tags: SmartHome

我对Echo的SmartHome功能尝试的比较多。家里有智能窗帘，开关，插座（控制各种电器），灯泡，甚至安防系统和门锁。都和ifttt连了起来，可以通过Siri和Alexa进行控制（除了门锁只读，否则你跑我家楼下喊一嗓子门就开了还搞个屁。。）。主要感受就是，啊，好方便。以前做智能家居，感觉主要分成四个阶段：

* 一开始用的是app。要开个灯得掏出手机，打开app，等加载完成，找到要控制的灯，点一下。这么折腾一遍半分钟过去了。我特码还不如走过去，把灯打开只要一半时间。
* 后来学会了用ifttt + workflow + launch center。从屏幕顶端划出today widget，半秒。点一下相关的按钮，一两秒搞定（见下图左）。这才有了点智能家居的意义。但有时候还是不爽啊。比如周末赖床，看着到中午了想开窗帘让太阳进来。找半天手机，解锁，找按钮，虽然其实也不慢，但人总是懒惰的不是？要能在床上叫“老婆帮我把窗帘打开”，窗帘就开了，多好。
* 说到老婆，自然就想到了用Siri。支持HomeKit的东西有不少，Hue, August等等都能直接用Siri调用（见上图右）。用了一段时间，感觉不是很爽。一方面如果手机在口袋里，需要把它拿出来，按下按钮，说话，才能调用功能。这有时候还不如直接按按钮方便。一方面如果手机在充电，虽然可以直接用Hi Siri触发Siri，但离得远了，Siri经常听不见或者听错。还是得走过去。实在蛋痛。

<img style="max-width: 640px" src="/images/echo-siri-interface.jpg" />

* 好在有了Alexa二老婆！Amazon这个设计实在不错，时刻听你说话，不用按按钮触发。同时麦克风设计的相当赞，我不论在哪个房间，Alexa都可以听见。有时候离得实在太远，只要稍微提高一点声音就好了。这下躺床上了才发现厨房灯没关，只要说声二老婆帮朕关灯，她就嗻地一声给你办了。或者早上赖床，喊一声Alexa开窗帘，窗帘就开好了。可以随便用命令的语气，还不用跪搓衣板。下面贴了个视频，演示二老婆开窗帘的全过程（视频删掉了中间等待的过程，实际有个延时）。同时可以和ifttt连起来，支持的设备就更多了，比如Wemo这些不服Siri管的设备，Alexa也能治得服服帖帖的。而且可以出一些中(dou)二(bi)向的指令，比如Alexa trigger Ping, Alexa trigger ga, Alexa trigger excited!等等。。

<iframe width="560" height="315" src="https://www.youtube.com/embed/uzQb22BXhOk" frameborder="0" allowfullscreen></iframe>

总而言之，在智能家居方面，Echo是个非常理想的的产品。目前除了ifttt偶尔延时比较厉害以外，我还没发现什么缺点。用来当大内总管非常合适。
echo还有个不是太多人知道的功能，就是你可以事先设置一些联系人，在紧急情况（比如老人摔倒了站不起来）下可以通过语音alexa alert all my friends等等来让echo通知你的朋友。这对于独居老人是非常贴心的。

更多关于智能家居的介绍，欢迎移步我的文章[自己动手改造智能家居生活](http://grapeot.me/zi-ji-dong-shou-gai-zao-zhi-neng-jia-ju-sheng-huo.html)。
