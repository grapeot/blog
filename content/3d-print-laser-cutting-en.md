Title: 3D Printing and Laser Cutting: Challenges, Trends, and Market Barriers
Date: 2024-11-18 07:00
Category: Life
Tags: English, Hardware, Review
Slug: 3d-print-laser-cutting-en

Recently, a few investor friends were discussing 3D printing and laser engraving technologies, so I thought I'd write something to dive into these two fields, introducing their technologies and markets. I'm not a professional in either of these areas, so please take this with a grain of salt.

We'll first talk about the technical bottlenecks of 3D printing, possible applications, B2B companies, and explorations in the B2C space. Then we'll discuss the technical similarities and differences, bottlenecks, and popular technologies in laser engraving.

### Technical Bottlenecks of 3D Printing

Let's start by looking at 3D printing technology and where its limitations, or bottlenecks. If we're talking about printers like those from Bambu Labs that are based on extruder nozzles, this type of printer is called FDM (Fused Deposition Modeling). Its basic principle involves an extruder nozzle that melts plastic and extrudes it layer by layer. Since melted plastic is sticky, different layers adhere to each other, ultimately forming a three-dimensional printed object. This type of printer mainly has limitations in four areas:

**First** is the build volume, which we've [mentioned before](/3d-print-faq.html). Currently, the build volume of printers isn't particularly large. Generally, flagship printers on the market have a build volume of a 250mm cube. Larger printers exist, like those with half-meter or one-meter dimensions, but they usually fall into the category of specialized printers, which are particularly expensive and not necessarily reliable.

**Why don't manufacturers increase the build volume?**
It's partly due to market reasons and partly technical reasons. As the printed object gets larger, more problems arise. First, there's the issue of how well the print adheres to the build plate and maintains flatness. If this layer doesn't stick properly, you might encounter warping, detachment from the build plate, or layer shifting halfway through the print. Second, larger prints naturally require more time, and people might become impatient while waiting. Third, as the print size increases, the overall print chamber becomes larger, making it a challenge to maintain uniform temperature throughout the space to ensure print quality.

**Second** is the issue of supports. From the principle of 3D printing, as it extrudes molten plastic, there must be support underneath. If there's no support, it's like building in mid-air; it can't suspend in the air and will just droop. This is a significant limitation inherent in 3D printing—you must ensure that every layer you print has something underneath to support it. This greatly restricts the modeling capabilities.

For the simplest example, say you want to print a tree. It's challenging because there's empty space between the tree canopy and the ground; you can't print that layer in mid-air. So, to print something like a tree, you need to add an extra structure called support. It's a three-dimensional element manually added in, where you first print some relatively fragile structures between the ground and the trunk to support the upper layers. After printing, you manually remove them with pliers. This step is called support removal, and it's quite a hassle.

**Third**, the bottleneck lies in materials. The materials used in 3D printing still have significant gaps compared to traditional subtractive manufacturing methods like CNC machining. For example, they might not be heat-resistant, acid-resistant, corrosion-resistant, or anti-static; they can't self-extinguish when ignited and lack biocompatibility, meaning they can't be implanted into the human body. Especially for FDM printers, this poses considerable limitations.

**Fourth** is the low precision. This is mainly because the fundamental principle of FDM involves melting plastic to print. You can easily foresee an issue with thermal expansion and contraction. When it prints at 100.0mm, after cooling down, it might only be 99.5mm. This is particularly troublesome for parts requiring tight tolerances. Moreover, each machine is different, so even if you download a model from the internet, you'll need to test-print and adjust it for your specific machine before proceeding with the actual print.

Now, let's look at some application scenarios that investors might consider reasonable.

**Architectural models** are not very practical. On one hand, most architectural models, even the components, are often much larger than the build volume of 3D printers. If you need to split and reassemble them, it's quite cumbersome. On the other hand, many architectural models require very complex supports for aesthetic purposes, which is another time-consuming and labor-intensive task. It's often easier to use plaster directly.

**Second**, 3D printing diamond necklaces is even less feasible. 3D printers can only print plastic or transparent resin, and their optical properties clearly aren't like diamonds. Currently, diamonds are primarily produced through high-pressure synthesis.

