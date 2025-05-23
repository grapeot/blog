Title: 高效Prompt Engineering指南
Date: 2024-03-04 19:00
Category: Computing
Tags: AI, Chinese
Slug: prompt-engineering-guide

我一直认为LLM/AI，比如GPT的出现极大地降低了很多领域的门槛。
最近在我强烈推荐下，周围不少人开始尝试使用LLM来处理更加复杂的任务。
但我们交流以后发现，他们的使用体验通常很差，遇到了各种问题。
在分析了他们的经验和使用场景之后，我意识到一个可能的重要问题是，即便使用LLM只需要用自然语言进行对话，但它还没有简单到不学就会的程度。
尤其是如何组织提问仍然需要一定的经验，即所谓的[prompt engineering](/tong-guo-prompt-engineeringti-sheng-dui-ren-lei-qiu-zhu-de-xiao-guo.html)。
本文旨在分享我对prompt engineering的一些心得。

Prompt engineering最关键的原则是确保你给LLM的任务难度要与其能力相匹配。
更具体地说，如果你的问题过于复杂，超出了AI的能力范围，那么你很可能会得到一个不尽如人意的结果。
AI对不同的领域擅长的程度也是不一样的。
如果你向AI提出的要求恰好是它的弱项，那么同样可能会得到错误或者没用的结果。
所以Prompt Engineering的核心在于选择LLM擅长的领域，在它不擅长的领域中，引导它利用代理的能力而非自身的能力来解决问题也是一个方法。
此外，将一个大问题拆解成若干个小问题，也可以规避AI"偷懒"的问题，帮助它更有效地给出答案。

需要注意的是，我们讨论的Prompt Engineering与媒体上常见的Prompt Engineering有所不同。
后者通常会尝试为AI赋予某种人格，例如让它扮演一名纽约时报的编辑。
然而，根据我的观察，这种方法并不一定比最朴实的prompt更好。
很多时候，直接要求AI"使用纽约时报的风格来修改文本"，跟先赋予它一个虚拟身份再进行修改没什么区别。
我们在这篇文章中讨论的是一些更高层次的策略，而不是如何编写人格这类基础模板。

为了具体说明，我们可以先看一下AI目前在生活中能提供哪些帮助，然后逐一分析如何在各个领域进行Prompt Engineering。

大家最常用的是可能是把AI当做百科全书或更智能的搜索引擎来用，向它询问知识性或事实性的问题。
遗憾的是，这并非AI的强项。
对于一些常见的通识知识，或者说是在其训练数据中频繁出现的相关知识，比如一年有多少天，AI可能会表现得相当好。
对于一些专门的知识，AI有时会给出错误的答案。
如果它能简单地回答"我不知道"，问题倒不大。
但是，现在的[AI](/recent-AI-advancement.html)还存在一个基本技术缺陷，它没办法对自己的答案给出一个确定的置信度。
当它不知道某个问题的答案时，它可能会非常自信的一本正经胡说八道，这比直接说"我不知道"更难顶。
面对这种情况，我们需要保持警惕，以下几个技巧可能会有所帮助：

1. 根据经验判断哪些知识是通用的，可以信赖。例如，使用Python的标准库进行编程的知识比如"我想把当前的时间用2024-01-23 03:22:33的格式输出，应该怎么写程序"，由于这些信息在stackoverflow或python文档中都有提及，因此可以认为是通用知识。而对于一些专门的知识，比如"NGC6888星云在天球上的具体坐标"，AI可能就难以凭借自己的记忆准确回答。
2. 对于自己不熟悉的领域，通过trial and error来验证AI的答案是否可靠。一开始，我们需要仔细地进行检查，看它的答案是否正确，有没有捏造事实。经过几轮核对后，我们可以逐渐获得感觉，知道哪个领域是专门的，它给出的知识是否可信。比如我一开始以为python异步编程可能是一个相当专门的子领域，ChatGPT不太懂，但在几次试探以后我发现他给出的答案都是正确的，这样就磨合适应，逐步建立信任。
3. AI不仅可以依靠自己的能力，像GPT-4或New Bing这样的模型还可以在网上搜索，然后总结搜索结果。因此，如果我们知道某个知识领域是LLM可能难以处理的，我们可以通过提示要求它不要根据自己的知识作答，而是通过搜索来回答。这样，它会去网上搜索，通常能大幅提升答案的可信度，因为它不仅会给出知识本身，还会提供每个来源的网页链接，方便我们进行核对。比如在买车的时候想要比较不同车型的一些特性就可以要求New Bing"列出一个表格比较mini countryman和mazda cx30的大小"，它会列出表格以后自己给出来源。可以点进具体网页里面复核。

编程这个应用场景跟上面说的情况是相当相关的。
例如，使用Python的标准库编程时，我们通常不需要提供任何额外的prompt，AI就能写出很好的代码。
但是，当我们需要使用特定的库，比如ASCOM库来编写Python程序时，AI可能会编出来一堆看起来很有道理的代码，但一跑发现全是错的，根本没有这些函数。
一种可能的解决方法是提供相应的背景知识，来让任务在AI的能力范围内。
例如，我们可以将ASCOM的文档或示例程序作为提示的一部分，供AI使用。
GPT-4-Turbo已经支持12万token的上下文窗口（context window），因此对于哪怕十几二十页的文档，它通常都能提供很好的答案。
不要害怕把整个库的示例程序或文档扔给它。

