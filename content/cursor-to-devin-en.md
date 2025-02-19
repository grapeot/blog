Title: [Agentic AI] Turning $20 into $500 - Transforming Cursor into Devin in One Hour
Date: 2024-12-17 10:00
Category: Computing
Tags: AI, Agentic AI, English, Cursor
Slug: cursor-to-devin-en
Summary: In the [previous article](/devin-vs-agent-cursor-en.html), we discussed Devin, an Agentic AI capable of fully automated programming. Compared to other Agentic AI tools like Cursor and Windsurf, it has several core advantages, particularly in process planning, self-evolution, expanded tool usage, and fully automated operation. This makes Devin appear to be a next-generation tool, setting itself apart from existing Agentic AI tools.

---

This article is part of the "Understanding and Deploying Agentic AI" series:

* [Agentic AI Series 1: Comparison between Devin and Agent Cursor](/devin-vs-agent-cursor-en.html)
* [Agentic AI Series 2: From Thinker to Doer — The Paradigm Revolution and Technical Architecture of Agentic AI](/agentic-ai-en.html)
* Agentic AI Series 3: Turning &#36;20 into &#36;500 - Transforming Cursor into Devin in One Hour (This Article)
* [Agentic AI Series 4: Using Cursor as a Universal Entry Point for AI](/cursor-ai-entry-en.html)

---

In the [previous article](/devin-vs-agent-cursor-en.html), we discussed Devin, an Agentic AI capable of fully automated programming. Compared to other Agentic AI tools like Cursor and Windsurf, it has several core advantages, particularly in process planning, self-evolution, expanded tool usage, and fully automated operation. This makes Devin appear to be a next-generation tool, setting itself apart from existing Agentic AI tools.

However, after using it for a while, my Builder's Mindset started stirring again, driving me to modify Windsurf and Cursor to achieve 90% of Devin's functionality. I've also open-sourced these modifications, allowing you to transform Cursor or Windsurf into Devin in just one minute. This article mainly introduces the specific approach to these modifications, using this example to demonstrate how efficient both building and expanding can be in the Agentic AI era. For simplicity in our discussion, we'll use Cursor to refer to this type of tool, and at the end, we'll discuss what minor adjustments would be needed if you want to use Windsurf instead.

| Tool                | Process Planning     | Self-Evolution    | Tool Extension   | Automated Execution | Price      |
|--------------------|---------------------|------------------|-----------------|-------------------|------------|
| Devin              | Yes (Auto, Complete) | Yes (Self-learning) | Many           | Supported         | $500/month |
| Cursor (Pre-mod)   | Limited             | No               | Limited toolset | Manual confirmation| $20/month  |
| Cursor (Post-mod)  | Near Devin          | Yes              | Near Devin, expandable | Still needs confirmation or workaround | $20/month |
| Windsurf (Post-mod)| Near Devin          | Yes, but indirect | Near Devin, expandable | Supports full auto in Docker container | $15/month |

## Process Planning and Self-Evolution

As mentioned in the previous article, an interesting aspect of Devin is that it behaves more like a methodical intern. It knows to create a plan first, then continuously updates the plan's progress during execution. This makes it easier for us as AI Managers to track the AI's current progress, while also preventing it from deviating from the original plan, achieving greater depth of thought and task completion quality.

While this functionality seems impressive, it's actually quite easy to implement with Cursor.

For Cursor, there's a special file called `.cursorrules` located in the root directory of the opened folder. What makes it special is that it allows you to modify Cursor's prompt to the backend LLM. In other words, all content in this file becomes part of the prompt sent to the backend AI, such as GPT or Claude. This provides us with great flexibility for customization.

For instance, we can put the content of the plan in this file, so every time we interact with Cursor, it receives the latest version of the plan. We can also give it more detailed instructions in this file, such as having it think through and create a plan at the start of a task, and update the plan after completing each step. Since Cursor can use agents to modify files, and `.cursorrules` itself is a file, this creates a closed loop. It automatically reads the file's content each time, understands the latest updates, and after thinking, writes the updated progress and next steps to this file, ensuring we always have the most recent updates.

