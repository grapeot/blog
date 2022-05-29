Title: 关于System Design Interview的随想
Date: 2022-05-27 18:05
Category: Life
Tags: Career
Slug: system-design-interview

最近招人季，不少小伙伴在问system design interview如何准备。我的建议是也许可以换一个角度思考：如果你是hiring manager，你为什么要插个system design进去呢？希望看到什么样的signal呢？

我主要会观察四点：

1. candidate有没有能力主导推动整个项目。比如是直接开始设计具体模型（不好的信号），还是先提到几个重要的模块，然后一个个开始深入（好的信号）。
2. candidate在介绍过程中的详略和顺序。这个可以体现价值观。比如有的candidate会上来就说我们怎么做evaluation（好的信号），有的会先搞清楚motivation是什么，为什么要做这个项目（好的信号）。这往往很能体现candidate的经验，以及和团队文化是否锲合。
3. 事先预见技术挑战。这个和第二点相关。junior candidate往往不知道一个问题难点在哪里，经常会在关键的，需要扩展性的地方一带而过，但是在他本身熟悉但是不是难点的地方给出大量细节。最终造成的结果就是一旦要加新功能，或者发现有什么问题，整个系统就要推倒重来。senior candidate往往知道一个项目难点在哪里，把大量时间花在这里，系统的扩展性很好。
4. decision making process。很多junior candidate常犯的错误是，没有意识到自己无意中已经做了一个工程决策。稍微好一点的情况是，意识到这里有个决策，但决策过程非常adhoc。最好的情况是，首先看这个决策是否重要，不重要就有意用adhoc的方法来决策，重要再正儿八经分析利弊。在整个过程中如何做工程上的权衡，是很能体现candidate能力的。

举个例子，比如bing有个object detection system，想实现：用户访问数据库中间100亿张图的任意一张，都可以看到一个bounding box，点这个box就可以触发visual search。如何设计一个系统来实现这样的功能。我们不讨论如何设计，就讨论一个问题，这个系统是应该offline（事先把结果算好，用户访问的时候直接读取），还是online（用户访问的时候现场算）。很多junior candidate会自动assume是offline或者online，直接开始讨论这个offline或者online系统的设计细节。这就是没有意识到这里有个决策要做。有的意识到了有两个选项，但给出的理由非常superficial，比如offline快很多啊，当然offline。或者数据量太大啦，当然online。更好一点的candidate会合计一下，offline的优点是快，缺点是贵+不灵活，online的优点是便宜，缺点是慢+traffic不稳定，然后给出决策和理由。但其实这里我挖了个坑，最好的方法其实既不是（纯粹的）online也不是offline，而是二者的结合，online+cache+offline bootstrap。这个坑不是为了害candidate，而是这就是我们的日常工作。我们面临选项A和B的时候，往往最终的决策就是A+B或者C。最好的candidate可以走到这一步，给出这种方案。