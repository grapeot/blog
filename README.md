# Computing Life

This repo is the underlying files for my blog [Computing Life](http://grapeot.me/), aiming to provide a start point for a basic blog site using [Peican](https://github.com/getpelican/pelican/), which is a static site generator.

There is a `gh-pages` branch of the repo providing a backup for the website [here](http://grapeot.github.io/blog/).

## How to clone this repo

Since we use `submodules` in git, it requires an extra switch to clone a complete version of this repo.

```bash
git clone --recursive git@github.com:grapeot/blog.git 
```

`pip install pelican` to install pelican, and then `make html` to get the generated static website.
