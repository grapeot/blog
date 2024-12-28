Title: [Agentic AI] Using Cursor as a Universal Entry Point for AI
Date: 2024-12-19 15:00
Category: Computing
Tags: AI, Cursor, English, Agentic
Slug: cursor-ai-entry-en
Summary: After completing [the previous article](/cursor-to-devin-en.html) introducing the modifications to Cursor, using Agentic AI in a "I say, you do" mode has become my primary method for leveraging AI. This further inspired me: is it possible to use Cursor or a similar editor as a universal entry point for AI? 

---

This article is part of the "Understanding and Deploying Agentic AI" series:

* [Agentic AI Series 1: Comparison between Devin and Agent Cursor](/devin-vs-agent-cursor-en.html)
* [Agentic AI Series 2: From Thinker to Doer — The Paradigm Revolution and Technical Architecture of Agentic AI](/agentic-ai-en.html)
* [Agentic AI Series 3: Turning &#36;20 into &#36;500 - Transforming Cursor into Devin in One Hour](/cursor-to-devin-en.html)
* Agentic AI Series 4: Using Cursor as a Universal Entry Point for AI (This Article)

---

After completing the [previous article](/cursor-to-devin-en.html) introducing the modifications to Cursor, using Agentic AI in a "I say, you do" mode has become my primary method for leveraging AI. This further inspired me: is it possible to use Cursor or a similar editor as a universal entry point for AI?

This idea stems from two main observations. Firstly, when we use AI as a consultant, we often need to perform a lot of copy-pasting, which could be streamlined within Cursor. With just a click of "Apply," the AI's response is inserted directly into the document we're writing. From the user's workflow perspective, Cursor provides a more natural interface.

Secondly, AI as a consultant has a significant flaw—at least in current AI products—the integration with search engines isn't very effective. Whether it's ChatGPT's Search, Proplexity, or PoE's Web Search Bot, they typically perform a simple browse of the first few results before giving a hurried answer. While this might suffice for single-turn AI Q&A, those accustomed to Agentic AI naturally expect higher task completion quality, such as scrolling through more results or iterating keywords multiple times to eventually get a systematic summary. Often, I'm willing to wait for higher quality answers, and this is precisely where an Agentic AI like Cursor can excel.

Therefore, I began a series of experiments to explore whether Cursor could replace ChatGPT or Claude.AI as a universal entry point for using AI. After some initial attempts, I was very pleased with the experimental results. Below, I will briefly introduce how Cursor can be used to accomplish various common AI tasks, especially traditional non-agent AI applications, and compare its advantages and disadvantages.

### Q&A

For the simplest common-sense questions, we can directly input questions into Cursor Chat to get answers. This is no different from traditional AI, with one notable advantage: we can directly call OpenAI, Anthropic, or even our own private AI within the same interface.

![Asking QWen2.5 in Cursor](/images/cursor-entry-chat-en.png)

Beyond that, a significant benefit is that because Cursor is an editor, we can conveniently collect and preserve the results of Q&A, turning them into reusable documents.

Another advantage of the editor is its versatility with text-related tasks. For example, I wanted to translate my Chinese blog into English. After requesting this in Cursor Chat, it provided an English version of the article. Clicking "Apply" automatically compared the Chinese and English documents, highlighting the differences. Interestingly, because the structure of the translation and the original is identical, the comparison naturally forms an alternating Chinese-English visual interface. Additionally, we can directly and intuitively modify the English text and finally accept and copy it to complete the translation. Although I believe this was not Cursor's original intention, the entire workflow is exceptionally convenient and natural.

![Translation task in Cursor](/images/cursor-entry-translate.jpeg)

### Integrating Private Document RAG

Cursor has a feature that can accurately find relevant functions even in a large codebase and use that information to assist in writing code. For non-development-related Q&A, this naturally serves as a RAG (Retrieval-Augmented Generation) engine.

When we submit a question in the Q&A window using Command + Enter instead of just Enter, Cursor first performs a search within the current folder. It then displays the top-ranked documents and their relevance below the text box, finally constructing the prompt using this information to complete the generation. These intermediate results can be expanded and viewed in the interface. Moreover, this feature can be used not only in Chat but also as a step in Agentic AI because the search function is also an Agent Tool that Cursor Composer can invoke.

![RAG in Cursor](/images/cursor-entry-rag-en.png)

In the example above, I placed all my blog articles in the current folder and then asked Cursor a rather complex question: how have my views and attitudes towards AI changed over the past two years since the release of ChatGPT? Cursor's response was impressive. It first organized some keywords on its own, then performed retrieval using these keywords, and the results seemed reliable. Next, it summarized and compared these articles, providing a rather in-depth answer.

Thus, even for non-development tasks, Cursor can naturally integrate with private documents for Q&A. Compared to a purely conversational chat interface, Cursor can seamlessly integrate these newly generated insights into new documents, continuing to use them in future searches. This forms a knowledge loop. This utility and the ability to explore, integrate, and add knowledge are very important for knowledge management. Therefore, if you use software like Obsidian for knowledge management, you might consider using Cursor to enhance the efficiency of knowledge retrieval and management.

### Search

Another unexpectedly useful feature is treating Cursor as a search engine. Although Cursor itself does not support web searches, this can be achieved through the tool's excellent extensibility. As mentioned in our previous [modified Cursor article](/cursor-to-devin-en.html), we can write a small crawler tool to perform searches and scrape web content, then describe these two tools in the `.cursorrules` file. This effectively extends Cursor's capabilities to include web searching and browsing.

I conducted several simple and complex experiments, and its answers were as impressive as ever. For example, when I asked about recent news from OpenAI, it accurately sifted through search results to summarize related events over 12 days of continuous live streams and mentioned that yesterday OpenAI officially released the o1 model in the API, reducing the tokens used for thinking by 60%. When I used similar keywords in GPT searches, I couldn't get such impressive results. For instance, GPT's response was still talking about the release of the latest model GPT-4o, which is outdated.

![Searching in Cursor](/images/cursor-entry-search-1-en.png)
![Searching in Cursor](/images/cursor-entry-search-2-en.png)

*Interestingly the second figures shows Cursor noticed a mistake it made and took notes in `.cursorrules` to prevent it from making the same mistake again.*

Another impressive example is when I wanted to recreate a niche game called "Beijing Floating Life" but couldn't remember its details. When I asked Cursor Agent, it not only performed a search but also iterated keywords multiple times, ultimately generating a fairly complete game report, which I placed [here](https://yage.ai/beijing_life_story.html).

Because the tools and the prompts in `.cursorrules` are self-written, the customization capability here could be very high. For example, you can set it to look at the top 20 results at once instead of being limited to the top three or five, or you can specify in the prompt that when searching for programming-related content, even if I input Chinese keywords, you should search using English first. This flexible customization allows it to achieve very high service quality.

### Personalization

Additionally, as mentioned in our previous article, throughout the use of Cursor, we can also achieve customization and personalized memory through prompts. For example, if you want it to answer in Chinese, or search a specific website for certain topics, or have a special database containing links you frequently use in chats, you can provide these either through prompts or by adding specific documents dynamically. It will use this additional information to answer accordingly. Therefore, it also serves as a private assistant that can grow and be trained.

### Limitations

However, as of now, Cursor still does not have an API that can be called programmatically, nor does it provide a mobile version. Therefore, all the operations mentioned above are done on a computer. But I believe that for an Agentic AI capable of performing tasks, having a mobile client is especially important. After all, interacting with Agentic AI often only requires speaking or chatting. This allows many tasks that previously required sitting in front of a computer to be done on a mobile device. Therefore, this is a considerable limitation in using Cursor as a universal entry point for AI. Let's see if any manufacturers can recognize the importance of Agentic AI on mobile platforms early and address this gap. But the good news is that with our experiments and the development of standard protocols like MCP, implementing these features is not very difficult nowadays.