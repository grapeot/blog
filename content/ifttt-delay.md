Title: Adding a Delay to IFTTT Recipes
Category: Computing
Date: 2016-10-04 10:00
Tags: SmartHome, English
Slug: adding-delay-to-ifttt-recipes

Ifttt is the de facto hub for [智能家居](/smart-home-lighting-control.html) now. Nearly everything can be connected to it and personally I have ~20 connected devices (hue, WeMo, echo, lock, thermostat, ...) and tens of recipes. But one thing ifttt still cannot do is adding delay to the recipes. Say, I have a good night trigger which will dim the bedroom lights when Alexa hears I say good night to her. But using official ifttt channels, you cannot further turn off the lights after 15 minutes. There are some discussions [online](http://webapps.stackexchange.com/questions/33674/ifttt-can-you-specify-a-delay-for-an-action) but looks there are no easy solutions yet. 

But from a coding perspective, it shouldn't be too hard. So I wrote a simple web service doing this open to the public. The background is, ifttt has a useful channel named "Maker" (now renamed to "Webhook"). Its action allows you to visit a certain URL, and the trigger allows you to listen on a secret URL. It will be triggered when anyone visits the URL. And my solution is to provide a web service, which takes the secret URL of the Maker (Webhook) channel and how long is the delay as input, and visits that URL after the delay. Then for my example of goodnight recipe, I will first set up a recipe that if a secret URL (say, with secret word Magic) is triggered, then turn off the bedroom lights. And for the Alexa recipe, it will dim the light and also send out a web request to my service, specifying the secret word Magic and delay of 15 minutes. By this way, after 15 minutes, the secret URL will be visited and the lights can be turned off. 

Currently the API is available at `https://lab.grapeot.me/ifttt/delay?event={EVENT}&t={DELAY IN MINUTES}&key={YOUR KEY}`. `EVENT` is whatever event you want the Maker (Webhook) channel to listen for. And `YOUR_KEY` can also be found in the Maker (Webhook) channel. For example, in our previous Alexa example, I will put `https://lab.grapeot.me/ifttt/delay?event=Magic&t=15&key=MY_KEY` as the URL. And visit this URL whenever Alexa hears good night from me.

Enjoy! And let me know if you have questions.