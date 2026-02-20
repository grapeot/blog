---
Title: AssemblyAI语音识别API试用感受
Date: 2024-09-02 12:45
Category: Computing
Tags: Chinese, Audio, AI, Review
Slug: assemblyai-speech-recognition-api-review
Summary: AssemblyAI语音识别API试用体验，对比OpenAI Whisper API的速度、准确率、稳定性，以及大文件支持等特色功能分析。
---

在之前我们做了[一些尝试](/GPT-API-usage-creation.html)，使用AI语音识别和AI来辅助进行表达和输入。经过一年多的时间，一方面我觉得这个[工具特别有用](/GPT-shortcut.html)，可以极大地拓展了我思维的深度，让我不用浪费时间在修改打错的字上；另外一方面，整个系统也经历了很多改动，比如后台的AI从GPT-4换成了Claude 3.5。

最近另外一个问题变得越来越严重，就是我用的语音识别引擎是OpenAI的Whisper API，它变得越来越不稳定，经常显示Timeout需要重试。为了解决这个问题，我尝试过在本地host一个开源的Whisper模型，但是速度比OpenAI的还是要慢很多，他们确实做了很多infrastructure方面的优化。

为了解决这个问题，我开始探索有没有其他公司的语音识别API可以使用。在搜索一段时间之后，发现了AssemblyAI这个公司。这个公司蛮有意思的，不同于别的公司比如TurboScribe那样就是Whisper API换壳，这个公司真的有自己的模型开发能力，发布了自己的论文和白皮书。所以我花了一段时间把AssemblyAI集成到了我的系统里，和OpenAI的Whisper API做了一些对比。一些感受：

1. 在速度上，OpenAI还是更快一些的。比如对一个3分15秒的文件进行识别，OpenAI只用了9.8秒就返回了结果，AssemblyAI在用Nano模型的情况下花了10.6秒，在用Best模型的情况下花了19.8秒，耗时大约是OpenAI的两倍左右。
2. 但是准确率AssemblyAI确实更高，尤其是使用Best模型的情况下。对一些关于咖啡烘焙的术语，它可以非常准确地表达出来，让我完全不用做任何修改就可以直接使用。这点非常impressive。但是Nano模型达不到这样的效果，还是不如OpenAI的。
3. 从稳定性的角度暂时还没有数据。我只是对OpenAI经常发生outage或者需要重试感觉不满，但也不知道AssemblyAI会不会有同样的情况。

所以从性能的角度来说，感觉OpenAI的API还是更好一些的。AssemblyAI是用两倍的处理时间换取稍微更高的识别准确率，我不确定对我的这种用场景是不是划算，现在暂时使用Assembly的API做一做长期测试。

在功能上，AssemblyAI提供了挺多蛮诱人的功能：

1. 它有类似OpenAI的Batch Mode，叫做Synchronous Mode，但OpenAI的Batch Mode只对LLM有效，对于语音识别是没有这个功能的。
2. AssemblyAI最大支持5GB的文件，对于大文件比如电影和YouTube视频的识别特别友好。OpenAI这方面做的很差，一方面没有Synchronous Mode，一方面文件大小的限制也特别死。而且我甚至觉得这不一定是模型的限制，而是前端工程师和后端没有沟通好。当你上传一个大文件的时候，OpenAI给的错误甚至不是API的错误，而是一个Nginx的错误，说Entity too Large，是个HTTP错误，这比较搞笑。
3. AssemblyAI还有Streaming recognition，让用户可以对着话筒说话识别，OpenAI也没有这个功能。
4. AssemblyAI还有Speaker recognition的功能，类似Zoom AI companion，OpenAI也没有这个功能。

总的来说，我觉得AssemblyAI看上去是一个相当靠谱的而且很容易集成的语音识别API，而且集成起来也特别简单，感觉不妨作为OpenAI的一个Alternative。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
