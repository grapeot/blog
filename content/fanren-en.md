Title: Forging a Knowledge Graph from a 10-Million-Character Epic with Three Dumb Methods
Date: 2025-06-07 9:00
Category: Computing
Tags: AI, English
Slug: fanren-en

## Introduction: It Begins with Forgetting

When reading an epic-length novel like *A Record of a Mortal's Journey to Immortality* or *A Song of Ice and Fire*, you've likely run into this problem: a character, say "Tihun," reappears, and the name feels familiar, but you can't recall when they first appeared, under what circumstances, or their current relationship with the protagonist.

This is a common phenomenon. Our brains are efficient at processing linear stories, but when faced with a system that is vast, complex, and dynamic over a long time span, we tend to lose information or make wrong connections (much like an LLM's hallucination). This isn't just a reader's problem. It exists in a more universal form in organizations like companies:

*   A new engineer wants to understand the evolution of a core module, only to find information scattered across Confluence pages, Slack threads, and personal emails from different eras.
*   A product manager trying to evaluate a new feature needs to know about all related historical attempts and their outcomes. This knowledge is often fragmented, living only in the memories of various team members, making it impossible to retrieve completely and objectively.

In both scenarios, the root problem is the same: we exist within a massive, dynamic, unstructured network of knowledge, but our perspective is inherently local and fragmented. We are limited by both breadth (we can't know all nodes simultaneously) and depth (it's hard to track all changes continuously and retain a complete history).

In the past, solving this relied on a few seasoned experts or massive manual effort in knowledge management. Today, AI offers a new possibility: can we outsource the high-load yet relatively low-difficulty cognitive tasks of memory and exploration to an automated, scalable AI system?

This led me to use the extremely complex case of *A Record of a Mortal's Journey to Immortality* as my experimental playground to explore a solution. Using an AI system engineering approach, I processed this ten-million-character magnum opus into a structured, interactively queryable knowledge graph, which you can browse [here](https://yage.ai/fanren/). The most valuable part of this project wasn't the final database, but the methodology developed during the exploration—a way to collaborate with modern AI to solve such complex cognitive tasks.

This methodology can be summarized by a somewhat counter-intuitive formula: Dumb Data + Dumb Methods + Dumb Models = Refined Knowledge. Let's dive into what these three dumb approaches are and why they are effective.

## Embracing Dumb Data: Building the Foundational Blocks for Knowledge Processing

When building an AI system, it's easy to fall into a kind of data purity obsession, expecting the AI to produce perfectly accurate results from the very first step. For instance, when extracting characters, we might hope it instantly recognizes that Mr. Li from Chapter 1 and Li Feiyu from Chapter 100 are the same person and provide a precise description. In a fragmented environment lacking global context, this is unrealistic. It's even a common failure pattern. Many people try to use AI for similar text comprehension tasks, find that it has all sorts of problems, and after a few attempts, conclude that AI isn't there yet and give up.

So my first principle is to embrace the inherent clumsiness of the initial data. The entire system was designed with the assumption that the data from the first pass would be of poor quality—full of duplicates, errors, and omissions. That's okay. It's like learning any complex skill; we can't get it perfect in one go. The key is to build a [self-correcting loop](/closed-loop-learning-en.html).

To this end, I first built two fundamental data access modules that could be repeatedly called by higher-level processes.

The first module is **Linear Scan**. In the system's cold-start phase, it acts like a diligent student with no memory, reading the entire text chapter by chapter with a single goal: to record every word that looks like a person's name or an item's name. This creates a vast and crude pool of candidate entities. This step doesn't aim for quality but for high recall. This is our most primitive, "dumbest" data, and the raw material for all subsequent work.

The second module is **Semantic Search**. With this raw data, this module provides a much more powerful way to access information. It uses embeddings to transform the entire novel into a vector space where semantic distance can be calculated. When I need to investigate an entity like "Mr. Li," the system can instantly retrieve all semantically related paragraphs from the entire text, even if those paragraphs only mention the name "Li Feiyu." This process breaks down the physical barriers of chapters, allowing us to validate and improve the initial dumb data with global context.

Together, these two modules form the data access layer of my entire system. They are low-level tools that don't directly produce the final knowledge but provide the foundational services for all the complex workflows on top. Accepting imperfection at the start and using a scan-then-retrieve mechanism to gradually refine it is the basis for getting the entire knowledge extraction process off the ground.

## Accepting Dumb Methods: Achieving Small but Steady Progress with a Knowledge Flywheel

With the basic tools for data processing in hand, the next question is: how to systematically improve the accuracy of the knowledge? For example, how do we generate a comprehensive and accurate biography for the Palm Sky Bottle, an artifact that appears throughout the book?

There are two ways to think about this. An intuitive approach is to design a perfect prompt that allows an LLM to read all relevant passages at once and produce the final answer, finding the perfect solution in one step. When the LLM fails to do so, we get frustrated.

The other approach, my choice, is to accept the "dumbness" of the method and trust in the power of iteration. I designed a three-step iterative loop, which I call the **Knowledge Flywheel**. This loop can be executed repeatedly, with each turn making the knowledge a little more refined. The core idea of this flywheel is to break down a massive problem into countless tiny, verifiable sub-problems, and then design an automated process that can continuously solve them.

Let's use a concrete example to illustrate how this flywheel operates. Suppose our initial "dumb" data pool contains both Li Feiyu and Mr. Li as separate entities. Each has an incomplete set of information generated through preliminary aggregation. One cycle of the flywheel goes like this:

1.  **Trigger.** The system initiates an information refinement task targeting Mr. Li. This can be triggered by an exhaustive iteration over all characters or by a user.
2.  **Invoke Foundational Modules.** The system calls the semantic search module mentioned in the first section, feeding it Mr. Li and its known context. The search results will likely return high-scoring passages containing "Li Feiyu." The system then submits the information snippets for both Mr. Li and Li Feiyu, along with the relevant original context, to an LLM for judgment.
3.  **Make a Tiny Advance.** Based on this information, the LLM determines that these two entities very likely refer to the same person. This is a very small, atomic piece of new knowledge.
4.  **Refine.** The system executes an update based on this new knowledge. It aggregates the information previously belonging to the two separate entities and modifies the knowledge base, marking "Senior Brother Li" as an alias for "Li Feiyu" or merging them into a single entity.

This process looks incredibly clumsy. We might have made several calls to retrieval and the LLM just to merge two aliases of a single character. A character might have seven or eight aliases, and there are thousands of characters in the novel. This means the flywheel needs to turn tirelessly for thousands, even hundreds of thousands of times. But the advantage of this dumb method is its stability and convergence. Each cycle is a logically clear, independent process with a very high success rate.

More importantly, every successful merge means a definitive improvement in the overall quality of the knowledge base. Even if each step forward is minuscule, through large-scale, automated cycles, these small advances accumulate into a massive qualitative transformation. Furthermore, this process is self-enhancing. Once Mr. Li and Li Feiyu are merged, future semantic searches seeded with this more complete, unified entity will find more comprehensive and accurate information, making the next turn of the flywheel even more effective.

The core of this dumb method is to systematically manage and accumulate countless tiny improvements using an automated process. It doesn't rely on a single flash of brilliance from one call but trusts in the power of iteration itself. Given the current capabilities and cost structure of AI, this provides a more robust and controllable engineering path toward refined knowledge.

## Choosing a Dumb Model: From Cost Anxiety to Creative Freedom

The ability to implement this heavy, iterative framework depends crucially on the choice of its power source. Here, I propose the third and most audacious principle: choose an open-source model that is "dumber" in terms of general capabilities. I ended up deploying a Qwen3-32B locally. This is a distilled model with 32 billion parameters. By any general capability benchmark, its overall performance cannot compare to top-tier, trillion-parameter-scale closed-source models like Gemini 2.5.

But it was precisely this choice that ultimately liberated the project's potential. The reason lies not in the model's capabilities itself, but in how it changed my workflow and mindset. This becomes clear when I recall my initial attempts using closed-source APIs. When I used them, I found myself shackled by two constraints:

The first was **cost anxiety**. The pay-per-token model meant that every API call was consuming a real budget. This created constant psychological pressure. I didn't dare to try computationally expensive dumb methods, like having the model perform pairwise comparisons of several thousand entities. I would spend a great deal of time optimizing prompts, trying to achieve the goal with the fewest calls and the least token consumption. This mindset kept me torn between optimal results and minimal cost, severely limiting my freedom to explore.

The second was **rhythm disruption**. To save money, I tended to use batch requests, which offered a 50% discount. But the response time for such requests was typically measured in hours. My workflow became fragmented: propose an idea, submit a batch of tasks, and then endure a long wait. This "submit-wait" pattern completely broke the fluid "think-test-adjust" rhythm. Many sparks of inspiration and impulses for improvement were extinguished during these long waits.

In its early stages, while using closed-source APIs, the project progressed slowly and was full of compromises under the dual burden of cost anxiety and rhythm disruption. And because the novel is so long, the first version still cost me over two hundred dollars. Seeing the bill, I was crushed, which is why I switched to deploying Qwen3-32B on local hardware.

This wasn't my first attempt at such a switch. In the past, I had tried to replace closed-source models with open-source ones many times, but almost every attempt ended in failure. There were two main reasons for this: first, the models themselves were not intelligent enough; often, just getting them to reliably output valid JSON format required a great deal of effort in prompt engineering. Second, local inference was too inefficient; running on consumer hardware like a Macbook was impractically slow. But this time, I found that the two key prerequisites for success have recently matured.

The first prerequisite is a **qualitative leap in model capability**. The Qwen3-32B I chose has significantly improved intelligence and instruction-following abilities compared to the open-source models I had used before. For my tasks, it could very reliably generate the JSON format I needed without special prompt tuning or a forced JSON output mode, which greatly reduced development and integration complexity.

The second prerequisite is the **maturity of the inference platform ecosystem**. I recently upgraded my hardware to a 5090 cluster, and inference frameworks like vLLM have kept up with support for new hardware. Using INT4 quantization, I could run an inference instance of a 32B model with a 128k context window on just two 5090 GPUs. In high-concurrency scenarios, I observed prompt processing throughputs of up to 3,000-4,000 tokens per second, and generation throughputs of 200-300 tokens per second (not simultaneously). This speed has made local inference a practical and highly efficient solution.

It was with these two prerequisites in place that my attempt to switch to local deployment finally succeeded. This transition brought not just a change in cost structure, but a paradigm shift in development. I could completely control this relatively dumb model. After a one-time hardware investment, the marginal cost of each call became nearly zero. This meant I had acquired a nearly infinite, free ability to make calls. The dumb method that required hundreds of thousands of cycles went from being an impractical, costly fantasy to a background task that could be started at any time and run all day.

Cost anxiety vanished, and the shackles of rhythm were broken. I could instantly validate every idea and iterate fluidly. I could boldly let the model perform the most arduous, mechanical cognitive enumeration tasks, while I focused my entire energy on designing and optimizing the knowledge flywheel system itself. Ultimately, this dumb model allowed me to truly master it, rather than be constrained by its cost and latency.

## Conclusion

Structuring a grand narrative like *A Record of a Mortal's Journey to Immortality* was an exploration of how to apply AI to process complex, massive unstructured information. This process has led me to believe that we are gradually moving from an era of "prompt magic" to an era of AI systems engineering that requires systematic thinking, an embrace of iteration, and skillful use of tools.

This knowledge flywheel, driven by dumb methods, actually plays the role we initially envisioned: an automated, scalable external memory system. It tirelessly performs the high-load yet relatively low-difficulty cognitive tasks of memory and exploration, upgrading an individual prone to forgetting and confusion into an enhanced reader with near-perfect memory and powerful exploratory capabilities.

Returning to the corporate knowledge management dilemma we mentioned at the beginning, this methodology also offers a viable path. It can automatically connect and integrate unstructured information scattered across Confluence, Slack, emails, and other corners, ultimately building a queryable collective brain for the organization. It allows submerged, fragmented knowledge to surface and connect, reducing the cost and friction of information retrieval within the organization.

In the end, the keys to this project's success all seemed to point to those counter-intuitive dumb methods: accepting imperfect dumb data, designing iterable dumb methods, and choosing a dumb model that is performant enough yet fully controllable. This perhaps suggests that in our future collaboration with AI, our core value as developers will lie more in how we design intelligent systems to harness these powerful tools, rather than merely pursuing super-intelligence in the tools themselves.