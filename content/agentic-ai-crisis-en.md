Title: The Dilemma of Agentic AI: How to Solve the Productionization Challenge?
Date: 2025-01-02 18:00
Category: Computing
Tags: AI, English, Agentic AI
Slug: agentic-ai-crisis-en

## The Dilemma of Agentic AI

In our [previous series of articles](/cursor-to-devin-en.html), we introduced the basic concepts and usage of Agentic AI. Through a series of impressive demos, we showcased this revolutionary AI paradigm. However, if you're like me and have tried to apply Agentic AI to various scenarios in life and work, you'll discover that while it appears to have many impressive applications and can handle many tasks, it often only achieves about 70-80% completion. To make the results truly usable, significant human interaction is still required.

For instance, we can give Cursor some basic information and have it write a product introduction. However, the content it produces lacks depth, brand tone, clear target audience, and often has a very AI-like writing style, requiring extensive human polishing.

We can use Realtime GPT or Cursor for speech recognition or translation, but it still makes mistakes with specific names or terminology that need manual correction.

We can use Cursor to call Blender's Python API to generate a 3D demo video, but strange errors occur, like incorrect camera angles or filming empty spaces.

We can have Cursor write code to call OpenAI's API, but whenever we tell it to use the GPT-4o model, it silently changes the model name to GPT-4. The program runs, but at a much higher cost.

We can use Cursor to create flowcharts using tools like Mermaid, but the resulting diagrams often have chaotic structures and messy styles, far from what we want. We need to prompt it many times to achieve the desired result.

In these examples, my feeling is that Agentic AI is somewhat awkward in many application scenarios. While its rough output does reduce the effort we need to invest, we still need to spend considerable time repeatedly prompting it to achieve our desired results. Moreover, if you think carefully, you'll realize this isn't just a minor imperfection in AI - quite the opposite, it's a fundamental crisis determining whether Agentic AI is practical.

The deeper reason is that what makes Agentic AI so appealing and brings multiplicative improvements to our productivity is mainly because it allows us to focus on the final deliverable. We only need to define what we want, rather than spending time explaining how to achieve it. By completely delegating the actual execution details to AI, we can truly set and forget, run multiple tasks in parallel, and achieve scalability. However, if in many scenarios, after AI delivers a result, we still need to spend significant time discussing and refining with it, this completely negates the advantages and value of Agentic AI.

In other words, while Agentic AI has many impressive scenarios where it can deliver previously impossible tasks to a very high standard in a short time, for many other scenarios, it still only achieves about 70-80% completion and requires significant human intervention. This limitation often leads to enterprises getting stuck in extensive manual remediation when trying to implement Agentic AI, preventing projects from scaling. This poses a fundamental crisis to the advantages of Agentic AI. Does this mean that outside its specialized scenarios, for most cases, its productivity improvements remain elusive?

It's important to note that the issue we're discussing here is different from our previous article. The previous article focused on how we can build tools to solve problems when AI can't do something, like performing web searches. That was a "zero to one" leap. But this time, we're discussing situations where AI can do the task but only achieves 70%, with the remaining 30% requiring our meticulous attention to finish. This pain point is more common and trickier - often more decisive in determining whether Agentic AI can be widely implemented.

In this article, we'll further explore: Why does Agentic AI seem to only deliver "70-80% completion," with the remaining portion requiring human polish? Does this mean Agentic AI is another hype that's easy to demo but difficult to implement?

## Root Cause: Disruption of Self-Iteration

At first glance, this issue with Agentic AI seems reasonable, but thinking deeper reveals a seemingly contradictory point: Isn't the core advantage of Agentic AI its "self-iteration"? If so, why do these application scenarios require so much human polishing?

