Title: Collecting and Visualizing Mouse Position Distribution
Date: 2011-12-12 07:35
Category: Computing
Tags: English
Slug: collecting-and-visualizing-mouse-position-distribution

(This post is translated from my [blog post](http://www.cnblogs.com/grapeot/archive/2010/03/01/1675335.html) in Chinese)

What if collecting the mouse positions in one day, and plot it as a heat map? 
Following figure answers. 
Although it is only from about 3000 samples with 5 seconds per sample, it actually indicates something.

![Example reuslt 1](http://pic002.cnblogs.com/img/grapeot/201003/2010030101051237.jpg)

A highlight of this figure is the red zone in the right-upper corner.
This is obviously from the close button (I am using Windows).
Lots of operations are among the central area.
This is also easy to understand.
The other two interesting points are the column in the right boundary, and the row of the task bar in the bottom.

It's interesting that there is only one vertical column on the right rather than left.
This is not the scroll bar because I usually use the scroll wheel instead of dragging the scroll bar.
After some experiments, I found if you are holding the mouse with the right hand, it's fairly easy to reach the screen's right boundary, but reaching the left boundary requires some intentional efforts.
That causes the vertical bar only appearing on the right.
Interesting finding, but not sure whether the analysis is correct.

About the task bar, there is only one yellow hotspot.
After checking the windows, I found that's the task manager.
This hotspot reflects my habit of launching task manager once entering windows, and often checking its status.

See, data speaks.
I also invited some friends to take part in the test, and get their heat map. Seems the mouse position can be an effective feature for person identification.

![Example result 2](http://pic002.cnblogs.com/img/grapeot/201003/2010030122040267.jpg)
 
(This guy seems like the "show desktop" feature much)
  
![Example result 3](http://pic002.cnblogs.com/img/grapeot/201003/2010030122023947.jpg)

(This guy relies on the buttons to minimize/close windows, and use click menu frequently)

![Example result 4](http://pic002.cnblogs.com/img/grapeot/201003/2010030122025659.jpg)
   
(This looks like a user just finished DotA lol)

About the implementation stage, I am using C# + WinAPI + [PowerShell background task](/using-a-timer-to-do-time-management.html) to collect mouse positions timely.
And use a C# script with OpenCV/EmguCV to plot the heat map manually.
The source codes can be found in the [original post](http://www.cnblogs.com/grapeot/archive/2010/03/01/1675335.html).
It should be easy to extract the code although the original post is in Chinese.

To summary, collecting, visualizing, and interpreting data, these are an essential part of mine from data.
There are quite a lot fun data around us.
Even the most common one may inspire important findings.