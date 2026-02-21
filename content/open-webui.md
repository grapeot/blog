---
Title: 重拾开源平台OpenWebUI的惊喜
Date: 2024-11-23 23:00
Category: Computing
Tags: Chinese, AI, Review
Slug: open-webui
Summary: OpenWebUI配合ollama实现完全本地的AI体验，功能媲美ChatGPT和Claude：模型对比、RAG知识库、canvas编程、语音对话、联网搜索等一应俱全。
---

今天花了一段时间研究 [OpenWebUI](https://github.com/open-webui/open-webui) 这个工具，尤其着重探索怎么把它和ollama在有Unified Memory的MacBook上面部署起来。概括地说，它基本上实现了[POE](/poe.html)、ChatGPT、Claude在内的所有功能，并且还有很多附加功能，并且还可以完全在本地部署。体验之好让我非常惊讶。

1. 它的模型推理端支持ollama和OpenAI的API，也支持Claude，所以支持多种流行的模型。它还支持模型的动态切换和对比。比如你可以选定GPT-4o和Llama 3.2，它会用分屏的形式把两边的结果放出来对比。它还提供了模型斗兽场的功能，会给你匿名展示两个模型的结果，让你选哪个更好。这也是一种让大家一起来评价模型质量的方法。它也支持对会话历史的编辑，而且不仅可以编辑你说过的话，也还可以编辑AI说过的话。

2. 一个别家都没有的功能是它可以全文检索，这在积累了一段时间的聊天纪录，突然想要找到之前聊过的一段话的时候特别有用。我也非常惊讶为什么包括ChatGPT和Claude在内的AI平台都不支持全文检索的功能，但是OpenWebUI提供了这个功能。虽然只是字符串匹配，不是模糊搜索，但也已经非常有用了。

3. 它支持上传文件，比如PDF文件。你还可以选择是使用OCR的方式理解，还是用文本parser的方式理解。它也支持图像理解，比如可以上传图像和Llama 3.2 Vision联系起来，进行问答。

4. 它支持RAG，可以自定义自己的知识库。里面一个很好的功能是它的定制程度特别高，比如可以自定义各种embedding。这些embedding可以使用OpenAI的API，也可以使用本地的BERT类的模型。让我意外的是，经过这个探索我才了解到最近比较好的一个embedding模型叫做[BGE-m3](https://huggingface.co/BAAI/bge-m3)。根据benchmark，它的retrieval的效果比OpenAI最大的模型还要好，而且这只是一个基于BERT的5亿参数的小模型。只需要`ollama pull bge-m3`一下，在OpenWebUI里面就可以无缝集成使用了，点点鼠标切成这个模型就好。但总的来说，我还是对RAG的问答结果相当不满意。相比于[直接把所有内容扔到context window里面](/GPT-knowledge-management.html)，效果差太多了。

5. 从编程的角度来说，它支持GPT里面的canvas或者Claude里面的artifact。写出的HTML和JavaScript的代码可以直接在浏览器中间预览，也可以现场编辑AI生成的代码文件，或者批量下载。它的编辑器甚至带自动补全，也可以现场运行写出来的Python代码。唯一缺失的功能是我还没搞清楚怎么样上传一个文件，然后让它写一个Python代码来针对这个文件进行可视化或者处理。但从网上来看，也许它有这个功能，只是我还不会用。

6. 它也有联网搜索的功能，可以调用Google、Bing、DuckDuckGo之类的API进行搜索。

7. 它也有语音功能，有批处理性质的正常的语音识别和朗读，也有类似GPT Chat Mode那样的直接对话功能，但还不支持实时对话。和其他feature一样，在语音方面也提供了很多自定义选项，比如可以用各种本地的语音识别模型，包括distill-whisper-large-v3，也可以用各种离线的TTS模型，比如CMU的一系列基于BERT的模型，效果意外的好。所以整个过程都可以做到全本地运行。

8. OpenWeb UI也支持对AI的自定义。包括自定义prompt，加入自己的私有知识库，使用自己的私有agent来为它加入各项能力。它也支持把这些自定义的AI模型进行分发，有自己的社区，可以下载、分享和评价别人做的自定义AI。

9. 当然，它最核心的一个优点是它是完全开源开放免费的系统，所以可以做到完全离线、完全定制、完全控制。想要什么功能可以自己写代码就加上了。就算断网也可以正常工作，尤其是在MacBook上面，很多模型推理的速度都还蛮好。比如我用的32B的千问2.5在M4 Max上可以到每秒18个token的速度。不论是[写代码](/ai-comment-oriented-programming.html)还是问答，还是RAG都够用了。

总的来说，之前我一直以为OpenWeb UI之类的开源套件只是对最先进的闭源AI模型和产品的拙劣模仿。毕竟像OpenAI和Anthropic这样的公司拿了巨量的投资，招的人也不少。但开源界包括Facebook企业在内的人都是在用爱发电。但是在试用了OpenWeb UI和ollama组合的开源套件以后，我感觉模型上它们只是比最新的模型比如o1略差，和GPT-4o或者Claude 3.5在能力上相当接近。从产品体验上，虽然有一些些不完美，比如还不支持实时语音对话，但基本上所有厂商有的功能它都有，甚至加入了新的功能和定制性。至少从今天晚上的使用体验来看还是很好的。这点让我非常惊讶。也许我应该[打破对闭源商业模型的迷信](/builders-mindset.html)，多探索一下开源的AI平台。毕竟这里面的定制化和这里面定制化的灵活度和想象空间是非常大的。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
