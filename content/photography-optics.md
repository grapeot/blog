Title: Photography and optics
Category: Life
Tags: Photography, English
Date: 2017-08-08

I was learning about photography recently, especially beginning from optics. Surprisingly, some incomplete dots I learned before was connected in the processs.

First, I want to recommend a course here, named digital photography. The instructor is a professor from Stanford CS, and a principal engineer at Google. So it's more a technical course (instead of art). All the lecture notes and videos can be found [here]( https://sites.google.com/site/marclevoylectures/home).

The things getting connected are:

* _The subscription of glasses_. The number +1.00, -0.75 (called diopter) is 1 / focal length! For example, a glass with +1.00 diopter means its focal length is 1 meter. And the 50mm lens we commonly used, can be also treated as a glass with +20.00 diopter. @_@ Or a 500mm telephoto lens is actually a +2.00 reading glass. 
* _When the aperture increases (i.e. smaller f number is used)_, the depth of field gets shallower, and _the tolerance to the misfocus also decreases_. This is also why the measurement of vision is usually done in a dark rom. Because the pupil enlarges itself to adapt to the dark environment, which is equivalent to increasing the aperture. And this will cause any flaws in the vision system to be more observable. There is also a small trick to overcome this – squint the eyes. This will reduce the aperture (in one direction only though) and limit the size of the circle of confusion. And everything becomes clearer.
* _When the aperture decreases (i.e. larger f number is used)_, it will also affect the image quality because of diffraction. The aperture usually isn't measured by absolute size (e.g. in millimeters), but using the f number, which is aperture diameter / focal length. Note the focal length here is not the 35mm equivalent focal length, but the real, physical focal length. With the same f number, if the sensor size (i.e. the size of the entire system, or the actual focal length) is smaller, that means the absolute aperture size is smaller, which directly determines how much the diffraction would be. This explains why for wide-angle lens, the sun-star is usually pronounced when the aperture is around 11. But for long lenses, even f/32 won't give you any sun-stars. Similarly, it's also harder for a medium format system to get sun-stars than an APS-C system. This also explains why iPhones have a large f value (f/1.8 for iphone 7 and 7+). For a smaller aperture, given iPhone's small sensor size / focal length, diffraction will be a big problem. Actually if you do any quantitative calculation, the Airy Disk's diameter is already more than the size of a pixel, even under f/1.8.
* The essential difference between a [macro lens](/microscope-objective-photography.html) and a regular lens is the focus distance (object distance) is much smaller for a macro lens. From the Thin Lens Formula 1 / f = 1 / u + 1 / v, this requires a large image distance. And the mechanical design of allowing this kind of distance is the key of macro lenses. That's why an inexpensive way of converting a regular lens to a macro lens is to use a macro adapter, which is nothing more than a closed tube, with no optical element. A tricky thing is, when the objective distance is close, the paraxial approximation is violated. This requires some optical redesign, and is partially why a dedicated macro lens is better than a regular lens plus a macro converter.

The Chinese version:

最近在学习摄影技术，从基本的光学开始学起。突然感觉好多之前不太清楚的点都串起来了。

首先推荐一门课，digital photography。讲师是stanford [cs的教授，google的工程师。所以会比较偏技术。所有课件和讲课的视频都可以在这里找到：[https://sites.google.com/site/marclevoylectures/home](https://sites.google.com/site/marclevoylectures/home)

然后最近突然觉得串起来的东西是：

* 眼镜的度数（+1.00, -0.75这样）原来就是1/焦距。比如100度远视或者+1.00的镜片，就是一个焦距是1m的凸透镜。凹透镜的焦距就是负数。所以我们平常用的50mm镜头，其实也可以当成一个2000度的眼镜用啊。。囧 或者500mm大长焦其实就是个200度的远视眼镜？
* 光圈越大，景深越浅，对成像的一点瑕疵，比如对焦不准也会越敏感。这就是为什么测视力大都在暗室里的原因。因为暗了，人眼的瞳孔放大，等于光圈变大了。这时候近视眼远视眼就更容易发现了。相应的，如果你眯眼强行缩小光圈的，可以把测出来的实力提高一两档哦。
* 光圈太小也会影响成像质量——会出现衍射。光圈一般不看绝对孔径，而是用f值来衡量。f值可以看成是传感器和口径的比例。同样的孔径，如果传感器（相应的，也就是整个系统）的尺寸越小，f值越大。所以我一下理解了为什么iphone的相机要定光圈2.8了，有可能是传感器实在太小了（面积是全幅相机的1/56），光圈比2.8一小就出现衍射成像就模糊了。相应的，傻瓜相机的光圈一般限制在f/8以上，全幅相机的光圈一般限制在f/16以上，而更大的中画幅相机可以到f/32都没有衍射。
* 所谓[微距镜头](/microscope-objective-photography.html)和普通镜头的核心区别是对焦距离（物距）小了很多。根据高斯透镜定律（1/物距 + 1/像距 = 1/焦距），像距就要大很多。所以微距镜头后面一般会有个很长的管子，或者你自己用卫生纸筒撸一个也行。此外，因为物距近了，旁轴近似（paraxial approximation）就不能用了，所以微距镜头往往还要重新设计做一些其他纠正。