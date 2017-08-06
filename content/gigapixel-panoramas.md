Title: Gigapixel Panoramas
Category: Computing
Tags: Photography, Computational Photography, Image
Date: 2017-08-03

<style type="text/css"> iframe { width: 100%; height: 400px; } </style>
<script type="text/javascript" src="https://lab.grapeot.me/gigapixel/Seattle/ZoomifyImageViewer-min.js"></script>

Bought a camera (Leica SL) recently, and spent some time (and money) on some old Leica R lenses.
One is 60mm f/2.8 macro with 1:1 adapter, one is 400mm f/6.8.
I found both of them can be pretty good at making gigapixel panoramas. 

Traditionally gigapixel panoramas are made by rotating the lens around the nodal point and shooting photos.
Later, a stitching software is used (e.g. PTGui or Photoshop) to generate the final panorama.
The final photo is so big that no screen can ever show it in full scale.
Therefore, special renderers are often used to show a part of the image and allow users to zoom in/out and pan around.

I tried to use the 400mm f/6.8 to shoot a gigapixel panorama on Alki Beach of Seattle skyline.
It was made from 160+ photos, and will be more than 12 meters long if printed out.
You can zoom in and drag around to check it out below.

<iframe src="https://lab.grapeot.me/gigapixel/Seattle/"></iframe>

Such "regular" panoramas are relatively easy. 
What makes it more difficult (and interesting) is when you extend it to macro photography.
First macro photography itself is very hard.
Extremely shallow depth of field asks for small aperture.
And because the lens is extremely close to the object, even millimeter level of hand muscle shake can bring considerable motion blur, which asks for fast shutter speed.
Both ask for a high ISO, which is not free but comes with noise.
Second, macro "panoramas" are not shot by rotating the lens, but by panning around the object.
This immediately violates the basic assumption of the stitching algorithms, and will bring parallax, which will confuse the stitching software.
To avoid parallax, usually those panoramas can succeed only in planar objects, such as dollar bills, and watches.
Here are two panoramas from my shooting.

<iframe src="https://lab.grapeot.me/gigapixel/Watch/"></iframe>

<iframe src="https://lab.grapeot.me/gigapixel/DollarBill/"></iframe>

To make a successful macro panorama, we need three things:

* The photos themselves need to be in high quality. This is because the viewers are able to (and will) zoom in to the max level, when even the tiniest flaws will become obvious. Use small aperture, low ISO, and fast shutter to achieve the best quality. How? Use a ring flash.
* Keep the panorama stitching in mind when taking the photos. Choose objects that don't have an obvious depth so the parallax can be controlled. Or you can also use shallow depth of field to blur out the farther parts. Leave enough overlap between frames.
* Usually it's hard to get the panorama done in one shot, so don't expect that. Look at the result, and figure out the reason of mismatching. Then fix it (by reshooting the photo or adding another one).

Basically I found the macro lens and telephoto lens are very fun.
They are not necessarily expensive (especially when you get used ones from Ebay), but can be used in a lot of projects.