Looking at our successful cases shown in the [livestream](https://www.superlinear.academy/c/academy/cursor-agentic-ai) - downloading CVPR 2024 papers, visualizing Amazon and Google stock prices, generating memes... these tasks share a common characteristic: AI's iteration standard is simply getting the program to run. Once it runs, you usually get a decent result. Agentic AI succeeds here partly because it genuinely has the ability to self-iterate and make programs run, and partly because these tasks themselves aren't complex - getting the program to run is roughly equivalent to achieving the goal.

However, problems arise when we try to extend Agentic AI to broader scenarios based on these successes. For some more complex tasks, a running program merely means the script can execute, not necessarily generating the results we want. Take the Blender video rendering example - the program can complete the rendering process, but AI can't see if it's rendering empty frames. Similarly with flowcharts, the program won't throw errors, but AI can't judge if the structure is messy or the theme is wrong through error messages.

Therefore, our fundamental challenge is that **the self-iteration component of Agentic AI itself is broken**. While it can make programs execute, without additional feedback mechanisms or objective quality assessment of the finished product, it can't build a complete iteration loop to continuously correct its output flaws. In other words, it appears to be running loops, but since it can't perceive "whether the product is good" and lacks ready-made success criteria, that crucial "iteration feedback" component completely fails.

Specifically, the "self-iteration" feedback loop is broken for two main reasons:

1. Product/AI Capability Gaps

    Some Agentic AIs (like Cursor) lack visual or multimodal capabilities, preventing them from "seeing" whether their output meets expectations. It can run a Blender script but knows nothing about the rendered video's content, let alone correct camera angles based on the footage. The same applies to web rendering - if AI only gets raw data or HTML source code but can't understand the actual layout, it doesn't know if the page formatting is messy. Unable to see or understand visuals, Cursor can only passively wait for us to point out problems, losing its automatic iteration ability.

2. Strong Subjective Standards and Open-ended Problems

    Some tasks, while Cursor can read and generate text, have highly subjective success criteria that can't be solved just by correct program execution. For example, writing style in translations or brand tone in copywriting - it can make guesses, but doesn't know if clients want formal or playful content. In these scenarios, Agentic AI can only repeatedly wait for us to say "not humorous enough" or "too colloquial" before making adjustments. It lacks a clear mechanism to measure whether it has achieved the ideal writing style, unlike the simplicity of "test cases passed means OK."

When these two situations occur, Agentic AI degrades into "traditional AI" - requiring us to constantly inject feedback and instructions to barely polish the results. Once this cycle becomes highly dependent on human input, it loses the efficiency of "liberating human resources and parallel processing" that Agentic AI should bring. This is also why many vendors and researchers are extremely focused on how to give Agentic AI richer perceptual abilities, and how to establish objective or semi-objective criteria for highly subjective tasks. Only by solving these two problems can Agentic AI truly break free from "70-80% completion."

## Complementing Self-Iteration Mechanisms: Perception Channels and Evaluation Standards

However, if we look at it from a different angle, this doesn't mean Agentic AI is doomed. Instead, it reminds us that **in more complex scenarios, Agentic AI still needs human-machine collaboration**, just at a more advanced level.

1. How to Complement AI's Perceptual Deficiencies?

    If the first type of deficiency (lack of vision, inability to know rendering results) is the main bottleneck, we can create a small tool for AI to help it capture screenshots of rendered images, process them with other visual models, or at least convert images to text descriptions so AI knows if there are obvious empty frames in the video.

    From a technical implementation perspective, "adding multimodal capabilities to AI" might only require (letting Cursor) write a script to call Claude or similar Vision APIs, giving Cursor an extra pair of "eyes." But making every scenario seamlessly integrated still requires considering complex coupling and debugging costs. It's not as difficult as imagined, but it's not simple either - each real business scenario might have unexpected pitfalls. If the scenario frequency is particularly high and ROI is large, this path is undoubtedly worth pursuing; if it's just a one-time need, manual guidance might be more cost-effective.

2. How to Define Clearer Success Standards?

    If the second type of problem (high subjectivity) is the main obstacle, then in scenarios like translation, copywriting, and flowchart creation, we need to more clearly tell AI "what is good." For example, when doing internal company translations, fix common professional terms or names, or when writing copy, must use a "light and humorous but not vulgar" tone. We no longer just say "translate this" or "write me an article," but crystallize those "implicit rules" into Prompt files or custom scripts.

    Meanwhile, we can even introduce a judge Agent to determine if the product quality meets standards. This Agent can access internal company libraries to understand more internal standards, like color schemes and brand tone, then provide scores or revision suggestions. Thus, AI can form a new internal feedback loop, without needing humans to correct every small flaw.

## High-Dimensional Collaboration with AI: Hands-off Boss or Super Employee Manager?

Actually, the fact that Agentic AI currently can't fully automatically handle various "scenarios with subjectivity and uncertainty" doesn't indicate its inadequacy. On the contrary, this perhaps proves its capabilities are stronger than ordinary AI - because we carry higher expectations and push it toward more complex tasks, making it face thorny problems that we wouldn't have expected AI to handle in the past. So when we say "it achieves 70%, still needing lots of human polish," it's often not that Agentic AI is regressing, but that our requirements for it have become broader and deeper.

It's like a car appearing reliable because we've screened out many ambiguities on the road: at traffic lights, humans judge whether to turn left or right; when encountering police stops or wrong-way electric bikes, humans handle those harder decisions. The car just needs to focus on "gas, brake, steering," so we think traditional cars are very reliable. But now cars with autonomous driving capabilities, although actually stronger than traditional cars, seem dumber because they're starting to encounter these previously untouchable uncertain problems.

Agentic AI follows similar logic. Precisely because it's more capable than ordinary AI, it's being used in more complex real problems, starting to encounter style aesthetics, visual judgment, data noise, contextual ambiguity, and various other pitfalls. At this point, it frequently pulls us in. This isn't AI getting dumber, but rather the difficulty level of its problems significantly increasing. It's precisely because its capabilities are strong enough that it's given more work, naturally more likely to expose shortcomings. This gap between actual intelligence level and perceived intelligence level is something we should particularly note when analyzing AI.

Therefore, how to help Agentic AI establish more complete "perception channels" and "evaluation standards" has become key to whether we can achieve breakthroughs in Agentic AI applications. This is probably also the focus of product form competition among various companies in 2025:

1. Enabling AI to Self-Iterate Effectively (Right Direction): Only through a company's long-term accumulation and thorough understanding of business problems can we give AI clear evaluation standards. On this foundation, AI can effectively self-iterate.
2. Enabling AI to Self-Iterate Efficiently (Fast Speed): Meanwhile, for evaluation standards beyond pure text, we also need to give AI more dimensional cognition, obtaining external information through multimodal interfaces or tools to efficiently conduct subsequent iterations.

Combining these two paths can help AI maintain effective and efficient self-iteration in more complex scenarios - both seeing results and knowing right from wrong truly deserves the Agentic paradigm.

Looking back, this trend perfectly corresponds to how we nurture new employees. For an ordinary worker, you need to break tasks into simplest steps, then list them one by one in SOPs, telling them "do this, then that"; for a highly capable new employee, you focus more on telling them "you need to achieve this business goal while not violating company culture," letting them explore details themselves. Agentic AI is that higher-potential employee, not needing us to break down problems piece by piece - it can spontaneously dispatch tools and automatically fill in large gaps in intermediate logic. But it also needs us to clearly define final goals and standards from the start. If a company lacks sufficiently rich documentation, standard color schemes or translation specifications, AI will repeatedly ask you "Is this writing okay?" "Is this translation too aggressive?" - just like a newcomer constantly needing you to correct their understanding of company style.

From this perspective, Agentic AI is more like an increasingly capable super employee who still needs our high-level management and training - as long as you're good at organizing requirements, defining standards, and opening necessary perception channels for it, it can quickly push previously seemingly tedious or impossible tasks to 70%, 80%, or even explore up to 90% or higher in many fields.

Therefore, what determines whether AI can truly land and demonstrate value has never been about how powerful the technology itself is. More core is often: Is your understanding of business processes deep enough? Can you distill those "ideas existing in team minds, hidden in internal documents" into clear instructions and goals? If you haven't even figured out your enterprise's market positioning, brand style, or what customers really need, even the most advanced Agentic AI can only self-iterate aimlessly. Ultimately, AI is just an aid; it can't replace you in insight into business essence and defining success standards. The stronger it gets, the more you need to focus on higher levels, depicting profound insights into products and users, so it can "know where to go."

## Postscript: How This Article's Viewpoint Gradually Deepened

<details>
<summary style="color: #3498DB; cursor: pointer;">Click to expand</summary>

<p>Previously, some colleagues were interested in how I iterate viewpoints and explore a topic's depth when writing. Today, I'll use an example to explain how I dig into a project and make its arguments increasingly profound.</p>

<p>The background is that I recently tried using Agentic AI like Cursor to draw flowcharts. This way, I just need to chat with it describing what I want to draw, and I can get a diagram, instead of drawing shapes, dragging cursors, and setting fonts in PowerPoint. However, the problem is that while Cursor can output a rough flowchart, slowly grinding through various details with it isn't much faster than drawing in PPT.</p>

<p>I eventually solved this problem using Prompt Engineering methods. By accumulating a Markdown file, I detailed my various preferences and detail requirements in it. When @ this Markdown file, Cursor could largely draw the diagram correctly in one go. So I wanted to write an article to introduce this discovery.</p>

<p>The <strong>first version</strong> of this article was a natural introduction to this problem. I first introduced AI's capability limitations (can't get diagram details right), then introduced how using tools to expand AI's capabilities can solve this problem. Next, I discussed more technical expansions, like when to use tools, how to create tools, and how to manage when tools multiply.</p>

