Title: 使用GPT实时语音API实现零延时AI辅助写作
Date: 2024-10-27 12:45
Category: Computing
Tags: AI, Speech Recognition, OpenAI, Chinese, Realtime
Slug: realtime-gpt

最近一两年我一直致力于[使用AI来增加写作和输入的效率](/GPT-knowledge-management.html)，而且确实感觉到了效率的质的提升。一个重要的观察是，当我们在写文章或者思考的时候，可能有一半以上的时间花在打字和改正错别字上面。这个东西不仅花时间，更重要的是它会打断我们的思路。所以写作的时候，一个非常常见的问题就是回读。写了一句话，回头改改错别字，这时候就忘了自己想要写什么了，再回头看几眼，终于反应过来，继续写。然后又陷入改错别字的循环。

这就是为什么我在过去一两年做了一个基于Telegram的机器人。你可以直接跟它说话，在思考的过程中一边想，一边把想到的结果说出来。通过这种方式，我发现它不仅能够让我们用语音输入这种方式来快速输入，更重要的是它可以避免改正错别字对我们思路的打断，让我们可以流畅地往下思考，拓展了思维的深度。

在用了这个机器人之后，我的思考和写作的工作流程发生了很大的改变。现在我更多的是 think out loud，开着录音的同时进行思考，想到什么就说什么。这样当思考到达一定阶段之后，不用重新整理、撰写文档，直接把语音识别出来的零散的思维结果交给 AI，它就会帮我整理成文，变成一个可以沉淀和分享的技术文档。

但是在这个过程中间，我还是有一个比较大的痛点，就是慢。一方面，Telegram是一个额外的App，我要打开它，切换到机器人页面，再按下录音按钮，是需要时间的。另一方面，它的识别也比较慢。在我彻底讲完一段话之后，它才会开始语音识别，有时候甚至要好几分钟才能拿到结果。总的来说，这个东西虽然对于重量级的写作好用，但是因为它的周转时间特别长，所以我在聊天等各种轻量级的场景中间就不太会用它。

## 第一轮迭代：集成实时API

