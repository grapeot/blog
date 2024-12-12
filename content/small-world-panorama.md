Title: Build a Small-World Fish-Eye Style Panorama
Category: Computing
Date: 2012-12-05 21:46
Tags: Image, Math, PhD, English
Latex:

Sometimes a small-world panorama is quite stunning. For comparison, a regular panorama is shown below.

<img style="max-width: 50%" src="/images/panorama1.jpeg" />

![](/images/panorama2.jpeg)

Spent about half an hour to do experiments and finally get a program to convert to regular panorama to small-world style.

The key is coordinate system transform, from rectangular to polar. This is pretty intuitive to derive. For a point $(\psi, r)$ in the target image, its correspondence in the original panorama is $(\psi w / (2\pi), h - ry / r_0)$, where h, w is the height and width of the original image, and $r_0$ is the expected radius of the output. 

<img style="max-width: 50%" src="/images/panorama3.jpeg" />

<img style="max-width: 50%" src="/images/panorama4.jpeg" />

Note we may need a nonlinear mapping for the radius to make the panorama more balanced. Here I choose the function $r_0^{-\epsilon} r^\epsilon$, where $\epsilon$ is a parameter to be tuned, controlling the "height" of the camera from the ground. You can see the difference between the two images above.

Another style of small-world panorama is also easy to derive and implement as the following photo.

<img style="max-width: 50%" src="/images/panorama5.jpeg" />