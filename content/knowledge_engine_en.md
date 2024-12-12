Title: Reflections on AI Knowledge Engines
Date: 2024-06-13 21:00
Category: Computing
Tags: English, Thought Fragments
Slug: ai-knowledge-engine-en

(From my message in the AI Productivity Training Camp group chat)

Someone mentioned using AI for meeting minutes. In fact, meeting minutes are a very basic yet difficult area, and we'll explain why it's challenging below. What I envision is a [knowledge engine](https://yage.ai/GPT-knowledge-management-en.html) that can, on one hand, collect and store information from various sources in our daily lives and work through speech recognition and input; on the other hand, it should be able to extract abstract knowledge from these raw materials; and it should also remind us in real-time when we're outputting information.

For example, when we're in a company meeting and someone mentions that product A needs to consider personalization, along with other less insightful content or short-term decisions, such as completing an action item by the end of the day, the AI should do two things:

1. Identify the former as a long-term strategic direction and the latter as a short-term, easily discardable item.
2. Index the former as part of the knowledge base while discarding the latter.

Then, in the future, when we're writing a document or mentioning in a meeting that product B also needs personalization, the AI should have the ability to remind us that we previously mentioned product A also needed personalization. It could suggest coordinating the two projects and considering reusability in the design architecture.

I believe an AI knowledge assistant like this would not just be a secretary but could help us think more deeply, take on more complex responsibilities, and create more value for the company. However, this is a very difficult problem. The main challenges are:

1. Lack of documentation: In many companies, this is a chronic issue. Much tribal knowledge is never documented, and some great ideas mentioned in meetings get lost because they don't involve action items. My solution to this is:

     - For all non-one-on-one meetings I attend, I use some hacks on my Mac to record both my voice and the voices of participants, then feed this to a local speech recognition model to transcribe and archive all meetings.
     - I extensively use my own [speech recognition](https://yage.ai/realtime-gpt-en.html) platform for efficient input, storing my spoken insights, including what I am saying now, as the foundation of the AI knowledge engine.
     - I haven't done this myself, but a colleague has set up a microphone array at home to record everything said in the office, including the voices of remote participants over the speakers and his own think-aloud moments, then feeds this to speech recognition. These three methods might form a feasible solution to the data problem.

2. Knowledge extraction: I personally think this is currently a very weak area for AI. For example, try taking a recording of a meeting you found insightful and ask the AI to extract the most important or insightful parts. You can tweak the prompts to see if it can produce surprising results.

    My experience is that, in many cases, the AI focuses more on form, producing beautifully formatted meeting minutes that list participants, time, a summary of the discussion, action items, and conclusions. The form is pretty, but the content is empty, missing many insights. I've tried various [prompt engineering](https://yage.ai/prompt-engineering-guide-en.html) techniques, but none have succeeded so far; the results are particularly poor.

    A small trick I've found useful is to first have the AI generate potential insightful questions based on the meeting, then have it answer these questions. This method of inspiring rather than commanding often works better than asking it to directly extract conclusions. I call this "inspire, not command," but even then, the extracted knowledge lacks depth.

3. Timely participation and reminders during output: This is not only a modeling issue but also an infrastructure one. When we input, the AI needs to constantly check our content and possibly perform retrieval-augmented generation (RAG). If we use public APIs for this, it could incur huge costs and latency issues, presenting infrastructure challenges. Additionally, constructing prompts effectively and using the context window to support our writing, retrieve relevant knowledge, and make reasonable inferences are significant challenges.

Overall, I think knowledge management could be a feasible way for AI to create tremendous value for human work, but so far, it's not a trivial problem. Of the three challenges discussed, only the first has been somewhat resolved, while the second and third remain quite difficult and open issues. I am also looking forward to seeing any related discussions and suggestions from others.