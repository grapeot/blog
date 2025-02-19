Title: 深空摄影器材从观望到破产（五）——控制系统的选择
Date: 2023-04-30 22:30
Category: Life
Tags: astrophotography, Chinese
Slug: astrophoto-tutorial-5


---

本文是《深空摄影器材从观望到破产系列》系列的一部分：

* [深空摄影器材从观望到破产（零）——引子](/astrophoto-tutorial-0.html)
* [深空摄影器材从观望到破产（一）——入门指南](/astrophoto-tutorial-1.html)
* [深空摄影器材从观望到破产（二）——赤道仪的选购](/astrophoto-tutorial-2.html)
* [深空摄影器材从观望到破产（三）——天文相机的选购](/astrophoto-tutorial-3.html)
* [深空摄影器材从观望到破产（四）——望远镜的选购](/astrophoto-tutorial-4.html)
* 深空摄影器材从观望到破产（五）——控制系统的选择（本文）

---

本文主要介绍天文生态摄影中心的控制系统。控制系统主要是一种电脑软件，具有多种不同的用途。各个控制系统的差异主要体现在两个方面：一是所提供的功能（以及未提供的功能）；二是它们的易用程度和稳定性如何。我们可以先了解一下控制系统提供了哪些功能，然后再探讨如何选择合适的控制系统。

## 控制系统

对于控制系统来说，它有七大常见功能和三大高级功能。

1. 它的第一个功能是GoTo。当你对准[极轴](/astrophoto-tutorial-2.html)后，比如想让望远镜指向猎户座大星云。在没有控制系统和电脑控制赤道仪之前，我们只能用星桥法，逐渐通过肉眼或低倍寻星镜来定位M42的位置。大致确定位置后，再进行长曝光确认。这个过程我以前也经历过，非常痛苦，因为它不仅要求我们在黑暗的夜空中定位一个肉眼看不见的天体，另一方面，它也对寻星镜和主镜的同轴提出了很高的要求。很多时候，调整起来需要二十分钟到半小时的时间才能找到目标。但是，在有了控制系统之后，只要在手机APP或电脑上点击"猎户座大星云"，电脑就会控制赤道仪自动转过去。

2. 第二个功能是解析。我们之前的文章提到过，解析的意思是电脑控制主相机拍摄一张图片，然后检测图片中的星点，并与已有的星图进行比对，从而计算出照片中心的坐标的赤经和赤纬。这个功能与GoTo功能是相互关联的，因为很多时候，由于极轴误差、地方时和北京时间的误差等原因，我们实际指向的方向与想要指向的方向之间存在差异。这时，通过解析比对星图并计算坐标，我们就可以知道实际指向的位置，并通过计算它们之间的差值来修正赤道仪的坐标系统。同时，这也帮助我们快速地将望远镜指向想要的坐标。  
  在解析过程中，有两个重要因素：焦距和像素大小。要得到正确的解析结果，需要正确填写这两个指标。解析分为两种：非盲解析（non-blind plate solving）和盲解析 (blind plate solving)。非盲解析需要知道大概的赤经赤纬范围，根据焦距和像素大小进行精确的优化。而盲解析是不知道大概的赤经赤纬范围，只根据焦距和像素大小进行全天的比对。在已知大概区域的情况下，非盲解析可以快速得到更精确的赤经赤纬。这两种方法都有应用，但一般来说，在控制系统里面使用的是盲解析。

3. 第三个用途是拍摄计划，这个相对容易理解。例如，今天我想拍两个目标：一个是M42，另一个是海鸥星云。由于它们在天球上的位置不同，上半夜可能更适合拍M42，下半夜则更适合拍海鸥星云。所以我可以先拍三个小时的M42，然后切换到M70进行拍摄。把这些序列事先准备好，并让电脑按顺序执行，这就是拍摄计划。

4. 第四个用途是中天翻转。虽然中天翻转可以仅通过[赤道仪](/astrophoto-tutorial-2.html)来完成，但为了避免对拍摄的干扰以及合理安排其他事项，我们还是用控制系统来进行控制。例如，如果只用赤道仪来控制，可能在翻转的那一刻我们正在拍一张单帧，这样就会浪费一些拍摄时间，尤其是在单帧时间较长时损失更严重。在这种情况下，我们可以让控制系统和中天翻转相互配合。当控制系统发现一帧需要拍摄20分钟，但离中天翻转只有10分钟时，我们可以等到中天翻转完成后再开始拍摄，这样就可以节约时间。  
  中天翻转的原理其实很简单，控制系统会不断地给赤道仪发送指令。如果这个指令成功触发了中天翻转，它会发现解析的图像转了180度，也就是解析出来的方向跟之前相比变了180度。控制系统通过这种方式来识别中天翻转已经成功。

