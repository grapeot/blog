---
Title: What metric should you use for weight management?
Category: Life
Date: 2022-09-19 19:30
Tags: English, Health
Slug: weight-management-metrics
Translation: weight-metric.html
---

I recently started a new project of my own weight management, and had some learnings on the which metrics to optimize. I share it here hoping it would inspire someone in selecting metrics in ML systems.

I'm a deep believer of "if you cannot measure it, you cannot improve it." So the first thing to manage my weight is to pick up a metric. I did the most straightforward choice — the body weight. It's the ultimate goal. It's easy to measure. There are a whole bunch of online suggestions on how to optimize for this specific metric so we have a solid road map as well. What else could do better?

But after a while, I found the body weight is a terrible metric for three reasons. First, it's noisy. Any 🍔🥛🚽 would make it appear that we gained/lost weights although the real body weight might be simply flat. So to overcome this, we usually look at weekly averages instead of each measurement, which brought the second issue, it has high latency and coarse granularity. If I lost one pound in the past week, what caused this success? What can I learn from it? Well, very little. Because there are a million things changed during the last 7 days. Some are intentional, some are unintentional. It's easy to make a guess, but it's hard to pinpoint to the real reason. Third, this high latency led to a very loose reward cycle. When I eat a cake, I got rewarded immediately — it tastes good, it gives high calories so I get happy right away. But when I did something right to control the weight like rejecting a cake, I didn't see the reward (metric improvement) until seven days later. This not only makes it hard to iterate, but also hard to get motivated. 

Fortunately I found a solution, that is to find an approximate metric. It should be correlated with body weight, and also responsive, accurate, and thus gives a tight reward loop. The metric I found is the blood glucose level. Long story short, there is some sensor (prescription only though) that can measure the blood sugar level every five minutes, and log the data to the smart phone. The first day I wear it, I had quite some findings from simple visualization. First, as the attached figure shows, my body responds to different food differently. The red arrows are when I ate chips, rice and pasta, and the green arrow is when I drank Soylent. I also had similar observations when I ate salad. This immediately gives a feedback to eat "healthy food," and gives a way of near real time rewards. Second, it soon becomes obvious that work out decreases blood sugar level as well. So for the two biggest technical weapons on the road map, I get clear feedback of whether it's effective, and became much more motivated due to tighter feedback loop.

![A sample glucose curve](/images/glucose-curve.jpg)

So overall my learning is, responsiveness of a metric is really important. It impacts accuracy of the roadmap, agility of iterations, and probably more importantly, how motivated of the team. And that's why I think make our evaluation (offline eval and field validation) really lightweight is super important.