Title: It's Not That I Prefer o3, It's That It Actually Started Doing Things Proactively
Date: 2025-04-20 22:00
Category: Computing
Tags: AI, English, Agentic AI, ChatGPT, o3
Slug: o3-en

Recently, I exported my ChatGPT usage history (by the way, Settings → Data Controls → Export all data gives you a zip file with all chat logs in JSON, easily visualized with a bit of scripting).

I was initially just curious about my usage patterns over the past few months, but the resulting chart surprised me. Two distinct spikes appeared during this period: one on February 26th (when image generation launched) and another on March 25th (when o3 was released).

![ChatGPT usage](/images/chatgpt_usage_202504.png)

The latter, o3, triggered an almost vertical surge in my usage after its launch. This was the first time I realized: it wasn't me consciously trying out o3; it genuinely changed my habits, quietly becoming my default assistant for life and work.

We used to call traditional AI like ChatGPT tools, query machines – you ask, it answers. But o3 is different. It's the first model that made me realize I could hand over a task, and it could research, think, try to persuade me, and even prepare an email to send. It acts like a real executor, not just a reflector.

The following personal anecdotes illustrate how this shift occurred. They aren't the most complex technical challenges or typical AI applications, but that's precisely why they're worth sharing.

## Image → Inference → Email: Fixing a Leaky Coffee Machine

My home coffee machine started leaking. Not a sudden burst, but persistent water pooling near the base after each use. Initially, I suspected an aging gasket, a common issue according to online forums.

I quickly found the part and replaced it. The problem persisted. To make matters worse, the machine was years old, well past its warranty. Still, I felt it shouldn't be a fatal flaw – it's just a leaky coffee machine, not an engine. I should be able to fix it.

So, I handed the problem to o3. Crucially, I didn't just tell it the coffee machine was leaking; I explained it like I would to a person, detailing my troubleshooting steps, the forums I'd checked, the parts I'd replaced. I also attached a photo of the machine and its model number.

The result was dramatically different.

o3 didn't offer a direct diagnosis. Instead, it did three things first:

1.  It looked up the repair manual for this specific coffee machine, including the exploded view diagram.
2.  Based on the diagram and the location I had already replaced, it inferred another likely leaking seal – a hidden part higher up that, if damaged, would seep water down along the pipes.
3.  It explained its reasoning, including the structural path, water flow direction, adjacent part numbers, and provided a link to the original PDF for me to verify.

![Espresso machine explosive view](/images/espresso_machine_explosive_view.png)

What amazed me wasn't whether its diagnosis was correct, but its ability to *read* the structural diagram and reason proactively. Typically, LLMs are oblivious to such images, but o3 started using images as part of its reasoning input, not just for captioning. When I pushed it further, asking "why not the part I replaced?", it traced the water path in the exploded view and pointed out that while my replacement part was common, it wasn't on the suspected leak path. Comparing it with the diagram, I saw it was right.

I then asked it to draft an email in English to the manufacturer's support, outlining the entire troubleshooting process, its diagnosis, and asking if I could replace the part myself. It quickly generated a draft, included the brand's customer service email, and reminded me to confirm the model and purchase date.

Even better, after the email, it added a note suggesting that if I planned to do the replacement myself, I'd need food-grade silicone grease and a specific-sized wrench, providing reference purchase links. I hadn't mentioned these; it judged and reminded me independently. This was the first time I felt ChatGPT wasn't just answering but actively *assisting* me in completing a task. It wasn't just giving a reliable diagnosis; it was a partner helping me gather evidence → eliminate hypotheses → prepare communication materials. The task wasn't carried by me alone; we did it together.

## Letting AI Handle the End-to-End Hassle

I occasionally browse auction sites for things like photography gear. Recently, I saw an item at Christie's in Hong Kong that looked like a good deal. The problem? The auction price is never the final price:

*   You have to add the auction house's commission (often tiered).
*   You need to factor in currency conversion (HKD to USD).
*   If importing, you add customs duties and brokerage fees.
*   Once landed, if shipped to Washington state, you also have to calculate sales tax.

You might think this isn't hard to calculate. But for someone with zero experience in taxes and imports, the ambiguous cross-border rules + constantly needing to check commission tables is genuinely procrastination-inducing. So I thought: could o3 just calculate it all for me?

I opened ChatGPT, pasted the item link, and told it: "This item is auctioned in Hong Kong, assume the hammer price is XXX HKD. I'm in Washington state. Help me calculate the final cost to get it in hand."

o3 didn't just do a "single-step lookup." It executed a complete chain-of-thought style operation:

1.  Identified the item category to determine the applicable Harmonized Tariff Schedule (HTS) code for import duties.
2.  Looked up the current US tariff rate for that category.
3.  Pulled exchange rate data to convert HKD to USD.
4.  Calculated the commission based on the auction house's official tiered rates.
5.  Simulated the scenario of sales tax being charged upon landing, estimating the applicable rate for Washington state.
6.  Provided links to all data sources for cross-verification.
7.  Gave an estimated final landed cost.

