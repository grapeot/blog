Title: No silver bullet in scientific computing
Date: 2011-05-10 02:19
Category: Computing
Tags: English, Research, Reflection
Slug: no-silver-bullet-in-scientific-computing

Is there a language/platform which can suit all the applications?
 
C#, my favorite language, with perfect editing/debugging environment and advanced ML libraries. But, the libraries are not optimized deliberately. In a competition with MATLAB to sort 0.5 billion numbers, MATLAB only needs 17s using 6 cores and 10G- memory, while the single-thread version of sorting function in .NET doesn't finish the work in 1 minute, and multi-thread LINQ cannot process this sorting task after exhausting all the 15G memory of my machine. Sometimes for computing intensive tasks, C# is not a good choice.
 
MATLAB is a popular language in research area. Its neat syntax and horribly powerful libraries/toolboxes make research development easy and efficient. And as mentioned before, the library is sophisticated optimized thus has good performance. But besides its uncomfortable editor, MATLAB has the drawback of low efficiency in several application scenarios, like programs with lots of loops or objects. Another disadvantage is, it lacks ability to control the computer in low level, thus cannot be easily integrated into web demo, Map Reduce, CUDA, etc. (OK, there is NE Builder and Jacket, but not that convenient, and much too expensive…)
 
There are some other options, python + PyNum + PySci, for example. But they all have this or that drawback and cannot become silver bullet solving all the problems easily. But wait… why we want to do all the work in one language, given we, researcher/PhD students from CS background, already know lots of languages? Why not practice like UNIX does, do one thing in one tool, then integrate small tools together to achieve a complex goal?
 
Actually this is fairy feasible. All the languages have mechanisms to invoke external programs. "system" in MATLAB, Process in C#, and os in python. Using files to communicate may also be a good idea. It's very simple to implement and not that slow as you think. According to my experiments, saving a 10000 * 10000 matrix in MATLAB into hard disk needs only 7 seconds (with -v6 switch to turn off compression), i.e. 14M elements/s or 114MB/s bandwidth. Data transfer in scenarios like [C# + CUDA](/efficiency-comparison-among-several-platforms-for-scientific-computing.html) may be even faster. A naïve implementation can achieve 6GB/s transfer rate between main memory and GPU memory. All the results indicate, data transfer is fairy cheap, therefore combining different tools to accomplish a complicated task may get both higher development and running efficiency.
 
No silver bullet in scientific computing. 1 + 1 may be more than 2. The art of UNIX programming is great. :D