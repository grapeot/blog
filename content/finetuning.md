Title: 从提示词到微调：让AI更像"我"
Date: 2024-12-23 19:00
Category: Computing
Tags: Prompt Engineering, Finetuning, AI, Chinese
Slug: finetuning

你有没有觉得AI讲话一股AI味？比如人类说话类似这样："我想点一个大份的炒面，要加辣，不要放香菜，打包带走。"但是AI说出来就是："我想订购一份大份量的炒面，请在制作时添加辣味调料，不要放入香菜，并且需要外带服务。" 就觉得怪怪的，好像领导在台上讲话，正式，官方，疏离。

这是一个我纠结了很久的问题。因为这个问题不解决，我就很难用AI来做翻译，写文章——一看就是不是我写的，甚至不像人写的。让AI的语气更像我，这个问题看起来应该很简单，但实际尝试以后会发现特别难。这个文章就用"调控AI的语气，让它更像我"作例子，来介绍一个非常强大但也很繁琐的工具，finetuning，或者叫微调。

我们会先介绍怎么从一个个失败的尝试里面，总结发现这个问题的难点：让AI内化他所受到的繁琐精细的指导。然后介绍微调适合和不适合的场景。最后介绍微调需要的一些技术技巧。

## 屡战屡败

调控语气最直观的方法当然是Prompt Engineering，这也是我第一个尝试的方案。但里面的一大难点是，怎么让AI把握好这个度。如果我们直接说"你的语气不要那么正式"的话，往往会走另外一个极端。AI各种插科打诨，这也不是我们想要的。所以，问题的难点就在于，如何向AI清楚地描述，我们希望它在正式和不正式的两个极端中间具体落在哪个点上。

在尝试了用一些抽象的语气描述，但还是没办法有效的调节AI的语气以后，我尝试了另一个方向。这个灵感来自我调教画图Midjourney的一个经历。我想表达一种细节繁复，但又不太张扬的风格，用语言描述了很久都很难让AI画出来想要的风格。然后高手说可以试试"洛克克风格（Rococo style）"，结果试了一把就是我想要的。类似的，鲁迅的文风具体是什么也是很难表达的。你可以花大量的文字来描述鲁迅的文风有哪些特征，但是如果让AI或者人只看这些描述，想写出来鲁迅风格的文字也非常困难。但因为AI在训练的过程中看过鲁迅的文章，如果你直接叫它用鲁迅的文章来写作，它可以学得惟妙惟肖。这就是背景，流派，或者说意象的力量。

因此，我尝试的第二种思路就是，试图让AI去找到一些跟我相近的流派或者作家的抽象概念，用这些拥有丰富背景和信息量的概念来帮助它理解到底应当如何把握这个语气。但遗憾的是，我和AI折腾了一圈，也没找到一个作家或者流派的风格能够比较好的捕捉我的风格。毕竟能在文坛上留名的都是大师，用大师们的风格来拟合我这种小透明，难度确实也太高了。

虽然这个方向失败了，但它也带来了一些启发：如果想要得到更细节的调控，单纯的描述是不够的，AI需要更多的信息。在有现成的概念的时候，这个信息可以用一个词来浓缩，但如果没有一个现成的概念，也许我们可以给它很多例子，让它现场学出来。这就是few-shot learning的思路。具体地说，在给它交代翻译任务的时候，我不仅给它英文的原文，而且还会附带上几篇以前写的文章，试图让它能够照猫画虎，翻译出一些AI味不那么浓的文字。

但这一招很不幸也失败了。我思考了一下可能什么原因，这可能是因为想要用几篇文章就来构建一种完整的风格，也确实太强人所难了。尤其是当文章的领域不尽相同的时候，相关的术语和用词习惯都没有任何可以直接借鉴的地方，最终还是得回归到AI自己的知识中去。就又变成默认的领导发言风了。

如果是这个原因的话，其实也不难解决。在构建这些例子的时候，我们不是随便抓几篇文章给它。而是在我以前写的文章里先做一把retrieval，然后把和要翻译的文字相关的小段作为例子。这样就可以实现它所看见的例子和它要翻译的文字之间有比较紧密的联系，从而大幅提升了给AI提供背景资料的效率。

