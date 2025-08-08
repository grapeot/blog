Title: When AI Hits a Wall: A Playbook for Effective Collaboration
Date: 2025-07-17 22:00
Category: Computing
Tags: AI, English
Slug: ai-unlearn-en

Sharing a great AI conversation with friends using screenshots has always been a minor project. I'd have to carefully scroll, screenshot, scroll again, screenshot again... and then stitch them all together with an app like Tailor. The process was tedious, mind-numbing, and often failed. So, when I started developing my own Multi-Agent Workbench for iOS, I was determined to build a one-click feature for long screenshots to end this nightmare once and for all.

I started, as I often do, with Document-Driven Development. I discussed potential technical solutions with an AI, which proposed four different approaches. Since my app is a simple WebView wrapper rather than a native client, I shortlisted two options that relied on JavaScript and HTML. I then tasked the AI with implementing each to see how they performed.

However, both approaches hit a wall with bizarre rendering issues. The AI's code was logically flawless, but the output was a mess. I had the AI add some logging for debugging, but we were quickly lost. A red flag started waving in my mind: the AI had failed twice on the same kind of problem. I began to suspect the issue wasn't about prompt precision but about the overall technical strategy. Instead of getting bogged down in the weeds, I pivoted. I described the symptoms to a different AI, a Planner AI specializing in research and analysis, and asked for alternative technical strategies from a higher-level perspective.

I also mentioned the app Tailor. It seems to stitch screenshots together based purely on image content, without any JavaScript or web-based manipulation. Instead of asking the AI to solve my specific problem, I asked it to explain the underlying principle. This became a moment of mutual inspiration: I provided the business and technical intuition, and the AI's job was to transform that fuzzy hunch into actionable technical intelligence. It came back with a fantastic discovery: Apple's native SDK includes highly efficient image alignment features. Specifically, it can use the iPhone's GPU to rapidly calculate the precise translation, scaling, and rotation needed to align two images.

This was a game-changer for me. I switched back into execution mode, feeding the Planner AI's findings directly to a coding-focused AI, Claude Code, and asked it to write the code. But the implementation was still broken. I did some basic debugging and had it print intermediate results, only to find they were completely nonsensical. I was stuck again.

Once again, I stepped back to reassess my approach. Reviewing the Planner AI's original response, I noticed it included not just an explanation but also a link to an Apple sample project. I downloaded the example, ran it with my own screenshot data, and it worked flawlessly on the first try. It was also lightning-fast. This was a massive breakthrough because it fundamentally changed the problem. We had established a "Minimum Viable Truth." Previously, we were navigating in the dark, completely dependent on the AI's coding abilities. Now, we had an unshakeable technical anchor—a piece of code *guaranteed* to work. All subsequent work could now revolve around iterating and expanding on this solid foundation.

This path felt much more robust. I returned to Claude Code, had it analyze the Apple sample, and tasked it with a simple prototype: take a screenshot, scroll, take another, and stitch them together *exactly* as the sample did, saving the result. Claude nailed it. However, when I asked it to handle a loop for multiple images, it faltered again. Even with our technical anchor, the more complex logic was just beyond its reach.

At this point, I realized we might be hitting Claude's limits for this task. But instead of diving in to debug the code myself, I switched tools. I moved to Gemini 2.5 Pro, an AI better suited for analysis and strategy. I gave it all the context, logs, and code, with a single instruction: "Don't write any code. Just tell me what's wrong." Two minutes later, Gemini delivered its diagnosis: a pixel-vs-point unit confusion and an inverted coordinate system. When I pasted Gemini's analysis back to Claude Code, it fixed the code almost instantly. It worked perfectly.

This winding journey to automated screenshots was incredibly insightful. Here are my key takeaways:

1.  **The most effective prompt engineering is often about refining the problem, not the prompt.** When an AI is stuck, changing the question can be more powerful than rephrasing it.
2.  **Start with what works.** Anchoring the AI's workflow in a "Minimum Viable Truth" provides an invaluable sense of certainty and direction.
3.  **"Which AI is best?" is the wrong question.** The right question is: "What are the capability boundaries of each AI, and which one is the right tool for the current task?"

Interestingly, I never once got bogged down in the technical minutiae. I didn't scrutinize JavaScript or Swift code, nor did I manually intervene in the AI's choice of data structures or algorithms. I left behind the skills that are traditionally considered "technical." Instead, I focused my time on defining the problem, analyzing competitors, setting the technical direction, and applying the right mental models for collaborating with AI. By "unlearning" my reliance on my own technical skills, I was able to build a fully automated screenshot app in just three hours. That's where the real leverage in productivity lies.
