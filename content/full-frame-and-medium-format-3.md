Title: 全幅与中幅（三）
Date: 2020-01-22 15:00
Category: Life
Tags: Photography, Medium Format, Full Frame, Chinese
Slug: full-frame-and-medium-format-3


---

本文是《全画幅和中画幅系列》系列的一部分：

* [全幅与中幅（一）](/full-frame-and-medium-format-1.html)
* [全幅与中幅（二）](/full-frame-and-medium-format-2.html)
* 全幅与中幅（三）（本文）
* [全幅与中幅（四）](/full-frame-and-medium-format-4.html)
* [全幅与中幅（五）](/full-frame-and-medium-format-5.html)

---

（本文成文于2018年5月）

最近在一些讨论中感觉不少人对由幅面变化引出的曝光和信噪比的变化有些误解。但一旦牵扯到画幅的讨论就不可避免曝光，景深，信噪比的比较。在这里想引入一个直观的比方/模型，希望能讲清楚这个问题。

如果不讨论严谨的信噪比的定义和公式，一个简便的模型是，我们可以把传感器看成一个个水桶。曝光的过程就是下大雨，每个水桶里面会积水（光子的能量）。然后我们会拿一个尺子去量每个水桶里面的水位（电压）。出来的数值经过一些变化就成了像素值。从这个简单的模型出发可以理解很多和曝光和信噪比有关的问题。

首先，噪音/噪点是怎么产生的。如果不考虑光强本身的随机噪声（比如一堵亮度均匀的白墙不同区域发射的光子数量有些微差别）的话，我们在照片中看到的噪点主要有两个来源。平时我们所说的噪声最主要的来源是这个尺子不是一个无限精确的尺子，而是有一定精度的。即使是几个水桶有相同的水位，也会得到不同的结果，在图像上的表现就是噪点了。比如这个尺子的精度是1mm，也就是说读数可能是实际水位正负1mm。那么你测量5mm的水位的时候就可能有4~6mm的读数，这是大约20%的相对误差。但你测量200mm水位的时候就可能有199~201mm的读数，这就是0.5%的相对误差。这就是为什么你在图像中会先在暗部看到噪点的原因。那如果我想在不改变水桶和尺子（传感器和电路）的情况下增加测量精度（信噪比）怎么办呢？简单，往里面多倒点水就好了。比如增加一档曝光，5mm的水位就变成10mm了，你回头在修图软件里面再把这档曝光拉回来，图片的亮度不变，但相对误差就变成了10%而不是20%了。这就是适当过曝以提升信噪比的直观原理。当然这种方法受到多种方法的制约，比如增加曝光要么增大光圈要么增大快门，增大光圈可能会因为各种像差损失画质，增大快门可能会手抖损失画质。或者如果水桶装满了，那量出来水位根本就是错的（偏低）也会伤害信噪比。总之这是个在一定范围内适用的小技巧。

另一种噪音是长曝导致的热噪音，可以理解为如果一直用水桶接水，一次接半个小时，桶会产生不同的形变甚至自己涨点水出来从而影响水位。这个形变的方式和程度是制造过程中产生的，所以产生的噪点的样式也是固定的。要想纠正的话可以用同样的参数挡住镜头长曝拍一张，然后从正常长曝的照片里面减掉，可以相当程度解决这种噪声。

那么现在问题来了，如果我从全画幅到中画幅的数码相机，或者从M4/3系统到全幅，会有什么变化呢？首先物理上这个变化是非常naive的。就是等比例放缩而已。比如4433中画幅系统，就是全幅的所有东西在每个维度上放大1.3倍。所以传感器的面积大了1.3x1.3-1=68%，在视角相同的前提下，镜头的焦距也长了1.3倍。在同光圈的情况下，镜头的入射瞳直径也变为了原来的1.3倍，也就是入射光的能量比原来大了68%。

那这些变化分别有什么影响呢？在光圈不变的前提下，首先根据[景深](/focal-length-in-photography.html)公式，焦距f增大其他因素不变，景深肯定是变浅了的。然后对曝光来说是没有影响的。也就是对于同样的ISO和快门的组合，出来的图片的亮度是一样的。具体地说这是因为，从全幅变到4433中幅，虽然入射光的能量大了68%，但底也大了68%，所以单位面积上获得的能量是一样的，最终的图像的亮度也是一样的。如果进一步思考的话，其实有一些有意思的问题。尤其是，入射光的能量（通光量）到底是什么东西？直观上它的定义是与入射瞳相交的所有光线的能量对面积的积分，但这个"所有光线"应该怎么算？从纯物理的角度出发，应该把镜头整个成像圈 (imaging circle)的光都算上，但这毫无实际意义——因为这样的话对同一个镜头，甚至对同样成像圈的不同镜头，不论我用什么底，得到的通光量都是一样的。这是个很trivial的物理量，对于分析包括不同幅面的影响在内的很多问题并无参考价值。所以一般来说，我们说的通光量其实指的是被传感器截获的光的能量。从这个定义出发就有了第二个问题，通光量和信噪比到底是什么样的关系？换言之，我们让相机接收到更多的光，是不是就可以得到更好的信噪比？