但遗憾的是，这种方式也失败了。和原生AI的翻译相比，用上面的方法得到的结果，要不然没有太大区别，要不然就不能实现相对精细的调节。在此之外，我也试了一些其他产品提供的工具，包括Claude的style以及各种不同的AI（提一嘴，Gemini AI味相对最少），但从抽象的角度来看，它们都没有超脱出上面介绍过的几种思路，效果也不理想。

## AI内化精细修正的武器：微调

上面的几种方法虽然失败，但还是有启发的：这个问题为什么难，主要在于它不是一个明晰的，可以用语言轻松描述的要求。AI读过了无数本书，肯定是见过这么一种平实亲切的语言风格的。在前面的一些尝试中也可以看到，它是有能力用我的这种风格说话的，问题的核心在我们怎么向AI表达出来这种风格到底是什么风格。

这个表达为什么难，主要是两个原因，第一是它很精细。比如你看上面AI和我的翻译，就差几个字，但语气风格就相差甚远。第二是可能正因为这个精细，AI如果想要内化这些修正的话，需要大量的例子，最好要能覆盖各种题材和场景。换言之，我们面临的核心问题是，怎么让AI内化这些零散，琐碎，却又精细的修正和指导。我们传统的武器是提示词，但它面对这样的需求似乎也显得力不从心了。

#### 微调是什么

这时候微调就自然作为一个解决方案出现了。微调不是一个新概念。在[以前的文章](/foundation-models.html)中我们也介绍过，在基础大模型出现前，微调其实是使用模型的主要方法。现在的AI（LLM）的基础是zero-shot learning或者few-shot learning，通过在输入的词字中提供的例子，来动态地学习理解用户的意图，然后进行输出。在整个过程中，模型本身是不发生变化的。

微调则恰恰相反，它需要改变模型本身的内容，通过这种方式来实现对模型行为的改变。具体地说，它需要让模型看很多训练数据，每个训练数据都有一个输入和一个期待的输出（ground truth）。微调算法会改变模型的内容（权重），来让它面对给定的输入，来尽可能得到和期待类似的输出。通过不断重复这样的权重调整，模型就可以内化我们在训练数据中给它传递的信息了。

一个简单的例子就是我们可以通过微调一个模型来让它判断一个客户评价是正面评价还是负面评价。我们在这里训练数据的输入就是客户评价本身，而输出则是正面或负面这样的判别结果。模型微调的过程，就是不断调整模型参数的过程，使得当它看到每一个输入的客户评价时，能给出正确的判断结果。

当然，判断客户评价是一个玩具级别的例子，对于现代的AI来说，不需要微调就可以做得很好。但是对于一些更复杂的需求，比如阴阳怪气的检测来说，微调就变成了一个有力的武器。微调可以让我们给模型提供大量的例子，让它仔细品味和推敲在不同条件和场景下应该如何做出判断，然后把这些零散的精细的修正给内化起来。

然而，这个对模型本身的改变是一把双刃剑。一方面，它可以让模型有效地接受大量的指导；另一方面，因为训练的模型规模非常大，它也是一个非常重量级的过程。一方面，我们需要准备相当多的训练数据，比如几百几千甚至更多个输入输出的配对样本；一方面，我们需要将一个巨大的模型加载到显存里，利用显卡的巨量算力来对模型的权重进行微小的改变。

因此，微调往往要求花费大量的时间来进行数据收集清洗、代码撰写调试和最终的量化封装。而另一方面，它的整个过程充满了风险与不确定性。尤其对于大语言模型，微调可能会导致模型的行为发生巨大的变化。比如彻底忘了以前学习到的技能或者知识（catastrophic forgetting）；或者整个模型完全坍缩（collapse），变成只会胡言乱语的一个废模型；或者模型变身话痨，在完成任务之后还不知停止，而是继续输出一些看起来有关，但仔细一看不知所云的东西。

另外，微调对于硬件的要求也是很高的，如果用家用的游戏显卡来进行微调的话，一般只能到1B，也就是10亿个参数的模型的时候显存就会爆了。但凡想要做有实用价值的微调，至少得四个4090起，远远更大的显卡集群也是很常见的。因此，它是一个非常重量级的操作。也是为什么我一直把它放在backlog里面，先尝试其他方法的原因。

