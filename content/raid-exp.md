Title: 一些关于SSD RAID性能的实验
Category: Computing
Date: 2019-08-12 10:00
Tags: RAID, Computer, DIY, Chinese
Slug: ssd-raid-exp

今天做了关于硬盘性能的一系列实验。

首先这是一个500G的硬盘的读写速度：

![500G HDD speed](/images/raid-exp-hdd.png)

这是用了两个这样的硬盘组成的RAID 0，可以看到性能基本翻倍，软RAID的overhead可以忽略不计了。

![500G HDD RAID speed](/images/raid-exp-hdd-raid0.png)

然后这是4T单盘的性能。好意外4T的盘性能只比500G的盘高这么一点点。说好的磁盘密度越大读写速度越快呢？是不是PMR的锅？

![4T HDD speed](/images/raid-exp-hdd-4t.png)

这是nvme ssd的性能... 雾... 草... 

![nvme SSD speed](/images/raid-exp-nvme.png)

两个结论：1）知乎上那帮叫嚣什么HDD + RAID 0战SSD的你可拉倒吧，给你30个HDD组RAID 0都被吊起来打。2）SATA SSD组RAID 0都没戏，因为接口速率才6Gb/s，理论值都干不过人家实测值。什么任务队列我都不拿出来欺负你了。。

所以最终结论就是，有钱还是上nvme ssd吧... 我的主板m2接口不够了只好去组SATA SSD RAID 0了... 

============我是可爱的分割线============

SATA SSD RAID的实验出来了... 结果有点意外。这是SATA SSD单盘的速度：

![SATA SSD speed](/images/raid-exp-ssd.png)

这是SSD+RAID 0的速度:

![SATA SSD RAID 0 speed](/images/raid-exp-ssd-raid0.png)

几个观察：

1. nvme还是爸爸。
2. RAID 0对SSD的加速效果相当有限。上次测HDD基本都是100%的加速（除了4K Q1T1），但对SSD，顺序读取只加速了80%，4K读写基本在50%左右。观察可见测试的时候CPU有个核占用率很高，可能是软RAID的性能原因。
3. 最后选用了2T nvme SDD做系统盘，8T RAID SSD做数据盘，8T JBOD HDD做备份盘的方案。现在做实验又快了！可以愉快地搬(mo)砖(yu)了！话说摩尔定律真是可怕，五年前哪能想到现在装台机器随便就需要18T的存储系统…
4.  可靠性有一些顾虑。不过现在几个小时备份一次，先帮dalao们蹚坑了。orz

=============我是更新的分割线===============

更新一下：

1. 我发现我的主板上内置了raid芯片，但启用之后比软raid还慢。原因可能是这种芯片毕竟不是为ssd场景设计，跟不上性能。
2. 硬raid的stripe size设置对性能影响较大。128k比16k明显快。
3. intel有高性能raid的解决方案叫rvoc，但仅对nvme/pcie有效。网上有人跑出来了12GB/s的可怕速度… 有卖一个16x pcie拆成4个nvme接口的卡，正好就是个超高性能的raid。
4. 说个悲伤的故事。幸运的是我的主板也支持这个功能，不幸的是我为了试验rvoc，把所有pcie都启用了rvoc支持。然后发现显卡用不了了… 我的cpu也没有核显，usb外置显卡插上也改不了bios设置… 就只好重置主板设置… 查阅说明书以后发现要把某个角落里面的某个跳线短接十秒。把乱七八糟部件拆掉一大堆以后终于找到了这个跳线，然后悲催地发现我没有短接的jumper cap… 试图用螺丝刀短接失败以后（似乎螺丝刀表面有绝缘涂层？），只好用杜邦线现撸了一个短接器出来搞定… 给自己蠢哭了…
5. 穷玩车，富玩表，傻逼玩电脑… 装机一时爽，一直装机一直爽… 跑程序日常…

![Task manager screenshot](/images/raid-exp-task-manager.png)