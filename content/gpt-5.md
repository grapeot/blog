Title: 超越聊天框简评GPT-5
Date: 2025-08-07 20:00
Category: Computing
Tags: Chinese, AI, Review
Slug: gpt-5

今天OpenAI发布了GPT-5。首先我想推荐一个文档，是OpenAI给它写的[Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)。这个文档与model card不同，解释了很多怎么把它用好的技术细节，更面向API用户而不是研究人员。对使用API构建产品的工程师尤其有价值。

经过各种调研，实验，代码编写，我最大的感受是，GPT-5可能不是一次重大的模型升级，但是它是一个重大的产品升级。它的很多feature都是针对让API用户能构建更好的产品来设计的。

最关键的一点是，GPT-5相比于友商和OpenAI之前的模型，可控性高了很多很多。我举三个栗子。第一是我们之前零零散散提到过，每个模型有自己的个性。比如o3，特别擅长使用搜索引擎来搜索，经常哐哐迭代三四轮，用十几个关键字搜索完了，再来回答用户的问题。最终事实上的正确率就很高。但他也有个缺点，就是思维欠缺深度，经常给一个流水账式的列表答案就拉倒。相比之下，Gemini 2.5 Pro思维的深度高很多，但是特别不喜欢用搜索引擎。不论用prompt，用few shot learning，甚至求爹爹告奶奶让它去搜索，最多就搜两个关键字应付一下，然后根据可能是错的信息已读乱回。我做了很多实验，都没办法改变这俩的风格，最终只能做个缝合怪，让o3去搜索，然后把结果作为输入prompt扔给gemini去做分析，效果倒是很好。

在这个背景下，GPT-5 API引入了两个参数，一个是reasoning_effort来控制reasoning的长度，一个是verbosity来控制回答的长度。reasoning_effort这个参数从o1开始倒是已经有了，但是从GPT-5开始才可以控制对工具的使用。同一个prompt，设置成high的时候，他可以疯狂搜索5分钟，看了450k token的资料，然后才来回答。设置成low的时候，随便搜15秒，看了20k token就返回了。设置成minimal（这是一个新的选项）的时候，搜都不搜直接就开始回答了。然后verbosity也很有效，也是一样的prompt，high的时候他可以做3000个token的具体分析和回答，low的时候260 token就闭嘴了。从这个角度来看，o3大约是reasoning_effort=medium, verbosity=medium的情况。Claude 4的回答风格特别简洁，以列表为主，类似verbosity=low的特例，Gemini 2.5 pro类似reasoning_effort=low, verbosity=high的特例。但GPT-5就可以随便排列组合，这对于我们开发产品特别有帮助，可以根据实际使用场景灵活trade off。也算是完成了OpenAI统一多种模型的目标。

另一种可控性表现在对输出格式的控制上。如果你试过把LLM的输出直接作为输出给另外一个工具使用的话就知道这件事有多难。举个例子，比如我想要让LLM的输出是一个python程序，这样我就可以直接扔给python去运行。如果你直接用prompt去让它输出python的话，有时候可以成功，有时候会输出

````markdown
```python
他写的code
```
````

就是用一个code block包起来了。显然这种东西是没办法用python来运行的。而且json mode也是没办法解决这个问题的，因为它会输出一个合法的json，但json里面有这种code block。如果你让LLM不要输出code block，它又会输出类似`python -c '(写的code)'`这样的东西。总之有很多奇奇怪怪的corner case。要一个个去解决，特别恶心。但GPT-5就不用什么技巧，不用prompt engineering，不用few shot learning，不用例外处理，不用奇技淫巧。你就跟它说，输出合法的python程序，它就work。非常好使。可控性到了一个新的高度。

这一下就出来了很多新的使用场景，因为The Art of UNIX Programming就提到过，UNIX的基本设计哲学就是用pipe + plain text做协议，每个工具把自己的事情做到最好。现在LLM可以轻松融入这个体系了，一下就多了很多可以使用的工具，也可以嵌入到已有的UNIX生态里去。后面做CLI工具就容易很多了。

另一个方面是状态更新。如果你用过Cursor或者Claude Code会发现它会先生成一个todo list，然后做一步勾一步，用户体验特别好。但如果自己实现的话还蛮麻烦的。现在GPT-5 API也支持这个功能了，叫tool_preambles。感兴趣的也可以去看一下最前面贴的Cookbook。

而这些API方面的改变，可能也是促成OpenAI把GPT-5免费开放给所有用户的原因。比如可能免费的用户就给reasoning_effort=low但是verbosity=medium，让你察觉不到偷懒。高级一点的用户才给更好的参数。后台自己调度更好的或者更差的模型。也可以把reasoning能力花在刀刃上，根据用户的query动态决定调用多贵的模型。总之灵活了很多。

这些关于API和产品相关的insights，目前在流行的评测文章里面还没看到，分享一下。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>