#### 适合和不适合的场景

从"内化精细修正"的这个目的出发，微调自然有它所擅长的场景和不适合的场景。对AI输出的风格进行改变是常见的使用微调的场景。比如这里的语气，或者它输出的格式（比如JSON），或者是对工具的使用。比如我有50个可用的工具，希望AI在里面做出选择，在适当的场合使用适当的工具。

在这些场景里，对AI模型进行微调有两个好处。第一种好处是它能实现别的方法，甚至比较复杂的PUA（Prompt Utilization Architecture，下一代的提示词工程）所实现不了的更精细的控制。第二个好处是它可以极大地缩短提示词的长度。比如就算我们可以用具体的例子来改变AI语气，或者可以通过提示词来向AI交代那50个工具的具体功能和用法。但每次做推理的时候，我们要从头处理和理解这些提示词，然后才能开始输出。这在成本和响应时间上都有不小的劣势。但如果我们用微调的方式把这些提示词的要求内化到模型里的话，就可以使用非常简单的提示词让AI有同样的输出。在这种情况下，不论是用户响应还是推理成本都得到了极大的改善。因而这样的场景，是微调所比较适合的场景。

而关于微调有一个广泛的误解是它可以用来注入新的知识或者技能。这个是不正确的。微调更像是把AI已有的能力进行启发和激活，它没办法给AI一种新的能力。或者比如更强的推理，和更多的知识。如果感兴趣的话，你也可以试一试，把一个知识库微调进AI里，和RAG进行比较，看看它能不能有效的利用这些知识。我做过这样的实验，结论是不能。但是我也好奇大家的实验结论。

## 微调的关键技术决策

但是就像前面所叙述的那样，我尝试了各种方法实在是没辙了，同时微调看起来也确实是一个适合的解决方法，正好最近又有了Agentic AI这个利器，所以我就探索了一下如何用Agentic AI来帮我完成微调这个任务。