5. 第五个用途是处理意外情况，例如出现云层或导星丢失。在这种情况下，控制系统可以在一定程度上提供解决方案和预案。比如，如果发现出现云层或导星丢失，此时如果仍然按照之前的程序进行自动对焦，星点就会飞掉，即使后面云散了也无法恢复正常拍摄。另一种可能的用法是将控制系统不仅连接到望远镜，还连接到远程天文台的可移动观测顶。这样，在发现出现云层时，系统会自动触发关顶，从而有效保证设备安全。

6. 第六个用途是进行校准场的拍摄，尤其是平场的拍摄。当然，在有暗场滤镜的情况下，也可以进行暗场和偏置的拍摄。此时，控制系统可以与平场板沟通，关闭平场板并打开灯光，或者在预定的时间拍摄天光平场，从而实现这些校准场的自动化拍摄，达到完全的无人支持。

7. 第七个用途是抖动。我们之前提到过，为了避免热噪声和坏点，方便在处理过程中把坏点和固定图案噪声去除，我们需要在拍摄几张照片后，控制赤道仪偏移几个或几十个像素的距离。这个功能被称为抖动，控制系统可以灵活地安排抖动。

除此之外，控制系统还有三个较高级的用法。

1. 第一个是多炮。多炮的难点主要在于，一个赤道仪通过横向排列（Side by Side）或者将另一个相机放在重锤杆上等方式，实现一台赤道仪承载多个相机系统。这个控制的难点不仅在于如何控制多个相机系统进行拍摄，还在于如何对两台相机进行同步。例如，当一台相机已经完成自动对焦后，它不能立即进入拍摄模式，因为另一台相机可能还没有完成自动对焦，导致OAG无法开始导星。或者，当一台相机已经完成拍摄时，它不能立即进入下一张的拍摄，因为另一台相机在完成拍摄后，赤道仪可能会产生抖动，导致废片。因此，如何处理多炮是一个相当考验控制系统设计的问题。目前比较流行的支持多炮的控制系统包括NINA和Voyager，但使用基于共享文件的并行编程也可以很容易地实现这一功能。

2. 第二个高级用途是脚本。脚本指的是类似于NINA里面的高级序列。我们可以在传统的计划拍摄这种序列化的程序之外，加入分支结构、循环和意外处理等高级特性，从而让控制系统的工作流更加灵活。它还带来了另一个好处，当一个控制系统可以读取一个脚本的时候，我们可以利用另外一个程序来批量生成一个很大的脚本，然后再让控制系统进行读取。这在比如[广域巡天](/duck-sky-survey.html)等需要牵扯到几十上百个拍摄对象的时候特别实用。包括ZWO的盒子、NINA和Voyager等主流控制系统都支持这一点。

3. 最后一个高级用途是扩展和插件。有很多开放的控制系统，例如Nina，它允许开发者编写插件并与其结合。在这种情况下，我们可以引入许多第三方工具。例如，我们可以与特定品牌的赤道仪（如AP）进行更好的沟通和可视化，或者将不同用户当前拍摄的多个图像汇总和展示，以便大家方便地挑选目标等。

流行的控制系统工具主要分为三个现代工具和一些老派工具。现代工具包括ZWO盒子、NINA和Voyager，它们的目标用户依次是从萌新到大佬。这些工具的复杂程度、界面复杂度和功能强大程度也是逐渐增加的。对于没有接触过天文摄影的新手，我们更推荐ZWO盒子，因为它隐藏了很多不必要的细节，门槛特别低。但相应的缺点是在降低门槛的同时，它的天花板也被降低了。很多时候，当我们需要一些定制化功能时，它无法实现，因为它把这些接口隐藏起来了。所以在熟练掌握天文摄影之后，可以考虑学习和熟悉NINA或Voyager等控制系统。