**Third**, making jewelry samples. The jewelry industry does use 3D printing. If you're interested, you can look into something called the lost-wax casting method—there are some impressive videos on Youtube. However, the basic process involves first 3D printing a plastic piece, then casting it in plaster, and finally metal casting. The entire process is quite complicated. So using this for jewelry design isn't as straightforward as you might think.

**Fourth**, the medical field. This is mainly limited by materials. Traditional FDM cannot get FDA approval. For example, if you try to print a heart stent using extrusion, doctors would probably disapprove.

### What's Different About Bambu Labs?

After discussing the inherent limitations of 3D printing technology and its application constraints, many investors are curious about why Bambu Labs is so impressive. This brings us to why making a 3D printer is challenging. Actually, creating a slow-printing machine isn't too difficult. But as soon as you slightly increase the build volume and have certain requirements for print speed, problems start to emerge.

It's not simply a matter of using bigger motors or increasing voltage to make it run faster for quicker prints. If you try that, you'll find that the printed objects become distorted. What used to be straight lines at slower speeds turn into wavy patterns at higher speeds—the print quality declines.

It's similar to handwriting: when you write slowly, your handwriting can be neat and beautiful. But once you speed up, the handwriting naturally becomes messier as you lose precise control of your muscles. For 3D printing, when moving at high speeds, you'll find that you need to put more effort into managing the printing path during rapid movements. Issues that weren't apparent at slower speeds become interfering factors affecting print quality at high speeds. Therefore, additional compensation is needed to ensure that the actual printing path matches the intended one.

So, what's the connection with DJI? To achieve dynamic compensation for a mechanical component during high-speed movements—whether for leveling or trajectory—to meet a kinetic goal, the control theory and flight control algorithms involved are almost identical.
Some investor friends might not be familiar with flight control algorithms, so here's a simple explanation. When driving a car and pressing the accelerator, you're essentially controlling a component of the car (the throttle angle) to accelerate the engine.
In contrast, controlling a quadcopter drone is different. When you push the joystick to make it fly forward, there's no mechanical component that directly corresponds to the command "fly forward." From a fundamental perspective, the only things we can control are the speeds of the four motors. So how does the drone achieve forward flight? It relies mainly on flight control algorithms.

These algorithms do two things: first, they integrate information from various sensors, such as the drone's attitude, the effect of wind, current motor speeds, and so on. Second, they combine the user's desired goal—like transitioning from a hover to flying forward at 2 meters per second. By integrating these, the algorithm translates them into "how should I adjust the voltage to the four motors," thereby driving the drone's mechanical components to achieve the user's intended objective.

As you can see, the challenges presented by this problem setup and the potential technical framework are very similar to the dynamic compensation required in 3D printing during high-speed movements. DJI has years of accumulation and investment in this area. That's why, even though everyone knows the direction to move in, no one had been able to achieve it until someone who left the flight control giant entered this field and solved the problem.

### B2B Company: Formlabs

Next, let's look at the market aspect. Traditionally, 3D printers have had clients in the B2B sector. One particularly interesting company is Formlabs, a printer manufacturer based in Boston that primarily serves enterprise users. These companies use 3D printing for rapid prototyping in product development, and to some extent, replace small-batch production with 3D printing. In other words, it truly serves as a productivity tool. So how has Formlabs managed to address the four issues mentioned earlier? Let's examine them one by one.

Regarding **build volume**, they've mainly relied on other printing mechanisms. Their printers don't use FDM but instead use stereolithography, known as SLA. They also have printers using selective laser sintering, or SLS. Theoretically, these printing principles are harder to scale up compared to FDM, but Formlabs has made innovations on this basis (with some an increase in price though). We won't delve into the specific technical details for now, but they have achieved large build volumes, high speeds, and high precision.

The **second point** is **supports**, which they've also addressed through SLA and SLS. SLA printers are much more forgiving with supports compared to FDM; they can use much smaller supports to sustain larger models. SLS has a revolutionary feature in that it doesn't require any supports at all. If you're interested in the technical reasons, we can explore that in detail another time.

From the **materials** perspective, this is a highlight of the company. They have a strong chemistry team that has developed many industrial-grade materials. For instance, their printers can directly print dental prosthetics that can come into contact with the human body, can be implanted, and have FDA approval. Their materials can be ceramic, resistant to high temperatures of one or two thousand degrees Celsius, silicone, various anti-static, acid-resistant, and ultra-high-strength materials. They can even directly cast metal components from their printed parts—it's quite remarkable.

