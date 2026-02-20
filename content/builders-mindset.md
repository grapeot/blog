Title: 使用Builder's Mindset重定义AI工具
Date: 2024-08-10 23:00:00
Category: Computing
Tags: Chinese, AI, Reflection
Slug: builders-mindset

在ChatGPT刚刚推出的时候，我就尝试过用它来规划旅行，但整个体验非常糟糕。比如它经常出现幻觉，把地址搞错，或者推荐一个并不存在的景点。由于交互界面完全是文本的，我也看不到每个景点在地图上的位置。最后不得不回归地图手动安排行程和确认住宿。因此感觉这种应用更多是噱头大于实用。

因为计划去温哥华旅游，在我花了两年时间深入研究[如何用AI改进生活](/GPT-API-usage-creation.html)和工作后，我又重新尝试了一次这类工具。出乎意料的是，这次的体验有了显著提升。我把这次的聊天记录分享在[这里](https://poe.com/s/ujjVzzUJSMLPKlZ48O7w)。

简单来说，我首先让AI推荐了温哥华的景点类型和适合游玩的区域，然后告诉它我们有老人和小孩，进一步缩小了选择范围。接着让它把这些景点标注在地图上，使我们可以直观地感受到景点的分布位置，从而确定最终的行程顺序和交通方式。最终，在AI的帮助下，我们生成了一个总体的行程。

整个聊天看似平淡无奇，但如果两年前甚至一年前让我来做，恐怕都无法这么顺利地完成。在这个过程中，我主要运用了以下几个技巧：

1.	使用不同的AI来解决不同的问题，比如利用网络搜索的AI来减少幻觉，而在需要阅读文档或生成代码时，则使用更智能的AI比如[Claude](/poe.html)。
2.	使用文档管理来高效地教会AI以前它不会的内容。比如通过粘贴Bing Maps的文档教AI生成一个URL，让我们能够直接在Bing Maps上查看所有景点的位置。
3.	使用Chain of Thought来规避潜在的陷阱。比如，引导AI使用地址而非经纬度来在地图上标注地点。

但其实这些技术上的奇技淫巧都只是表面现象。现在的AI体验好功能强，并不是因为AI比以前更聪明，或者我使用的工具Poe比其他客户端更好，而是因为我具备了Builder's Mindset。

所谓Builder's Mindset，就是我们对待工具的态度从被动转变为主动。我们不再只是工具的User，而是工具的Builder。当没有现成的工具时，我们构建工具；当现有的工具不好用时，我们改进工具。在AI时代，这种构建和改进变得特别简单。比如，虽然到现在为止，AI还没有一个功能能将推荐的景点直接显示在地图上，但我们只需要粘贴Bing Maps帮助文档的URL，就可以立即教会AI实现这个功能。阅读文档、理解参数含义、构建正确的URL，这些以前需要我们自己动手的体力活，现在都可以交给[AI编程](/ai-comment-oriented-programming.html)来完成。

因此，具备这种Builder's Mindset的人，可能是AI时代最大的受益者，并且会与那些被动的User拉开明显的差距。不过，这种Mindset的转变并不是一蹴而就的。一方面，它是一个专门的领域，有许多陷阱和技巧；另一方面，它需要时间和经验的积累。比如，我之所以知道Bing Maps有这个功能，也是因为在过去构建其他工具时，学到了相关知识。

如果要我从过去两年甚至更长时间的AI使用经验中只教给你一样东西，我会毫不犹豫地选择Builder's Mindset。这也是[课代表](https://www.superlinear.academy/)和我一起创建了From Users to Builders这个AI课程的原因之一。感兴趣的同学可以参加我们最新的[免费试听课程](https://maven.com/p/36a1f5/level-up-team-productivity-with-personalized-ai-agents?utm_medium=ll_share_link&utm_source=instructor)，或者去[现场课程](https://maven.com/kedaibiao/genai/)看看学员们的评价。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
