---
Title: Things I Wish I Knew as a New Grad -- Suggestions on a Software Engineer's Career
Category: Life
Date: 2022-09-08 19:30
Tags: English, Career
Slug: new-employee-suggestions-en
Translation: new-employee-suggestions.html
---

[[中文版]](/new-employee-suggestions.html)

Recently some of my friends graduated from school and began their career as software engineers.
And they asked me for suggestions on an effective start in the industry.
I took this opportunity to think about my career, and summarized a few key learnings that I wish I knew as a new grad.
Back to that time, I was young, I was energetic, but didn't know which direction to go in the career, other than "doing what my manager told me to do."
And to make things worse, I didn't know I didn't know.
So I wasted quite some time and energy, only to learn some simple principles.
And this is what this post is about -- what is important and what is not important in a software engineer's career.
Note this topic is highly subjective.
Different people would have different answers to the question, and there is no wrong answer.
So take my words with a grain of salt.
And this post is very distilled and dense.
I plan to add more solid examples to make it easier to digest especially for new grads.
But at the current stage, let's begin from here.

The first question I'd like to discuss is, how important is "tech capability?"
Especially around junior devs, we often hear complaints like:
That senior engineer has no tech competency.
He wrote code slower than me, and couldn't reverse a linked list well.
How was he promoted?
This is actually a common pitfall: treating how well a dev codes as the golden standard to evaluate a dev's performance.
I put a quote around "tech" because it's a very broad and ambiguous word.
In this paragraph, by "tech," we mean the specific capability of writing code.
For example, one could solve leetcode fast and precise, bug-free, in one shot.
Or one knows about data structures and algorithms well, with depth and breadth.
For this kind of capability, my opinion is, it's not that important, for two reasons.
First, in the real world, it's rare to see complicated algorithm problems like on leetcode.
Most of the time, we just invoke libraries to do the heavy lifting.
Second, this kind of tech ability belongs to low-level execution if we think from a project's perspective.
And as we will discuss again later, its impact on the timeline is quite limited.
Recruiting someone that can do the job 100% fast and 200% fast, may make little difference on the timeline.
But making a mistake on the overall architecture that requires a total rebuild is very costly and may affect whether the project could succeed.
So the low-level execution is not that impactful if viewed from a big picture.

So, does that mean technical capabilities are not important?
It's not the case as well.
But the technical capabilities are much more than how well and fast one can code.
Here we need to introduce a concept of software engineering.
Due to the limit of classroom settings, the practice of software engineering is not well taught at school.
But it's the core of software development.
With decades' of evolution, despite a few exceptions, the complexity of modern software projects well exceed the limit of one single human.
A mediocre project would easily require a team of 3~5 people working for years to build and maintain.
And to make these big projects tractable, it demands a specialized knowledge system to guide us effectively collaborate across teams and across time.
This knowledge system is very complicated (as expected).
It's about software.
It's on building stuffs (engineering).
So it's named software engineering.
Nearly all performance review criteria in the industry are around software engineering.
Defining or even summarizing its scope is far beyond my ability.
But I want to name a few points that are often overlooked by junior devs:

* **Extensibility**: the ability to think about not only the present, but also the future when doing designs and coding.
  It's quite challenging to make accurate prediction on the future.
  It's not uncommon to see projects on the road map got dropped for various reasons, which means all the design around this project is rendered useless.
  Or a project that was not forseen got intaken to the plan, which requires a substantial change to the architecture.
  So how well a design could accommodate future changes could bring a large amount of benefits, or suffering.
  This is an example on the across-time dimension.
* **Ease of maintenance**: the ability to think about not only myself, but also others to maintain the project, when doing design and coding.
  If the code is put in front of the future me or others, will they be able to understand it easily?
  Any possibility to make it easier to understand from the framework level?
  Any pitfalls or error-prone places?
  Can we make it fool proof?
  Can we build better tests so we would feel comfortable even when another team come to change the code?
  This is an example on the across-team dimension, and also a deciding factor of whether a project could succeed or fail.
* **Redemption from repeated work**: an emphasis from software engineering is automation.
  Manual operations not only waste time, but more importantly could introduce mistakes.
  Computers could repeat the same task a thousand times without making a mistake.
  But humans cannot.
  So it becomes critical for a developer to bear sensitivity to repeated work and actively get rid of them using automation.
  It is again easier said than done.
  Among all the possible places to do automation, which one shall we put first, and which one second?
  Can we improve the efficiency of automation by building one system to power multiple scenarios?
  Can we bring in innovation to improve the workflow itself so it would be easier to automate?
  For example, if multiple clients come to say I need a faster horse or bull or ostrich, probably they actually wanted a car?
  This kind of work not only saves time, but also reduces human error.
  And this is the origin of infrastructure.