下面首先介绍一下在利用微调解决AI语气问题的过程中，我所做的几个关键决策。正如我们在[之前职业发展的文章](https://yage.ai/new-employee-suggestions.html)中提到的那样，这些技术决策比实际操作的时候动手有多快、有多细心、投入了多少时间要重要很多。因为一旦我们做错了决策，哪怕写码再快，这条路走不通还得彻底返工。这个浪费的时间是写码快个两三倍都找不回来的。因此我们会先花一些精力来理清楚里面的一些基础概念和技术决策，然后再介绍更为细节的实操方面的技巧。

我们在这里主要做了三个重要的决策：

#### Parameter Efficient Fine Tuning

我们使用了一种叫做parameter efficient fine tuning的方法，具体说是LoRA。LoRA的基本思想是，它并不去改变整个模型几十亿级别的参数，而是用一种特别的low rank decomposition来极大的减少待训练的参数量。不涉及数学细节，一种直观的理解方式是，它类似在模型中最关键的地方插入了一些楔子，通过只改变这些楔子的权重来起到四两拨千斤的作用，从而明显的改变模型的整体行为。

这样就可以让模型训练这个数学问题的规模降低到以前的几百分之一，从而让我们即使在民用级别的游戏显卡上，也可以进行相当大规模比如3B、7B模型的有效微调。当然这仍然是一个工程上的tradeoff，它的效果很多时候还是没有完整微调那么好，但是当我们没有条件去购买或者租一个大型的显卡集群的时候，这不失为一种有效的折衷方案。

#### 逆向合成数据

第二个关键决策是训练数据从哪来。要想解决翻译的语气问题，最完美的方法当然是给很多英文文本，然后让人类比如我来把它翻译成中文，这样就有了成对的训练数据，可以用来指导训练。但是一般微调至少需要几百几千个训练数据，让我人肉翻译几百几千段话，实在是太浪费时间了。在企业里常见的方法是雇人来标注，但在我们的场景里，且不论钱的问题，从撰写标注指南、确定例子，到和标注人员沟通、验收、迭代等等，这本身就是一个时间上的无底洞。大企业可以弄一个人甚至一整个组来干这件事情，还能保证有利可图。但对我们个人来说完全不现实。

因此在数据方面，我直接采用了LLM来生成数据。具体的说我利用现在的LLM中翻译语气自然的特点，先把我所有的中文blog抽出来作为输入，然后让AI把每一个自然段翻译成英文。这样我们就有一对输入是中文、输出是英文的数据对。接着我们再把它进行反向，把翻译出来的英文变成输入数据，而我写的中文文本作为期待的输出，这样就方便的构建了大量的训练数据。

举个例子，比如我的blog中间提到"提供几个不同的API，让客户端可以提交一个新任务，然后返回一个任务的ID"，这句话翻译成英文就是"Offered several different APIs. This would allow the client to submit a new task and receive a task ID in return"。接下来我们把这段英文当成输入，并且告诉微调的程序，请调节这个模型的参数，使得它的输出尽可能的接近我写的那段中文。通过这样的方式，我们就得到了很多的训练数据。

#### 使用商业API进行Opportunity Sizing

我做的第三个技术决策是Opportunity Sizing。正如我们之前所提到的，微调本身是一个非常重量级的操作，需要投入很多精力，而失败的风险也不低。因此在我们确定投入大量的精力之前，我们需要先投石问路，看看这种方法到底有没有希望成功。考虑到代码撰写、集群租赁的成本非常高，我在这里直接用了OpenAI提供的微调API来进行Opportunity Sizing。

具体地说，我选用了训练数据中间的一小部分，然后上OpenAI的网站，用GPT-4o的微调功能先试了一把。50个训练数据花了三美元，但从返回的模型来看，它在一定程度上已经实现了对语气的把握，比原生的GPT-4o的AI味要少了一些。因此我进一步加大了投入，用了更多的训练数据，做了一个规模更大的验证。这次得到的结果还是蛮令人振奋的，在一些例子和推理参数的设定下，它可以得到相当好的结果，我有时候甚至以为这句话真的是我写的。但是在另一些例子上，它的效果仍然不尽如人意，有时甚至会出现collapse的情况。而且整个过程也很贵，即使训练数据的一个子集上进行微调，也花了我一百美元。

因此我通过使用OpenAI的API，暂时规避了代码调试和集群租赁的繁琐，通过一个肯定正确的实现，来验证了这个方向是有前途的。但同时因为它价格实在是太贵了，也让我下定决心不能继续用GPT-4o进行微调，而需要使用开源模型来降低成本，同时实现更大的灵活度。因为毕竟OpenAI的API并没有暴露出所有跟微调相关的参数设置，而有可能在我们的需求里，想要把微调的效果给弄上去，需要调整那些没有暴露出来的参数。

#### 核心：降低门槛

而这三个决策有一个清晰的脉络，就是降低门槛。

整个技术决策的过程是这样：我们首先用了LoRA解决了算力方面门槛过高的问题，用AI半合成数据解决了数据方面门槛过高的问题，用OpenAI的API解决了实现正确性门槛过高的问题，以100美元为代价确认了这个思路的可行性，并且做出决策：我们需要投入更多的精力在该源数据上进行微调。而下面我们会具体介绍一下，在具体执行的过程中，我们又用了哪些技巧来让这个非常复杂的项目在几个小时内变为现实。

## 微调的实现细节

实现微调的过程在Agentic AI的帮助下相对直观，基本上跟Cursor描述一下你想干啥就好了。但是也有一些坑。这里总结几个经验教训。

#### 硬件部署

微调的部署一般有两个方法：一个是使用类似OpenAI的微调API这样的服务。OpenAI这个API为什么贵，主要是因为GPT-4o是一个特别大的模型。但如果我们要直接微调开源模型的话，不论是AWS还是AnyScale，也有很多类似的API可以使用，它就比对GPT的微调便宜很多。而且由于模型是开源的，我们也可以进行很多定制。

第二个方法是我们直接租用一个GPU的机器或者机群，这个跟在网上租一个虚拟机是完全一样的，唯一的区别就是这台机器有GPU，我们就可以对它进行彻底完全的定制，想干什么就干什么。

在我的这个场景里，因为我希望用多种方式来探索微调这种方式有哪些利弊，所以我用的是第二个方案。具体地说，我是在Lambda Labs上租的NVIDIA GH200。最近它有个活动，只要1.8美元一小时，这个价格对一个64核CPU + 520G内存 + 96G显存 H100的机器来说，还是非常划算的。总的来说使用体验不错，但唯一的坑是它的CPU相比于传统的服务器CPU实在是太弱了，所以需要做一些额外的优化，比如用多核来进行数据处理才能保证训练的过程中CPU不是瓶颈，而把GPU的利用率提上去。

#### 文档管理

微调是一个非常复杂的项目，比如我的最终版的微调的核心程序有八九百行。因此如果我们还是照以前那样无脑地用Cursor来写程序的话，往往会陷入一种鬼打墙的情况。比如它前面在我们的指导和纠正下改正了一个错误，但是当进行多轮对话之后，可能因为前面的纠正出了最新一轮对话的context window，它就丧失了这个背景知识，从而在新一轮的更改中又把它改回去了。这是使用Cursor进行大规模工程实现的一个典型failure pattern。

这个问题的解决需要我们之前提到的[Document Management](https://yage.ai/ai-comment-oriented-programming.html)，也就是在它改完错误之后，我们可以通过提示词让它把新学到的经验要求写到`.cursorrules`，这样这个要求就被作为提示词的一部分，每一次都被发给AI，它以后就不会再犯这个错误了。但随着最新版0.44的Cursor的发布，我发现它对这个指令的响应越来越不敏感。所以如果有需要的话，还是手动明确让它总结经验比较稳妥。此外，让它在`.cursorrules`里面维护一个总体计划和当前进度，也是避免它做一半开始忙活另外一个不相关的东西的一种有效的做法。

总的来说，在使用Agentic AI编程的过程中，我们的角色更像是一个开发经理，主要职责是评估开发效果、指导开发方向和同步开发进度，同时启发AI做出适当的笔记，从而让它自己也能得到成长。一个有意思的地方是，我在这个介绍微调的文章里完全没有提我们要用什么库，用什么框架。这是因为现在这些都是Agentic AI来处理了，我们没有必要去关注。我们的精力应该花在去做"要不要用微调"，以及上面提到的各种关键决策上。

#### 更多的附属任务

在使用Agentic AI做了最核心的微调任务之后，我们还可以让它做更多的Unit Test，以及量化可视化和推理的工作。比如结合数据引擎，我们可以让它把训练生成的Hugging Face格式的模型首先与LoRA模型合并，然后用 llama.cpp 进行量化和在Mac上进行推理。此外我们还可以让它生成与商业模型的对比，比如[这个网页](https://yage.ai/genai/style_finetune.html)就演示了GPT-4o和我微调的通义千问2.5 3B和7B模型之间的对比。

![Finetune result example](/images/finetune-example.png)

上面是一个具体的例子，我们可以看到，微调过的模型对于语气的把握还是比较准确的，很多时候和参考答案非常接近。

## 小结

总的来说，我们通过微调实现了精细把控AI语气的困难问题。在整个过程中，有几个地方是要提醒大家注意的。

1. 微调是一个灵活度，限制和风险都很大的技术。我们在使用微调之前，一般会先做很多更轻量级的尝试，然后才走微调这条路。而且即使在真的微调之前，也会先用成熟的API进行一些opportunity sizing，避免浪费时间，把风险维持在可控范围内。

2. 但好消息是，现在即使是对普通消费者，微调也是一个能用得起的武器。在算法上，我们可以使用LoRA之类节约显存的算法。在数据上，我们可以使用LLM来生成数据。而在硬件上，我们可以租用云服务提供商现成的API或者硬件。

3. 即使有了这些技巧，对Agentic AI来说，微调仍然是一个相当难的工作。因此在这个过程中，我们要尤其注意让AI从头到尾维护一个文档，把我们的目标计划和它学到的经验总结在上面。这样可以极大的提高AI的工作效率，避免陷入反复犯一个错误的境地。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>