<p>But you can see this version has no appeal - why should I care about your niche need to use Cursor to draw flowcharts? So in the <strong>second version</strong>, we mainly adjusted the structure focusing on story development and reader perception. I first introduced an abstract problem, trying to evoke reader resonance. This problem is that even for advanced paradigms like Agentic AI, we'll encounter in certain scenarios the issue that "making a rough 70-point work is simple, but the remaining 30 points still need lots of human effort to finish."
Then introduced the solution: we can build tools (in this case, prompts) to solve this problem. Then detailed when and how to build tools, and how to manage many tools.
Finally deepened this technical problem: the significance of this technical solution isn't just solving the flowchart drawing problem itself, but more in this mindset of accumulating and reusing tools, which will help you eventually precipitate a tool library. And the reuse and combination of these tool libraries will make AI's capabilities exponentially stronger as time passes.</p>

<p>Through such deepening, we deepened the depth of viewpoints.</p>

<p>In the <strong>third version</strong>, we further expanded our argument. The previous argument was purely technical, but actually this argument's other side is mindset. Why when we discovered AI could only do 70 points, we didn't feel this task might not suit AI and abandon it returning to manual work, or passively accept this fact - I'll manually supplement the remaining 30 points? Why did we think about actively changing the status quo, making AI succeed in one go through tools? This is a Builder's Mindset.</p>