* Actually execution still occupies a fundamental position in software engineering, but not in the ability to write code fast, but the ability to **debug**. 
  It's not practical to expect a complex system works like a leetcode practice, we write the code, hit run, and it runs perfectly.
  When we face an unexpected output, how to debug is our daily work.
  Junior devs often take an approach of [random debugging](/seeking-help-effectively-through-human-oriented-prompt-engineering.html).
  They randomly come up a reason, and change something, expecting them to work.
  If not, another possible reason is tried.
  Sometimes they get lucky and solve the problem.
  But most times not.
  More senior devs would take a principled approach.
  They observe (e.g. read the log), and design experiments to probe the scope of the bug, until they deterministically find the issue.
  Think about random search and binary search, and it'll be easy to understand the dramatic difference in efficiency.

Unfortunately, the things we just discussed barely appear in the curriculum, probably because they are hard to evaluate through an exam or even a semester-long project.
And that's what motivated me to write this post, and even teach at university some day.
But all these skills can be learned in the daily work.
On one hand, we need to examine ourselves often, on the gap on these aspects.
On the other hand, we also need to actively observe others and learn from them, especially those we admire (or dislike), checking how they deal with those aspects.
A side note is, a lot of junior devs think system design interviews are very hard, with no clue on how to tell whether an answer is good or not.
The points above may provide a good outline to answer this question.

Of course, technical work is not 100% of a dev's daily work.
One couldn't advance much on the career ladder is his/her skill set is limited on the technical side.
The non-technical aspect is actually more complicated, with more variables and potential trade offs.
And my opinion on what qualities are important is:

* **Take initiative**: a big change from school life to company life is who drives the daily job.
At school, the students have a clear expectation on when to do what, with a clear schedule of taking classes, handing homework, and doing exams.
However, such kind of "doing what the manager told me to do" way is far from enough.
Probably the first sign of growing from a junior dev to a senior dev is to put thought on the projects.
Why did we put one month on this item?
Could we optimize the workflow?
If so, what shall we do? Do we need to initiative another project?
Who is the best person to do that? Is it myself? If not, how can I convince him/her and the manager?
No one prevents ourselves from lying down after finishing the job.
But putting the extra thoughts, and having the motivation and courage to taking the initiatives, is the first step of stepping up for more responsibility.
* **Making decisions**: regardless of technical or non-technical decisions, making high-quality decisions is critical in one's career.
One obvious example is to decide which university to apply, which would possibly affect one's entire life.
Which offer to accept, whether to do internal transfer, which strategy to use when proposing promotion to the manager, ... All of these involve decision making.
And it's needless to say how important it is.
The hardest part of making a decision is not to pick up a better one from option A and option B, but to realize there is a decision to make.
For example, it's rare to see someone talking about promotion during the first 1-1 with the manager.
But it's not because we all analyzed the pros and cons of talking about promotion, and then intentionally decided it's of our best interest not doing that.
Instead, for most of us, it's simply because we didn't know there is such an option of talking about promotion during the first 1-1.
If we think about it twice, it's actually not as a bad choice as it appears at the first glance.
By doing so, we could tell the manager we care about promotion, could learn about the procedures and criteria of promotion, and potentially kick off an improvement plan for the next level.
So this decision is not a no brainer as it seems, and may bring quite some impact if we realize there is a decision to make.
Of course, those "unknown unknowns" are hard to discover by ourselves, and that's why we need to have mentors/friends to remind us.
Another important thing about decision making is, when we face option A and B, the best choice is usually neither of them, but A+B or option C.
Thinking out of the box is also a good way of resolving a dilemma.
* **Communication**: as mentioned above, one core problem software engineering tries to solve is smooth cross-team collaboration.
This inevitably involves a lot of communication.
I don't want to talk about specific communication tricks such as how to present the idea precisely or how to make slides, but want to emphasize that the most important thing is, realizing there is such an option of communication.
For example, if you have a new idea but not sure whether it's useful or not, a good next step is to talk about it with others, including but not limited to the manager.
On one hand, this will bring inspiration.
For example, you may find this is a common need among three different teams, but it requires some tweaks to really meet all the needs.
On the other hand, this also helps build personal branding.
People are sensitive to perceive others' interests and talents.
And when they first think about you when they meet a technical challenge, you are now the domain expert, and now have your own impact and branding.
* **Deal with credits**: one nature concern of the example above is, what if others claimed my credit during the discussion? 
They may propose their own project based on my idea. 
Or my manager may assign the project to others.
And my answer is, it's a good thing.
If the idea is easy enough to be stolen by only a quick talk, probably it's not challenging enough to pursue.
And if others have the expertise to drive the project without you, probably it's a crowded area and not suitable for one's expertise area as well.
This kind of iterative "initial idea - communication - inspiration - execution" takes time, and it's common that your idea also inspires others.
Credits become more when one shares it with others.
So don't be afraid that others will benefit from your idea.
Instead, one should worry more if he/she couldn't find inspirations to benefit others.

