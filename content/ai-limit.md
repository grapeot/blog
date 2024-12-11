Title: 何时以及如何不使用AI工作
Date: 2024-03-13 23:00
Category: Computing
Tags: AI, Machine Learning, Chinese
Slug: ai-writing-limit

我一直在朋友圈鼓吹[万物皆可AI解决](https://yage.ai/ai-it-impact.html)也不是一两天了，但今天我想唱个反调，自我精神分裂一把。就是说，当我们对[AI的能力边界](https://yage.ai/foundation-models.html)有了一定的了解，知道了哪些事情可以用AI来完成之后，很多时候还是要有所不为，恰当地决定哪些环节让AI介入，以真正实现我们的想要的效果。

具体来说，前段时间在课代表的号召下幡然醒悟，AI的尽头是卖课。要卖课就需要有一个足够装逼的自我介绍。根据之前我的一向观点，这个东西得试试用AI来说效果怎么样。但和其他任何问题一样，使用AI与否并不是一个非黑即白的问题。很多时候，我们的选择都处于完全使用AI和完全不使用AI之间的某个点。如何选择这个点则是最见功力的地方。

对于这个特定的问题，我比较了三种不同的策略。第一种是最偷懒的方法，只要能用AI就用AI。我整理了所有可能相关的信息，并口述给GPT，告诉它这个AI课程的目标受众以及自我介绍的要求，比如需要体现我的credibility，需要吸引人报名。以下是AI给我写出来的文字。

> Dr. Ya Ge, a visionary in the field of Computer Vision and Machine Learning with a Ph.D. from Columbia University, stands at the forefront of innovative applications of GPT. With 10+ U.S. patents, 20+ papers on top conferences/journals, and impactful algorithms used by billions globally, Ya's expertise bridges the gap between theoretical research and real-world applications. His commitment to exploring GPT's capabilities since its inception underpins his belief that humanity is on the cusp of a new industrial revolution, where proficiency in GPT can provide a decisive productivity advantage. Ya's diverse achievements, from being an Olympic torchbearer to hosting a photography exhibition with Leica, underscore his multifaceted approach to innovation and makes him an unparalleled mentor for those seeking to leverage GPT's transformative power in their professional journey.

第二档是，我人肉挑选了最重要的信息，写了一个提纲，然后用[最直白的语言](https://yage.ai/prompt-engineering-guide.html)口述出来，让AI整理文字。在这种情况下，AI主要承担的是文书工作。以下是AI输出的自我介绍。

> Dr. Ya Ge is deeply committed to creating functional products by developing specific mechanisms, fostering continuous innovation, and utilizing effective tools. His algorithm has been integrated into Photoshop, Bing, and Pinterest, benefiting millions of users. His achievements have also attracted global media attention. Ya has contributed to advancing human science by publishing over 20 papers at top-tier conferences and securing more than 10 U.S. patents. Since the emergence of GPT, Ya has been diligently exploring its potential, gradually forming a strong belief that we are at the cusp of a technological revolution akin to that of steam engines. He posits that individuals proficient in AI could have a significant advantage over those who are not. Leveraging his proven career coaching skills, Ya has discovered a practical and effective method to enhance productivity.

最后一档是完全人肉，人肉选取材料，人肉整理脉络，人肉打磨语言。以下是我亲自坐镇亲自指挥亲自写出来的版本。

> Dr. Ya Ge has devoted his passion into building working solutions to complicated engineering problems since he got his PhD degree in Columbia University. With emphasis on tailored mechanism, continuous innovation, and specialized tools, Ya consistently delivered algorithms and systems to Photoshop, Bing, and Pinterest, which have benefited millions of people and got widely reported by global media. Ya also contributed to pushing the boundary of human science by publishing 20+ papers on top conferences/journals and inventing 10+ US patents. Since the initial appearance of Large Language Models (LLMs, often referred as AI), Ya has been exploring its potential and gradually built a belief that, we are at an intersection of technology revolution similar to steam engines, and people who know how to properly use AI may build a decisive advantage over those who don't. 

在这个过程中，我明显感觉到第一个版本与后两个版本之间有较大的差异。因为没有经过我的深思熟虑，AI选取的材料虽然看起来与可信度相关，并且使用了华丽的词藻来进行自我介绍，但其深度与后面两个版本相比还是有明显的差距。

在与合伙人课代表的讨论中，我意识到第二个版本与第三个版本之间存在显著差异，尽管它们的基本内容和结构完全相同。AI的措辞显得特别diplomatic，带有一种疏离感。如果将人类写作比作一个人在讲台上热情洋溢地演讲，那么AI写作则像是一个外交官冷漠地念稿。这种疏远感导致文本缺乏感染力和说服力。比如人肉版本的开头has devoted his passion into building working solutions。devote，passion，working，寥寥数语却非常opinionated。相比之下，AI写的deeply committed to creating functional products 就平淡如水。

课代表还指出了AI在用词上也有一些微妙甚至诡异的感觉，例如它倾向于使用"utilize"这样的词，这不仅显得过于正式，还暗示了对技术的不熟悉。类似你天天用筷子吃饭，要是说我今天utilize筷子完成了吃饭这个壮举，就会给人一种微妙的暗示你对筷子并不熟悉，觉得会用筷子是一件特别牛逼的事情。相比之下，人类的用词更加直接和自然，比如就会直接使用"use"。所以，尽管从内容信息量上看两者相近，人类写作自然地展现出张力、活力和感染力，而AI写作虽华丽却缺乏深度和灵魂。课代表将这一对比总结为米其林和预制菜，我感觉是非常精准的。

我的learning主要有三点。

1. 决定是否采用AI并非一个简单的非黑即白的问题，关键在于搞清楚我们要落到其中哪一档，或者哪几档的结合。
2. 判断是否使用AI不仅仅是一个技术层面的考量，或者说AI是否有能力完成任务，同时也涉及到非技术层面的问题。例如，在AI卖课这种严肃的场景下，如果用户花费数百美元却得到一盘预制菜，这本身就是对用户的不尊重。因此，选择不使用AI不仅仅是因为AI的能力限制，更重要的是体现出我们对用户的尊重。
3. 通过这次实验，我对AI写作与人类写作之间的差异有了更深刻的理解。以前我只是觉得AI写的文章看起来有些诡异，一股AI味儿。但经过深入的实验、思考和讨论，我对它在用词选择和感染力上的微妙差异有了更深刻的体会。