直观上这是符合直觉的。一般的噪声水平是固定的，信号的强度越大，信噪比当然越大。仔细思考的话，"接收到更多的光"其实有两种方法，一个是不改变幅面，单纯增加曝光（比如增大光圈，延长曝光）；一个是不改变曝光，单纯增大幅面。前者我们在上文已经讨论过了，因为每个桶里面接到了更多的水，所以信噪比是升高了的。后者从水桶模型出发也有一个直观的解释。

首先要比较两个传感器，我们得先搞清楚什么参数是一样的，什么参数是不一样的，否则吵半天发现基本假设不同，完全是鸡同鸭讲。我们先从最简单的情况出发，假设有一个M4/3系统的传感器和一个全幅传感器的所有参数包括数码分辨率都是一样的，也就是说有同样多的桶，每个桶的尺寸是一样的，每个桶的尺子也是一样的。但因为全幅相当于M4/3系统整个拉长拉宽了2x2倍，所以等于全幅的每个桶上面套了一个4倍大小的漏斗。这样想的话全幅的水位就会4倍于M4/3，所以信噪比自然也就更高了。但这种假设会带来一个问题，全幅的水桶更容易满，所以更容易过曝，但这是不合理的。因此我们需要修正一下前面的假设，让全幅的水桶的高度也是M4/3的四倍高，但尺子还是一样的，这样就符合真实情况了。

我们也可以从另一个角度得出同样的结论。我们先假设全幅的桶和M4/3的桶完全一样，包括占地面积也一样。那这样全幅的传感器就有4倍多的桶。大家用同样的尺子测量，各自得到了一些读数。但为了对比的公平，二者的数码分辨率必须相同，所以全幅会把相邻的四个桶的读数取个平均，得到最终每个像素的读数。这样其实就是物理里面的多次测量取平均，信噪比自然也会提升了。

回到通光量的讨论。网上有一种说法是，中幅比全幅信噪比大是因为同样的光圈，入射瞳更大所以通光量更大，通光量更大所以信噪比更高。这种说法是有问题的。入射瞳更大所以通光量更大这个逻辑针对的理论上的通光量的定义，也就是不管底有没有接到光，只要成像圈不变，我都算到通光量里面。但如果我们用上面我们的定义，入射瞳更大通光量不一定更大，信噪比也不一定更高。比如如果不换底单纯增大焦距光圈不变增大入射瞳，但还是用个全幅在那接光的话底接到的光能量和信噪比都是不变的，只有用个中幅在那接光信噪比才会增大。换言之，中幅比全幅信噪比大是因为底变大了，不是因为入射瞳变大了。入射瞳变大是我们为了比较公平给定的一系列约束的结果，而不是中幅信噪比之所以更高的原因。

上面牵涉到了一些对数码分辨率的讨论。那么，如果幅面不变，单纯增加数码分辨率，对于信噪比有没有影响呢？从水桶模型的角度出发，单纯增加分辨率对信噪比是没有影响的。这是因为虽然水桶的数量更多了，可以通过多个水桶取平均的方法来增大信噪比，但每个水桶的水位下降了，噪声更大了，如果定量计算的话会发现二者正好抵消。换言之，如果同样是全幅传感器，用同样的光学系统，唯一的区别是传感器的数码分辨率不同，在这种情况下把照片打成同样的物理尺寸，从噪点的角度看二者应当是一样的。但这是否就意味着增大分辨率就毫无用处呢？也不是，因为分辨率和信噪比是两个独立的概念。根据奈奎斯特采样定律，如果分辨率不够，一些细小的pattern就不会在照片上体现出来。而信噪比针对的是信号和噪音的比例，直观地看就是有多少噪点。有可能两张图片的分辨率不同，但信噪比一样的。反之亦然。

总的来说，水桶模型可以提供不同幅面之间，曝光和噪声方面的一些定性讨论，有助于纠正一些错误认识：增大幅面会影响曝光；只要把焦距/通光口径做大不增大幅面就能增大信噪比；增大数码分辨率有助于增大信噪比等。也许你已经注意到了，这个水桶模型的缺陷是，我们没有考虑ISO。因此如果要探讨ISO对信噪比的影响的话就不能用这个简单易懂的模型了。而且这个模型目前没有定量计算的能力，所以只能做一些单变量的定性探讨，对于多变量之间的权衡就无能为力了。不过考虑到我的目标是把复杂的东西讲得简单易懂，这个模型还是有一定意义的。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
