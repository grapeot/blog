Title: 一些关于天文摄影自动对焦算法的思考和尝试
Category: Computing
Date: 2024-02-26 16:00
Tags: Astrophotography
Slug: auto-focus

我最近因为想利用AI来控制天文摄影设备，所以正在开发一个类似NINA的系统。也因此开始研究自动对焦算法，有一些思考分享一下。在详细介绍算法之前，我想先谈谈我对自动对焦的两个基本思考。首先，如果我们有两种不同的算法，A算法和B算法，我们应该如何判断哪个效果更好。其次，自动对焦为什么难，我们需要面对和解决哪些技术挑战。

关于如何测量算法效果，方法相对简单。我们可以在不同的天气/环境，不同的镜子/相机/电调，不同的光学场景下，通过改变电调的位置，在合焦点附近及其远处拍摄图像，从而获取不同电调位置的图像。我们会拍摄两个版本的图像：第一个版本是短曝光图像，作为自动对焦算法的输入，模拟实际自动对焦时的情况；第二个版本是长曝光图像。因为短曝光图像往往难以清晰显示哪个对焦位置更佳。长曝光图像在导星和环境稳定的前提下，可以作为一个清晰的标准，帮助我们判断哪个对焦位置更优。

通过在多种场景、多种设备、不同光学条件下收集数据，我们可以构建一个包含自动对焦输入数据的测试数据集，并通过分析长曝光数据作为ground truth，确切地知道最佳合焦点。当比较A和B两种对焦算法时，我们可以看它们在整个测试集上与标准答案的平均差距，差距越小的算法就是更好的算法。这种方法好处是，比如一个用户抱怨某种特定场景自动对焦算法有问题，我们做了一个修复，解决了这个特定场景的问题，但可能反而弄挂了其他3个场景。如果我们有一个标准的、全面的测试集，我们就能发现这个修复版本可能反而导致整体性能下降。这种情况下，算法不仅没有修复问题，反而可能是一个退步，不能发布。

那自动对焦为什么难呢？主要有四个方面的因素。
首先，自动对焦大多采用短曝光。在这种情况下，分析的图片本身星光较弱，进行星点检测和大小判断相当具有挑战性。
其次，虽然在合焦点附近，由于星星较亮，进行星点检测和分析相对容易，但自动对焦不仅需要在合焦点附近进行判断，更多时候需要在失焦处检测星点并判断其大小。在这些区域，星点更暗淡，边界也不那么清晰，这给算法带来了更大的挑战。
第三个因素是光学望远镜的光学缺陷，如彗差，可能导致星点不是正圆，这使得我们难以使用Moffet或高斯函数来拟合星点，从而准确判断其大小。此外，某些反射望远镜在失焦时因为蜘蛛架的衍射星点形状奇特，进一步增加了检测和分析的难度。
最后，自动对焦算法是一个在线算法，而不是离线算法。它需要即时根据每张图像的不完整信息做出决策，决定是继续前进还是调头，这在信息往往不足以判断合焦点的情况下，对算法的要求更高。
因此，一个优秀的自动对焦算法不仅应在合焦点附近表现出色，在相对失焦的情况下也应保持稳定，不仅对圆形明亮的星点有效，在星点边缘模糊或存在像差的情况下也能良好工作，不仅在收集到足够多的图片后能确定合焦位置，还能基于部分信息做出合理的决策。

下面我想简单介绍一下我目前正在实验的一个算法。这个算法首先对每张图进行星点检测。不过，与对检测出的星点进行形状测量，然后依靠某种数学模型计算星点半径的传统方法不同，我们采取了另一种方法。因为传统方法在面对星点较暗或边界模糊、形状不规则时往往不够稳定，得到的数据不可靠，我们的方法是观察检测出的星点周围较大的区域（目前选定的是30×30像素的范围），计算这个区域的信息熵。信息熵的值越小，意味着信息量越高；值越大，则说明区域整体更杂乱，基本上是噪音。通过这个信息熵，我们可以非常稳定地描述当前星点的质量，这是第一个技术决策，即使用统计量而不是基于星点拟合来进行自动对焦。

第二个技术决策涉及到在计算出不同位置的信息熵后，我们可以观察到一条曲线。下一步需要通过曲线拟合来进行内插，以找到合焦点。一个重要的决策是，相比于那些偏离曲线最低点较远的地方，我们应该更加重视那些在合焦点附近或信息熵较低的数据点。这在数学上很容易描述，即通过加权曲线拟合，给予那些信息熵较低或在曲线上位置较低的数据点更高的权重。这样，曲线拟合就会更倾向于贴近合焦点附近的数据点，而对于那些偏离较大的数据点，即使拟合不上也无关紧要。通过这种方法，我们可以充分利用那些在合焦点附近信噪比较高的数据点，获得更高的分辨率，确切地知道合焦位置，即使它不在两次对焦步骤的确切某一步上，而是在两步之间，也能用非常高的分辨率确定具体的合焦位置，避免受到那些实际上非常不合焦的地方的干扰。

我在自己的远程台上实践了一下这个算法，使用折射望远镜进行了测试。下面这张图展示了信息熵随着对焦步数的变化情况。我们可以看到，即使在f/4快镜和离合焦点大约500步的地方，这个曲线依然非常稳定，没有出现变成先高后低的折线。这个曲线不对称是一个比较常见的现象，是因为望远镜焦前和焦后的光斑未必一致。还得在更多的数据和器材上测试才能知道这个算法效果怎么样。至少现在鸭哥版NINA（叫NIYA）已经可以完整的执行拍摄任务了（goto，解析，自动对焦，导星，制冷，拍摄，park等等）。

![Auto focus curve fitting](/images/auto_focus_curve.png)