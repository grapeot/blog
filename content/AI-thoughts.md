Title: 人工智能的一些随想
Category: Computing
Date: 2023-02-04 16:00
Tags: AI, Machine Learning, Chinese
Slug: AI-thoughts

玩了一晚上OpenAI的ChatGPT，有一些关于技术的看法：ChatGPT的核心优势两点：1. 它对交互的目的有了很准确的把握；2. 它可以记住上下文，准确知道你在下一句话说的对上一句话的指代是什么意思。还有第3点是它生成的文本都是符合格式的，比如你要叫它分析东西，他会列12345，叫它写信会知道落款等等。但一方面这个GPT-3已经演示过了，一方面只要解决了第1点（目的的理解），基本上就可以做到，所以我没有把这一点列入核心优势。

它的弱点主要在，跟这个世界基本上是脱节的。他可以生成大段漂亮的文字，看起来非常自然，但如果真的去看的话，会发现内容上很多错误。比如生成菜谱，有配料表，第一二三步，看起来很正确，但里面的信息都是错的，比如用高压锅腌咸鸭蛋。生成学术论文，有引用格式也正确，但真的去看他的引用文献的话会发现是编出来的，没这篇文章。这也是GPT-3决定的。GPT-3只是一个文本生成模型，他没有自己的知识库。或者从更抽象的程度来说，GPT-3是一个纯统计的模型，不是rule based，它没有任何硬的约束。所以它适合做一些主观题，给出一些模棱两可的回答。却不适合当作搜索引擎来使用，查阅客观事实。

这两方面的特质决定了[ChatGPT的应用范围](/GPT-API-usage-creation.html)。它很擅长通过对话理解人的意图，所以适合用于客服系统等需要大量交互的地方。在这种场合，它的输出不用是具体的文本（可以是一些搜集信息的追问，但不用提供客观事实），而是某个客服话题，来返回一些文档，从而规避各种事实错误的问题。ChatGPT的远景不应当是一个独立的人工智能（standalone AI as is），因为我个人认为GPT-3这种纯粹基于文本生成的统计模型无法解决事实错误的问题。它的出路在于和知识库结合起来，也就是像笨笨的Siri和Alexa那样加入硬性的规则和知识——或者搜索引擎的索引。这样才能解决事实错误这个痛点。当然，如何平衡软的统计规律和硬的规则是一个很难的问题，技术上也有很多可能的路线。这里不具体讨论。总之，ChatGPT在交互方面给了我们很惊艳的启发，甚至可以直接产生商业价值，但我个人认为这些光鲜亮丽的回答背后暗藏着一种技术路线的尽头，和一种知识+生成模型的模式的希望。

---

之前发过文，介绍对ChatGPT的一些思考。总的来说是觉得媒体过分乐观了。不过我个人觉得里面的确藏了一些革命性的东西，但这个革命不是ChatGPT本身。而是一种思潮。为了解释这种思潮，我们需要先退一步，看看NLP的经典任务。NLP是一个比较零散琐碎的领域，有很多任务。比如给一段yelp review，看它是正面的情感还是负面的情感。给一段话，看里面有没有名人名物（named entity）。从2018年开始，NLP基本被Transformer统一，里面又分成两派，BERT和GPT。二者之间的区别远远不是表面上看起来双向和单向这么简单。二者的训练目标和使用方法是截然不同的。BERT是一种传统的模型，它的训练目标是，给它看很多句子，把这些句子中间的一个词遮住，然后叫它猜这个词是什么。它的使用方法是，在新的应用场景里面用新的数据简单训练（微调，finetune），然后应用。比如上面看yelp review的例子，BERT会看很多很多的文本（不仅限于yelp review），然后得到一个预训练的模型，这一步不需要任何人工标注。然后喂给它yelp review，告诉它这个是正面的，那个是负面的。这样把BERT内部的一些参数进行细微的调整，它就可以完成判断yelp review的态度这样一个任务了。

相比之下，GPT的训练目标是生成一段新的文本。它从头开始训练的目标就是跟人对话。使用方法也是直接跟它对话。比如yelp review这个例子，它在默认情况下甚至不需要看更多的yelp review就可以得到相当好的结果（zero shot learning）。当然你也可以用对话的方式给它看一些例子（叫做instruct），然后它会给出更好的结果。

