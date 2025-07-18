Title: 当AI陷入鬼打墙：一次关于协作策略的复盘
Date: 2025-07-17 23:00
Category: Computing
Tags: AI, Chinese
Slug: ai-unlearn

因为各种墙，每次我想和朋友截图分享一段精彩的AI对话，都要做一个不大不小的project：小心翼翼地滚动屏幕，截一张，再滚，再截一张……最后用Tailor之类的App拼接起来。这个过程繁琐、枯燥，而且常常失败。所以，在开发我自己的Multi-Agent Workbench iOS客户端时，我下定决心：必须内置一个一键长截图的功能，彻底终结这个噩梦。

我的第一步和以前一样，是Document Driven Development。我先和AI探讨了要实现这一点可能的技术方案。AI给了四种不同的方案。因为我的这个客户端为了省事不是原生客户端，而是一个WebView套壳，所以我选用了利用JavaScript和HTML的两种方案作为备选。然后让AI分别实现，看看效果怎么样。

但两种方案都遇到了诡异的问题。AI给出的代码在逻辑上天衣无缝，但就是无法正确渲染。我花了点时间让AI打log调试，但很快陷入了毫无头绪的境地。在纠结的过程中，我脑中逐渐亮起了一个红灯：AI已经连续两次在同一层面的问题上失败了。这让我开始警惕，问题可能不在我的提示词不够精确，而在更高层的技术策略。所以我没有死磕技术细节，而是回头把这个症状讲给另一个更擅长做调研和分析的 Planner AI 听，从更高层的角度问它有没有什么别的技术方案。

在这里我也跟它叙述了Tailor这个app。Tailor似乎仅仅是根据图像内容来进行的长图合并，而没有进行任何JavaScript或者网页上面的处理。我没有问AI怎么具体解决我的问题，而是问它这到底是什么原理。这一刻我和AI在互相启发：我提供了商业和技术直觉，AI则负责将这个模糊的直觉，转化为可执行的技术情报。 它迅速调研并带回一个令我惊喜的发现：苹果原生SDK就支持高效的图像对齐。具体地说，给定两张图片，可以用iPhone的GPU非常高效地算出来：图像A跟图像B要经过怎样的平移、缩放和旋转才能对齐。

这对我来说是一个新知识。所以接下来我就又切回了执行模式，把 AI 的调用结果直接扔给了 Claude Code，让它去写代码。但写出来结果还是不对。我进行了一些 debug，让它输出了一些中间结果，发现牛头不对马嘴，于是又一次被卡住了。

这个时候，我就又一次复查是不是方向错了。这次回头去看 AI 给我的答案，发现里面不仅有解释，而且给了一个苹果的例子程序。我把那个例子程序下载下来，在我的数据上一跑，一遍就成功了，而且速度特别快。这一下让我轻松了很多，因为这改变了问题的性质。这说明我们找到了一个“最小可行真相”（Minimum Viable Truth）。在这之前，我们是在依赖AI的技术力在黑暗中航行；在这之后，我们有了一个不可动摇的技术锚点，它确定是work的。我们下面所有的工作只要围绕这个锚点进行迭代和扩建就好了。

这条路确实更加稳妥。我回到Claude Code，让它读了一下这个苹果的例子，然后让它实现一个最简单的原型：就截一张图，向下滚动一些，再截一张图，再严格按照苹果的示例，合成一张稍微长一点的图，保存在相册里。Claude完美地实现了这个目标。然而，在处理多图合成的循环时，Claude再次陷入了困境。尽管我们有这个技术锚点，但它似乎还是无法驾驭更复杂的逻辑。

到了这里，我开始意识到，这个任务可能到达了Claude的边界，它可能没有能力看出问题在哪里。但我还是没有亲自下场debug，而是切换成了Cursor里更适合分析，谋定而后动的Gemini 2.5 Pro，把所有的log，背景，问题都交给它。我给它的指令只有一个：别写代码，告诉我问题出在哪。两分钟后，Gemini交出了它的诊断报告：像素与点的单位混用，以及一个坐标系颠倒的bug。当我把Gemini的分析贴给Claude Code了以后，它很快就把代码改好了。完全正确。

经过这次曲折的迭代之后，我终于用上了全自动截图。而且这个过程我觉得蛮有启发：

* 第一，最有效的提示工程有时候不是优化语言，而是优化问题的定义本身。
* 第二，从一个能工作的程序出发往往会给 AI 的工作流带来极大的确定性。
* 第三，“哪个 AI 模型最好？”这个问题可能本身就不对。我们应当关注的是每个 AI 模型的能力边界在哪里，对于当前这个任务，哪个 AI 模型最合适。

一个有意思的观察是，在整个过程我没有纠结任何技术细节。我没有去看具体的 JavaScript 或者 Swift 的代码对不对，也没有去手工去干预AI选择的数据结构和算法。这些传统意义上有技术力的活我都没有碰。但是，我把大多数的时间花在定义问题、分析竞品、选定技术方向，以及应用适合 AI 的思维框架上。正是因为我能够及时unlearn我引以为豪的技术力，才能让我花三个小时就写出来了一个自动截长图的app，反而抓住了生产力的提升的杠杆。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>