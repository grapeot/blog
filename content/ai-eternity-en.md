Title: My Journey to Cybernetic Immortality: An Experiment to Push Life's Boundaries
Date: 2025-07-06 20:00
Category: Computing
Tags: AI, English
Slug: ai-eternity-en

## How AI Leveled Up from Intern to Mentor

Over the past couple of years, my relationship with AI has undergone a fundamental transformation. It has evolved from a capable but subordinate intern who followed my instructions into a "big brother" figure—a mentor capable of providing profound guidance on complex decisions. This shift was sparked by my solving one deceptively simple problem.

The catalyst for this metamorphosis was high-quality, high-volume context.

Let me share a real example. A while back, I faced a complex career decision involving several potential opportunities, each with its own intricate set of pros and cons. I took about ten minutes to dictate everything I could think of into my phone: the history behind the decision, my long-term goals, the technical and organizational challenges of each option, my boss's likely perspective, and even the potential concerns of higher-level management.

I fed this raw, unedited stream of consciousness directly to the most powerful AI model available at the time. What I got back wasn't a simple list of pros and cons, but a remarkably mature analysis. It pinpointed a core conflict between my long-term ambitions and short-term choices—a conflict I hadn't fully recognized myself. Based on my own assessment of industry trends, it also raised a potential risk I had completely overlooked. The depth and breadth of the analysis far exceeded my expectations. It even offered perspectives from a VP and CEO, which helped me proactively address their main concerns when I presented my case. That half-hour conversation with AI gave my career a significant boost.

This experience led me to a crucial realization: the real bottleneck in our collaboration with AI isn't its intelligence, but the bandwidth of our communication. The limitations we often perceive in AI are, to a large extent, merely symptoms of this narrow communication channel. This article is a reflection on the series of experiments and thoughts that followed, all aimed at systematically widening that bandwidth.

## 1. Paving the Road for Expression to Combat Input Friction

My journey of discovery was not a single leap but an iterative process of deepening understanding.

Initially, like most users, I was amazed by AI's capabilities but also frustrated by its limitations. It would often provide unsuitable solutions, confidently spout nonsense, or suggest ideas I had already considered and dismissed.

Through continuous use and interaction, I began to see the problem from an empathetic viewpoint: if I were the AI, could I provide a better answer with only the few brief prompts I was given? The answer was almost always no. This led me to a realization: AI, like humans, needs an onboarding process. A new employee, no matter how brilliant, can only offer superficial or impractical advice without understanding the company's background, past projects, and team dynamics.

This observation formed my core hypothesis: AI's performance is often constrained not by its intelligence, but by the context we provide. The richer and more precise the context, the more it transforms from a generic intern into a nuanced expert. Take hallucinations, for example. They often occur because AI is trained to be helpful. When it lacks sufficient context, it must make assumptions to fulfill that "helpful" directive, leading to made-up "facts." Providing context is not just an auxiliary factor for high-quality AI responses; it's a decisive one.

But this hypothesis immediately ran into a practical challenge: providing sufficient context requires a massive amount of input. I personally dislike typing. It's inefficient, especially on a mobile phone. Even on a computer, the speed of typing lags far behind the speed of thought. This high input friction is the single greatest obstacle preventing us from unlocking AI's full potential.

