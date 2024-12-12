Title: An rm and git accident
Category: Alive
Date: 2013-12-13 11:00
Tags: Linux, Chinese

The background is, I have a git repo of `nodejs` code.
There is a `controllers` folder in the repo, which I just made some (well, a lot of) changes and am about to commit the staged changes.

Then *in the root folder of the repo*, I suddenly have an urge to check the `upload` folder:

    ➜ server git:(master) ✗ ls uploads 
    0_0_1386887901885.jpg 0_0_1386887901885.txt 17_17_1386623141156.jpg 17_17_1386623141156.txt 8_8_1386622199071.jpg 8_8_1386622199071.txt

Hmmm, some random files. Why not just delete all of them?

    ➜ server git:(master) ✗ rm *
    zsh: sure you want to delete all the files in /home/grapeot/PhotoSwarm/src/server/server [yn]? y
    rm: cannot remove `controllers': Is a directory
    rm: cannot remove `node_modules': Is a directory
    rm: cannot remove `public': Is a directory
    rm: cannot remove `uploads': Is a directory
    rm: cannot remove `views': Is a directory

Oops.

Did I just remove all the files in the root folder instead of the `upload` folder?

Looks so. WHAT???

WHAT??? All my codes are gone???

Actually it's not too bad right now.
Because the files in the root folder are all backed by git, while `.git` is a folder and is hidden, which prevents `rm *` removing it.
And the newly changed files in `controllers` are not affected at all, although they are not staged, which means they haven't been protected by git yet.

And in a hurry, I immediately took measures to recover the files from git:

    ➜ server git:(master) ✗ git reset --hard HEAD
    HEAD is now at 85f95f2 add a new controller for the mjpeg stream

Yeah all the files in the root folder are recovered!
Long live the git!

Wait...

Wait... What's here in `controllers`?

The old files?

Oh shit I just overwrote the unstaged changes!

And they cannot be retrieved back because it's overwriting, not deleting!

当时满脑子想的都是。。[自作孽不可活](https://yage.ai/inspiration-fragments-20131130.html)啊。。

So the lessons are:
1) Stop doing anything when an emergency happens. Think twice before you act.
2) Use [trash-cli](https://github.com/andreafrancia/trash-cli) instead of native `rm`. An alias may help.

P.S. The final ending is I rewrote the patch in 15 min. 
It's much faster because the memory was still fresh.