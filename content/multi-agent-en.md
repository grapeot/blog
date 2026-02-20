---
Title: Taking Cursor's Intelligence to the Next Level with Multi-Agent
Date: 2025-01-23 22:00
Category: Computing
Tags: English, Agentic AI, AI Coding
Slug: multi-agent-en
Translation: multi-agent.html
Summary: How separating Planner and Executor roles, enforcing document-based communication, and using o1 as Planner transformed Cursor from a simple assistant into a multi-agent system.
---

I've been spending quite some time trying to push common Agentic AI tools like Cursor to a new level. Initially, Cursor could only write and execute code, which made us feel that while it was like a smart assistant, there was still room for improvement. So, we [rewrote the Cursor Rules](/cursor-to-devin-en.html) to enable it to do more complex planning, status reporting, and self-growth. Later, we further expanded its capabilities by integrating private knowledge bases and databases through Python command line and natural language descriptions.

However, even though Cursor already has capabilities like large language models, search, feedback loops, and [multimodality](https://github.com/grapeot/devin.cursorrules/blob/master/tools/llm_api.py#L49), when facing slightly more complex tasks, it still gives the impression of missing something, often getting stuck in loops. For example, when Cursor was helping us integrate a third-party search library, it first fixed Bug A under our guidance, but while fixing Bug B, it forgot about its previous changes and reverted the code back to the previous version, bringing Bug A back. This back-and-forth continued. Although it eventually got fixed, it wasted quite a bit of time. For more complex projects, it might not even be able to complete them at all.

### Why Does It Get Stuck in Loops

If you're familiar with Context Window Management, you'll recognize this as a typical loss of control: when the same model has to handle both high-level planning and low-level execution, all information gets crammed into the same context. It first needs to filter out what's truly useful for planning from the messy information pile before making decisions. This puts an enormous cognitive burden on the model. The reverse is also true - if it focuses on execution first, it easily forgets what the Planner said earlier or loses focus among the many execution details. As a result, neither planning nor execution is done well, failing on both fronts.

This led us to make our first major change: separating the Planner from the Executor.

### First Decision: Separating Planner and Executor

Our inspiration actually came from management theory: if you make someone be both a manager and a coder, and hold them to the standards of both roles, they'll inevitably fail at both management and coding. The same applies to Context Windows. So I kept a separate context for the high-level Planner, letting the Executor focus on low-level implementation while the Planner maintains control of the big picture. This way, they don't interfere with each other. This simple layering immediately reduced the error rate significantly, without even needing to switch to a more powerful model. The Executor could focus on writing code and debugging, while the Planner, like a leader, would periodically review and direct the Executor to perform specific bug fixes and version changes.

But then an unexpected problem emerged.

### Second Decision: Enforcing Document-Based Communication for Agents

The problem was that while the Planner and Executor were separated, they still communicated through conversations. This meant that as soon as the context window got too long or was truncated, the Planner's instructions would be completely lost. For example, if the Planner said "remember to run a version compatibility test," but after several rounds of debugging, Cursor truncated the context window and this instruction was lost. Since it wasn't in the Executor's context window anymore, the Executor would completely forget about it the next time it executed.

It's like in a company where both management and execution teams are too busy working to write documentation. As a result, the execution team can't track progress without the boss's reminders, and the boss can't remember technical details, asking the same questions repeatedly. (Why does this sound so familiar?)

So we realized that even with context window isolation, we hadn't truly solved the memory loss problem. We came up with a particularly basic solution: providing a shared Scratchpad document for the Planner and Executor. Any thought analysis, test results, encountered bugs, and final discussion conclusions would be written into this file.

This meant:

* The Planner could check current challenges and progress in the document at any time, and leave new task instructions;
* When the Executor completed a feature or hit a snag, it would update the results and feedback in the document for the Planner to read and remember.

By turning the conversation pipeline into a persistent notebook, we basically solved the LLM context loss problem. Even if the conversation refreshed temporarily, we just needed to reference the document. The probability of memory loss and stepping into the same pitfalls immediately decreased significantly.

### Third Decision: Bringing in o1 as the Planner

After we separated the Planner and Executor and established the public document, a new problem emerged: when using a regular model as the Planner, it often lacked depth and could only give superficial advice to the Executor. For example, with a data processing pipeline, an experienced senior engineer would first validate on a small-scale dataset before deploying to large-scale data, saving lots of debugging time.

But if we used a simpler Planner, it would often try to debug directly on the final large-scale data. This would often waste a lot of time. More annoyingly, Cursor has a timeout for task execution, so if we're testing with actual production data, it might timeout before completion. This would prevent it from iterating automatically.

This problem wasn't hard to solve - we simply replaced the Planner with a more intelligent model that's better at reasoning, like o1. But after the switch, we discovered another amusing problem. o1 loves to over-engineer. Sometimes it gets extremely passionate about analysis and refinement, thinking about how to cover every edge case, or turning a small program into a Concurrent Large-Scale Platform, making the process extremely bloated.

Sometimes I even felt like I had hired a professional manager who spent all day thinking not about completing a task for me, but about building some fancy platform. I kept feeling like the next thing they'd tell me is that we need to hire more Claudes... It's like in human teams when you bring in a famous consulting firm. These consultants, to show their expertise, often provide extremely sophisticated and massive but bloated solutions. People work hard but it doesn't actually help the final business goal or necessarily improve efficiency.

So we made Decision 3.5: using prompting to make the Planner moderately restrained, coupled with clear acceptance criteria. Our final approach was to still use o1 as the Planner, but through prompting, give it a Founder Mindset - don't always think about making it perfect in one go or building the industry's most impressive platform, but rather Bias for Action, seizing opportunities as they come. Start with a simple prototype, and after validating feasibility, gradually add more features.

Especially when the Planner assigns tasks to the Executor, it needs to clearly specify the necessity and verification method for each step breakdown. At the same time, the Executor can raise questions in the document's feedback section, and if they feel the solution is too complex, they can challenge the Planner to re-examine whether it's really necessary or needs further decomposition. We use this kind of interaction and acceptance mechanism to control the Planner's reasoning.

### Practical Example

For example, the DuckDuckGo search in my [Cursor rules](https://github.com/grapeot/devin.cursorrules) had been having some issues - it was unstable but without clear patterns about when it would fail. After introducing the Multi-Agent system, o1 as the planner first designed a series of experiments for Claude to run. Claude wrote the code based on this and gave the experimental results back to o1. o1 then analyzed these, instructing it to search for specific keywords and look at issues on the DuckDuckGo Python library's GitHub.

After several iterations, we discovered there was a bug in version 6.4 of the DuckDuckGo python library that was fixed in the latest 7.2 version. The o1 planner then instructed Claude executor to upgrade the version, and then designed ten different test cases for Claude to test one by one. Finally, it directed Claude to write documentation summarizing our learnings, what measures we used to cross-check and ensure our implementation was correct, and why this achieved the user's goals.

This entire Multi-Agent development experience made me feel that the quality of task completion went up another level. Previously, it was just like having an assistant who completed tasks and handed them to you. Now it feels like there's a more experienced supervisor who will do their own cross-checking before reporting back to you. It feels like we've evolved from being a manager to a senior manager.

### The Root Cause of Three Changes: Context Window

Looking back, we weren't doing Multi-Agent just for the sake of it, but rather through a process of continuously hitting pitfalls, reflecting, and iterating step by step.

* Because we encountered the problem of contexts interfering with each other, this forced us to split roles.
* Because we encountered memory loss issues, this forced us to use documentation as the main communication channel between Planner and Executor.
* Because regular models had limitations in thinking depth and planning ability, this forced us to switch to a more intelligent Planner.
* Because the more intelligent Planner had a tendency to over-engineer, this forced us to control its complexity through prompting and other methods.

From basic Cursor Agent Mode all the way to Multi-Agent, we've figured out three practical experiences and seen that multi-agent systems can indeed take AI collaboration to a new level. It not only fixes bugs more thoroughly but can also perform more complex abstract thinking, achieving more results in the same development cycle.

On the surface, this system might just look like adding o1 on top of the original Claude in Cursor, but actually, the internal thinking is much more profound than this appearance. When we analyze and improve any LLM system, we must understand what's actually in its context window. We need to ensure its context window has enough information to support task completion on one hand, while being sufficiently clean and clear on the other. Once you grasp this point, our three changes emerge naturally.

I hope our thoughts, experiences, and especially lessons can provide some inspiration when you're building your own multi-agent applications. Perhaps next time when you encounter context loss, memory loss, or conversation loss, you'll think to reverse-engineer from the context window perspective what input the LLM is receiving. Consider whether it's necessary to separate their context windows and prepare an appropriate communication channel for them.

The implementation of this Multi-Agent system has also been [open-sourced](https://github.com/grapeot/devin.cursorrules/tree/multi-agent), and we welcome everyone to use and contribute to it.