So, I built myself a [voice recognition tool](/realtime-gpt-en.html). Unlike traditional voice-to-text solutions, it uses the [GPT-4o-realtime model](https://platform.openai.com/docs/guides/realtime), which excels in accuracy, low latency, and intelligence. This enabled me to communicate with AI in a "think out loud" or even "brain dump" fashion. I no longer needed to meticulously craft written language; I could say whatever came to mind, and the AI could understand me perfectly, even when I spoke quickly.

While not a perfect solution, this tool dramatically expanded the communication bandwidth between me and AI. It allowed me to pour a massive amount of context into it at a very low cost, laying the groundwork for all subsequent experiments.

## 2. Building a Foundation for Memory to Combat Forgetting Friction

After solving the single-session bandwidth problem, a new, deeper pain point quickly emerged: my new AI mentor had amnesia.

I found that while I could efficiently provide context, I spent most of my time not asking new, insightful questions, but mechanically repeating the same information. For every new conversation about a project, I had to re-explain its history, technical background, team members, and my personal preferences. It was a terrible feeling, degrading a creative, intellectual exercise into a repetitive, manual task.

My initial workaround was simple: I started maintaining a series of "Master Prompts" in local documents, like "My Family Background" or "Project A Background." This helped to some extent, but the experience was still poor. I had to manually find, copy, and paste these prompts, and I had to remember to update them whenever information changed. It was a high-friction, unsustainable solution.

Through this process of manually maintaining prompts, I gradually realized that our current way of using AI is like cramming for an exam after skipping all the classes. We keep AI completely isolated from our lives and only hastily brief it on our background when we need it to solve a problem.

This prompted a fundamental shift in my thinking: What if I didn't have to cram? What if I could invite AI into my life on an ongoing basis, letting it observe and learn on its own, rather than relying on my periodic reports?

This idea directly led to my next core experiment: I started using my Apple Watch to make [all-day audio recordings](https://yage.ai/life-api-part2-en.html) of my life.

The setup is simple: I just open the Voice Memos app on my Apple Watch. Its battery can handle about ten hours of continuous recording, covering most of my day. Each day, I collect these audio files, run them through speech-to-text, and store the resulting text in my personal database.

At first, I just wanted to use these recordings as a source of background knowledge. But I soon discovered an unexpected compounding effect. Because I had already developed the habit of "thinking out loud" with my voice tool, my daily recordings naturally captured a wealth of raw material from my deep interactions with AI—including the complex tasks I assigned it, my corrections to its output, and my own thoughts and insights.

This made my recorded data incredibly valuable. It was no longer just a collection of life's ambient noise, but a high-quality information funnel, constantly absorbing the fragmented but precious information I produced, whether intentionally or not. In a sense, my earlier efforts to solve input friction had unintentionally paved the way for this solution to memory friction, allowing the recording experiment to quickly demonstrate its immense value.

Of course, having data isn't enough; you need to use it effectively. To that end, I built my own ChatGPT-like tool called the Agentic Workbench. Its key feature is its ability to connect to my local, personal database. I implemented an Agentic Retrieval System, which isn't a fixed workflow like RAG. Instead, when the AI is thinking through a task and autonomously determines it needs more background information, it triggers a search tool. It formulates its own keywords, retrieves relevant information from my memory database, and uses that information to support its analysis and response, iterating on the keywords for further searches if necessary. This turned information retrieval into a low-friction, AI-driven process.

For instance, I was driving once and, distracted, nearly sideswiped another car. In the past, because I was driving and couldn't take notes, the moment would have been lost. But because I was recording, I could immediately start a verbal post-mortem without any action on my part: what just happened, my initial reflections, what I thought the problem was. I even gave the AI a to-do item on the spot: "Remind me tonight to summarize the lessons from this incident and add them to my 'driving mistakes' log." Later, my automated scripts processed the recording, identified the to-do item, and generated a reminder. The incident wasn't forgotten; it was captured and processed, contributing to my long-term driving safety. This is the value of combining zero-friction recording with an agentic system.

## 3. From Auditory to Visual: Expanding the Boundaries of Perception

Once the workflow for capturing and utilizing auditory data was running smoothly, a logical question followed: if auditory information is so effective, what about visual information?

Human perception is multimodal, with vision often being the dominant sense. To give my AI partner a more comprehensive understanding of my physical environment, I began my next experiment: recording my visual world with a first-person camera.

I started with a magnetic wearable camera, the Insta360 Go 3S. It's tiny and can be easily attached to a magnetic necklace to record a first-person perspective. However, it has significant limitations, such as a battery life of only about four hours, making true all-day recording impossible.

This limitation once again sparked my inner engineer. I am currently using an ESP32 microcontroller and a dedicated CMOS image sensor module to design and build a wearable camera that leverages the microcontroller's deep sleep function to achieve much longer battery life. The project is still in progress, but the basic hardware prototype is working.

Although the tools are still imperfect, I have been conducting this visual recording experiment for two weeks. After capturing tens of thousands of images, my initial impression is that it captures a vast amount of information that is highly complementary to the audio recordings. For example, when I asked an AI to analyze the photos from the past week, it was able to identify my frequently used objects, the places I often go, and even the physical distance and posture in my interactions with family members.

Of course, how to structurally utilize this visual information, when it should be invoked by the AI, and how it can be fused with auditory information to support AI's reasoning are all questions I am actively exploring. This experiment is more of a starting point, opening a new window for AI to observe and understand the physical world I inhabit.

## 4. From Thought to Action: When the GUI Becomes Friction

With my AI system possessing increasingly rich multimodal perception and long-term memory, it had already become a powerful thinking partner. But my exploration didn't stop there. A brilliant thinker who cannot act is ultimately limited in value.

Thus, my next direction became clear: how to enable AI to cross the chasm between the digital and physical worlds and become an action partner that can do things for me?

In this process, I discovered a new, almost ironic type of friction, which I call "action friction." This friction arises when an AI has to operate systems designed for humans, systems full of unstructured steps and redundant information.

Let me give two classic examples.

The first is grocery shopping. Most of us now use apps like Instacart or Weee!. But if you analyze the process, you'll find it's still a high-friction, manual task. You have to search for keywords, choose from a bunch of brands, add items to your cart, and try to remember what you're out of at home. The whole process is filled with repetitive clicks and short-term memory burdens. To me, this is a low-value, optimizable time sink.

When OpenAI released its o3-based Operator (the previous gpt-4o versions were too difficult to use), I immediately experimented with this scenario. My instruction was not a simple shopping list but a more macroscopic goal, such as: "Analyze my Weee! orders from the last three months, and based on my purchase cycle, generate a shopping list for this week and add it directly to the cart."

The result was ideal. It acted like a true butler, analyzing that "you consume a carton of milk every 5 days on average, and it's now been 6 days," and then automatically added all the necessary items. In the end, a tedious 30-minute manual chore was transformed into a 5-minute intellectual task of final review and checkout.

The second example, shipping a package, better illustrates AI's superpower in taking action. Filling out an address online in the US is a classic high-friction experience. A single piece of address information is forcibly split into four or five input fields on a webpage: street number, street name, city, state (usually a dropdown menu), and zip code. Each field has a different interaction model.

I tried letting the Operator complete this task for me. I just gave it a single, complete address string and the command: "Go to the Shippo website, use UPS to send this package for me, and don't select insurance." Like a skilled operator, it navigated the website step by step, filling in the correct information, selecting the right state, and perfectly understanding and operating this redundant, human-designed GUI.

This experiment left me with a powerful impression. The Graphical User Interface (GUI), a great invention from decades ago meant to reduce friction for ordinary computer users, has in many cases evolved into a new, significant source of friction itself due to its complexity. The emergence of AI has completed an interesting historical cycle. As a non-human intelligent agent, it is exceptionally good at operating these friction-filled GUIs designed for humans, liberating us from the cage of "convenience" we built for ourselves.

So, AI is not only reducing our cognitive friction but also the friction of action between us, our lives, and the digital tools of our own creation.

## The Endgame and Philosophy: My Cybernetic Immortality

Now, we can return to the original question: why am I doing all of this?

The driving force behind it all is my pursuit of a pragmatic form of **"Cybernetic Immortality."**

To help you understand this concept better, let's start with a very practical calculation. Take the grocery shopping example from before. If I drive to the supermarket myself, the round trip plus shopping takes about an hour and costs $100. If I use AI assistance to shop online, it might take only 10 minutes, but the goods plus service fees might cost $120.

There's a trade-off here: I spent an extra $20 to save myself 50 minutes. How do I view this transaction? I see it as using $20 to buy back 50 minutes of my life. This is a very serious equation. Because in those 50 minutes, I can spend time with my children, brainstorm a new experiment, or read an important paper. The value of these activities far exceeds $20. This mindset of trading money for life is the simple starting point for all my actions.

This way of thinking, refined through continuous practice and reflection, has formed my personal philosophy, which I call Cybernetic Immortality. I want to emphasize that the "Cybernetic Immortality" I speak of is not the ethereal consciousness-uploading of science fiction films. It is an extremely pragmatic view of life that any of us can practice right now.

Specifically, as I see it, Cybernetic Immortality comprises three core layers:

First, **increasing the density of life.** This is essentially a form of time arbitrage. By using tools like AI, I can trade large amounts of time spent on low-value, repetitive manual labor for time invested in high-value intellectual work, such as creation, learning, and deep thinking. While a day still has only 24 hours, the density of one's life output can be completely different.

Second, **improving the quality of life.** This relates to the focusing of energy. Human willpower and concentration are finite resources. By outsourcing tedious tasks to AI, we not only save time but, more importantly, we conserve precious mental energy. This allows us to engage in the things we truly love with a fuller, more focused state of mind, which directly determines our daily happiness and satisfaction.

Third, **expanding the boundaries of life.** This is the part that excites me the most. Some things cannot be solved simply by spending more time; they involve breaking through capability barriers. Just as I could never experience flight without an airplane, which expanded the boundaries of our physical movement, AI is a tool that is dramatically expanding the boundaries of our cognitive and creative abilities. It can act as a mentor, offering high-level perspectives I wouldn't otherwise have access to. It can help me analyze massive amounts of data, completing research that would be impossible for me to do alone.

So, for me, the essence of Cybernetic Immortality is to use intelligent tools to maximally compress the junk time and repetitive labor in our lives, while infinitely amplifying our creativity, experiences, and impact. It's about living a life of infinite breadth, depth, and height within a finite amount of time.

Of course, my exploration is far from over.

Currently, all my efforts are still focused on building an "Augmented Me." This system is highly personalized, centered around me and serving me.

But this raises a grander, more complex question: What will the world look like when this capability is no longer my personal patent, when everyone starts building their own cybernetic immortality system?

How will my cybernetic immortality system interact with others? How will two AI mentors, each with a complete memory and high-level perspective, assist their human counterparts in collaboration or competition?

And are we, so deeply assisted and influenced by AI, still the ones who are truly living our lives?