和查询/搜索不同的一点是，在编程问答中，对话往往会很长。
这主要是因为生成的程序代码较长，几个来回以后会占用大量的上下文窗口，可能导致回答质量下降。
具体表现就是AI讲到后面就忘了前面说的一些细节了。
为了避免这种情况，我们可以通过维护一个"记忆库"来帮助它。
例如，过几轮以后就把最新的代码贴上去（即使代码很长也没关系），这样可以刷新它的记忆，避免忘记之前的细节。

管理上下文窗口还有一个小技巧，就是善用ChatGPT的编辑功能。
比如我们让它写了一段代码以后，有一些地方不太理解，所以追问了几个问题，得到了解答。
然后现在想要继续刚才的对话，继续写代码。
这时候因为我们下面的的代码跟之前的追问没有什么关系，为了避免这些追问占用大量的上下文窗口反而把AI弄糊涂了，可以利用GPT的功能编辑之前的问题。
通过在下一个问题中添加最新的代码或编辑后续问题，来刷新记忆，确保对话集中在一个主题附近。

在使用[AI辅助编程](/ai-comment-oriented-programming.html)的过程中，另一个非常常见的应用场景是文书工作。
这包括撰写文章草稿、电子邮件草稿，以及进行文本摘要等任务。
AI/LLM在这一领域表现出色，可能是因为它在训练过程就是在不断进行这类工作。
因此，我们通常不需要采用特殊技巧来提高其准确性或效果。
但有时候要注意不要使用过分含糊的要求。
适当的细化要求可以让AI更好地帮助你。
比如"把下面的文字翻译成英文"可能就是比较生硬的直译。
但如果说"阅读这段中文博客，体会其中的用词风格和文风。使用类似的文风把它翻译成一篇英文博客"
里面还有一个坑是如果输入的文本过长，GPT可能会偷懒。
比如让它翻译一篇很长的文章，开始几段还可以，后面就开始把例子偷偷跳过去，只留下主要的论点。
再后面就开始大段大段跳了，直到最后一段又开始正常翻译。
就特别像一个很聪明的人在划水。
这种需要大段输入+大段输出的场景就需要上下文窗口的管理，比如把文章切成几段，分别喂给它翻译，就不会偷懒了。

数学这种应用场景，其实并不是AI特别擅长的领域。
这主要是LLM的训练过程中决定的，它的训练目标只是要根据给定的上文输出可能的下文。
因此原生的LLM并没有真正的数学计算能力。
例如，当看到"3688×2688"时，它知道下文可能是一个数字，但它优化的时候并不会具体纠结这个数对不对，
在这种我们明确知道AI不擅长的领域，就可以通过agent来增强他的能力。
这里的agent一般是第三方程序，比如计算器或Python，来帮助进行一些计算。
比如prompt可以是"编写一个python程序来计算3688x2688"。
这时候AI就知道去写一个程序，然后在OpenAI自己的沙箱中运行这个程序来生成正确结果。
或者当我们询问"仙女星系和M33这个星系两个在天球上的距离到底有多远"时，如果仅依赖它的知识或直觉生成能力，往往会得到错误的结果。
但是，如果我们启发它编写一个Python程序来计算，它就能非常准确地给出结果。

另一个AI不擅长的领域是需要深入见解或深度理解的领域。
这可能是因为AI对齐的限制或者训练数据的限制，它给出的回答往往是正说反说的车轱辘话，要挑错一点没有，说有用也一点没有。
目前，我还没有找到一种特别有效的策略来解决这个问题，主要是因为它本质上是一个文本处理任务，也难以找到其他agent来协助解决。

AI最后一个非常严重的限制是到目前为止，除了少数特例，比如用DallE生成艺术性图像，基本上只能生成文本。
因此，如果你想要的输出可以用文本来表达，比如代码，那使用AI将会非常适合。
但如果输出无法用文本表达，比如UX设计或3D模型，那么使用AI就会变得困难。
不过，这种情况并非无解，你可以构建一个特殊的agent来扩展LLM在这方面的能力。
例如，我最近通过构建一个[agent控制机器人](/ai-robot.html)并提供一些接口，使其能够控制机器人系统，就采用了这种方法。
虽然像让望远镜指向某个方向、让相机进行多少秒的曝光这类操作本身不能用文本来控制，但通过构建agent，我使AI能够通过Python代码来控制这些机器人系统，从而赋予它额外的能力。
当然，这是一种较高级的应用，需要一定的开发经验。

总的来说，Prompt Engineering的基本原则是将问题分解成AI擅长处理的范围，并选择AI所擅长的领域，或者使用agent来扩展AI的能力。
一个直观的记忆方法是把AI看作一个实习生：态度积极、愿意加班、接受过基础教育，但缺乏深度见解，对一些专门领域的认知不足。
使用这种直觉来构建prompt往往可以得到不错的效果。随着时间的推移，我们会逐渐积累更多经验，对哪些问题、哪些领域的问题适合AI有更深刻的理解。
有了这些认识后，我们就能更合理地组织prompt，一步到位地让AI写出符合我们要求的答案。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
