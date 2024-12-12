Title: Seeking Help Effectively through Human Oriented Prompt Engineering
Date: 2024-09-11 12:44
Category: Computing
Tags: AI, Prompt Engineering
Slug: seeking-help-through-human-oriented-prompt-engineering

I often lurk in various communities and frequently see people seeking help and others offering assistance. Unfortunately, I find that the majority of this help is ineffective, with very few actually resolving the issue. For example, someone might ask in a group, "I'm facing problem X, how do I solve it?" and people might offer suggestions like, "Try A, see if it works, or try B." But ultimately, after trying them, nothing seems to work, and the whole request for help just fades away.

The reasons behind this are complex, but here I want to discuss a small angle. In many cases, simply using some [straightforward prompt engineering](https://yage.ai/prompt-engineering-guide.html) techniques and slightly altering the way we phrase our questions can greatly enhance the effectiveness of seeking help, potentially leading to more useful responses quickly.

Before looking at this small technique, let's first observe the biggest problem people face when seeking help and assisting each other. My observation is that the biggest problem is people just guessing what could explain the problem the person is facing. In other words, A could lead to X, so you should try fixing A.

Take a simple example: someone asks, "The light bulb at my home isn't lighting up, what should I do?" A natural response might be, "If the bulb is broken, it won't light up, so you should buy a new bulb and replace it." This line of thinking seems fine, but if you observe more, you'll find it's a very inefficient way to solve problems. In programming, it's called random debugging, or just guesswork. The reason is that there might be many causes for X, and testing them one by one takes a long time.

Using the previous light bulb example: it could be due to a power outage, a broken power strip, a faulty light switch, or a broken wire, not just a broken bulb. Checking each possible cause could take forever. There's also a possibility of user error, such as replacing the bulb and the lamp, only to discover a week later that the circuit breaker was off. Don't laugh, this is quite common when seeking help.

So, if we want to avoid random debugging, is there a method to efficiently identify the cause of the problem? This is actually a very valuable and fundamental question. Getting this right can significantly elevate your work and life. In essence, it's not complicated; we shouldn't just guess the possible causes of X, but rather design a series of experiments to narrow down the range in reverse.

For the light bulb example, you might first test if other lights on the same power strip work. If they don't, it could be a power strip or circuit breaker issue, or a power outage. If they do, it indicates a problem with the light itself. The light could have issues with the bulb, wiring, switch, etc. You could use a test lamp near the bulb to see if there's power. If there's power but the bulb doesn't light, it's a bulb issue, so replace the bulb. If there's no power, it could be a wiring or switch issue. Through these simple experiments, you can accurately identify the root cause in a couple of minutes and address it. This process saves much more time than buying a new power strip or bulb.

But why don't people help others this way online? Part of it is because few people have this reverse debugging mindset, but another crucial reason is the way questions are asked. Most help-seeking posts ask, "What should I do?" leading others to suggest what you should try, like replacing the bulb or power strip. This way of asking implies you're looking for a direct final solution, and consequently, you receive scattered and unmethodical answers.

How to solve this problem? In [AI](https://yage.ai/recent-AI-advancement.html), there's a prompt engineering technique called Chain of Thought, which can be applied here. Rather than asking for the final solution, a better question is to ask, "What could be causing this, and how can I verify it's the reason?" In the light bulb example, you might say, "My light isn't working, are there any methods to help me identify which part is the problem?" This way of questioning encourages people to consider multiple possible issues, not just a broken bulb, leading to more effective answers.

From another perspective, thinking this way might reveal you don't need to ask others online and could solve it yourself. Or, when you realize you truly can't solve it and need to ask others, you'll naturally write out your thought process, which greatly helps in receiving more effective assistance.

In summary, this reverse debugging mindset is a crucial skill in work and life. It can save us considerable time and enable us to achieve things previously unattainable. Using simple prompt engineering techniques, we can also instill this mindset in others, helping them solve our problems more effectively and inspiring them to solve their own issues more efficiently. This is also the purpose of writing this article.