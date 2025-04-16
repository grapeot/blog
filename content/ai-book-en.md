Title: We Fed an AI Three Years of Our Group Chat History. It Wrote a Surprisingly Deep Book.
Date: 2025-04-15 22:00
Category: Computing
Tags: AI, English
Slug: ai-book-en

For the past couple of years, we've been constantly using large language models to write summaries, PRDs, code, poetry... you name it. Yet, there's always been a nagging feeling: something's missing before AI truly becomes a core part of our productivity.

It's not that the models aren't powerful enough. GPT can already craft impressive articles, generate complex functions, and even analyze financial statements. But ask it to do something genuinely useful in a team context – like debriefing a problematic product launch, helping understand the decision-making thread over the past year, or drafting a reliable collaboration guide for the team – and it often flounders.

We kept asking ourselves: Why can't AI truly participate in complex cognitive work yet?

Initially, we blamed poorly written prompts, insufficient model intelligence, or our failure to break down tasks effectively. Gradually, however, we realized the problem might run deeper: the world AI interacts with is incomplete.

## Why Isn't AI Truly Productive Yet?

Simply put, we organize information in human ways and expect AI to understand it like a human.

Humans rely on implicit memory, contextual intuition, and tribal knowledge.

*   You see your boss frown, and you know they dislike a certain direction.
*   You grab coffee with a colleague and exchange a flurry of fuzzy ideas about future plans.
*   You review 10 pull requests and get a gut feeling about who understands the system architecture and who's just going through the motions.

We don't write this stuff down in documents, nor do we need to.

But AI *does*. It lacks long-term memory. It lacks contextual awareness. If you don't feed it the files, it doesn't even know what the team has *done*.

That's why AI fails spectacularly at tasks that seem simple to us. It's not a lack of intelligence; it's that we've never clearly explained the world to it. This is the core reason we've struggled to hand off complex tasks to AI.

## Information Ruins: AI's Toughest Challenge

There's a type of data that AI dreads most, and it's the kind we generate constantly:

*   Three years of Slack channel history.
*   A WeChat group filled with arguments, idle chat, forwarded links, stickers, and inside jokes.
*   The back-and-forth revisions of product requirements within a group chat.
*   Combative PR comment threads between engineers.
*   Even discussion boards in user communities.

This data shares common traits:
It's dense, fragmented, messy, yet utterly irreplaceable.
We call it **Information Ruins**.

This kind of data inherently has three characteristics:

1.  **Immersive:** It's the primary channel for a team's actual decision-making trajectory.
2.  **Highly Unstructured:** No clear topics, threads, or defined audiences.
3.  **Low Signal-to-Noise Ratio:** Packed with irrelevant information, making it a headache even for humans to parse.

But precisely because of these traits, it's incredibly valuable. It holds the team's knowledge map, decision weights, cultural inertia – the truly irreplaceable organizational wisdom.
The problem? AI is almost helpless when faced with this kind of data.

![Information Ruin](/images/ai_book_ruin.png)

## We Tried Everything... Nothing Quite Worked

We didn't set out to have AI write a book.
Our initial goal was much simpler: could AI help us make sense of our WeChat group discussions? We'd done some manual整理 (tidying up), but it was exhausting, slow, and painful.

Our first thought was RAG (Retrieval-Augmented Generation). This was the go-to approach for structuring content back then: chop the text into small chunks, create embeddings, and use prompts for generative answers.
The result? The model could tell us *who* said *what*, or if topic X was discussed. But when we asked:
"How did the team's understanding of AI collaboration evolve over these three years? Were there key points of contention and consensus?"
It drew a blank. Not because it wasn't capable, but because it lacked a complete, panoramic view from which to form a judgment.

Next, we tried Agentic Workflows.
Theoretically, agents can plan tasks, autonomously use tools, and engage in multi-step reasoning – sounds great. But the reality was:
In this highly unstructured data, the agent had no idea what to do next.
The content was too chaotic, the clues too fragmented, with no clear goal or easily referenceable information blocks. The outcomes were:

*   Finding nothing relevant.
*   Endlessly extracting small snippets and summarizing them.
*   Getting stuck in loops: "I found content similar to what you mentioned..."

This led us to question our expectations of AI. Maybe the world we were feeding it was simply unsuitable for its comprehension?

## The Turning Point: GPT-4.1 and Gemini 2.5 Arrive

Our breakthrough arrived quietly.
In a way, the release of GPT-4.1 didn't cause much fanfare. Unlike previous versions, it didn't boast flashy new capabilities or introduce novel interaction methods or model types.
But it brought two crucial changes:

1.  Support for million-token context windows.
2.  Simultaneous support for prompt caching, reducing costs by an order of magnitude.

Gemini 2.5, also featuring a million-token window, launched a few weeks prior, proving smarter and more proactive than its predecessors. Although it lacked prompt caching (making costs daunting), its capabilities were undeniably strong.

Suddenly, we realized:
For the first time in history, models possessed two critical attributes simultaneously: **massive memory capacity + high-quality intelligence.**
Separately, neither attribute could change the game:

*   `o1` was smart but capped at ~200k tokens, unable to handle low-density context.
*   Gemini 1.5 Pro could remember a lot but often produced muddled output, lacking judgment.

Our previous attempts failed precisely because no single model could comprehend a chaotic world.
Now, things were different.
We had a model capable of reading *all* the chat logs, then thoughtfully saying, "I think this issue you discussed deserves its own chapter."
We decided to give it a shot.
We bundled three years of WeChat history – without cleaning it – and fed it wholesale into the model. No chunking, no pre-defined questions, just dumped directly into the context window.