<p>So in article organization we can use two lines, explicit for technology, implicit for mindset. Through setting foreshadowing, let readers subconsciously realize mindset's importance while reading technology. At the article's end, we throw out Builder's Mindset to deepen the theme, making readers realize this article actually has two aspects of Learning, thus increasing the article's drama and tension.</p>

<p>The <strong>third version</strong> mainly focused on solving the "AI from 70 to 100 points" problem, without dwelling on causes. But if you think carefully about why, you'll find this very strange. Agentic AI's core advantage is that it can self-iterate, delivering what we want in one go. Why does it iterate to a 70-point result? In the <strong>fourth version</strong>, we further deepened viewpoints on "why."</p>

<p>After careful thought we'll find this is because AI's self-iteration feedback loop is broken. Either AI lacks ability to verify results, like Cursor lacking visual capabilities; or results are too subjective, like whether flowcharts look good or match my taste, Cursor can hardly judge. So, the solution to the former is we can directly introduce visual models to connect AI's feedback loop, fundamentally solving this problem. But it involves many product and model changes, too heavyweight. Therefore, another method is we adopt an accumulation-iteration approach, making feasible improvements to specific scenarios in short term through building tools. Then like the previous version introduce specific technical solutions and builder's mindset. This argument and organization method further explored internal reasons for this technical problem, thus deepening depth.</p>

<p>In the <strong>fifth version</strong>, we made some comparisons between Agentic AI and traditional AI, further deepening viewpoints. Agentic AI appears to have core features of being able to self-iterate, work completely independently, and indeed achieve good independent work effects in many scenarios. But our argument is this is an illusion. Why can it self-iterate in these scenarios? Because these scenarios are relatively simple, like its success standard is simply program can run.</p>

<p>If wanting to use Agentic AI in more complex real life, inevitably must return to human-machine collaboration theme, otherwise will hit walls. Traditional AI's human-machine collaboration mainly means task decomposition and hand-holding guidance, very artificial. But Agentic AI's human-machine collaboration mainly means humans responsible for defining problems and providing domain knowledge, AI responsible for improving general understanding and decision-making abilities. This actually very similar to human society structure, like companies recruiting employees, on one hand provide training and SOPs helping employees copy examples to complete tasks, on other hand require employees smart enough to infer by analogy, self-learn. So, from this perspective, AI only achieving 70 points in many scenarios isn't Agentic AI's flaw, but rather because it finally touches world's subjective and ambiguous qualities. Then introduce how to solve this problem from feedback loop perspective.</p>

<p>So through these five different versions, we step by step explored deeper meanings behind using Cursor to draw flowcharts. Now when we have fifth version and compare with first version, we'll feel difference really huge.</p>

<p>But actually these explorations weren't done by me alone, many core viewpoints came from <a href="/o1-pro-en.html">o1 Pro</a>. This is also something I want to share. On one hand o1 Pro gives me feeling its capabilities completely different from other AI models. If my attitude toward GPT-4p is "you go help me do this work," toward normal o1 is "wow, this AI knows this thing, not bad!" my attitude or expectation toward o1 Pro often is "big brother, teach me." Under appropriate prompting, it can really bring very deep insights, even deeper than my thoughts. If other AIs often check omissions and fill gaps, telling me things I don't know, o1 Pro truly breaks my capability boundaries, letting me reach previously unreachable realms. I'm now very looking forward to trying o3 model, and also decided to renew $200/month ChatGPT Pro Plan.</p>

</details>

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>