The self-evolution functionality can be implemented using a similar approach. In the `.cursorrules` file, we add prompts that make Cursor reflect on its mistakes when corrected by users and consider if there are any reusable lessons to record. If there are, it updates the relevant section of the `.cursorrules` file. This way, it can accumulate project-specific knowledge.

A typical example is that current LLMs, due to their relatively early knowledge cutoff date, many don't know about the GPT-4o model. If you ask them to call GPT-4o, they'll remove the 'o', thinking it's a typo. But if you correct them: "This model actually exists, you just don't know about it," they'll record this lesson in the relevant section of `.cursorrules`, and won't make the same mistake again, thus achieving learning and improvement. However, this still depends on whether the prompt is effective - sometimes it might miss points, and won't necessarily record knowledge we think should be noted. In such cases, we can also nudge it using natural language, directly telling it to make a note of this. This more direct approach can also achieve experience accumulation and growth of the AI.

Therefore, just by using the `.cursorrules` file along with some prompting techniques, we can add Devin's impressive process planning and self-evolution capabilities to existing Agentic AI programming tools.

If using Windsurf, there's one difference: possibly for security reasons, it doesn't allow AI to directly modify the `.windsurfrules` file. Therefore, we need to split it into two parts, using another file like `scratchpad.md`. In the `.windsurfrules` file, we mention: before each thinking process, you should check the Scratchpad and update the plan there. This indirect method might not be as effective as putting it directly in `.cursorrules`, as it still requires the AI to call an agent and think based on the feedback results, but it works in practice.

## Extended Tool Usage

Compared to Cursor, one of Devin's major advantages is its ability to use more tools. For example, it can call a browser to search, browse web pages, and even use its own brain to analyze content using LLM intelligence. While these aren't supported in Cursor by default, the good news is that because we can control Cursor's prompt directly through `.cursorrules`, and it has command execution capabilities, this creates another closed loop. We can prepare pre-written programs, such as Python libraries or command-line tools, then introduce their usage in `.cursorrules`, allowing it to learn on the fly and naturally understand how to use these tools to complete its tasks.