And that's when the story took a different turn.

## Reflect-Extract-Build: A Counter-Intuitive Collaboration

We didn't generate a book overnight.
Initially, we simply asked the model: "What did you learn from this pile of chat logs?" We didn't expect anything profound. From an engineering perspective, it was just facing 400k+ tokens of messy text.
But surprisingly, it offered some insightful observations.
It highlighted several themes we had debated but never formally summarized:

*   How personality differences in AI interaction styles within the team affected usage patterns.
*   Prompting as a metaphor for management (you're not just writing instructions; you're setting performance metrics).
*   The challenge of building mental models for multi-model collaboration.

We suddenly realized: the model wasn't just answering questions; it was more like synthesizing reading notes.
So, we formalized this into a loop:

1.  **Seed Idea Input:** We gave it a general direction, like, "What patterns in the team's AI usage are worth noting?"
2.  **Viewpoint Generation:** The model output several potential insights.
3.  **Challenge/Verification:** We asked it to find specific evidence from the chats to support or contradict these viewpoints.
4.  **Refinement:** The model updated its views, filtering down to a few more mature, nuanced perspectives.

We ran this cycle many times, keeping each interaction under ~10,000 tokens, with the model retaining some history from previous rounds.
Once these viewpoints felt solid, we instructed it to write a chapter for each. Each chapter aimed for 4000-5000 words, resulting in about seven chapters total.
Finally, we stitched them together and polished the text to form this little book.

We also employed some prompt engineering tweaks:

*   Splitting the chapter writing into batches (e.g., Ch 1-3, then Ch 4-6) to prevent the model from getting "lazy" with too many tokens in one go.
*   Making the model restate the objective before each writing task to enhance focus.
*   Counteracting the tendency for weak endings by prompting: "Please end the chapter with 'To be continued...'" (which we then removed in post-processing).

These might seem like minor tricks, but they were crucial for nudging the model towards producing high-quality output.

## The Result: Surprisingly Human-Like

We initially expected [this little book](https://www.superlinear.academy/c/ai-resources/ai-book-draft) to be a disjointed collage at best.
But upon reading it through, we noticed several surprising things:

1.  **Natural Pacing:** Chapters flowed logically without excessive repetition.
2.  **Presence of Viewpoints, Not Just Summaries:** Some sections even self-corrected, like "Earlier, we discussed X, but looking back, counter-example Y might also exist."
3.  **Structural Cohesion:** It moved from *What are we using AI for?* → *How is AI reshaping our organization?* → *Future collaboration paradigms*. This showed a clear progression of thought.

We certainly wouldn't claim it's a publishable masterpiece. But we can confidently say this is the first time we've seen a language model construct a cognitive structure from highly unstructured source material.
This isn't just about technical achievement; it's the first time we felt AI wasn't just an instruction-follower, but a reader allowed to *think*.

## Intelligence ≠ Compute Power. Intelligence = Memory × Immersion

This experiment forced us to rethink: where does AI's intelligence truly come from?
We used to believe bigger models, stronger reasoning, and more complex agent setups were the path to more useful AI.
Now, we suspect the real breakthrough isn't in the model itself, but in the **information flow**.

Previously, AI could only see small snippets at a time. We tried forcing coherence with RAG and caching mechanisms, but it was merely simulating reading fragment by fragment.
The 1M token context window enables something different: an **immersive, uninterrupted deep processing capability.**
Just like human reading.
You don't read a book three pages at a time, constantly asking someone to find and stitch together the next pages. You read it through, reflect, maybe reread parts.
Now, AI can finally do the same.
**Memory capacity and immersion time are the fertile ground for intelligence.** Understanding didn't emerge from stronger reasoning alone; understanding finally had the *soil* it needed.
We don't necessarily need more neurons; we need more complete input.

![Memory Flower](/images/ai_book_memory_flower.png)

## So, What Does This Really Mean?

Sure, we made a book. But that's not the point.
The point is, we've glimpsed a possibility: **AI no longer needs us to sanitize the world for it; it can directly confront raw reality and begin to understand it.**
What does this unlock?

*   It means we might stop manually cleaning customer interview transcripts and just let AI identify product opportunities directly.
*   It means we might stop summarizing team decisions in PowerPoints and instead have AI generate debriefs straight from Slack.
*   It even means we could potentially use AI to read all the Pull Requests for a project and write its code evolution history.

This isn't science fiction. This is now.
The book we created isn't primarily for others to read. It's the first knowledge product we co-created with the model. An attempt to transform the detritus of human language into a logical structure a machine can comprehend.
We failed many times. Tried wrong approaches. Wasted plenty of tokens.
But this time, it feels like we've genuinely opened a door.

## Epilogue: The Book is Just the Surface, Rebuilding Understanding is the Core

What will AI ultimately do? No one can predict accurately.
But one thing becomes increasingly clear:
**AI's key capability isn't writing code or generating images, but building understanding.**
This isn't the *next* step for generative AI; it's not the future – it actually started some time ago.
We're just trying to articulate it more clearly now.

Does your team have documentation you've always meant to organize but never found the time? An internal discussion forum you suspect holds fragments of strategic thinking? A pile of interview recordings you haven't had time to listen to?
Try feeding it to an AI. Don't ask it to summarize. Don't ask specific questions.
Just tell it: After reading all this, tell me – what did you learn?
That's how we started.
[This little book](https://www.superlinear.academy/c/ai-resources/ai-book-draft) is just the first answer it gave us.

(This post was drafted by GPT-4.1 based on prompts, structure, key points, and feedback provided by DuckGo [placeholder for original author "鸭哥"]).