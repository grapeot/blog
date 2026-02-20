---
Title: When AI Becomes Your Direct Report: Three Management Pitfalls Tech People Must Overcome
Date: 2025-02-01 19:00
Category: Computing
Tags: English, AI Management
Slug: ai-management-en
Translation: ai-management.html
Summary: Uses a debugging session to illustrate three key AI management skills: resisting the urge to take over, providing visual context instead of vague complaints, and teaching methodology rather than giving answers—the shift from IC to manager mindset.
---

Tonight, I asked AI to take multiple local small images and stitch them together into a large image following certain rules. The process wasn't particularly dramatic - it only took me five minutes to help AI complete the task. However, during this process, I found myself consciously using several AI management techniques that newcomers often lack. So, I'd like to share these specific techniques to see if they might be helpful to others.

## Breaking the "Curse of Knowledge": The Evolution from Tech Expert to AI Manager

Here's how it started: I asked AI to generate a stitched composite image, but the result showed obvious seam artifacts that were immediately apparent to the eye. Yet it was hard to pinpoint exactly what was wrong. As a veteran coder who's been writing code for what feels like centuries, my hands were already on the keyboard, ready to dive into checking coordinate origins, size normalization, and scaling details.

But just as I was about to take over the code, I suddenly realized this was a typical trap in the AI era. This trap stems from the "Curse of Knowledge." The more technically proficient someone is, the more likely they are to want to jump in and debug AI's work themselves. This happens because we're so familiar with these programming details that we can quickly guess the possible causes of problems. Plus, programming gives us that satisfying dopamine hit, so our fingers itch to jump in. And yes, this often can speed things up, since at this stage, AI's debugging capabilities in our familiar domains aren't as sophisticated as ours.

But why did I resist this urge? Because I realized two things:

1. First, this would rob AI of an opportunity for self-improvement. While we could quickly solve the problem with our technical skills, it's like a boss stealing work from their subordinates - a major management faux pas. We should give team members as many opportunities as possible to grow, rather than micromanaging everything. Otherwise, while it might look like problems get solved quickly, team members never truly improve because they're just copying answers.

2. Second, this is a common trap that new managers often fall into. While doing the work yourself might be faster than waiting for subordinates to figure it out in one or two instances, when you have multiple reports, the mindset shift from "I can code, so I'll fix it myself" to "I'll be a manager and teach team members how to fix it" can lead to exponential efficiency gains and better scalability.

## Rejecting Blind Debugging: Providing Visual Context

Based on these two reasons, I suppressed my urge to jump in and decided to see what would happen if I didn't dive into the frontline but instead assisted AI with debugging from a more macro perspective.

I first asked myself, how should I describe to AI where the problem lies? Whether dealing with humans or AI, directly showing the erroneous output image seems like the most intuitive approach. But putting myself in their shoes, if I were given this image with obvious stitching artifacts, I'd also struggle to immediately identify the root cause. It would require careful observation of the exact locations of the flaws, then working backwards from there to identify the specific bug in the code. Ideally, we'd want to add some logging around the image generation too.

In other words, if we just tell AI "you did it wrong" and show it the generated image, we're essentially setting it up for failure. This is because AI lacks sufficient context and precise information to quickly locate the bug. I can easily imagine what would happen if I did this - AI would just spin its wheels, making random changes each time and asking if the result is correct. Upon learning it's not, it would take another shot in the dark, ask again if it's correct, and continue this cycle of apologies and iterations. So whether working with humans or AI, I try to avoid this whiteboard programming-style debugging where you can only stare at code and guess the cause. I wouldn't throw a problem at a subordinate that can't be judged by eye alone and expect them to figure it out in isolation.

From this perspective, a natural thought is that for AI to successfully fix the issue, we need to provide it with more comprehensive information. For example, we should visualize the position, size, and arrangement relationships of each small image in the final composite. This way, it can intuitively see if the image layout makes sense, and it also makes it easier for me to verify the correctness of its output. So I used this reverse-thinking manager mindset to tell AI: your result is wrong, but to help you understand where it went wrong, first create a visualization showing the position of each small image in the composite, so I can see where everything is being placed.

AI quickly generated a visualization. It was obvious that the top row was disproportionate to the images below - this was why we saw stitching artifacts in the final version. At this point, I could already see what the problem was. But for the same reasons as before, I still showed this visualization to AI and asked it to "look at where the problem is," let it make corrections, and add the lessons learned to the cursor rules.

After this, AI examined the visualization itself, quickly understood where the problem was, and actually corrected the code to generate the right image. Throughout this process, I never directly gave AI the answer. Instead, like a human manager often does, I introduced best practices. Through mechanisms and procedures, I let it discover the problem itself and come up with its own solution.

## Cognitive Scaffolding: Cultivating AI's Problem-Solving Abilities

From this story, I want to share two main insights:

The first point is that many people are reluctant to use AI for various reasons - maybe because AI hallucinates and can deceptively give wrong answers, or because AI is too weak and its coding efficiency is far below their own. But I want to point out that these aren't problems unique to AI. Similar issues often appear in managing human organizations.

For instance, many human colleagues make various mistakes at work, sometimes going down wrong paths or making incorrect assumptions and speculations. When such colleagues submit code, would you pass it directly to your boss without any review? Of course not. We first conduct code reviews and various cross-validations to ensure the quality of the code and reports, only submitting them further after we've verified they meet our standards.

From another perspective, AI's current tendency to spin its wheels when writing code and its low efficiency is very similar to what we see with inexperienced employees in human teams. As human managers, we often first try to help them grow fundamentally, learn working methods, accumulate experience, and through this approach become more scalable, achieving far higher productivity than working alone. This is especially important for new human managers to note. The difference now is that while everyone can use AI, many haven't realized that our role has quietly shifted to becoming AI Managers.

And this is precisely my second point. To effectively utilize AI, the key isn't becoming an LLM expert who knows all the technical details about transformers and fine-tuning. On the contrary, to use AI most effectively, we need to complete the mindset transformation from IC to Manager. Looking back at the three decisions we made in this simple example:

1. Don't fight AI for the keyboard. When subordinates encounter problems, our responsibility isn't to jump in and fix things ourselves - that's neither scalable nor gives them growth opportunities.
2. Don't let AI work in the dark. It's like throwing a new intern into a legacy codebase and expecting immediate output - that's setting them up for failure. In such situations, AI can only spin its wheels, fail to debug, or start hallucinating. This isn't AI's fault, but rather the manager not providing enough information.
3. Teach fishing instead of giving fish. The key of us teaching AI to work isn't helping it debug and giving it the answers directly. Instead, it's teaching it methodologically how to find bugs itself. This way, our role becomes that of an enabler and multiplier, achieving true multiplicative productivity growth.

So the most crucial mindset shift is to stop focusing on making yourself stronger, and instead learn to stand in a manager's position to make AI stronger. Like human managers, we don't need to be more technically proficient than AI, but we need to better understand how to create conditions for its success. Next time AI messes up a task, try asking yourself these three questions:

1. Is the information I provided sufficient for a human colleague to understand the task?
2. If I were new, what materials would I want when receiving this task?
3. Are there any general methods that could guide thinking without getting into technical details?

After all, the most scarce resource isn't AIs that can write code, but AI managers that can enable AI to deliver.