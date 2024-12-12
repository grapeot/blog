Title: More Tips about Time Management
Category: Life
Date: 2015-02-01 19:00
Tags: TimeManagement, nodejs, Chinese
Slug: more-tips-about-time-management

Was keeping thinking about and trying out new time management methods/tools recently, and had some new thoughts.
I'd share it here and hopefully it can also benefit others.

## The Pomodoro Technique

Learned about the [Pomodoro Technique](http://pomodorotechnique.com/) these days. 
Compared to the somewhat complicated GTD, it's easier to begin with.
As an old user of GTD, I found two aspects especially interesting:

* The time is expected to be divided into "uninterruptible" blocks and intervals between them. This will explicitly encourage more focus, and boost performance considerably.
* Record time usage and review them every day. This is pretty related with traditional Chinese culture (三省吾身), which I always appreciate.
Possibly the most dangerous state is the self-satisfactory mind, while hard to find spots to improve.
But this habit will help reveal out problems often and quick, and push us out of our comfort zone.

## Plus for Trello

Since I generally use [Trello](https://trello.com/) to [manage time and projects](/using-trello-to-do-time-management.html), a tool to record my time on each project and task would be extremely useful.
Previously I paid $60/year for [RescueTime](https://www.rescuetime.com/), which uses a system-wide app to monitor the title of the active window to provide an automatic time recording.
But it still lacks finer-scale ability to tell which project I am working on, especially when most of my work was performed in a terminal.
That turned me to [Plus for Trello](https://chrome.google.com/webstore/detail/plus-for-trello-time-trac/gjjpophepkbhejnglcmkdnncmaanojkf?hl=en), which provides card-level time recording and analysis as a Chrome Extension.

![Sample interface of RescueTime](https://www.rescuetime.com/images/imac.png)

_Sample interface of RescueTime (from official website)_

The feature is simple, click on an icon on a Trello card, and a timer will run.
Click it again, timer stops and the elapsed time will be added to the card as comments, with some optional information typed by the users.
Board-level and user-level Scrum graphs and charts are also available for further analytics.

It turns out to be very useful (and free!).
Now I can review my daily time usage and the focus level.
Since I plan and record generally everything on Trello, this also gives me a good review of what are the largest distractors.
Basically speaking, an awesome tool, until the moment I feel like to see the project-level and even task-level time distribution.

## Automatic Review Tool

Since Plus for Trello can only provide board or user level statistics, and I am using labels to distinguish different project so every card can be managed from one single board, Plus cannot really help me in determining how much time I spent on each project.
So I investigated on the Trello API, and wrote a simple `nodejs` script (100+ lines) combined with `crond` and [Google Chart](https://developers.google.com/chart/).
It pulls out Plus records (as comments) every day, computes the project and task level statistics, draws pie charts, and sends an email to me in the early morning, to help the daily review and planning process.
A sample email is shown below.

<img style="max-width: 100%" src="/images/TrelloSampleEmail.png" / alt="Email template with Trello task checklist" alt="An email interface showing a Trello board invitation">

## Overall System

The development of this automatic system fills the last part in my [overall time management system](/yi-xie-guan-yu-shi-jian-guan-li-de-zong-jie.html).
The basic principles are (_italic fonts_ denote Trello terminologies): 

* Tasks are arranged as _cards_ on Trello, with progress and thoughts in the _description_, and project as _labels_.
* When leaving some task (say planned 2 hours for task A, in the end of the 2 hours), quickly write down the current status and immediate next step in the _comments_. This will help much when you need to pick up the task again next time.
* Track and record time usage in the _comments_ with Plus for Trello, which can also be used on mobile because essentially it's all about plain-text comments.
* Daily review the time usage of previous day, with the help of the developed automatic tool. Think about possible improvements on today, and do planning on Trello.
* Weekly and monthly reviews (e.g. on long-term goals, project progress, and financial states). Set reminders for such reviews with _due time_ and [_Calendar Power-Up_](http://help.trello.com/article/811-viewing-cards-in-a-calendar-view).
* When some project or task is finished, go over the _description_ (which is expected to be a document by the end of the project), and copy them to OneNote or other notebook app for experience accumulation and easy retrieval in the future.

Hope it would be useful.