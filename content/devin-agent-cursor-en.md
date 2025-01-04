Title: [Agentic AI] Comparison between Devin and Agent Cursor
Date: 2024-12-12 08:00
Category: Computing
Tags: English, AI, Programming, Cursor, Agentic AI
Slug: devin-vs-agent-cursor-en
Summary: I recently subscribed to Devin, an AI programming tool, for $500 per month. It claims to be a versatile intern capable of performing many tasks that traditional AI tools like Cursor and Windsurf cannot handle. After using it for a while, I noticed significant differences between Devin and Cursor in terms of design philosophy and user experience, which I'll summarize in this article.

---

This article is part of the "Understanding and Deploying Agentic AI" series:

* Agentic AI Series 1: Comparison between Devin and Agent Cursor (This Article)
* [Agentic AI Series 2: From Thinker to Doer — The Paradigm Revolution and Technical Architecture of Agentic AI](/agentic-ai-en.html)
* [Agentic AI Series 3: Turning &#36;20 into &#36;500 - Transforming Cursor into Devin in One Hour](/cursor-to-devin-en.html)
* [Agentic AI Series 4: Using Cursor as a Universal Entry Point for AI](/cursor-ai-entry-en.html)

---

I recently subscribed to Devin, an AI programming tool, for $500 per month.
It claims to be a versatile intern capable of performing many tasks that traditional AI tools like Cursor and Windsurf cannot handle.
After using it for a while, I noticed significant differences between Devin and Cursor in terms of design philosophy and user experience, which I'll summarize in this article.

It's important to note that when I mention Cursor, I'm not referring to traditional auto-completion tools like Copilot or natural language programming tools like Copilot Chat. Instead, I'm specifically discussing Cursor's recently released Agent mode. In Cursor Composer, you can now switch from Normal mode to Agent mode, where you can submit requirements, and Cursor will iteratively complete tasks by calling various tools.
The experience is very similar to Windsurf, so the Agent Cursor discussed here represents an advanced product form that completes tasks through multiple rounds by calling various tools on your computer in an agent-like manner.

Overall, my most striking observation is that Devin's design philosophy and objectives differ significantly from Agent Cursor. Interacting with Cursor feels more like working with a tool, while Devin feels more like working with a person. The following three aspects revolve around this distinction.

## Local Execution vs. Global Planning: From Task Completion to Process Planning

While using Cursor, I distinctly feel that it's like a technician who strictly executes specific tasks.
Give it a clear instruction, and it will quickly execute and output results.
Devin, however, is more like a more methodical complex system or intern.
It has a more complete workflow mindset, first developing a high-level plan, then breaking down steps for execution and validating results.

Although both Devin and Cursor feature multiple iterations, Cursor's iterations are merely for testing to verify goal completion.
Devin, on the other hand, is more like a seasoned professional. It first lists a high-level plan, then checks off items one by one, constantly adjusting strategies during this process, keeping you informed of its progress, and making you confident that the entire project is under control.

This is an interesting distinction that indeed enables Devin to complete more complex and variable tasks and provide more systematic solutions.
For example, when we tried to have both AIs clone a website, Devin was notably stronger in higher-level abstract thinking and planning. It knew to first call various tools to download the website locally, then observe the function and style of each webpage and module, then plan the webpage structure, and finally begin execution.

Cursor, however, clearly wasn't designed for projects of this complexity. Its first iteration didn't think to download the website locally first, instead directly hallucinating a webpage.
Then, even after being explicitly reminded to crawl the website content first, it missed many important details and created only a greatly simplified version.
So overall, their design purposes feel very different. Devin was designed more like a methodical software engineer with plans and procedures, while Cursor is more of a tool to help us quickly and automatically solve some clear, relatively small problems.

## Tool Usage Flexibility

Their second difference lies in tool usage flexibility.
Cursor's main agent capabilities are limited to the file system, code generation, and command execution.
However, Devin can utilize more tools, such as launching browsers, using visual capabilities to understand frontend content, and even performing automated frontend interaction tests.

It can also call its own LLM (corresponding to an intern's brain?) to complete some relatively independent and more flexible tasks.
For example, my blog had some links that needed fixing.
These link errors didn't follow any obvious pattern, so Cursor struggled with this type of problem.
It couldn't summarize patterns from these broken links to write a program for batch processing.
In other words, this problem wasn't suitable for programming solutions but required higher-level intelligence.

Devin solved this problem well. Throughout the process, it didn't use any programming but instead opened files one by one, used its LLM to understand them, found the problems, and fixed them (PR is [here](https://github.com/grapeot/blog/pull/31)).
This difference both supports the procedural differences we mentioned in the previous point and demonstrates how Devin's more diverse capabilities allow it to complete more complex tasks through combination.

However, this tool usage flexibility is a double-edged sword. For instance, in another example, I asked both Devin and Cursor to go to the CVPR website and download the authors, titles, and PDF links for this year's 2000 papers. Cursor performed consistently well with this clear programming task. It quickly wrote a crawler, parsed the CVPR website content, and generated the final result file.

But Devin chose an unexpected manual route. It first opened the browser, and after using its image capability to read the browser and the first page, it gave me a result file with only three papers.
When questioned "This only has three papers, where are the others?", it surprisingly chose to open the browser again, outputting three papers at a time, page by page. This process was both amusing and frustrating.

In some ways, it indeed resembles working with a diligent but inexperienced intern. However, from a tools and task completion perspective, Cursor's stability and task completion capability are more important here.

## Dynamic Growth of Prompts and Knowledge

Another related difference is their management and iteration of knowledge.

In using Devin, it strongly emphasizes knowledge and experience summary and accumulation.
For example, in the CVPR crawling example above, I gave feedback: "You need to first check how many articles there are, and if there are many articles, you need to choose to use a program for batch processing." After I gave this feedback, it automatically generated a knowledge entry stating that next time when doing web crawling, it needs to handle situations differently based on the data scale. Then when I asked it to do the CVPR task again, it didn't fall into the same trap.

![Devin accessing knowledge](/images/devin-access-knowledge.jpg)

This design of dynamic iteration and evolution makes the whole process feel especially like mentoring an intern.
Including when I had Devin onboard a new Github repo, I guided it through initializing the repo, installing various dependencies, and taught it how to run various tests and what indicates which components are working properly.
After one round of guidance, it transformed all this information into knowledge, and later it could handle my blog repo very proficiently.

This dynamic evolution design hasn't been seen in Cursor yet, but I'm optimistic as it should be easy for Cursor to implement. Currently, Cursor can already use files like `.cursorrule` to customize project-specific knowledge, so the mechanism is already there - it just needs to connect to a knowledge organization prompt.

As an aside, regarding prompts, Devin has [a document](https://docs.devin.ai/learn-about-devin/prompting) that I find particularly helpful. It teaches you what kinds of prompts are most effective when communicating with Devin. For example, you need to clearly define success criteria, such as passing certain tests or verifying that certain links match. This aligns with our viewpoints in the [builder's mindset course](https://maven.com/kedaibiao/genai), and when you apply the same principles to using Cursor, you'll find that Cursor also becomes much smarter, capable of self-verifying task completion and iterating.

## Control and Scenarios

Because of these three differences in design and product aspects, I get a very clear impression: Devin was designed to be like a person - methodical and capable of growth, though with higher unpredictability.
Sometimes it might stare at an MD file for ten minutes, making me wonder if it's secretly playing with its phone in the background.

![Devin thinking](/images/devin-10min.jpg)

But it's also better at handling more complex projects. In comparison, Cursor is a more intuitive programming tool. You can anticipate what pitfalls it might encounter and prevent them beforehand, but this is more difficult with Devin. Sometimes even after it falls into a pit, it's hard to understand why it made that mistake even in retrospect.

For practical use, I currently lean towards Cursor because these two tools actually target very different scenarios.
Devin emphasizes complex software engineering development. For instance, it costs $500 per month, and it runs slowly - taking half an hour to several hours for a small project is normal.
But if the project can be completed with Cursor, it might finish in five minutes.
So Cursor is more suitable for lighter, more life-oriented small tasks.
And I believe many of Devin's designs and experiences, including Prompt Engineering techniques and iteration approaches, can be easily implemented by Cursor.

So perhaps Cursor's competitor isn't really Devin, but ChatGPT.
In other words, if what you want isn't actually code but an artifact - like an icon, a document, or even a Photoshop image - you can use Cursor.
Only when the final deliverable is a complex software engineering project is Devin a more suitable tool.

I'll continue exploring if there are more interesting ways to use Devin to make our daily work and life more convenient.
