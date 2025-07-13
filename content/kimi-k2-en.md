Title: Kimi K2: An In-Depth Review Beyond the Chatbox
Date: 2025-07-12 17:00
Category: Computing
Tags: AI, Kimi, Agentic AI, LLM
Slug: kimi-k2-en

Whenever a new large model is released, a wave of reviews inevitably follows. But there's an interesting phenomenon: the vast majority of these reviews are confined to the one environment we're all most familiar with: the chatbox.

This is a fundamental limitation. In 2025, with Agentic AI on the rise, evaluating a model designed for agentic tasks within a chatbox is like interviewing a director of engineering with a whiteboard coding challenge. The feedback you get is almost entirely disconnected from their core competencies.

Moonshot AI's Kimi K2, from its very inception, has clearly prioritized Agentic capabilities—the ability for an AI to autonomously use tools to complete tasks. This is a rare choice in the field. For instance, DeepSeek R1 only added tool-calling capabilities long after its initial release, and many platforms like Ollama still lack full support. Kimi K2 takes the opposite approach, developing agentic features as a core competency from day one. This alone merits an evaluation using a paradigm that more closely aligns with its intended design.

## Why We Must Move Beyond the Chatbox: The Dilemma of Evaluating Agentic AI

But first, we need to establish a clear premise: what is the core of Agentic AI? It consists of two inseparable elements:

1.  **Autonomous Decision-Making and Feedback Loops:** This is the essence of intelligence. An agentic model doesn't just passively answer questions; it must be able to autonomously break down a large goal into a step-by-step action plan. Crucially, it observes the results of its actions—like a file being written successfully or code compilation failing—and then uses this feedback to adjust and decide its next move. It's a continuous perceive-think-act cycle.
2.  **Tool Use and Environmental Interaction:** These are the "hands and feet" that connect the model's brain to the real world. The model itself can't directly operate your computer; it needs to call tools. These tools can be OS-level functions like reading/writing files and executing code, or they can be functions that connect to the outside world, like performing web searches or fetching video content.

Understanding these two points makes it clear why simply chatting with an AI is completely inadequate for evaluating its agentic capabilities.

Firstly, chatting, in most cases, doesn't require any tool use, so it's impossible to evaluate that capability. The interaction is purely text generation. You ask, it answers; you don't command, it does. In 2025, using the same methods to evaluate ChatGPT for an agentic model is simply out of touch.

Secondly, the chatbox severely limits the complexity of tasks. A true agentic task requires persistent context and environmental awareness. Tasks in a chatbox are often isolated with extremely short contexts. They cannot facilitate the kind of feedback loop mentioned earlier, where the model decides on the next fix based on the previous failed compilation.

Therefore, the only way to assess the true capabilities of an agentic model is to put it in a real-world environment where it can get its hands dirty. I spent some time systematically analyzing Kimi K2 by directly calling its API through code, in a way that is much closer to its intended design.

## Programming Test: The Friction Between High-Level Intelligence and Execution

In the world of Agentic AI, programming is a classic comprehensive task. But evaluating a model's true programming ability can't be done by pasting code back and forth in a chatbox. That question-and-answer approach fragments a continuous, complex engineering task into countless discrete, trivial interactions. Using AI this way is like trying to send a WeChat message with the mindset of sending a telegram: compressing a rich, collaborative information space into a tiny box with frequent context loss, then manually patching things together. It's both inefficient and counterproductive.

This is precisely why the emergence of agentic programming environments like Cursor or Claude Code is so revolutionary.

Their core value is providing a true arena for AI models to flex their muscles. In this environment, the model is no longer just a chatbot but a copilot with access to tools for reading/writing files, executing code, and more. It can finally work like a human developer in a real codebase, establishing that critical feedback loop and truly participating in stateful, continuous workflows.

So, to assess K2's real capabilities, the first thing I did was integrate it into the powerful agentic programming environment, Claude Code (see the appendix for how), and have it build a Frogger-style game from scratch for me. (Below is a video of the game it created.)

<video src="/images/chicken_cross_road.mov" controls width="100%"></video>

The first version it produced was quite playable, and after a couple of iterations, it was mostly bug-free. However, the development process was far from smooth; it was a bumpy ride. I had a distinct feeling: there's a significant gap between the model's high-level intelligence and its low-level tool execution.

