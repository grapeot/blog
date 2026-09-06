---
Title: Exploring GPT-6 Astra's 3D Modeling: Exploded Views, Rigging, Motion Capture, and Video Generation
Date: 2026-09-05 21:00
Category: Computing
Tags: English, Agentic AI, DIY
Slug: gpt-6-astra-3d-modeling-en
Translation: gpt-6-astra-3d-modeling.html
Summary: Four 3D experiments with GPT-6 Astra: Hakurei Shrine exploded view, browser walkthrough, Psyduck rigging and MoCap, and video generation, plus an open-source skill.
---

Following the release of GPT-6 Astra, plenty of stunning demos started popping up online. Inspired by what I saw, I decided to run a few hands-on experiments to see what compelling use cases this new 3D modeling capability genuinely unlocks.

For my first experiment, I started with a relatively straightforward modeling task: recreating the Hakurei Shrine from Touhou Project in Blender. Here is the exact prompt I used. I dictated it via speech-to-text while sitting in a restaurant, so you will notice several transcription errors. Fortunately, modern AI parses the underlying intent without breaking a sweat:

```
嗯，我们去试试看哦，就是首先用 Blender 建一个伯利神社，就是东方project 里面的伯利明神社。你得先上网调研一下，它这个神社大概要长什么样，有哪些基本元素，然后你用 Blender 就把它建一下，然后渲渲出一个环视的动画
```

I did not provide any reference imagery—I simply asked the model to research the shrine online on its own. After roughly half an hour of autonomous work, it generated the model below. Keep in mind that this is a fully realized 3D asset; the image below is just a render from a single perspective.

![Hakurei Shrine render](/images/hakurei_shrine_rendered.jpg)

The output was genuinely impressive. While there are obvious geometric approximations—such as the noticeably low-poly trees—the overall aesthetic, layout, and atmosphere feel charming and faithful to the source material.

With the basic 3D model in place, what cool things could we build on top of it? I am a big fan of a YouTuber whose exploded-view videos are amazing, so I gave GPT a more detailed prompt to generate an exploded-view animation. The plan was to reveal the shrine's internal structural components first, assemble them step by step, and finally populate the diorama base with trees and rocks for a complete showcase. A few dozen minutes later, GPT delivered an excellent result. Here is the video:

<video src="/images/hakurei_assembly.mp4" controls width="100%"></video>

That success gave me a serious confidence boost. Given how capable AI has become at coding, my next step was to port the scene into the browser with first-person rendering and collision detection, letting visitors explore and walk through the space freely. The model executed the migration smoothly. An amusing detail along the way: while writing code, the model seemed almost impatient—it called out to Grok to write the code while handling visual verification itself. Whether that was an emergent quirk or deliberate training, the division of labor struck an effective balance between speed and quality. We deployed the result live; if you are interested, you can play with it [here](https://yage.ai/share/shrine/). It features three tabs: exploring the virtual scene in first-person, inspecting the entire diorama, and viewing the exploded assembly.

I also tested other categories of 3D modeling. Character modeling, in particular, still leaves plenty of room for improvement, as generated figures tend to stray considerably from the original designs. GPT clearly shines when working on architecture and environmental scenes. Characters are not impossible, but getting them right requires an exhausting amount of manual micro-management. Hopefully, future model iterations will address this gap.

With those initial tests completed, I wondered whether we could push this workflow into more demanding applications. That led to two further experiments. The first was real-time motion capture. Anyone familiar with modern live-streaming has likely run into VTubers—streamers who interact with their audience through digital avatars driven by motion capture instead of appearing on camera in person. It is a massive market backed by an intricate technical pipeline.

Typically, a streamer signs with an agency that commissions a custom 3D model, followed by rigging—embedding virtual bones and joints into the mesh so it can articulate naturally like a human body. Once rigged, motion capture algorithms take over: computer vision analyzes live video from the streamer's webcam, identifies skeletal joint positions, and retargets those movements onto the virtual avatar in real time.

Even without diving into technical minutiae, this workflow is inherently complex, with steep technical hurdles across every phase. Tasks are usually split across specialized roles—concept illustrators, 3D modelers, riggers, and MoCap engineers—before the studio delivers a finished package. To test whether AI could handle this entire chain end-to-end, I had it create a 3D model of Psyduck, rig its skeleton, and build a browser-based web app for real-time motion capture and rendering. Whenever I move in front of my webcam, the on-screen Psyduck mirrors my movements. If you want to try it out, you can test it [here](https://grapeot.github.io/psyduck-demo/). The model pulled off the entire workflow remarkably well. Here is a screen recording of the result:

<video src="/images/psyduck_mocap.mp4" controls width="100%"></video>

The quality turned out solid. Naturally, it lacks the hand-crafted polish of an experienced human team, but when you consider that delivery time and production costs dropped by one or two orders of magnitude, it is genuinely remarkable. With further refinements, the results could be even better.

The second scenario I explored was using 3D modeling to drive AI video generation—for instance, turning a sentence or two of prompt into a one- or two-minute educational clip for kids. For this test, I used the porcelain firing process as an example. I gave GPT a detailed prompt asking it to research how porcelain is fired, outline a storyboard, draft narration, and build the required 3D models.

The AI began with research and storyboard planning, then created the corresponding models in Blender and set up keyframes. These structured 3D intermediate assets ensured that physical interactions and visual forms remained coherent throughout the scene. On top of that foundation, it fed the renders into a fairly standard video generation model—I used Grok Imagine here without paying extra, since it's included with my existing SuperGrok subscription. A few hours later, it produced a complete educational video with sound effects and narration. Here is the result:

<video src="/images/ceramic_video.mp4" controls width="100%"></video>

Given how mature commercial AI video tools have become, this experimental pipeline cannot compete directly with commercial production suites. What makes it interesting, though, is how it charts a path combining grounded Blender modeling and rendering with generative AI video, achieving significantly better visual and physical consistency across shots.

Throughout this process, I was repeatedly blown away by GPT-6 Astra's 3D modeling prowess. In the past, whenever I experimented with OpenSCAD or Blender for programmatic modeling, the experience was filled with friction. With GPT-6 Astra, those same workflows came together quickly and smoothly. That does not mean blindly tossing prompts at the model will produce great results. The underlying methodology—especially structuring autonomous self-iteration loops and managing Blender-specific nuances—remains essential. I compiled these practical lessons and methodologies into a reusable Skill so anyone can reproduce similar outcomes. It is open-sourced on [GitHub](https://github.com/grapeot/gpt_3d_skill), and I hope you find it useful.
