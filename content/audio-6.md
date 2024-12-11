Title: 音频碎碎念（六）—— 模电
Date: 2022-12-26 19:00
Category: Life
Tags: Sound Engineering, Chinese
Slug: sound-engineering-6-analog-circuits


---

本文是《音频碎碎念系列》系列的一部分：

* [音频碎碎念（一）—— HiFi科学派](/sound-engineering-1-scientific-hifi.html)
* [音频碎碎念（二）—— 响度的玄学](/sound-engineering-2-loudness.html)
* [音频碎碎念（三）—— 频率的玄学](/sound-engineering-3-frequency.html)
* [音频碎碎念（四）—— 线材的玄学](/sound-engineering-4-cables.html)
* [音频碎碎念（五）—— 听音环境](/sound-engineering-5-environment.html)
* 音频碎碎念（六）—— 模电（本文）
* [音频碎碎念（七）—— 放大器](/sound-engineering-7-amplifiers.html)
* [音频碎碎念（八）—— 放大器输出级](/sound-engineering-8-amp-output-stage.html)
* [音频碎碎念（⑨）—— D类放大器](/sound-engineering-9-class-d-amp.html)
* [音频碎碎念（十）—— 地狱听音环境实操](/sound-engineering-10-real-example.html)

---

今日HiFi玄学：看了一天模电，已经被无穷多种电子管弄疯了。。几个感想：

1. 模拟电路设计里面已经有了很多计算机或者说控制论的基本思想。比如我们天天用的把交流电转成直流电的稳压电源，我原来以为就是先用二极管电桥整流，然后用电容滤波就好。但后来发现它的核心部件其实是一个[运算放大器](/sound-engineering-7-amplifiers.html)。这个运放跟CPU一样，不停比较当前输出电压和给定的参考电压的大小，然后根据这个关系来控制一个电阻的阻值，从而形成一个负反馈回路来维持电压稳定。这就是一个小计算机/微型控制器啊。但它从头到尾都是模电元件构成的，三极管，电容电感电阻等等。太神奇了。
2. 模拟电路里面有很多不完美的特性也很有意思。比如基本上所有音频系统里面都要用到的一个东西是变压器。变压器有个铁芯用来增加磁性。但铁磁性物质有个问题是磁滞回（类似机械里面的旷量，搜索关键字磁滞回曲线）。这就导致变压器的响应不是完美线性，输入小了会没反应，大了会饱和，所以会导致音频变鸭器的输出信号里面有失真，会引入谐波失真。这个东西很难消除，所以有很多精力花在让这个谐波尽可能好听上，比如引入偏置电流，让这个谐波尽可能是偶次谐波等等。
3. 这又引出一个问题，是[总谐波失真](/sound-engineering-8-amp-output-stage.html)其实是一个非常差的指标，因为它完全没有考虑谐波的特性。比如人对低次谐波其实非常不敏感，但对高次谐波很敏感。所以完全有可能一个放大器A的THD比B要大，但因为A的谐波次数更低，所以人耳听到的A的失真比B反而要小。声学工程界基本上不会用THD来评价一个放大器的好坏，这可能是为什么[HiFi科学派](/sound-engineering-1-scientific-hifi.html)推荐的THD完美的廉价放大器纸面参数好看，但听感很差的原因。