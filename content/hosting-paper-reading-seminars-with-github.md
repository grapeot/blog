Title: Host paper reading seminars with github
Category: Computing
Date: 2012-08-30 22:57
Tags: github, PhD, English
Slug: host-paper-reading-seminars-with-github

[Github](https://github.com/) is a well-known tool within the dev community. People use git(http://git-scm.com/) and github to collaboratively build awesome stuffs and also enjoy the social life (xD, geeks). I find it also useful in our daily research, say, to host a paper reading seminar. (I assume you are familiar with git in the following text)

As a version control system, github is good at managing the codes, for example, LaTeX docs. With different branches, people can try different ideas in the writing, while still keep the master branch neat and ready to present at any time. As a user-friendly git-based community, github provides elegant web interfaces for git, with other necessary features such as wiki, issue tracker, as well as easy ways to generate project pages. Today we are talking about how to use these two features (git branch and github pages) to host a paper reading seminar with little effort.

Let's start from the [pages](http://pages.github.com/) of github. It's a quick way to generate a set of theme-enabled pages from the simple [mark-down language](http://en.wikipedia.org/wiki/Markdown). This provides a good option for a seminar page, where we can present list of papers, a brief introduction, notifications about time/location, and also slides. Since github is a git-based website, the page has a "download" button by default, linking to the content of the associated git repository. (This doesn't bother .git directory, will only deliver the latest content without any version control information.) Therefore it's natural to put the slides in the git repo, so that the slides will be compressed and delivered to the user when s/he clicks the download button.

Given I'm using [beamer writer](/new-features-of-beamer-writer.html) to write slides efficiently, using git to track them is also a good idea. However, we don't wish to mess up the hosted slides with the LaTeX source code. Anyway, readers are not interested in how the slides are written and compiled. Then here comes the branch. We can put the compiled slides in the master branch, which will be downloaded by default, and the source code in another branch. This way we can split our "development" with the final "release".

Then we are ready for the overall receipt. First use our [beamer writer](http://lab.grapeot.me/beamer/) to generate beamer codes efficiently. Revise the code a little bit locally and track the changes with git in a branch other than master (say, a branch named "LaTeX"). When you are ready to go, compile the pdf slides in the master branch, push it to github, and create a page. That's it. You can also update the slides after that (stay focused and keep shipping yaaaayy) and push the latest changes to the git repo.

So [here](http://grapeot.github.io/prs120828/) is a sample page about our paper reading seminar. Convenient page generation, native version control with git, slides hosting... And even automatic slides compilation with git hooks. What else can you demand from these free tools?