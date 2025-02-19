Title: 使用ZWO相机山寨Leica Monochrom
Date: 2022-04-11 00:19
Category: Computing
Tags: Photography, Drone, ZWO, Chinese
Slug: yasselblad

徕卡和飞思都有一些黑白相机，比如徕卡M10 Monochrom，飞思 IQ3-100 Achromatic。这些相机把拜耳滤光片去掉了，用的就是类似[天文黑白相机](/astrophoto-tutorial-4.html)的黑白传感器，所以一方面高感表现非常惊人，ISO 51200都高度可用，一方面也非常适合拍摄艺术摄影。我个人非常喜欢黑白摄影，所以一直想拥有一个这样的相机。但我同时也是[中画幅胶片摄影](/full-frame-and-medium-format-1.html)，尤其是6x6画幅的爱好者，所以一直幻想有一天可以有一个方形画幅的黑白机出现。然鹅考虑到黑白相机的售价，比如全幅的徕卡 M10M售价将近6万，4433 5440的飞思售价35万，就算某一天真的出了6x6黑白机我肯定也是买不起的。最近ZWO正好出了ASI533MM，我就厚着脸皮把工程样机要了过来，做了一个真·方形画幅黑白机。既然这个相机出生在西雅图，又和哈苏一样是方形画幅，就叫它鸭苏吧。

![Yasselblad logo](/images/yasselblad_logo.png)

整个实现非常土，用的就是一个[树莓派4](/smart-home-air-quality.html)跑Linux做主控，加上一个电容触摸屏做实时预览和操控，再加上一个超薄透气充电宝做供电。打印一个外壳把所有东西装进去拉倒。目前通过[3D打印](/3d-print-faq.html)的转接环兼容徕卡M口的镜头，其他手动头也很容易兼容。为了系统稳定，弄了一个小风扇对着树莓派的散热鳍片吹。初号机长这样：

![Yasselblad camera body](/images/yasselblad_1.jpg)
 
![Yasselblad camera body](/images/yasselblad_2.jpg)

![Yasselblad camera body](/images/yasselblad_3.jpg)

外壳全靠低端打印，系统连接全靠飞线，开关全靠插拔电线，快门全靠电子快门，可以说是非常山寨了。。最后一张图可以看到操作界面。这个软件是自己肝了一天写的程序，支持实时取景，手动模式调节ISO和曝光时间，含有元数据的raw输出（其实就是fits），jpg输出，局部放大对焦，Wifi传输照片，远程操控。关于元数据，有图为证！

![RAW exif data](/images/yasselblad_fit_header.png)

实测了一把，高感如预期的一样惊艳。我和佳能R5对比了一下，简直乳佳。。这两张图都是徕卡50mm f/2 APO，在几乎同一个时间，同一个机位，拍摄的同一个物体。用的ISO 51200。注意因为是同一个机位，所以在传感器上物体的大小也是一样的，所以佳能其实也只用了1寸大小的底。这个是否公平有点争议。同时R5是前照传感器，也不是佳能的最高水平。不过我觉得鸭苏的优势还是很明显的。

![Image quality comparison](/images/yasselblad_comparison.jpg)

因为ZWO的相机和M10M等相机不同，是没有UVIR滤镜的，所以这个相机其实还可以手持拍红外和紫外摄影。这是M10M等相机做不到的。比如下面是两个红外的样张：

![IR photos](/images/yasselblad_photo_1.jpg)

![IR photos](/images/yasselblad_photo_2.jpg)

请忽略炸掉的高光。。高光溢出警告和高光优先测光还在实现中，未来固件更新会加入进去。黑色的天，白色的云，闪亮的植被，都展现着红外照片的魅力。这下终于不用背着66胶片相机+禄来红外卷去拍红外了。而且禄来那个IR400卷分辨率可能和这个900万像素的传感器也差不多。当然，这样的宽光谱响应也对镜头的色差纠正提出了新的要求。如果很在意锐度的话还是最好在镜头前面加一个UVIR Cut滤镜。

![IR photos](/images/yasselblad_duck.png)

总的来说我的感受如上图所示。众所周知，中文是从右向左读的，跟我一起念，鸭苏香！现在问题来了，如果我把这个设计改进并且小批量试产，卖12000左右，会有小伙伴感兴趣吗？

感谢黄一凯对本文的贡献！

<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
