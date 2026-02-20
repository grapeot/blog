Title: 用Multi-Agent让Cursor智能程度再上台阶
Date: 2025-01-23 23:00
Category: Computing
Tags: Chinese, Agentic AI, AI Coding
Slug: multi-agent

我最近花了不少时间，想要把Cursor这种常见的Agentic AI工具推到一个新的高度。最开始，Cursor只能写代码、执行代码，这让我们觉得虽然它像一个聪明的小弟，但还有提升空间。于是，我们[改写了Cursor Rules](/cursor-to-devin.html)，让它能做更复杂的规划、状态汇报和自我成长。再往后，我们通过Python命令行和自然语言叙述，为Cursor接入了私有知识库和数据库，进一步拓展能力。

可即便Cursor已经具备了大模型、搜索、Feedback Loop、[多模态](https://github.com/grapeot/devin.cursorrules/blob/master/tools/llm_api.py#L49)这些能力，在遇到稍微复杂一点的任务时，它总是给人一种还是少根筋的感觉，经常陷入鬼打墙的境地。比如Cursor帮我们接一个第三方搜索库。它先是在我们的指导下修好了Bug A，却在修Bug B的时候忘了自己做过的改动，又把代码改回了上一个版本，把Bug A又带回来了。来来回回倒腾。最终虽然还是修好了，但浪费了不少时间。如果是更复杂的项目，甚至可能就做不出来了。

### 为什么会鬼打墙

如果你对Context Window Management比较熟悉，会发现这是一个典型的失控现象：当同一个模型要同时负责高层规划和底层执行的时候，所有信息都挤在同一个上下文里。它要先在杂乱的信息堆里筛选出对规划真正有用的部分，然后才能做决定。这对模型来说是个极大的脑力负担（Cognitive Burden）。反过来也是一样，如果它先埋头执行，就容易在大量执行细节里忘了Planner曾经说过什么，或者找不到焦点。结果就是既没规划好，也没执行好，两头不讨好。

所以这促使我们做了第一项重大转变：把Planner和Executor分开。

### 第一项决策：分开Planner和Executor

我们的灵感其实来自管理学：如果让一个人同时当经理和码农，而且都用各自本职的标准去要求它，必然导致他既干不好管理，又写不好代码。Context Window也是一样。所以我给高层Planner留了一个独立的上下文，让Executor去专心处理底层实现，而Planner继续保持对全局的掌控。这样两者不会互相干扰。这种简单的分层，甚至不需要更换更强的大模型，就立刻让错误率下降了不少。Executor能自顾自地专心写代码、跑调试，Planner也像一个领导那样定期复盘，让Executor再去执行具体的修Bug、改版本的操作。

但结果一个意想不到的问题又冒出来了。

### 第二项决策：强制Agents使用文档沟通

问题出在，Planner和Executor是分开了，可它们仍然用对话来沟通。这就导致只要context window一长，或者被截断，Planner的指令就彻底丢失了。比如Planner前面说“你记得跑个版本兼容测试”。结果Executor debug几轮以后Cursor把context window截断，这句话丢失了。那因为它不在Executor的context window里面，Executor下次再执行的时候就会完全不记得这回事。

这就好像公司里管理层和执行层都很忙，吭哧吭哧干活，没人干写文档这种小事。结果执行层没有能力跟踪进度，全靠老板提醒。老板自己也记不得技术细节，天天跑来问同样的问题。（怎么感觉这么眼熟

所以我们发现，就算做了context window的隔离，我们其实还是没有真正解决失忆问题。于是我们搞了一个特别土的解决方案：给Planner和Executor准备一个公共的Scratchpad文档。任何思路分析、测试结果、遇到的Bug、最后讨论的结论，都写进这份文件里。

这样一来：

* Planner可以随时在文档里查看当前难点和进度，也能留下新的任务指令；
* Executor在做完一个功能或踩到什么坑，就把结果和反馈更新到文档，Planner读到了就不会忘。

这样通过把对话管道变成一个持久化的笔记本，我们基本解决了LLM上下文丢失的问题。哪怕对话一时刷新了，只要再引用文档就行。失忆和踩同一个坑的概率立刻就降低了很多。

### 第三项决策：请我大哥o1来当Planner

等我们把Planner和Executor拆开、也建了公共文档后，又出现了一个新问题：如果用普通模型当Planner，它常常没什么深度，只能给Executor一些很superficial的建议。比如说我们有一个数据处理的pipeline，如果是一个有经验的senior engineer来做的话，他会先在小规模的数据上面验证通过，然后再部署到大规模的数据上面去，这样会省下很多debug的时间。

但如果用一个比较简单的Planner来做的话，他往往会一把就直接在最终的大规模数据上面进行debug。这往往会浪费很多时间。更烦的一件事情是，cursor对于任务执行有一个timeout，如果真的是用正式生产数据来进行测试的话，它可能没有跑完就timeout了。这会导致它反而没办法自动迭代。

这个问题本身不难解决，我们直接把Planner换成更智能、更善于推理的模型，比如o1就好了。但换了以后发现另一个搞笑的问题。o1很喜欢over-engineer。有时候特别热衷进行分析和细化，每一步都在想怎么覆盖各种边缘情况，或者把这个小程序做成一个Concurrent Large-Scale Platform，搞得流程极其臃肿。

我有时候甚至感觉雇了一个职业经理人，他每天想的不是去帮我完成一件事情，而是去做一个可以特别fancy的平台。我总觉得他下一步就是要跟我说要招更多的Claude了。。。这就好像你在人类团队，请来了一个很有名的咨询公司。这些咨询师们为了显示自己很牛逼，往往给出一些特别精致、庞大但是臃肿的方案。底下的人忙了半天，但其实对最终的business goal一点用都没有，也不一定能提升效率。

所以这里我们做了第3.5项决策：通过prompting让Planner适度克制，并且搭配清晰的验收机制。我们最终的做法是，还是使用o1去做Planner，但是通过prompt让他有一个Founder Mindset，不要老想着一步到位，做成业界最牛逼的整个平台，而是Bias for Action，有什么机会就抓住它。先做一个简单的prototype出来，在验证了可行性之后，再一步一步往上加更多的功能。

尤其要Planner在跟Executor布置任务的时候，需要明确每一步拆分的必要性和验证方法。同时让Executor也能在文档的反馈区提出疑问，如果觉得方案太复杂，可以challenge Planner再次审视是不是真有必要，或者做进一步的分解。用这样一套交互和验收机制去控制Planner的推理。

### 实战例子

举个例子，我的[Cursor rules](https://github.com/grapeot/devin.cursorrules)里面调用的DuckDuckGo搜索一直有点问题，它不稳定，但是又没有明确的规律什么时候会挂。在引入了Multi-Agent系统以后。o1作为planner首先设计了一系列实验，让Claude去跑，Claude根据这个写了代码，然后把实验结果给o1。o1再去做分析，指示它搜索什么关键字，去这个DuckDuckGo Python library的GitHub上看issue等等。

这样迭代几轮之后就发现是DuckDuckGo python库的6.4版本里有一个bug，最新的7.2里面修复了，然后o1 planner就指示Claude executor把版本升级了上去，然后又设计了十个各种不同的test cases，让Claude一个个去测试。最后又指挥Claude写了一个文档来总结我们的learning是什么，用了什么样的措施来cross-check保证我们的实现是正确的，为什么这个已经实现了用户的目标等等。

这整个Multi-Agent的开发体验让我感觉它完成任务的质量又上了一个台阶。以前只是一个小弟把任务完成了直接丢你手里。现在的感觉是它有一个更有经验的监工，他自己会先去做一些cross-check，然后再跟你汇报。感觉我们从一个manager变成了一个senior manager。

### 三大改变的根本原因：Context Window

回头看看，我们其实并不是为了做Multi-Agent而做Multi-Agent，而是一个不断踩坑、不断反思、逐步迭代的过程。

* 因为我们遇到了上下文彼此干扰的问题，这逼着我们去拆分角色。
* 因为我们遇到了失忆的问题，这逼着我们去把文档作为Planner和Executor之间沟通的主要渠道。
* 因为普通模型的思考深度和规划能力都有局限，这逼着我们更换了更智能的Planner。
* 因为更智能的Planner有一个趋势是会over-engineer，这逼着我们通过prompting等各种方法来控制它的复杂度。

从初级的Cursor Agent Mode一路走到Multi-Agent，我们算是摸出了三条实用经验，也看到了多智能体系统确实可以把AI协作提升到一个新水平。它不仅把Bug修得更干净，也能进行更复杂的抽象思考，从而在相同开发周期里做出更多成果。

从表面上看，这套系统好像只是把Cursor里面原本的Claude上加了一个o1，但是其实它内部的思路比这个表象要深刻很多。我们做任何LLM系统的分析和改进，都必须要理解它的context window里面到底是什么。要确认它的context window一方面有足够的信息来支持它完成任务，另一方面也需要足够整洁和清晰。抓住了这一点，就可以自然而然地引出我们的三个改变。

希望我们的这些思考、经验，尤其是教训，能够给你在构建自己的multi-agent应用的时候带来一些启发。或许下次当你再遇到上下文丢失、上下文失忆、对话丢失的时候，就会想到应该从context window的角度来逆向思考LLM接收到的输入是什么。有必要把它们的context window分开，并且给它们准备好一个适当的沟通渠道。

此外，这个Multi-Agent的实现也已经[开源](https://github.com/grapeot/devin.cursorrules/tree/multi-agent)，欢迎大家参考。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>