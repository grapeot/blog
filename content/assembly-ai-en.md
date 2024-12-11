Title: Comparison of AssemblyAI and OpenAI Whisper API
Date: 2024-09-02 12:44
Category: Computing
Tags: AI, Speech Recognition, AssemblyAI, OpenAI, English

Previously, we made [many attempts](/GPT-API-usage-creation.html) using AI voice recognition and AI to aid in expression and input. After more than a year, on one hand, I find this tool particularly useful as it greatly expands the depth of my thinking and saves me time from correcting typos. On the other hand, the entire system has undergone many changes, such as the backend AI switching from [GPT-4](/GPT-scared-me.html) to Claude 3.5.

Recently, another issue has become increasingly serious: the voice recognition engine I use, OpenAI's Whisper API, has become increasingly unstable, often showing timeouts that require retries. To solve this problem, I tried hosting an open-source Whisper model locally, but it was much slower than OpenAI's; they have indeed optimized a lot in terms of infrastructure.

To solve this problem, I started exploring whether other companies' voice recognition APIs could be used. After searching for a while, I discovered a company called AssemblyAI. This company is quite interesting. Unlike other companies like TurboScribe, which are just rebranded Whisper APIs, this company genuinely has its own model development capabilities and has published its own papers and white papers. So I spent some time integrating AssemblyAI into my system and did some comparisons with OpenAI's Whisper API. Some observations:

1. In terms of speed, OpenAI is still faster. For example, recognizing a 3-minute 15-second file, OpenAI took only 9.8 seconds to return the result, while AssemblyAI took 10.6 seconds using the Nano model and 19.8 seconds using the Best model, roughly double the time of OpenAI.
2. However, AssemblyAI is indeed more accurate, especially when using the Best model. For some coffee roasting terms, it can express them very accurately, allowing me to use them directly without any modifications, which is very impressive. But the Nano model does not achieve this effect and is still not as good as OpenAI's.
3. From the perspective of stability, there is no data yet. I am just dissatisfied with OpenAI frequently experiencing outages or needing retries, but I don't know if AssemblyAI will have the same issues.

So from a performance perspective, OpenAI's API still seems better. AssemblyAI uses twice the processing time for slightly higher recognition accuracy, and I'm not sure if it's worth it for my use case. For now, I'll use Assembly's API for some long-term testing.

In terms of functionality, AssemblyAI offers quite a few enticing features:

1. It has a Synchronous Mode similar to OpenAI's Batch Mode, but OpenAI's Batch Mode is only effective for LLM, not for voice recognition.
2. AssemblyAI supports files up to 5GB, which is particularly friendly for recognizing large files like movies and YouTube videos. OpenAI performs poorly in this regard, with no Synchronous Mode and very strict file size limits. Furthermore, I even think this is not necessarily a model limit, but rather a lack of communication between frontend engineers and the backend. When you upload a large file, the error given by OpenAI is not even an API error but an Nginx error saying "Entity too Large," which is quite amusing.
3. AssemblyAI also offers Streaming recognition, allowing users to speak into the microphone for recognition, which OpenAI does not have.
4. AssemblyAI also has Speaker recognition functionality, similar to Zoom AI companion, which OpenAI does not have.

Overall, I think AssemblyAI seems to be a fairly reliable and easily integrable voice recognition API, and integrating it is particularly simple, making it a viable alternative to OpenAI.