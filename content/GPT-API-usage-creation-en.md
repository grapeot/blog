Title: Improve Writing Efficiency Using GPT-4 and Whisper API
Category: Computing
Date: 2023-03-31 16:00
Tags: AI, Machine Learning, GPT
Slug: GPT-API-usage-creation-en

Recently, I have been dedicating more and more time to writing documents and articles. In this process, I gradually realized that the most significant factor limiting my writing speed is not the speed of my thoughts, but my typing speed, especially when completing relatively simple tasks. To solve this issue, one method is to practice typing to improve typing speed, while another possible approach is to use automatic speech recognition software for input. However, after trying speech recognition, I found several problems.

Firstly, the current speech recognition software, particularly those closely integrated with real-time communication such as WeChat's voice recognition and iPhone's Dictation, do not have high accuracy rates. Secondly, while typing, we can go back and make modifications halfway through the writing process, but with speech recognition software, it is impossible to return to previous parts for revision, which can disrupt the train of thought. Thirdly, the text input from speech recognition software is often quite colloquial and contains many filler words, requiring significant effort to reorganize and rewrite.

To address this issue, I conducted some experiments and eventually discovered a feasible method using the popular Chat GPT, specifically GPT-4. The general approach involves first using a speech recognition API (I used OpenAI's Whisper API in this case) to transcribe speech into text, and then utilizing GPT-4 to correct speech recognition errors and reorganize the text based on a complete reading. GPT-4 is highly suitable for this task as it is more intelligent and has significantly higher input token limits, increasing from 4000 tokens to 8000 tokens.

Based on this, I started building the software. First, I used GPT-4 to create a framework that includes both frontend and backend components. Then, I employed GitHub's Copilot to write code through extensive AI auto-completion. However, the coding efficiency was lower than expected, as GPT-4 generated code with many detailed errors that needed to be corrected and debugged one by one. Moreover, GPT-4 lacks the ability to assist in debugging, often generating inaccurate API interfaces or irrelevant debugging suggestions. Consequently, this part took some time, especially when accommodating the specific requirements of iPhone's audio encoding.

Eventually, with AI's assistance, I managed to develop a complete app within approximately one hour and deployed it on my website, making it open-source. For those interested, you can visit the website: [https://lab.yage.ai/notes/](https://lab.yage.ai/notes/), but please note that it is a demo site and may be unstable. Also, be aware that I can see all the text you input in the backend, even though I won't intentionally look at it. Please do not misuse it, as I am currently covering all API-related costs. The entire codebase is open-source, and if you are interested in deploying it on your own website, you can check the corresponding GitHub link [https://github.com/grapeot/VoiceNoteTaker](https://github.com/grapeot/VoiceNoteTaker).

In summary, by using GPT-4 and the Whisper API, I successfully built an application capable of correcting and reorganizing text transcribed from speech recognition. Despite some challenges encountered during development, with AI's help, I was able to complete the project in a short amount of time. The open-source code of this application can serve as a valuable reference for those interested, helping everyone write more efficiently.