In terms of **precision**, they've used various innovations to address this effectively. I own one of their printers, and if you model something at 100.0 millimeters, it prints out at exactly 100.0 millimeters without any deviation, unlike FDM printers that require constant adjustments.

So, they've mainly compensated for the aforementioned four shortcomings through principle innovation and material improvements. However, relying on these alone doesn't make it a truly industrially valuable production tool. The reason is that 3D printing, especially photopolymerization printing, has a particularly cumbersome process. You need to pour in resin first, then it starts printing. After printing, you have to manually remove the printed part, clean it with alcohol, and then cure it under ultraviolet light—it's labor-intensive and time-consuming.

To solve this problem, they've developed an entire ecosystem. For example, they've created a continuous resin supply system, much like the continuous ink supply in printers, allowing several liters or even dozens of liters of resin to be continuously fed into the printer. It ensures appropriate temperatures, prevents overflow, and avoids running out of resin. They have a complete set of automatic part removal and cleaning kits called Form Auto, which is really cool. The entire process is controlled much like a robot. This approach allows for the formation of large-scale 3D printer farms without requiring much human intervention—everything is automated. Plus, it uses industrial-grade materials, precision, efficiency, and reliability.

This is what a 3D printing company aiming at the B2B market should look like.

### B2C Attempts and Market Challenges

Now, let's take a look at what a company would do if it wants to target the B2C market.

In fact, Bambu Labs has been making some efforts in this direction. Although, according to some research reports, it seems that Bambu Labs's biggest buyers are still those 3D printing farm operators who purchase Bambu Labs's machines in large quantities to provide batch printing services and sell them on platforms like Taobao. But besides that, Bambu Labs has also made many efforts aimed at ordinary consumers.

Think about it: as an ordinary consumer, what's the biggest hurdle when you want to use a 3D printer to make things? It's the inability to do 3D modeling. So if we can find a way—for example, by building a community where people can share the models they've created, perhaps even charge a fee and make a profit—that would greatly enhance the activity level of the entire field. Maybe, as an average consumer, even if I can't do modeling myself, I can directly download one from the community, pay a small fee, and then slightly tweak it according to my own needs and print it out. This is their wishful thinking.

But after I tried it, I found that the results weren't very good, mainly for the following reasons.

First, 3D printers are still quite difficult to handle. Especially with materials that are not so easy to print, like TPU or PETG, even just getting a model to print correctly isn't that simple. You need to learn some things; the failure rate is high, and it's not very friendly to novices.

Second, as we mentioned earlier, accuracy is an issue.
On the one hand, this means that the printed figures or collectibles look quite ugly, with many layer lines on the surface.
On the other hand, it also means that if you want to print a part to fit with something you already have, you need to adjust it several times; you can't expect it to succeed in one go.

Third is the lack of demand. There are only a few types of things suitable for printing. The most outrageous thing I've printed is a pair of slippers. Most others are small decorative items for daily life, like jack-o'-lanterns.
At first, it's a bit novel, but after printing a few times, you realize it's entirely a first-world problem, and then the printer just gathers dust.
I'm rather pessimistic about this. Even as someone who enjoys DIY, I don't use my printer very often. I can hardly imagine why an average person would need to use their printer once or twice a month.

### Laser Cutting

Having talked about 3D printing for a while, let's now look at laser cutting.

Overall, from a technical standpoint, laser cutting or engraving is fundamentally different from 3D printing. But if we look at a higher level, in a more abstract sense, there are many similarities between the two.

From a technical perspective, laser cutting and engraving belong to **subtractive manufacturing** and are in the same category as CNC or numerically controlled machine tools. 3D printing is **additive manufacturing**.
Subtractive manufacturing means you start with a large piece of material and then drill, hollow out, and carve it to shape it into what you want.