So now we know what are treated important in the industry (in my opinion).
How can we grow in those aspects?
In addition to deliberate practices, probably the most important thing is to find mentorship.
A lot of things that may take long to learn from personal experiences, could be explained, shared, and learned in no time if someone tells you.
(It holds true the other way around though. 
There are also a lot of things that can only be learned by experiencing, instead of from others' words, or books.)
Here I mainly want to talk about how to get along with the manager, and how to find a mentor.

* **Manager**: the first principle working with the manager is, you two are on the same boat.
The primary responsibilities of one's manager are to make one happy and help her/him grow.
So she/he could deliver more and more along the time.
There shouldn't be much concern when talking with the manager.
For example, feel free to talk about what motivates us in the work.
No matter it's the excitement after solving a challenging technical problem, seeing the users benefit from the product, or the most direct promotion and higher salary, there is no wrong answer.
The key is we should figure it our by ourselves (a lot of people even don't know what they want) and let the manager know.
So the manager could make us happy more effectively.
Any plans, ambition, things that make us unhappy in the work, are all good topics.
Or even "how can I take advantage of you as a resource" is a good one as well.
Meanwhile, managers are humans too.
Some of them are doing their job well, and there are also managers that don't fit the position.
So if there are anything that flags room of improvement, discussing with the manager is a good first step, so you both could grow.
In the worst case, don't forget the last resort of transferring to another team.
This is an option too.
* **Mentor**: managers usually have a lot of managerial tasks such as meetings, docs, reports.
So it's not uncommon to see the manager is not the sharpest one in the team in the technical aspects (otherwise why would they hire you :))
So it's a good practice to find a mentor in the same or different team, to answer any technical questions, or things that are not ready to be discussed with the managers yet.
The most important thing on finding a mentor is probably giving him/her the desire to mentor you.
Asking insightful questions, talking about latest tech trends, no matter what it's about, make sure you did the homework and it's a good use of the mentor's time and expertise, instead of something that can be easily googled.
So this becomes a win-win sustainable relationship.
* **1-1 meetings**: another related topic is how to effectively have 1-1 meetings with either the manager or the mentor.
A lot of junior (or even senior) devs often get out of ideas of what to discuss in 1-1s, which usually end up as plain status updates.
This is actually very uneconomical.
Progress updates could easily be done through emails/docs/slack, and if the manager/mentor has questions, they could do simple follow up comments or adhoc meetings.
1-1s, on the other hand, is a rare opportunity that the manager/mentor could get to know YOU directly and personally.
So it should be treated seriously and planned accordingly -- not to impress the other side, but to expose you to them, so they could help you better.
Here are three examples of potential topics: the first is to talk about yourself.
What you want (roles, salary, projects, resources), why it's still not there yet, where is the gap, how to improve, any projects having grow opportunities for the gap.
The second is about the team.
Any happy/unhappy points about the procedures and policies, why this reorg and why that decision.
And the third could be about projects.
Instead of giving organic updates, a deep dive is more proper.
And by that I mean, focusing on the tech decisions that were made, and the rationale behind it.
Focus more on the "why"s instead of "what"s. 
This will be very helpful for the manager to promote this work to his/her manager.

Overall, it's not an easy task to finish the transition from a student to an engineer, especially considering the big gap between what the education provides and what the company needs.
Without a change on the mind set, it's very easy to view the picture using a "tech-first" perspective, and have confusions on how things work in a company.
But it will be much easier with a mind set of "this is a brand new world and I need to learn."
At the end of the day, they are nothing more than learnable skills.
In the end, I want to re-state that, I'm also an ordinary engineer like you will meet every day.
And I share these potentially immature thoughts just because I thought it might be useful for someone.
They could be wrong, could be misleading.
So comments are welcome so we can grow together.

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
