Title: [Agentic AI] From Thinker to Doer — The Paradigm Revolution and Technical Architecture of Agentic AI
Date: 2024-12-13 14:00
Category: Computing
Tags: AI, Agentic AI, English, Cursor
Slug: agentic-ai-en
Summary: Before discussing Agentic AI, I'd like to share two short stories. While chatting with someone online, I wanted to compare Amazon and Google's stock performance over the last five years to support a point I was making. I first searched online for existing comparisons and tools but found nothing. Then I asked ChatGPT if it could help me find or generate a stock price comparison chart. It said it couldn't. By this point, I was ready to give up, as it wasn't worth spending 5 minutes making a chart during a casual conversation. As a last resort, I tried Cursor's latest Agent mode, simply throwing my request at it: generate a chart showing Google and Amazon's stock prices over the last five years, with both stocks aligned at their starting points for easy comparison. To my surprise, Cursor automatically started writing code, installing dependencies, debugging, modifying the program, re-executing, and within a minute gave me exactly the chart I wanted, as shown below. I was truly amazed. It just works.

---

This article is part of the "Understanding and Deploying Agentic AI" series:

* [Agentic AI Series 1: Comparison between Devin and Agent Cursor](/devin-vs-agent-cursor-en.html)
* Agentic AI Series 2: From Thinker to Doer — The Paradigm Revolution and Technical Architecture of Agentic AI (This Article)
* [Agentic AI Series 3: Turning &#36;20 into &#36;500 - Transforming Cursor into Devin in One Hour](/cursor-to-devin-en.html)
* [Agentic AI Series 4: Using Cursor as a Universal Entry Point for AI](/cursor-ai-entry-en.html)

---

## From "Ask and Answer" to "Ask and Do"

Before discussing Agentic AI, I'd like to share two short stories.

While chatting with someone online, I wanted to compare Amazon and Google's stock performance over the last five years to support a point I was making. I first searched online for existing comparisons and tools but found nothing. Then I asked ChatGPT if it could help me find or generate a stock price comparison chart. It said it couldn't. By this point, I was ready to give up, as it wasn't worth spending 5 minutes making a chart during a casual conversation. As a last resort, I tried Cursor's latest Agent mode, simply throwing my request at it: `generate a chart showing Google and Amazon's stock prices over the last five years, with both stocks aligned at their starting points for easy comparison`. To my surprise, Cursor automatically started writing code, installing dependencies, debugging, modifying the program, re-executing, and within a minute gave me exactly the chart I wanted, as shown below. I was truly amazed. It just works.

![Stock price comparison](/images/agent_ai_stock_comparison.png)

The second example: while working on a webpage, I needed to make my profile picture circular – in graphic design terms, adding a circular mask. Drawing from my previous experience, I didn't open Photoshop or ask ChatGPT how to operate Photoshop. Instead, I directly threw the image at Cursor and described in its agent mode what shape I wanted the image to be PS'ed into. Cursor churned out some command line instructions I didn't understand, installed dependencies, and produced an image. The circle size was wrong, so I gave it that feedback, and it figured out the correct image dimensions using command line tools and gave me a perfect image.

These two examples had a profound impact on me because they represent a fundamental shift in how we use AI. If we look at ancient AI products – like ChatGPT and Claude from a year ago – their usage pattern was "ask and answer" – we would consult them about things we didn't know. This is why many articles from that time compared ChatGPT to Google. But by late 2023, at least for developers, our way of using AI largely became Copilot-style, or "ask and write." We expected AI not just to tell us things, but to help us write code that we would then run to execute other tasks.

However, in the examples above, what I expected from AI wasn't code anymore, but rather an actual task or artifact. It could be [a document](https://yage.ai/cursor_stock/), a Photoshop image, or a data visualization chart. In other words, the AI usage pattern became "ask and do." This change is fundamental. Because whether it's ask and answer or ask and write, AI was only completing an intermediate step of the task. After gathering information, I had to make my own judgments. After collecting code, I had to debug it myself, organize it, make it run correctly, and then organize the results before I could use them or deliver the work I was responsible for.

But "ask and do" bridges all these intermediate steps, allowing AI to complete the entire task end-to-end, truly delivering what we ultimately want. For instance, when I wanted that chart, I didn't need to help AI break down where to find data or how to create the visualization. I could directly expect AI to give me the chart, and I could just paste it into the chat. Similarly, when I wanted to Photoshop an image, I didn't need to learn from AI how to use Photoshop. I could directly expect it to give me the final result, which I could then upload. This is a fundamental change that allows us to truly focus our energy on areas full of uncertainty, greater difficulty, and requiring our thinking and creative abilities, rather than spending vast amounts of energy on execution and decomposition work. This change will further push the ceiling of what we can accomplish, enabling us to do things we couldn't do before.

## Core Characteristics of Agentic AI: Tool Usage and Multi-Turn Decision Making

The evolution from "ask and answer" to "ask and write" to "ask and do" is driven by Agentic AI. Before diving into more details about Agentic AI, I want to explain my understanding of what Agentic AI is. This term is quite confusing even within AI circles on the internet. The generally accepted definition is that an AI capable of completing specific tasks can be called an Agent. But this definition is actually very broad and ambiguous.

For example, if I create a GPT and teach it how to do fortune telling through prompting, it meets the definition of completing a specific task, but it can hardly support the scenarios we mentioned above. Similarly, if we connect AI to a company's internal knowledge base for RAG to create an intelligent customer service bot, it's different from public GPT because it has internal company knowledge. Therefore, it can complete a unique specific task and could be considered an Agent. But likewise, it can't support the "ask and do" scenarios we discussed above. I could give many more examples, like fine-tuned models or models with specific output formats. But none of them touch on what I consider the two most core points: tool usage and multi-turn decision-making capability.

Tool usage is relatively straightforward to understand. For instance, one of AI's longstanding challenges is its inability to perform precise mathematical calculations. But if we give it a calculator tool, instead of using its token generation ability for calculations, it can use the calculator, perfectly complementing its mathematical computation shortcomings. Similarly, tools for internet searches or querying internal company databases can greatly improve AI's capability gaps, allowing it to achieve things it couldn't do before and might not be able to do for a long time – like knowing this morning's news – after all, we're unlikely to reduce the training time of an LLM from several months to several hours. Therefore, only when an AI has the ability to use tools, can it better adapt to diverse task requirements and have real-world impact beyond just generating text.

So what does multi-turn decision making mean? Our traditional AI reasoning process is turn-based. For example, you ask it a question, it gives you an answer, and then it waits for your next instruction. Even AI with tool-calling capabilities, like Open WebUI, works in a similar mode. Colloquially, it's like "kick once, move once." But if you've used Agentic Cursor or Devin, you'll find their working mode is autonomously multi-step, shifting from turn-based to real-time strategy. For example, it will first execute a command, and if the command succeeds, it stops and waits for your next instruction. But if the command fails, it will modify and debug based on the error message until the command succeeds. Therefore, from a turn perspective, its single turn can contain multiple instructions, and the number of instructions is not fixed but dynamically determined based on the results of tool calls. This multi-turn decision-making ability is another important factor that makes Agentic AI useful.

## Basic Technical Architecture of Agentic AI

Given how useful Agentic AI is, if we want to create a tool similar to Agentic Cursor to adapt to our own workflow, how should we do it?

First, this is still a very new and rapidly developing field, so unfortunately there isn't a mature framework or library that guarantees you can create something good just by following it. However, I think their basic patterns are still traceable. To build an Agentic AI system, there are four key aspects:

1. **LLM with Tool-Calling Capabilities: From Language Output to Real-world Impact**

    The LLM itself needs to have the ability to call tools. Modern LLMs, whether closed-source like GPT and Claude 3.5 or open-source like Llama 3.2, all have quite good tool-calling capabilities. Considering that training a large language model from scratch is beyond the capability of most companies, we'll simply skip over this part.

2. **Clear Success Criteria: Setting Task Endpoints and Verification Standards for AI**

    This Agent system needs clear success criteria or termination instructions. For example, when we assign AI a task: "I have a file with 5,000 data rows, help me convert the format." When you tell AI that the success criteria is that the output file must also have 5,000 rows and no nulls, versus not telling it these standards, the quality of task completion can be vastly different. This isn't actually an AI-specific challenge; we often face similar issues when assigning tasks to other humans. When we set clear completion standards for tasks, humans or AI can self-check and iterate. The completion level and probability of meeting our expectations will be much higher. When we haven't clearly communicated these standards, even if AI or humans have multi-turn decision-making capabilities, it will degenerate into a "kick once, move once" situation, where they just do something basic and wait for your review. For example, at most ensuring their program can run or has no syntax errors, but wasting much of their potential that they could actually achieve. Meanwhile, in the process of thinking about how to communicate task completion standards to AI, this also forces us to consider a question: does AI have appropriate tools to verify if its task has been completed? If not, we might need to first have AI create such a tool.

3. **Tool Description and Standardization: Establishing Clear Capability Interfaces for Agents**

    We need a mechanism to clearly describe to AI what tools it has, what each tool does, what their inputs and outputs are, and how AI can call them. This area doesn't yet have a mature industry standard, though some companies are trying to promote open standards where if you describe your tools using their protocol, for example Anthropic's Model Context Protocol (MCP). Any AI supporting that protocol can call your tools. When everyone uses the same standard, mutual cooperation and integration becomes much simpler. Of course, we're still in the early stages of Agentic AI development, so even if we don't support this Anthropic-advocated protocol, we have many other standards, like Open Web UI's protocol, or we can even define our own private protocol.

4. **Orchestrator: Control Center for Multi-turn Execution and Parallel Strategies**

    Although when discussing Agentic AI, most online articles focus on describing the Agent Orchestrator component, it might be the part with the lowest uncertainty. This Orchestrator maintains a multi-turn decision-making workflow, calling the LLM based on our assigned tasks to decide what tools to use, and based on the LLM's response, actually calling these tools and returning results to the LLM, then proceeding with the next step of reasoning. It might also implement features like parallelization to speed up the entire reasoning process. The industry has some tools in this area, like Microsoft's [AutoGen](https://github.com/microsoft/autogen), but currently there isn't a very mature unified library or framework.

## Conclusion

As AI silently shifts from "ask and answer" to "ask and do," each of us needs to reposition our roles and mindsets. In this entirely new mode of human-machine collaboration, what is our core value? How should we and our companies prepare for the future? When AI is no longer just talking but can actually do work, we finally can, and must, invest more energy in creative thinking, strategic planning, and exploration of unknown territories. After all, mechanical repetition and implementation details will be easily taken over by AI, while true value will come from understanding the essence of problems.

Perhaps you can start incorporating such Agentic tools in your next project. Even if you start with just a small task, using Cursor as a data visualization assistant, automatic format converter, or rapid prototype designer. In this building process, you'll gradually find your role shifting from an executor to a guide and planner, from a executor troubled by details to a boss skilled at leveraging AI capabilities. And this is the charm of the Builder's Mindset.

This future doesn't just belong to cutting-edge tech companies or any particular industry, but to all those willing to invest themselves in it, continuously thinking and building.