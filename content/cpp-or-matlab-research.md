Title: C++ or MATLAB for research?
Date: 2013-05-29 21:03
Category: Computing
Tags: C++, MATLAB, Research, English

I used to be (and still am) a big fan of C#/C++, and wrote all the research codes in these languages. But after reading [this post](http://stackoverflow.com/questions/8828860/why-is-matlab-so-popular-in-the-computer-vision-community-even-with-opencv-being/8832028#8832028) by [Olivier Duchenne](http://www.di.ens.fr/~duchenne/) discussing about MATLAB's advantages, my view is changing and think MATLAB may be a better candidate for research...

### Why did I like C#/C++ for research?

* High efficiency, much faster than MATLAB (10x~20x empirically).
* Also not hard to write code with neat grammar, e.g. stream operation, and lambda expressions. OpenCV also supports imread/imshow and lots of matrix operations.
* Flexibility and convenience to transfer to a real working system, with mature industry-level support, such as networking, database, parallel, regular expression, and GPU.
* Looks cool lol

### And why may MATLAB be more suitable for research?

Research is different in building a system in that we don't know whether the algorithm will work beforehand. Therefore there will be a lot of trial and error involved. Prototyping, instead of building industry-level systems, is the daily work of researchers.

Therefore MATLAB is suitable for

* Super fast prototyping. The program may be slow, but it works.
* (May be repeating the first point) Lots of high-level functions
* Less possible bugs (e.g. type casting) and easier debugging with less code and simpler language

And if we agree that research is mainly about prototyping in the shortest time, the advantages of C#/C++ don't really matter here.

### So any take-away messages?

Yes.

* No silver bullet. Analyze the need and pick up the right tool.
* Research is about prototyping so choose the tools for fast development and verification. Transfer to other platforms if really reaching the production/demo stage (which, to be honest, is pretty rare in research field)
