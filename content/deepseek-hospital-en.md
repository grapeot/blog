Title: From the All-Purpose Hospital to Smart Triage: Using a Hospital Analogy to Understand the Evolution of DeepSeek’s Models
Date: 2025-02-08 15:00
Category: Computing
Tags: AI, DeepSeek, English
Slug: deepseek-hospital-en

DeepSeek’s v3 model has sparked a lot of discussion recently. However, many people (myself included) may find themselves facing a sea of articles, unsure which are clickbait and which contain real substance. If you want to understand why DeepSeek is so impressive, which materials should you read? How can you confirm your understanding is correct? And how do you grasp the intuition behind these complex papers in a straightforward way?

With these questions in mind, I read the DeepSeek v2 and v3 papers. In this article, I’ll use the analogy of a hospital’s triage system to help non-technical LLM enthusiasts understand the intuition behind the papers.

Before we get into the details, let’s clarify a few points:

1.	This article focuses on DeepSeek v3, the model that achieves GPT-4o-like performance at a low cost. We will not discuss the R1 “reasoning” model here.
2.	This article is a popular science piece that uses analogies to illustrate the underlying technical intuition of the paper. Inevitably, analogies can lead to some oversimplification or distortion. I’ll do my best to strike a balance between clarity and accuracy. However, if you only need a rough understanding of DeepSeek’s technical ideas, this article should suffice. But if you want to replicate their results or carry out further innovation on this basis, you must study their papers carefully. The depth here is not enough to support rigorous scientific research and engineering practice.

## LLMs Are Like a Hospital

Let’s get to the main topic. In some ways, a Large Language Model (LLM) is like a huge hospital where patients enter through the main entrance, see a doctor, and then leave. The “patients” here are the input text, and the “discharged patients” are the model’s outputs. While the “patients” go from admission to discharge, they go through a series of procedures: tests, consultations, prescriptions, registration, and payment—analogous to the complex series of internal operations the model performs on the input.

Along the way, we typically look at three metrics:

1.	Intelligence level of the model: i.e., the quality of service it provides. Did it effectively “treat” or solve the user’s query or request?
2.	Throughput and latency: i.e., the time from when a “patient” enters to when they leave (average inference time), as well as how many patients the hospital can handle in a day.
3.	Model size: i.e., whether the hospital is a massive medical complex or a small, one-story clinic. This factor has a major impact on real-world deployment.

Traditional LLMs are like a hospital staffed by general practitioners, each of whom can handle all specialties. When a patient arrives, all the doctors go into action to treat that one patient. Once that patient is done, they all move on to the next. This is the so-called dense model. It has some advantages: it’s simpler to train, has lower memory usage, and a smaller overall model size. Since every doctor is a “jack of all trades,” their training can be standardized. Although training any given doctor may still be challenging, the process (procedure) is uniform, and you don’t have to spend extra effort tweaking the program for each specialty. Also, because each doctor can handle multiple roles, the total number of doctors (parameters) and the space (computational footprint) needed is reduced.

## Mixture of Experts

Another type of LLM architecture—beyond this traditional approach—is called a Mixture of Experts (MoE). It’s more like the hospitals we’re familiar with in real life: each doctor has a specialized field. They all receive some foundational medical training, then go on to specialize deeply in their chosen area. When patients arrive, a triage desk figures out which department they need—code debugging goes to “surgery for code,” mathematical proofs go to “logic internal medicine,” creative writing goes to the “literature & arts department,” and so on. Each expert can then focus on their niche instead of doing everything. This helps distribute training and inference workloads.

This design has pros and cons. A big upside is that when a single patient shows up, not all doctors need to drop what they’re doing to treat them. Instead, based on the patient’s condition, only the relevant department(s) is activated. For example, if a car accident victim arrives, you don’t need the oncology department to pitch in. This design saves resources and boosts throughput.

However, from another angle, it also makes the model’s internal structure more complicated. Each incoming patient (input text) must first go through an automated triage module (often called a router in LLMs) to decide which specialties (potentially multiple) to activate. Only the experts in those specialties participate in the diagnosis and treatment, which is exactly why it’s called a Mixture of Experts.

Because in an MoE setup only a subset of experts is activated for any given patient, achieving the same performance (the same medical service quality) as a dense model typically requires a larger overall model. You’re adding more capacity. However, since only part of the model is active during inference, speed and throughput remain on par with dense models—even though you have more parameters on standby.

One key difference between an MoE-based LLM and a real-world hospital is that in the LLM, the specific domain each expert focuses on is not predetermined. In a real hospital, orthopedics and ENT (ear, nose, and throat) are fixed specialties. But in an LLM, the domains are discovered dynamically during training. For instance, the algorithm might find that combining orthopedics and neurosurgery into a single “neuro-ortho” department yields better overall results, so it will spontaneously form that new department during training.

MoE and dense models represent different approaches with no absolute right or wrong. DeepSeek v2 and v3 both adopt an MoE-style strategy. Before we dive into these two models, let’s take a look at the main challenges in training an MoE-based LLM.

## Challenges of a Mixture of Experts

Compared to traditional LLMs, MoE training is much more complex. One major hurdle is that the interplay between each expert’s specialty and the triage module (router) can easily fall into a trap: some departments become overcrowded while others stand empty. For example, if one expert is good at both writing poetry and coding, many tasks (input tokens) might be assigned to that single expert, leaving the expert specializing in string theory nearly always idle. In such a scenario, the MoE effectively collapses back into a dense model, with massive load imbalance, resource waste, and bottlenecks. After all, we’ve built a giant hospital with many doctors and an enormous footprint, yet only one-tenth of the staff and equipment are in use. In fact, it might have been better to return to the simpler dense setup. Therefore, preventing load imbalance is a major area of research for MoE systems.