Additive manufacturing means you start with nothing and gradually, like doing addition, build the object up bit by bit.
So you can see that there is a fundamental difference between it and 3D printing. Why emphasize this difference?
Because the manufacturing method determines the types of things you can make and the difficulty involved.
For example, if you want to hollow out a hole in the middle of a completely enclosed object, CNC cannot do it.
But 3D printing can achieve this.
Conversely, if you want to create a structure that suddenly extends out in mid-air without support at the bottom, CNC can easily do it—just remove the material below—but 3D printing cannot.
Similarly, some things can be made by both additive and subtractive methods, but with varying degrees of difficulty. For instance, if a workpiece has a screw hole on the side, 3D printing basically can't produce it, but for CNC, it's just a matter of drilling a hole.
So, due to this fundamental difference, laser cutting and 3D printing are suitable for different scenarios and target markets from a manufacturing perspective. We'll discuss this in more detail later.

But from a more abstract perspective, you've also noticed that laser cutters and 3D printers actually look quite similar. This involves another basic concept in the manufacturing field, which is the concept of **axes**.

If you look at machines like the **xTool**, which has two belts moving the laser head back and forth on a plane, this structure is called a **CoreXY** configuration.
Its characteristic is that the X-axis and Y-axis each have a motor and a belt, and by controlling these two motors, you can move the laser head to any position on the plane, much like a printer.

And a 3D printer is basically adding a Z-axis on top of that.
Of course, laser engravers also have a Z-axis, but this Z-axis is only used for focusing and doesn't move during the manufacturing process.
This mechanical structure called the CoreXY configuration is used in many low-end CNC machines, 3D printers, and laser cutters.
It's precisely this shared mechanical structure that makes all three look quite similar.

Returning to the topic of axes, in a CoreXY structure like this, you can see it has two degrees of freedom—the X-axis and the Y-axis. This is called **two-axis manufacturing**.
That is to say, it can only print or cut things on a plane. This is a manufacturing method with significant limitations.
If we add a Z-axis on this basis, it becomes **2.5D**. A 3D printer is a typical example of a 2.5D device.
Why is it called 2.5D instead of 3D?
The reason is that it has a significant limitation: its Z-axis is always vertically downward.
This means that, for example, if you want to print a sphere, you can't ensure that the printing head's normal vector always aligns with the shape you're printing.
It can only apply the material from a rather awkward angle. This is why when 3D printing a sphere, near the top, layer lines tend to appear.

On this basis, if we add a rotating mechanism that allows the workpiece to rotate, we introduce a **fourth axis**.
This is called **four-axis**, or sometimes **three-plus-one axis**, because the standalone rotational axis still has significant limitations.
For example, xTool's engravers can switch to an accessory for engraving cups. It has a mechanical clamp that holds the cup and rotates it, allowing the laser head to engrave on it. This is a typical "three-plus-one axis" setup.

If we add another axis, allowing the cup not only to rotate along its axis but also to rotate in other directions, it becomes **three-plus-two axes**, or **five-axis**.
This is very common in CNC machines. Currently, there are some attempts to introduce this into 3D printing, but it's still not very common in laser engraving.
The advantages are:
First, it can ensure that the cutting head or printing head is always aligned with the normal vector at any given time, eliminating the appearance of layer lines. Of course, this assumes there are no obstructions between the tool head and the workpiece.
Second, it can often eliminate the need for supports, which is particularly enticing for 3D printing.
But the algorithms involved are much more complex. In the CNC field, how to perform five-axis programming is a vast industrial market. Similar hobbyist-level software on the market also costs several thousand dollars a year.

### Technical Challenges of Laser Engraving/Cutting

After understanding the basic technical aspects, let's examine the similarities and differences between laser engraving and 3D printing. Previously, we discussed the challenges faced by 3D printing, such as high-speed printing and handling different materials. However, these issues are not problems for laser engraving.

The reason is that hobbyist-level laser cutters are unlikely to use industrial-grade kilowatt-level CO₂ lasers. They typically employ lasers with relatively low power, which means it takes longer to ablate materials. Therefore, their bottleneck often isn't whether the print head can move quickly and precisely (with some exceptions we'll discuss later). Since you have to wait for the laser to slowly burn through material anyway, high-speed control isn't a critical issue for them.

Similarly, they don't require material handling. For example, 3D printers need to handle different melting temperatures for various plastics, require moisture-proofing, need to maintain appropriate chamber temperatures, ensure bed leveling, and so on. None of these are necessary for lasers. Even Z-axis precision isn't particularly crucial for them. A slight deviation in the Z-axis can lead to serious problems like warping or first-layer detachment in 3D printing, directly causing print failures. But for laser engraving, it might just slightly enlarge the laser spot, slowing down the ablation speed—a non-fatal issue.

