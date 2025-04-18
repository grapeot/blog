Title: 音频碎碎念（二）—— 响度的玄学
Date: 2022-12-22 19:00
Category: Life
Tags: Sound Engineering, Chinese
Slug: sound-engineering-2-loudness


---

本文是《音频碎碎念系列》系列的一部分：

* [音频碎碎念（一）—— HiFi科学派](/sound-engineering-1-scientific-hifi.html)
* 音频碎碎念（二）—— 响度的玄学（本文）
* [音频碎碎念（三）—— 频率的玄学](/sound-engineering-3-frequency.html)
* [音频碎碎念（四）—— 线材的玄学](/sound-engineering-4-cables.html)
* [音频碎碎念（五）—— 听音环境](/sound-engineering-5-environment.html)
* [音频碎碎念（六）—— 模电](/sound-engineering-6-analog-circuits.html)
* [音频碎碎念（七）—— 放大器](/sound-engineering-7-amplifiers.html)
* [音频碎碎念（八）—— 放大器输出级](/sound-engineering-8-amp-output-stage.html)
* [音频碎碎念（⑨）—— D类放大器](/sound-engineering-9-class-d-amp.html)
* [音频碎碎念（十）—— 地狱听音环境实操](/sound-engineering-10-real-example.html)

---

之前思考了为什么hifi领域玄学横飞，摄影领域却少很多的情况，也跟大佬交流了，一直想不明白。觉得是自己想得太多而学得太少，所以去看了（正在看）一本大部头的音频教科书。现在感觉这个玄学其实不能怪爱好者们，是因为我们的耳朵本身就充满了玄学。我现在倾向认为[科学派（哈曼神教）](/sound-engineering-1-scientific-hifi.html)无限扩大了频率响应等曲线的重要性，在器材选择方面价值相当有限。我们不说什么复杂的理论，就看怎么测量一个声音有多响。这玩意远远不是读一下声压级的事情，因为我们的耳朵：

1. 对不同频率的声音响应不一样。一样声压级的信号，如果[频率不同](/sound-engineering-3-frequency.html)，大脑感觉到的响度也是不一样的。这个和眼睛还比较类似，但从下一个开始就不一样了。
2. 对不同带宽的声音响应不一样。一样声压级，一样平均频率的信号，如果带宽不一样，大脑感觉到的响度也是不一样的。
3. 对不同持续时间的声音响应不一样，在一定范围内，声音持续时间越长，感觉越响。
4. 听见的频率和信号的频率不一样。人耳是一个非线性系统，比如同时听到600Hz和700Hz的声音，大脑会觉得听到了同时听到了400，500，600，700Hz的声音。所以根据信号频谱来计算响度也不靠谱。
5. 前后的声音信号还会相互影响。比如100ms之前听了一个信号A，它会对100ms后（现在）的信号B产生压制，导致B听起来的响度更小。其实MP3压缩就利用了这一点。
6. 那我不测量/计算响度，就光测一下人耳这个系统的pulse response总行吧。对不起也不行，人耳是个主动系统（有源系统），它就像一个劣质的[放大器](/sound-engineering-7-amplifiers.html)一样，即使在静室里也自己在生成各种背景噪声，叫做otoacoustic emissions（不是耳鸣）。这个本身也会干扰测量。

就尼玛特别玄学。。我不是说测量是绝对不可能的，了解了这些之后我甚至觉得哈曼曲线这种找人主观打分是最靠谱的测量方法。但问题在于绝大多数哈曼神教的信众抛弃了哈曼曲线的应用前提，认为音响设备的好坏用几个简单的曲线就可以衡量，有绝对的优劣。这种对测量复杂度敬畏的丧失本身就造就了一种傲慢。而傲慢是科学最大的敌人。我不觉得这种极度简化复杂度，天天想着300元设备+EQ能战10万设备的"科学派"是对待音频系统的理性态度。（BTW我不是说这个不可能，因为很多高价器材玄学也特别多）

但同时我也不是说就应该玄学。最近我在看一些国内的论坛，[模拟电路](/sound-engineering-6-analog-circuits.html)咱也看不懂，主要就看一些数字相关的讨论，被里面伪科学的成分实在震惊了。9000美元的电源线咱就不说了，毕竟是高压交流电，还是有可能造成影响的。一帮人在那讨论USB线材的好坏，一根HiFi USB线卖到1000美元就比较魔幻了。你是数字信号，再烂的[线材](/sound-engineering-4-cables.html)也不可能把1变成0，0变成1。好吧，就算USB里面有+5V这个电源线，要是碰上打雷，还可能对DAC的模拟部分造成差模干扰（至于打雷的时候能不能听见先不讨论）。一帮人在那讨论光纤线的好坏，说单模光纤音质比多模好就看不懂了。你特码连电源都没了啊魂淡，光也不可能对任何电路造成串扰。很多高端品牌（几万美元）的设计也特别奇怪。比如数字音频信号的传输，一大问题是jitter，就是因为音频信号是没有时间戳的，所以信号传输的过程中如果一会快一会慢信号就会失真。所以很多高端品牌都在做类似原子钟一样的皮秒精度的晶振，然后收个几万美元。可是这玩意不是加个时间戳就完全解决了么？tcp协议的序列号，电影工业的timecode都是现成的实现，精度远高于最高MHz的音频信号，其实不用花钱。还有一些高端品牌着重强调放大器内部做了物理隔音，保证振动不会影响到放大器，作为卖点之一收几万美元。可是你是个电子电路啊，没有任何移动组件，关物理振动什么事情。所以对这个领域了解越深，越觉得水很深，厂家和用户若有意若无意都在把水搅浑。在花钱之前需要先做好学习。

当然我也没有学习好，可能过段时间观点还会发生变化。只是感觉现在音频消费领域的发展还是非常野蛮的，没有特别科学的指导。从最早的玄学挂帅到哈曼神教本身已经是不小的进步了，但还是一方面跟我个人的体验很不相符，一方面迷信的色彩还是在。我自己也要做一些实验，来看看有没有可能推动这个领域发展一下。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