Another common issue is patient routing once the hospital is very large. When the hospital is just a single floor or a single building, going from one department to another isn’t too difficult. However, imagine a hospital complex with dozens—or hundreds—of separate buildings spread across multiple campuses. That’s like a very large model that cannot fit onto a single GPU or even a single machine, so it must be distributed across multiple nodes. Each node is like a different campus; inter-node communication is like a patient driving from one campus to another. Even within a single node, different GPUs might be analogous to different buildings in that campus, with less overhead for traveling between them but still some cost.

So, even if an expert doctor can diagnose quickly, if patients have to run around from campus to campus for checkups, prescriptions, and treatments, efficiency can be severely reduced by communication overhead. This is the second big challenge facing MoE systems. DeepSeek v2 and v3 address these issues with a series of innovative solutions.

## DeepSeek v2

DeepSeek v2 tackles these two core issues in MoE—the load imbalance problem and the communication overhead problem—through three main strategies, leading to significantly improved “diagnosis” efficiency.

1.	Medical Record Compression (Multi-head Latent Attention, MLA)

    They observed that the most time-consuming part for a doctor isn’t necessarily the diagnosis itself but having to read through all the old medical records (the historical tokens in the context) and then record the new diagnostic notes (updating the KV cache). For accuracy, medical records are typically very detailed. This large amount of reading and writing in the medical record significantly limits efficiency. DeepSeek v2 introduces a technique akin to shorthand or abbreviations, letting doctors use special symbols instead of writing out long-winded notes. This is realized through MLA, which compresses the KV cache. It greatly reduces memory usage and speeds up the entire consultation process.

2.	Department Subdivision and Shared Experts (DeepSeek MoE)

    The paper describes an MoE framework (based on earlier works) that splits large departments into smaller ones, so a patient might consult several mini-experts instead of just one big department. They also keep some shared experts for general tasks. This second-layer mixture of experts helps achieve greater specialization without compromising generalization, alleviating load imbalance by distributing tasks more effectively.

3.	Limiting Patient Travel Between Campuses (Device/Node Limited Routing)

    Conventional MoE often needs extensive all-to-all communication, where every input might interact with every expert across multiple devices or nodes. DeepSeek v2 introduced device-limited routing, and DeepSeek v3 extended this to node-limited routing. For example, if a hospital has over a hundred campuses, their design ensures most patients can be fully diagnosed and treated in just two or three of them, massively reducing the commute time (communication cost) and increasing overall efficiency.

## DeepSeek v3

DeepSeek v3 represents another major upgrade from v2, making improvements both algorithmically and from an engineering perspective.

Algorithmic Improvements

1.	Adaptive Load Balancing without Auxiliary Loss (Auxiliary-Loss-Free Load Balancing)

    In a traditional MoE, the triage desk (router) and each expert are trained jointly. That means if the triage module is misbalancing loads, it can inadvertently affect the experts’ medical training, and vice versa. Empirically, we see that forcing load balancing by adjusting experts’ core skills can degrade their specialization. DeepSeek v3 introduces a new routing optimization strategy so that when load imbalance arises, it only updates the triage algorithm, leaving expert training untouched. This decoupling reduces disruptions to each expert’s learning process and leads to better overall performance.

2.	Multi-Token Prediction (MTP)

    DeepSeek introduced an innovation allowing the model to predict multiple tokens at once. Traditional LLMs generate text one token at a time, whereas DeepSeek can generate and verify several tokens together during training, improving information utilization. In inference, it enables faster decoding (so-called speculative decoding). It’s like a doctor anticipating a likely diagnosis and getting medication ready in advance. If the lab results confirm the diagnosis, there’s no need for extra checkups—just send the patient to pick up the meds. If the test results invalidate it, you revert and correct the course. Over time, the model learns to improve the success rate of these “preparations,” boosting overall efficiency.

3.	8-bit Mixed-Precision Training (FP8)

    DeepSeek v3 widely uses 8-bit floating-point precision. It’s akin to using X-ray instead of more cumbersome CT or MRI scans whenever possible to cut down on unnecessary overhead. While there’s some risk of misdiagnosis due to lower precision, engineering optimizations keep this error within acceptable bounds, significantly speeding up training and inference.

Engineering Optimizations

1.	DualPipe

    This strategy cleverly staggers different training operations. It’s like running the registration, exam, prescription, and payment processes in parallel for different patients. While Patient A is undergoing exams, the doctor might be seeing Patient B, while Patient C pays and picks up medication. This concurrency drastically cuts down on idle time and boosts throughput.

2.	Intelligent Pharmacy Management

    They store frequently used “medicine” (weights and data) in GPU memory, and less frequently used resources on the CPU or in low-precision buffers. It’s like keeping common medications readily available in the hospital pharmacy, while rare medicines are in a central warehouse and fetched only when needed. This leads to more efficient use of limited resources.

## Conclusion

From an all-purpose hospital to specialized departments, and then on to smart triage + pipeline parallelism + avoiding over-treatment—this is how the DeepSeek team has iterated its LLM architecture. By continually optimizing the “hospital,” they maintain or even improve the quality of the model’s performance while mitigating communication and memory bottlenecks in large-scale deployments.

That said, let me reiterate: these analogies are just a way to help non-experts get a quick sense of what’s going on. The actual papers contain a lot of math, distributed systems theory, and engineering details. If you plan to replicate or innovate on their research, it’s essential to study the original publications in depth. And if you think any part of these analogies is misleading or incomplete, please feel free to comment. Let’s work together to explain the papers more accurately and accessibly.