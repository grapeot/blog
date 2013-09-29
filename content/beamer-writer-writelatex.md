Title: Update on Beamer Writer: Online Compiling with WriteLaTeX and Error Messages
Date: 2013-09-30 18:28
Category: Computing
Slug: update-on-beamer-writer-online-editing-with-writelatex
Tags: BeamerWriter

After moving the compiler implementation of our [Beamer Writer](http://lab.grapeot.me/beamer/) to node.js, we are able to provide more features than our old version (which used the client javascript).

* One of them is directly exporting (as well as compiling) the LaTeX code on [writelatex.com](http://writelatex.com/).
The usage is straightforward.
Like before, after writing the outline, click the `generate` button to get the LaTeX code in the output textbox.
If you wish to further edit/compile/collaborate with others online, click the `export to writelatex.com` button.
And Beamer Writer will redirect you to writelatex.com, a website provides cross-device real-time editing, compiling and collaboration services.
Of course, manual copy/paste to your favorite editor without involving cloud LaTeX services is always an option.
* The other useful feature is to add the compilation error massage.
In the old version, when an illegal outline is fed into the compilation engine, it will fail silently, forcing the users find the errors by ourselves.
And now for certain errors, we are able to identify its position and show the corresponding error message in the output box.

We hope beamer means a efficient and light-weight presentation tool for you. 
Enjoy.