On one hand, Kimi K2's intelligence is top-tier. Its understanding of the task, its decomposition of the game logic, and the quality of the final code are all at the forefront of the industry. It understood my intent well and wrote effective programs or performed effective debugging. It has a very "smart brain."

On the other hand, when this brain needed to interact with the real file system through its "hands and feet" (i.e., tool calls), systemic friction began to appear. For example, within the Claude Code environment, it seemed to have its own preferences for handling file paths, causing it to repeatedly fail when trying to read or write files. The "string to replace not found" errors in the logs weren't accidental bugs but a persistent pattern. It felt as if the model and the tools were speaking the same language with different accents, leading to frequent misunderstandings.

More seriously, when dealing with particularly complex tasks, it would sometimes just... stop. This sudden interruption of the reasoning process is fatal for an agentic system. An agent that cannot reliably complete its tasks is an unreliable one. So, what could be the root causes of these issues? I suspect two main factors:

First, systemic tool mismatch. Claude Code is an environment tailor-made by Anthropic for its own Claude models. Its tool instruction format, internal prompt templates, and expectations for model output are all fine-tuned to perfectly match the "personality" of the Claude models. (General-purpose agentic tools like Cursor or Trae also require specific adaptations for each model. The reason I didn't use them here is that they lack a convenient integration method like Claude Code Router). Kimi K2 was like a highly skilled actor with a different accent, suddenly thrown into a script written for another star. It could grasp the general meaning of the lines but kept stumbling on key nuances of tone, rhythm, and subtext. The file path issue mentioned earlier is likely a symptom of this "accent" mismatch.

Second, a more specific technical reason might be context window limitations. Agentic programming environments are very context-heavy. They need to stuff conversation history, system prompts, and the code from multiple open files into the model's memory. The Claude 4 model that Claude Code is natively designed for has a 200K context window. Kimi K2's currently available API has a 128K context window. When the total context of a task exceeds this limit, the model's behavior can become unpredictable, such as the sudden reasoning halts I observed. This might not be Kimi forgetting what to say, but rather its "workbench" being too cluttered to process new information. This is just one possibility; another is that, similar to Gemini 2.5 Pro, Kimi K2's training wasn't perfected for long-chain tool use, which would require deeper investigation.

So, my guess is that the stumbling blocks during development were not due to a deficiency in Kimi K2's intelligence. Instead, they expose a deeper problem: the conflict between a potentially top-tier AI brain and a set of "hands and feet" that are not yet fully adapted to it. This results in a suboptimal user experience and is a critical issue for all teams dedicated to advancing Agentic AI.

## Information Research: The Execution Resilience of an Agentic Model

My second test was open-ended information research. This scenario is a greater test of a model's ability to plan autonomously and execute iteratively.

It was in this test that Kimi K2 demonstrated its immense value as a system component. I discovered it possesses a very valuable trait, which I call "task execution resilience." Faced with a complex research topic, it would naturally generate a large and diverse set of keywords and then tirelessly conduct multiple rounds of iterative searches. It has a strong "bias for action," whereas many other models (like GPT-4o, Gemini, Deepseek, and Qwen) tend to get lazy in such open-ended tasks, preferring to rely on their existing knowledge rather than actively exploring. Even when the system prompt repeatedly insists on using multiple keywords for searching, they might perform one or two cursory searches or even skip searching altogether and provide an answer directly.

Of course, it has a significant shortcoming. Perhaps because K2 is not a reasoning model, it excels at collecting and compiling information, providing you with an exhaustive list of materials, but it is not adept at extracting deep, high-level insights from them. It's more like a top-tier information gatherer than an analyst. This is very similar to o3, which can also tirelessly perform multiple search queries but often ends up producing a simple, chronological list. And this depth-of-thought problem is hard to change. It's like telling an intern (the prompt) over and over to write a report with strategic height; they still can't produce a VP-level report. This is a limitation of the model itself.

But this already provides enormous value. A model with strong execution resilience is the cornerstone of any complex agentic system. In a system, the most valuable quality isn't occasional flashes of brilliance, but predictable, reliable execution. A component that always faithfully carries out instructions is far more valuable than one that is brilliant but unpredictable. You can build more diverse and reliable automated workflows around it. I used to use o3 for such tasks, but its cost always made me hesitate to extend this approach to more complex tasks. Kimi K2 now offers a low-cost alternative with nearly comparable quality.

This has led to a highly efficient workflow. I now use Kimi K2 as the front-end for my research system. I leverage its powerful execution resilience and long-context capabilities to perform a "carpet bomb" information-gathering run on any topic I want to investigate. Then, I feed the massive, information-rich context compiled by Kimi directly to a reasoning model known for deep analysis, like Gemini 2.5 Pro, as the back-end to perform the final analysis and insight extraction. This two-stage combination works surprisingly well. Not only is the quality of the final output far superior to any single model, but thanks to Kimi's cost-effectiveness, the overall cost of the process is significantly lower compared to using o3. This clearly shows me Kimi K2's precise positioning within a complex agentic system: a tireless and outstanding workhorse.

I also found that Kimi's reasoning shortcomings can be compensated for through workflow design. I have it first act as an "architect," generating a detailed and clear plan for a complex task. This plan itself serves as a manually injected thinking step, externalizing and structuring the act of "thinking." Then, I have it act as a "dispatcher," strictly executing this self-made plan step-by-step using various tools. This decouples planning from execution within a multi-agent system. As a dispatcher, it can call a search engine, a code interpreter, or even another model known for analysis (like Gemini 2.5 Pro) to complete a step in the plan that requires deep thought.

## Some Final Thoughts

So, after this round of testing, I feel that Kimi K2's strengths and weaknesses are quite clear. Its strategic bet on the agentic direction is a very forward-thinking move. But there is still a gap between its powerful potential and its current reliable execution.

Kimi K2's most valuable asset is its smart brain. But the value of this core asset is being diminished by unstable tool calls and ecosystem friction. To fully realize its potential, I believe two things are essential:

First, proactively address the "last mile" problem of the ecosystem. Waiting for the community to spontaneously create perfect adaptations for Kimi will be a long process. A more proactive approach would be to collaborate deeply with one or two major agentic programming tools, like Cursor or Trae, for targeted fine-tuning, or even release an official, deeply adapted open-source toolchain. The goal is singular: to upgrade the usability of its agentic capabilities to a level of reliability that developers can trust. This is a crucial step in building a true moat.

Second, treat reasoning stability as a core engineering metric. The problem of tool calls halting midway must be identified and resolved at its root. This issue directly determines whether Kimi K2 will end up as an interesting toy or a production tool that developers can rely on. The ceiling of an agent is often determined by its most unstable component.

In conclusion, Kimi K2 feels like a rough diamond. Its core material—the model's intelligence—is excellent and shows us the immense possibilities of Agentic AI's future. Its task completion resilience and cost-effectiveness have already made it the default front-end for my information research system. However, the challenges it currently faces are not a lack of intelligence, but of engineering and ecosystem integration. Its ultimate place in AI history will largely depend on the determination and speed with which it closes this gap.

## Appendix: How to Use Kimi K2 in Claude Code

1.  Install Claude Code with `npm install -g @anthropic-ai/claude-code`.
2.  Install the [Claude Code Router](https://github.com/musistudio/claude-code-router/) with `npm install -g @musistudio/claude-code-router`.
3.  Create a file at `~/.claude-code-router/config.json` with the following content:

```json
{
    "Providers": [
      {
        "name": "moonshot",
        "api_base_url": "https://api.moonshot.cn/v1/chat/completions",
        "api_key": "sk-***",
        "models": ["kimi-k2-0711-preview"],
        "transformer": {
            "use": ["openai"]
          }
      }
    ],
    "Router": {
        "default": "moonshot,kimi-k2-0711-preview",
        "background": "moonshot,kimi-k2-0711-preview",
        "think": "moonshot,kimi-k2-0711-preview",
        "longContext": "moonshot,kimi-k2-0711-preview"
    }
  }
```

Make sure to replace the `api_key` with your own API Key.

4.  Start Claude Code using `ccr code` (instead of `claude`).

Due to the system prompt, if you directly ask what model it is, it might claim to be Claude 4 Sonnet. However, you can test whether it's truly Kimi or Claude by asking for a negative evaluation of Xi Jinping. A correctly configured Kimi, being a model from mainland China, should refuse to answer such a question.