其实这几年BERT基本上都是比GPT好一截的，因为直接搞一个跟人对话的模型实在是太难了。但从GPT3开始，GPT开始屠榜了，接着又出了ChatGPT，展现出了研究者都很惊讶的上下文理解能力。这里面有一个insight，就是如果想要去完成"理解一件事情"的任务，最好的方法似乎不是去训练一个模型来理解这个东西，而是去训练一个模型来生成这个东西，然后用里面暗藏的逻辑去理解。这个似乎也是合理的，因为我自己就有体会，很多时候以为自己懂了，但真的试图去教别人的时候才发现没有完全理解。所以教学相长好像也是合理的。这就是我说的一个应用范式上的革命。

为什么这是个革命呢，这是因为如果纵观这十几年的深度学习的发展，里程碑性质的东西没几个，但他们都有一个共同的特点：让我们可以用更多的GPU，更多的数据，训练更大的模型。比如AlexNet用GPU end to end训练，一下好了很多。ResNet解决了梯度爆炸的问题，把层数从10层一下推到了1000层，性能爆炸，到现在ResNet改都是state of the art。NLP那边，受制于LSTM很难并行化，相对进展缓慢，直到Transformer可以大规模并行，一下有了突破。接着就反哺CV，Visual transformer继续屠榜，并且催生出了CLIP，Latent Diffusion这样的现象级模型。所以一个主题是，深度学习牛逼的地方就是，只要你给它更多的数据，更复杂的模型，它就能给你更强的智能。到现在都没有看到传统机器学习的饱和的情况。我们这十多年干的事情，就是类似保持摩尔定律，让这个更多数据更多参数的趋势能够持续下去。直到GPT这个东西出现：理解一个东西的最好方法是去生成—这个如果被时间证明真的是正确的道路的话，可能是一个非常根本且重大的发现。这个也不难验证，现在这个观察只在NLP领域成立，CV还没有类似成熟度的研究。所以我们可以拭目以待，看看CV领域有没有类似的规律。对于业内的人来说，这也是一个disruptive innovation的机会。

---

纵观[人工智能的进展](/recent-AI-advancement.html)这么多年的历史，越来越有一个感受，人工智能之所以难只是因为人类太弱鸡。人工智能的定义其实一直在变化。举几个例子：二战的舰炮火控计算机，可以根据目标的距离，方位，速度，风向，根据物理模型进行快速精确的操作，从而引导舰炮打击目标。这个计算机甚至是纯机械或者机电的，但计算速度和精度都远超人类。这算不算人工智能？如果说给个公式死算不算人工智能，要有逻辑推理能力。那我们再看70年代的四色定理的证明。人类证不出来的数学定理，计算机通过极其复杂的推理证出来了（当时甚至没人能审这个证明过程，因为太长了，拖了好久才确认是对的）。这算不算人工智能？如果说光有推理能力不算人工智能，还得有知识，80年代的专家系统比如Mycin，甚至可以通过决策树的方式来看病开药，而且比普通诊所的医生误诊率都低。有知识，有推理，超越能力，算不算人工智能？它们和我们现在俗称的人工智能差别到底在哪里？我们这些年的发展主要在干啥了？

如果回到现代，看看现代的潮流：机器视觉希望让电脑看懂照片，自然语言处理希望让电脑看懂文字，语音识别希望让电脑听懂声音。仿佛只有这些才算人工智能。这些问题有个特点：都是人类擅长计算机不擅长的东西。当然这个计算机不擅长的界限这么多年一直在变，比如前面提到的证明数学定理，用决策树问诊，好像电脑一旦能做出来这些就又不算人工智能了。但最后剩下的这几个计算机的老大难问题，仔细看看其实都是人类的缺陷。

举个例子，为什么理解一张照片很难？一个重要原因是相机有两大先天缺陷，第一是拍出来是二维图像，天生丢了一个维度，第二是仅限可见光，又丢了无数信息。所以造成了很多歧义。为什么理解语言很难？也是因为有很多歧义，自然语言处理搞了几十年的问题，怎么判断用户说的苹果到底是苹果电脑还是苹果这个水果，这句话中间的"它"，到底指代的是什么。这完全就是语言的落后性决定的，如果重新定义单词表不搞这些同义词不搞缩略指代，搞成类似脚注的形式，这个问题就会容易很多。而这个语言的落后性，又是因为人类阅读和说话的声音局限的，带宽太低了才要用奇技淫巧在语言上做文章。所以你看现在定义的人工智能为什么难，完全是因为人类弱鸡。要是真有个AI机器人有深度传感器，有多波段相机，有为高带宽通信专门设计的语言和知识，这些视觉理解语言理解根本就不是问题。我要是AI都要感叹，扶不起来啊！

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