最近，OpenAI 发布了他们的[实时 API](https://openai.com/index/introducing-the-realtime-api/)，这个 API 就是新版的 ChatGPT 实时语音对话背后的技术。我把这个 API 和现有的系统进行了集成，做了一个 Web版本的工具，网址是[https://f.gpty.ai/](https://f.gpty.ai/)，代码开源在[https://github.com/grapeot/brainwave/](https://github.com/grapeot/brainwave/)。

在进行一些试验之后，我发现它的体验非常好。一方面，这个工具可以在用户录音的过程中，就把已经录下来的语音发给 OpenAI。同时那边就会立即开始处理。这样，当用户讲完话的时候，它就可以非常迅速地输出语音识别的结果。这一下把延迟降低了几十倍。比如以前我花了十五分钟做了一个think out loud的长考之后，要等个两三分钟才会出语音识别的结果，中间可能还要超时重试。但是现在就只需要等一两秒，它就开始非常迅速地往外吐结果。

如果说这是一个意料之中的体验提升的话，另外一个意料之外的好处是，它的语音识别质量远好于之前我用的同样是 OpenAI 自家的 [Whisper或者第三方比如AssemblyAI的模型](/assemblyaiyu-yin-shi-bie-apishi-yong-gan-shou.html)。一方面，它识别明显更准，另外一方面，它对于中英文混合的情况支持得也非常好。我的理解是，这是因为 Whisper 毕竟不是一个 LLM，它的 Language Model 虽然有，但远远没有 GPT 那么大。所以虽然我们把 GPT 拿来做语音识别有点大材小用，但它还是可以很轻松地打败目前主流专门做语音识别的相对小一点的模型。

在试用了一段时间之后，我发现因为这个操作和反馈时间都比之前的Telegram Bot要更快、更敏捷，所以我愿意更多地把它用到更轻量级的应用上面。比如微信聊天的时候也会随手用一下这个语音输入。

但是这个体验仍然不完美。其中一个类似于Telegram的问题是，我还是得要打开一个网页，点一个按钮，然后再开始说话。虽然这个已经比Telegram少了一个选联系人步骤，但是和好用还是隔了相当大的距离。

## 第二轮迭代：和iphone深度集成

有没有一种可能，我们彻底跳过这些繁琐的UI操作？只要按一个键，就可以开始说话呢？在进行一些摸索之后，我发现这个是完全可能的。对此，我进行了三个改动：

第一，是在网页的前端加了一个URL parameter。当这个URL含有`start=1`的时候，我们就不需要用户手动去点录音按钮，而是自动就开始录音。

第二，是在iOS里面有一个功能叫[Shortcuts](https://support.apple.com/guide/shortcuts/welcome/ios)。它可以让用户写一些程序并且把它分享出去。于是我就写了一个一行的shortcut程序，把这个含有start=1的URL放进去让它打开。执行的时候它就会弹出一个Safari，立刻开始录音。

第三，是对于iPhone 15或以后的型号来说，有一个硬件按钮[Action Button](https://support.apple.com/guide/iphone/use-and-customize-the-action-button-iphe89d61d66/ios)。你可以自定义长按Action Button时候的系统行为。这里面我们可以把刚才做的Shortcut连起来。

所以现在体验就变成了我们长按Action Button，就会有一个我们刚才做的网页前端蹦出来，并且自动开始录音。我们直接就可以开始说话了。这个体验相比于之前基于Telegram或者甚至基于网页收藏夹的体验又好了很多。

## 第三轮迭代：用app实现零延时

在这么用了一段时间之后，我确实感觉爽了，但是还是不够爽。一个主要的问题是，就像下面的动图显示的那样，当我从我长按Action Button到这个网页加载完毕开始录音，还是有2秒左右的延迟。这个确实已经是个不错的体验了，但是实际中对人的心理影响还是蛮大的。

![Web application is slower.](/images/brainwave_web.gif)

要想优化任何问题，第一步就应该是搞清楚它的瓶颈在什么地方。这里面比较明显有网页内容的下载、渲染、麦克风的初始化和网络连接。除了网络连接以外，其他三个其实都可以预先加载好。但是因为我们每次都要重新下载和加载这个网页，所以很多优化方法用不上。

一个非常直观的解决方法就是我们把它从一个网页变成一个app。那这样它就可以在系统后台挂载了，每次不用重新从网页上下载，不用重新初始化麦克风，甚至网络连接都可以挂起，到前台的时候直接重连就好。稍微想一下，这个响应时间可以做得特别快。所以我就又在[Cursor的帮助](/ai-coding.html)下做了一个iOS的客户端，在上面说的缓存各种资源以外，这个App还干了几件额外的事情。

第一件事情是：它实现了一个URL scheme，这样可以和Shortcuts进行集成。这个类似于网页版的"start=1"的URL parameter。这样当我们长按Action Button的时候，它就会使用这个特殊的URL scheme来调用这个App。在这种情况下，这个App就会立刻自动开始录音，而不用等用户手动点录音按钮。

第二个是它利用了苹果的Universal Clipboard，实现了当你在App上说了一段话之后，这个话会自动地拷贝到包括iPhone、Mac等所有设备的剪贴板里面，而不用像网页版因为iOS的系统限制一定要再手动按一个拷贝按钮。这一下又为这个工具带来了一个新的使用场景：在Mac上写作的时候，我也可以通过长按Action Button，在iPhone上呼出这个程序。讲完话之后，在Mac上直接按Cmd + V粘贴，结果就出来了。

第三是，在使用网页版的时候，有时候我讲了一大段话，结果发现网络连接有问题，全白说了的情况。为了解决这个问题，这个App还提供了一个重发功能。你可以选择把刚才说的话作为一个音频文件保存在本地的File App里面，也可以把它直接原样重发给客户端。这在网络断了的情况下特别好用。

第四是，因为App原生就支持本地化，所以我们可以根据用户的系统语言自动进行中英文适配。这个对AI的功能没有影响，只是在界面上对用户更加友好。

![App is much faster.](/images/brainwave_app.gif)

在经过了这些改进之后，如上面的动图所示，整个系统无论是可用性、健壮性还是响应时间，都有了翻天覆地的变化。我们只要长按Action Button，几乎没有任何延时，立刻就能开始说话。而且说完话之后，结果就拷贝到了所有苹果设备的剪贴板里，去哪儿都能用，特别方便。所以总的来说，我们通过这一系列的改进，把用户体验做了一个系统性的提升。

## 使用Cursor快速开发的坑

我的整个开发过程都是在 Cursor 的帮助下进行的，包括和 GPT API 的集成、FastAPI 的后端、网页前端、iOS App，都是通过 Cursor 完成的。整个过程大约花了 8 小时左右。其中，API 集成加后端加网页前端花了大约 3 小时，剩下 5 小时都是在跟 iOS 作斗争。主要时间其实花在了重构代码，让它的工程质量更高，而不是在实现功能上。最终的代码用了 MVC 架构，各个函数放在多个文件里，方便复用，逻辑也比较好。但里面也有一些细节比较花时间，比如 OpenAI 要求 API 上传的文件的采样率在 24k 赫兹，但是不论是网页还是 iOS，流行的采样率都是 48k 赫兹，AI对这个很不适应，老把正确的代码改错，中间浪费了不少时间。

总体感觉 Cursor 比 Copilot 或者类似的裸 ChatGPT 写代码还是要方便很多的。最关键的就是我的手工操作少了很多，不用拷贝来拷贝去。在使用 Cursor Composer 的情况下，我甚至连创建文件、切换标签这种东西都不用手工去做了，它都会自动帮我做好。它甚至可以帮你把错误信息的拷贝粘贴这一步都省掉。Cursor Composer 和 Linter 有比较紧密的结合，它会像 Agent 一样，不断地调用 Linter，然后再调用 LLM 去修正 Linter 的错误，直到有一个能够过编译的结果。

因为这三点，我使用 Cursor 写程序的感受和使用这个新开发的 App 写作的感受一样，就是可以真的集中精力思考我到底想要什么，而不是把精力花在给 LLM 打字、去复制粘贴代码、创建文件，或者把错误信息贴来贴去上。但这里面也有一些坑，就是因为整个过程太方便了，所以一个非常自然的反应是，我们就不想看它写的代码了，直接Accept Accept。这会造成一个问题是，有可能它做了一个很大的改动，我们全盘接受之后，发现不是我们想要的，但因为改的文件太多很难撤销回去了。

这种情况有两个可能的解决方法。第一个是我们使用 Git，相当于给我们自己装一个时光机器。第二个是还是得坚持看一下它写的代码是不是我们想要的。不一定要抠细节，只要大概看一下有没有做我们不想要的改动就可以了。及早地发现这些不想要的改动，才是更根本的解决方法，而不是被动地依赖时光机器，跑出来才发现不对，再回头改。总的原则就是：我们要做好AI的老板，要评估和控制它做出来东西的质量，而不是反过来我们被动地去接受它给我们的东西，然后adhoc地去改。这也是我们的[AI课程](https://maven.com/kedaibiao/genai)中强调的重要思想。

## 后记：集成收费功能

书接上回，在做出来一个使用 AI 高效进行辅助思考和沉淀的工具之后，朋友圈里不少高手在问哪里能够下载使用这个 app。我之所以暂时没贴出来 app 链接的原因是这个 API 还是蛮贵的，我希望在这个 app 里加入收费的功能。这样哪怕不说长远的盈利，至少短期来看也能分担 API 的成本。但是在稍微进行了一些系统设计之后，我很快就发现这是一个非常复杂的东西，比我之前想象的要复杂很多。具体来说，它主要有以下几个难点：

第一，要想收费就必须要有用户的概念。但只要牵扯到用户的管理，尤其是密码的存储，就会牵扯到信息安全里的很多最佳实践，比如加盐、哈希、令牌鉴权等等。这里面一方面需要对数据库有着相当健壮的配置，另外一方面在代码的撰写上也有很多技巧。不论用不用 AI，都需要花很多的精力去保证这些代码是符合最佳实践的，才能保证用户的信息安全。

第二是就算做好了用户管理，给他们发 email ，包括单据、订阅、退款的通知等等，也不是一个简单的问题。我以前确实做过一些自己搭 SMTP 服务器批量发送邮件的事情，但是这种服务器很容易被各大邮件服务提供商认为是垃圾邮件。要想避免这一点不是完全不可能，但需要投入大量的精力。当然市场上也有很多类似 Mailgun 或者 SendGrid 这种批量邮件发送的服务，但是它们的配置和集成也是一个需要时间的东西。

第三个难点在于支付本身，这是一个巨复杂的东西。现在市场上流行的方法是和 Stripe 等支付服务的 API 进行集成。但你仔细想的话会发现里面有很多细节需要处理，比如我们要给新用户提供试用，给老用户要提供订阅服务，订阅了就要给他发每月的单据，续订需要及时提醒，如果用户不续订了，有时候根据法律还要退款。这里面每一个功能都需要我们单独和 API 进行集成，可能还要提供自己的政策和网页，特别复杂。

所以总的来说，给一个 app 加入收费功能是一个听起来很简单但实际上极其复杂的一个东西。从这个角度来说，我突然理解了为什么 Apple 要像 App Store 上面的软件抽成 30%。其中一个重要的好处是，如果我做一个 iOS app 的话，以上所有东西我都不用考虑，或者说至少我可以不考虑。

对于用户管理，我可以直接使用 Apple ID，Apple 会帮我做好所有的邮箱认证、密码管理等等服务，直接给我一个经过验证的用户 ID，下面我就可以用这个用户 ID 在服务器这边进行所有的管理。此外在登录方面，我也可以直接调用 Face ID 等功能进行登录，用户体验很好。
在 email 方面，我也不用烦心，相关单据的发送也是 Apple 完成的。当我需要发送 newsletter 之类市场材料的时候，我也能拿到每个用户的邮箱，使用 Mailchimp 之类的软件批量发送。
至于支付就更简单了，一切都是 Apple 来解决，我不用跟任何 API 打交道。不论是续订的提醒、单据的发送、扣款、退款，全都是 Apple 搞定，我只要坐着收钱就行。

从这个角度来说，我瞬间理解了为什么苹果能抽到三成的"苹果税"，这里面确实是有非常大价值的服务，能够极大的缩短我 go-to-market 的时间。当然，到底是选择一次性把这些开发成本给交完，还是慢慢出血交 30% 的流水，这就要看不同公司、不同产品的情况了。至少对于我这种目前看市场不是特别大、比较需要快速试水迭代的产品来说，还是非常有吸引力的。

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