此外，还有一些比较老派的控制系统，如SGP。但是，由于这些系统逐渐跟不上最新的硬件，现在使用的人相对较少。尽管如此，仍然有很多专家坚持使用这些老派系统。

## 导星系统

在控制系统之外，还有一个类似的电脑软件叫做导星系统，尤其是目前最流行的工具PHD2。我们之前在赤道仪介绍中提到过导星系统，这里我们会更详细地介绍它的用途、算法和注意事项。

首先，导星系统的主要用途是针对[赤道仪](/astrophoto-tutorial-2.html)的周期误差进行频繁的修正，从而保证赤道仪的跟踪误差被限制在一定范围内。导星系统的算法非常简单，感兴趣的同学可以去阅读PHD2的代码。这些算法其实都没有达到PID算法的程度，而是非常直观的闭环控制算法。

然而，需要注意的是，导星系统中赤经和赤纬使用的控制算法是不一样的。这是因为赤经始终在运动，而赤纬在理想情况下是静止的。因此，对于赤经来说，它只需要进行速度的调整就可以完成导星的目标。在这个过程中，整个轴始终是朝一个方向运动的，因此回差的影响相对较小，或者说基本上不受回差的影响。

然而，赤纬则不同。赤纬的修正方向可能是向前，也可能是向后，因此它受回差的影响更大。这就要求导星算法对于回差要有不同的处理。

为了实现优秀的导星效果，或者说让导星成为现实，校准是一个必不可少的步骤。所谓校准，就是让导星控制系统通过控制赤道仪，使其朝某个方向移动一小段距离。接着，通过测量这段距离移动后，星点移动了多少像素。这样，我们就可以构建一个标尺。这样，当我们想让导星相机上的星点移动x个像素的时候，就知道要向导星系统发送一个多久的导星信号。

常见的导星硬件主要有两种：第一种是导星镜，第二种是偏轴导星。导星镜是通过一个较小的望远镜和一个较小的相机组成一个额外的拍摄系统。导星镜的画质不需要特别好，因为它不会影响主镜的成像或最终的成片的星点。大多数导星镜都不是APO设计。导星相机通常也只需要小靶面相机，如USB 2的行星相机，因为它们不会直接影响成片，也没有高帧率的要求。

偏轴导星是在主镜的光路上插入一个小棱镜，将主镜的光分一部分出来。换句话说，在主镜成像场的边缘，将这部分光分出来单独作为导星。这两者各有优缺点。偏轴导星的优点是它的焦距与主镜的焦距相同。同时，偏轴导星没有导星镜和主镜之间的刚度问题，因此精度更高。在做防结露处理时，偏轴导星只需针对主镜，而导星镜系统需要单独处理。

但是，偏轴导星也有一些问题。一般来说导星系统对曝光要求较高，如需在三秒或五秒内完成曝光。相比于主镜的300秒或600秒，这是非常短的时间。在焦距特别长的情况下，偏轴导星的视野里可能没有足够的星星来完成导星，这时偏轴导星就不太现实，需要依赖导星镜系统。第二个缺点是偏轴导星通常只分主镜成像圈边缘的光，那里的星点质量可能不太好，这在一定程度上会影响导星的质量。第三，偏轴导星需要吃掉大约20mm的后截距，但导星镜系统则不影响主镜的后截距。因此，在选择导星镜和偏轴导星之间，需要权衡各自的优缺点。

在硬件之外，导星系统还要注意一个问题在于分辨率的适配，这里的分辨率是指每像素对应多少角秒。从经验来看，导星系统的分辨率应该是主镜分辨率的三分之一到三倍左右。当然，大多数人不会让导星镜的焦距比主镜还要长，所以一般来说，只要分辨率在主镜的三分之一就可以了。当然，在不明显增加器材重量的前提下，适当增加分辨率也是没有坏处的。例如，如果主镜的分辨率是每像素对应1.5角秒，那么导星系统的分辨率应该是每像素4.5角秒或者3角秒都可以。

总的来说，这篇文章主要介绍了电脑上常见的控制软件，包括控制系统和导航系统。对于控制系统，我们提供了七大基础功能和三大高级功能，用户可以根据这些功能以及自己的应用需求来挑选合适的控制系统。而对于导航系统，我们介绍了它的算法、校准过程以及在使用过程中需要注意的事项。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
