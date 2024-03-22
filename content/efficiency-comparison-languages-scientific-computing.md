Title: Efficiency comparison among several platforms for scientific computing
Category: Computing
Tags: PhD, Research, Parallel, English
Date: 2012-12-03 22:45

[Update2] I used the library [eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page) to reimplement the algorithm, reducing the code from 84 lines to 41 lines (wow), and time increases 11%. Looks acceptable, with similar workload as unoptimized C#, but the same speed as heavily optimized C# (with 164 lines of code and unsafe compilation). What's even better is eigen is a header library requires no pre-building or linking. 

Looked at Boost for a while yesterday and also found similar usage of lambda expression and smart pointers as in C#. Considering C++ as an option for the future seriously... 

[Update] I further optimized the C# code and made its speed from 204ms to 124ms. The same trick made C++ implementation from 124ms to 105ms. This makes me prefer C# more. The code is also updated on github.

Please consult the [prezi slides](http://prezi.com/6wpbvnq56ddn/efficiency-comparison-of-scientific-computing-among-different-languages/). Basically the conclusions are:

 * MATLAB sort of astonishes me. I guessed it should be the fastest with the sophisticatedly optimized matrix library.
 * For loops turn to be "speed killer" in MATLAB and Python. On the contrary, C family languages are able to optimize such loops well.
 * It's also a bit surprising to see C# only costs twice the time as C++. But only limited to tedious imperative style without using any libraries.
 * Functional style (map for Python, arrayfun for MATLAB, LINQ for C#) and imperative style (for for all the three languages) make no difference for MATLAB, but C# prefers imperative style, while Python favors functional style.
 * I'd use C# for its flexibility from dev speed to running speed.

Code is available on [github](https://github.com/grapeot/EfficiencyComparison).

<div>
<object id="prezi_6wpbvnq56ddn" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="550" height="400" name="prezi_6wpbvnq56ddn" >
<param name="movie" value="http://prezi.com/bin/preziloader.swf">
<param name="allowfullscreen" value="true">
<param name="allowFullScreenInteractive" value="true">
<param name="allowscriptaccess" value="always">
<param name="wmode" value="direct">
<param name="bgcolor" value="#ffffff">
<param name="flashvars" value="prezi_id=6wpbvnq56ddn&amp;lock_to_path=0&amp;color=ffffff&amp;autoplay=no&amp;autohide_ctrls=0"><embed id="preziEmbed_6wpbvnq56ddn" type="application/x-shockwave-flash" width="550" height="400" src="http://prezi.com/bin/preziloader.swf" name="preziEmbed_6wpbvnq56ddn" allowfullscreen="true" allowfullscreeninteractive="true" allowscriptaccess="always" bgcolor="#ffffff" flashvars="prezi_id=6wpbvnq56ddn&amp;lock_to_path=0&amp;color=ffffff&amp;autoplay=no&amp;autohide_ctrls=0" style="width: 550px; height: 400px;">
</object>
</div>
