Title: Scraping photos from Facebook groups
Date: 2014-06-27 12:00:00
Category: Computing 
Tags: English

## Motivation

After becoming a (student) pilot, I joined some pilot Facebook groups.
Looks a popular game among pilots is to give out a photo of a runway or airstrip, and then ask others to tell where it was taken.
This "Name the airport" game acts as a way for the pilots to (gently) show off their experience, and also helps to start a conversation.

As a newbie, I don't have many chances to recognize where it is for most of the photos.
But as a CV guy, maybe it's the time to test some old and new techniques in image search.
For a newly posted photo, if we can get similar photos among the existing photos in the Facebook group, hopefully we can figure out where it is by reading the comments.
And it's also a good opportunity to put up my (a lot of) old code for future references, and possibly open source for the community.

Then here comes the problem, how to scrape the photos from a Facebook group?
The [Graph API](https://developers.facebook.com/docs/graph-api) doesn't have an entrypoint for photos within a group.
And some googling confirmed that [[1]](http://stackoverflow.com/questions/4869595/how-do-i-retrieve-photos-from-a-facebook-group-using-the-graphapi)[[2]](http://stackoverflow.com/questions/10076163/how-do-i-retrieve-photos-from-a-facebook-group-using-the-graph-api).
So looks it's time to get our hammers and drills again, let's get `chrome`, `curl`, and `awk` to rock.

## Solution

The basic idea is, to first manually get an HTML page consisting of links to all the photos in a group, and then use text processing tools to extract the FBIDs and do the scraping with `curl`.
This page is easy to find at URLs like `https://www.facebook.com/groups/<GROUP_NAME>/photos/`.
Scroll down a bit until you hit the end.
It may take one minute or so if the group has many photos, but it's much faster (and posts much less stress to the memory) compared with scrolling down the timeline of the group.
After that, launch Chrome's developer tools, copy the source code from `Elements` tab to a file, say, `photos.html`.
Don't use `Source` tab 'cause it's the "real" source code before all js and ajax works, and we want the code after the rendering.

Then things become easier.
Easy `grep` will give you the FBIDs of the photos as well as links to the photo pages.
The code is like

```bash
cat photos.html | grep -o 'https://www.facebook.com/photo.php?fbid=[0-9]*' | sort | uniq 

```

And then `curl` will scrape such photo pages, which contain the URLs to the actual images, to local disk.
Given Facebook requires authentication if the group is not public, we need to use cookies to "pretend" our `curl` has been logged in.
To get the cookies (actually the `curl` commandline directly), in the developer tools of Chrome, select `Network` tab, find the Facebook HTML page (refresh if you don't see it), right click and select "Copy as cURL".
Paste it somewhere and you'll get a sense about how it works.
The commandline is like (I replace my cookies with `<COOKIES>` for obvious reasons. You'll see your actual cookies on your machine)

```bash
curl 'https://www.facebook.com/photo.php?fbid=10100123918096165' -H 'accept-encoding: gzip,deflate,sdch' -H 'accept-language: en-US,zh-CN;q=0.8' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'cache-control: max-age=0' -H '<COOKIES>' --compressed
```

`awk` will help generate batch scraping scripts from the URLs and the curl template.
Remember `printf` is your friend.
You may also need `-o` option for `curl` to specify the output file names.
Alternatively, I used `vim`, `grep` and `paste` to interactively (instead of fully automatically like pure `awk` does) generate the script.

Execute the script to download a bunch of HTML files.
I use a single thread, scraping at around one page per second, and Facebook didn't ban me. 
After that, you'll find the image URL and the download link are waiting for you in each scraped page.
Simple `grep` will do the trick to extract them.

```bash
grep -o 'fbPhotoImage" src="https[^""]*.jpg"' *.html | sed 's/fbPhotoImage" src=//' | sed 's/"//g' | sed "s/\.html:/ /" | tee urls.txt
```

Then `curl`/`wget` the photos, with `xargs -P` or whatever you like.
I did single threading here again and wasn't banned by Facebook.
Not sure whether it violates the user terms though.

## Future work and lessons learned

I scraped like 3000 photos from the group, and now extending the image search engine proposed in my new ECCV paper to index them.
Still tuning... 
Hope it helps me to enjoy the game more. ;)
Some lessons learned:

* `bash` (the whole toolchain) is your friend
* Put your code on github, and `git submodule add` will add reference to it with dependency resolving like a charm. I use it for my search engine builing, with header only C++ code. 