The key was – I didn't ask step-by-step. It decomposed the task, executed sub-modules, and summarized the results on its own. Plus, a bonus: it reminded me that if customs duties were paid before a certain date, an older (potentially lower) rate might apply due to an upcoming policy change, advising me to watch the declaration window. I hadn't even considered that.

This wasn't just "AI helping me with math"; it was me giving it a vague goal, and it automatically ran the entire process, even pointing out details I'd missed. What used to require five web pages, a spreadsheet, a calculator, and some experience to figure out the landed cost, now just needs one sentence: "Calculate this for me." This isn't a minor convenience; the entire task was effectively delegated to the AI.

## My AI Public Opinion Desk: Harvard, Trump, and the Underlying Financial Leverage War

Scrolling through the news one day, a headline caught my eye: "Trump Considers Cutting Harvard's Federal Funding and Revoking Its Non-Profit Status." Initially, I dismissed it as campaign rhetoric. But then, news followed about restricting international student quotas, potentially revoking the 503(c) non-profit status, coupled with reports of Harvard starting to sell off some assets. Suddenly, I realized this wasn't just talk; it could be an attack on the entire financial model of top US universities.

So, I gave this problem to o3, asking if it could help me:

*   Review the timeline of events.
*   Explain the relevant legal provisions, like 503(c), international student aid mechanisms, federal research grant standards.
*   Compare if similar actions or policy changes have occurred historically.
*   Analyze the potential impact on Harvard and the financial markets.

I didn't have high hopes – complex news spanning law, policy, and public opinion is often AI's weak spot. But o3's handling was impressive.

It first listed relevant news sources from the past month, creating a mini-timeline explaining the situation's evolution. Then, in clear language, it explained the definition and conditions of 503(c) non-profit status and the tax and structural changes its revocation would entail. It pointed out that while Harvard is wealthy, its operations heavily rely on federal research funding. Cutting this off would not only affect projects but also have knock-on effects on international PhD student scholarships. It even drew an analogy to the UK pension crisis in 2022 to analyze the potential market impact of Harvard selling assets.

I initially just wanted to understand the situation, but it acted like a structured intelligence analyst, elevating the issue from gossip to the level of financial weaponry. The report was well-structured, devoid of emotional bias or taking sides, simply laying out the logical consequences of "if this actually happens." You could think of it as a neutral but highly capable intern policy researcher – not overstepping, but guiding you to a higher-level problem space. This is especially helpful for someone like me, unfamiliar with the intricacies of the US political and economic system.

## An Unexpected Bonus in Leather Care

It started simply: the leather interior in my car was a bit dirty, and I wanted a cleaning kit. I planned to buy the one recommended on the car brand's official website for convenience, but the price was shocking. They could practically rob you and still generously include a leather cleaner – truly touching.

I gave o3 the car model and asked for recommended brands and products. As usual, it listed several options, including the official recommendation. But it didn't stop there. It crawled some forums and product manuals, then pointed out: "The one you're looking at is actually private-labeled by Company X. You can buy the original brand version directly; the formula is almost identical, and it's 20 times cheaper."

I was stunned. I hadn't even considered private labeling, so naturally, I didn't mention it in the prompt. It had independently analyzed the product's OEM source, provided a formula comparison table and chemical ingredient list, and finally offered links to the alternative for me to confirm.

This made me realize for the first time: Agentic AI like o3 doesn't just mechanically achieve goals; it even starts to *proactively optimize the objective function*. It understood that what I really wanted was good cleaning results without being ripped off by brand premiums. So, based on my task intent, it bypassed the literal meaning of my prompt and gave me a smarter choice. I didn't teach it consumer psychology, yet it started making consumer judgments I agreed with; I didn't explicitly ask it to save me money, but it understood my implicit desire not to overspend unnecessarily.

This isn't just an information tool; this is an agent learning my personal (frugal) taste.

## The Tipping Point for Agentic AI: Not Just 'Can It?', But 'Will It Act?'

From these examples, it became increasingly clear: we used to treat AI as an answer machine, starting from a prompt and hoping for an accurate response. The change o3 brings is that it starts proposing action steps, completing task structures, reminding you of omissions, and even rewriting your goal itself. This isn't just an improvement in language model capability; it's a shift in the authority structure of tasks.

AI transitioning from "you ask, I answer" to "let me help you get this done" is a significant milestone worth noting. It makes many tasks you wouldn't have started seem feasible; it makes many processes you didn't want to rethink reusable; it turns work you thought only humans could do into "AI + me" collaborations.

And all these changes boil down to a very real metric: my usage frequency skyrocketed.

Reflecting on these cases while writing this, I see a common thread. It's not just that AI is stronger, but that:

*   It proactively connects information → action → feedback → external expression.
*   It doesn't wait for your prompt but keeps pace with your thinking.
*   It doesn't need explicit instructions but completes the task model itself.
*   It serves not only complex problems but also changes the starting point of everyday decisions.

Have you had similar experiences? Maybe you didn't initially intend for AI to do something, but later found it not only capable but surprisingly clever? Feel free to share your stories, usage paths, screenshots, and reasoning chains in the comments below.