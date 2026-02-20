Title: 百万级别二次元角色识别数据集
Category: Computing
Tags: Chinese, AI Technique, Image Processing
Date: 2019-06-21 18:54
Slug: anime-character-recognition

在[上一篇文章](/anime-head-detection.html)里，我们做了一个效果不错的动漫头像检测模型。这个模型本身并不复杂，但它可以帮助批量化处理数据，从而为更多彩的应用奠定基础。一个自然的问题就是，我们有没有可能做一个类似Amazon XRay的东西，你给我一张ACG图片，我告诉你这是哪部番里面的哪个角色？这样的模型本身并不复杂，现成的face detection - alignment - recognition的框架可以轻松搞定。但关键是训练数据很难找。这篇文章主要就是解决了这个问题，开源了一个百万级别的二次元角色识别数据集，方便各位丹友们炼丹。

在我们之前对StyleGAN的调教中用到了Danbooru 2018数据集。这个数据集是一个同人画师数据集，很多画师在上传的时候都会选择这是什么角色。这天生就非常适合做角色识别。我们从2018年的630万张图出发，做了以下过滤和处理：

* 首先我们根据每张图片的tag，根据tag的属性过滤其中的人物角色tag。如果一个图片没有任何角色tag，我们就直接丢弃这张图片。
* 因为当一个图片有多个角色tag的时候我们不知道哪个脸对哪个tag，所以我们目前丢弃了所有有2个或以上角色tag的图片。
* 接下来我们对剩下的图片用[这个模型](/anime-head-detection.html)进行头像检测。对于检出多于一个头像的图片直接丢弃。
* 注意这里我们没有进行人脸校准，主要是因为没找到适合的模型。也许未来会标注训练一个。

最终得到一个97万张图，7万个角色的数据集。平均每个角色有13.85张图像。但和大多数数据集一样，每个角色有多少张图像是个非常长尾的分布。在7万个角色中，有2万个角色只有一张图片。如果我们把图像最多的100个角色画一个直方图的话，长这样：

![Stats of the anime head detection dataset](/images/anime-character-recognition-stats.png)

其中图片最多的是初音未来，有接近25000张图。。公主殿下到底是多受欢迎。。然后最受欢迎的前20个角色是：

* hatsune_miku 初音未来
* hakurei_reimu 博丽灵梦
* flandre_scarlet 芙兰朵露·斯卡蕾特
* kirisame_marisa 雾雨魔理沙
* cirno 琪露诺
* izayoi_sakuya 十六夜咲夜
* remilia_scarlet 蕾米莉亚·斯卡蕾特
* kochiya_sanae 东风谷早苗
* rumia 露米娅
* shameimaru_aya 射命丸文
* patchouli_knowledge 帕秋莉·诺蕾姬
* inubashiri_momiji 犬走椛
* fujiwara_no_mokou 藤原妹红
* komeiji_koishi 古明地恋
* reisen_udongein_inaba 铃仙·优昙华院·因幡
* yakumo_yukari 八云紫
* alice_margatroid 爱丽丝·玛格特罗伊德
* komeiji_satori 古明地觉
* hinanawi_tenshi 比那名居天子
* kazami_yuuka 风见幽香

我特码。。真是给你们东方厨跪了。。前几个角色的可视化结果如下：

![Examples of the characters](/images/anime-character-recognition-examples.jpg)

感觉标注的质量还是比较高的。

有了这个数据集，我们就可以做之前提到的角色识别了。在删去了置信度低于0.85的头像以后，我们用剩下的56万张图+ArcFace loss训练了一个ResNet18的baseline。这个模型在测试集上可以达到37.3%的精度。相应的训练集，验证集和测试集也都在数据库中提供了。感兴趣的同学可以训练自己的模型，和baseline进行比较。

最后就是传送门啦，请猛击我吧！
[https://github.com/grapeot/Danbooru2018AnimeCharacterRecognitionDataset](https://github.com/grapeot/Danbooru2018AnimeCharacterRecognitionDataset)