In fact, these tools themselves can be written using Cursor in just a minute or two. For example, for web browsing functionality, I made a reference implementation in the [open-source project](https://github.com/grapeot/devin.cursorrules). There are some technical decisions to note, such as using browser automation tools like playwright instead of Python's request library to handle JavaScript-heavy websites. Additionally, to better communicate with the LLM and facilitate its understanding and crawling of subsequent content, we don't simply use beautiful soup to extract the webpage's text content. Instead, we convert it to markdown format following certain rules, thus preserving more detailed base information like class names and hyperlinks, supporting LLM in writing subsequent crawlers at a more fundamental level.

Similarly, for search tools, there's a small caveat: whether it's Bing or Google, their API search quality is far inferior to their client-side search, mainly due to historical reasons where different teams handle API and web interfaces. However, DuckDuckGo doesn't have this issue, so our reference implementation uses DuckDuckGo's free API.

Regarding Cursor using its own brain power for deep analysis, this is relatively more complex. On one hand, Cursor does have some degree of this capability - in the above two tools, when we print webpage content to stdout, it becomes part of Cursor's prompt to the LLM, allowing it to make intelligent analysis of this text content. But from another perspective, Devin has a unique ability to use LLM for batch processing of relatively large amounts of text, which Cursor can't do. So to give it this capability, we implemented an additional tool - very simple, just setting up our API key in the system beforehand, then letting this tool call GPT or Claude or our local LLM API, thus giving Cursor the ability to batch process text using LLM. In my reference implementation, I use my own local vllm cluster, but it's very simple to modify - just remove the base_url line.

However, even after these modifications, there are still two tools that we can't implement due to Cursor's limitations:

1. Devin appears to have image understanding capabilities, which is why it can perform frontend interaction and testing, but due to Cursor's limitations, we can't pass an image as input to the backend AI - this would require changes to its implementation.
2. Devin mysteriously doesn't get flagged as a bot by anti-crawling algorithms during data collection, but our web retrieval tool often encounters CAPTCHAs or gets blocked. This might be solvable, and I'm still exploring, but it's definitely one of Devin's unique advantages.

## Fully Automated Execution

The final interesting feature is fully automated execution. Since Devin operates in a completely virtualized cloud environment, we can safely let it execute various commands without worrying about LLM attacks or it running dangerous commands by mistake. Even if you delete the entire system, just start a new container and you're good to go. However, Cursor, running on the local host system, has strong security concerns. This is why in Cursor's agent mode, we need to manually confirm before executing each command. This is acceptable for relatively simple tasks, but now that we have complex process planning and self-evolution capabilities, Cursor can also handle long-term complex tasks, making this interaction method seem unsuitable for Cursor's capabilities.

To solve this problem, I haven't found a Cursor-based solution yet (Update: on 12/17/2024 Cursor also added this feature, called Yolo Mode, but it still doesn't support development in Docker), but Windsurf has considered this, and I think from its design, you can see that it was aiming for a Devin-like product form from the start, with the current code editor being just an intermediate form. More specifically, Windsurf has a feature that connects directly to a Docker container and runs there, or if we have a configuration file, it can help you start a new Docker container, do some initialization, and map a local folder over. Therefore, all commands it executes, except for changes to the local folder, are performed in the Docker container, having no impact on the host system, thus greatly improving security. [[Example Configuration]](https://github.com/grapeot/devin.cursorrules/blob/master/.devcontainer/devcontainer.json) [[Documentation]](https://docs.codeium.com/windsurf/advanced#dev-containers-beta)

On this foundation, it also introduced a blacklist/whitelist mechanism, automatically rejecting commands on the blacklist and allowing those on the whitelist. For commands on neither list, LLM intelligently judges whether there's risk to the host system - for example, if it wants to delete a file in the folder, it will ask for user confirmation, but general commands like `pip install` are allowed directly. Note that this feature seems to only be enabled when running in a Docker container. If we're running commands on the host system, the experience is still similar to Cursor, requiring frequent confirmations. Additionally, automated command execution needs to be enabled in the configuration. [[Documentation]](https://docs.codeium.com/windsurf/cascade#terminal-commands)

## Summary

Therefore, we can see that while Devin's product form and design philosophy are indeed very advanced, from a technical barrier perspective, the gap between it and existing Agentic AI tools isn't as wide as we might imagine. Using popular tools that cost $15-20 per month, like Cursor and Windsurf, we can implement 90% of Devin's functionality in an hour and use it to complete complex tasks that weren't possible before modification. For example, I assigned Cursor a task to analyze the returns of popular tech stocks over the past 5 years, conducting an in-depth data analysis, and it provided a very [detailed and comprehensive report](https://yage.ai/cursor_stock/). Additionally, I had Windsurf crawl the posting times of my blog's top 100 articles and visualize them in a GitHub contribution graph style, which it could complete fully automatically. These types of tasks couldn't be done with traditional Cursor and Windsurf - only Devin could do them, but after making these simple modifications, we can achieve the effect of a $500/month tool with a $20/month tool. I even did a deeper experiment: as a dev completely unfamiliar with frontend development, I spent an hour and a half creating a [recruitment website](https://github.com/grapeot/WeiLaiKeJi/) complete with frontend and backend. This efficiency is quite close to or even higher than Devin's.

Finally, all files mentioned in this article can be downloaded from [this GitHub repo](https://github.com/grapeot/devin.cursorrules) - just copy the contents to your current project folder and you're ready to go.