Therefore, from a technical difficulty standpoint, the competitive advantages of 3D printer manufacturers can't be directly transferred to the laser engraving field. However, that doesn't mean laser engraving is simple; it has its own unique challenges.

**First is the light source.**
The main issue here is that different materials respond differently to various wavelengths of light. For instance, the most affordable blue-violet lasers around 435 nm have particularly high absorption rates for materials like wood, making them ideal for engraving and cutting wood and plywood. But when it comes to metals, their reflectivity is exceptionally high. So, you'd either have to increase the laser's power substantially or use lasers with different wavelengths, such as infrared lasers at 1064 nm. This is why laser engravers on the market are often tailored either for metals—especially stainless steel—or for other materials like stone, acrylic, and wood. Of course, some of the latest models have introduced dual light sources, which we'll discuss later.

**The second challenge** is that if you've actually used a laser cutter, you'll find that while it seems straightforward, there are many pitfalls in practice. One example is when you try to cut wood; it produces smoke, and quite a lot of it. This smoke poses two problems. First, if you don't extract it, it accumulates inside the chamber, obstructing the laser and causing its power to drop sharply, leading to job failure. Second, if you do extract it, doing so indoors might trigger fire alarms, and venting it outdoors requires long ventilation ducts and powerful fans—a complex setup. Therefore, designing such a workflow is also a challenge for laser engravers, especially if they aim to transition from B2B to B2C markets; this is an issue that must be addressed.

### Technological Trends and Market Challenges

Beyond these, there are three factors that various manufacturers are currently competing over.

**First is engraving speed.** Note that this speed refers to engraving speed, not cutting speed. This is because there's a niche market within laser engraving—such as engraving on leather or wood for souvenirs or corporate customization. It doesn't require the laser to cut through materials bit by bit but merely to leave a mark on the surface. In this case, speed becomes a very important indicator.

**How do laser cutting/engraving manufacturers address this?** They use a different technology, moving away from the traditional Core XY mechanism to control the laser spot's movement with two mirrors. Controlling mirror deflection is much faster than moving a mechanical head around, enabling a breakthrough in speed by orders of magnitude. This type of laser is called a **galvanometer laser**.

However, it has its own drawbacks. First, its power is often limited to relatively low levels. Second, its working area isn't very large. Third, at the edges of the working area, the laser's incident angle is no longer perpendicular to the object's surface, which can lead to reduced power or incorrect cutting direction when cutting. Therefore, while galvanometer lasers have their advantages and disadvantages, they haven't dominated the market and currently survive in a very niche engraving segment.

**The second trend** is adding **color** to the engraving. This is quite interesting because, in subtractive manufacturing, people generally don't expect colors. The main principle here is that if you use a laser of a specific wavelength on certain metals, it forms an oxide layer during ablation. When the thickness of this oxide layer varies, it produces different interference effects with light, resulting in different colors. Some manufacturers have released experimental features based on this, but it hasn't been widely adopted due to its heavy dependence on specific material properties and the need for a lot of trial and error.

**The third trend** is focusing on **intelligence**. The traditional workflow for laser engraving is as follows: it uses a low-power laser to outline the position to be engraved; then you manually align the object to be engraved, match both sides, and press start. You can see this is highly inefficient, especially for B2B users who might need to engrave ten or twenty items at once, like small leather goods—aligning each one individually is too slow. So now, artificial intelligence is being incorporated to intelligently recognize the position of each workpiece and suggest optimal placement methods. This has become a selling point.

However, from a market perspective, laser engravers face the same challenge as 3D printers: they are currently mainly in the B2B market, and the B2C market remains untapped. Once we consider the B2B market, their competitors are entirely different. For example, in industrial production, there are kilowatt-level water-cooled CO₂ cutting machines. Why would I buy your toy-grade laser engraver that doesn't even have mature software support? If targeting B2C, they can only cater to Taobao shop owners customizing corporate souvenirs, but they can't reach the broader consumer base. As an ordinary consumer, what would I do engraving stones at home for no reason? Up to now, I still haven't seen a solution to this problem. Whether it's laser cutting, desktop CNC, or 3D printers, they all face the same issue: where exactly is their market?