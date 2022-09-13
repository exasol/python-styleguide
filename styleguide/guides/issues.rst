📝 Issue Tracking
=================

.. toctree::
   :maxdepth: 1
   :hidden:

   issues/security
   issues/bug
   issues/refactoring
   issues/documentation
   issues/feature

Summary
+++++++
Issue tracking is a great tool to track pending work and improve the overall communication within a project.
But similar to every other tool, it needs to be used with care.

    | "A fool with a tool is still a fool"
    | -- Grady Booch

This guide will try to help you to get the best out of the issue tracking for you, your teammates and the project(s)
you are working on, by answering the following questions:

* When to create an issue?
* What makes a good issue?
* How to maintain an issue?
* How to maintain a backlog?

When to create an issue?
++++++++++++++++++++++++
Let me start by saying there is no perfect and one size fits all ruleset to decide this question, otherwise there would be some code doing that for us.
The good thing though is, humans are great in dealing with fuzzy problems. Still most people want to have something to orient themselves.
Asking more specific questions often helps in this situation.

The following question(s), helped us in the past, to get a better handle on this:

* What is the cost/benefit ratio of creating an issue?
    * cost being mainly time and effort
    * benefit being the upsides we gain from having an issue

* What is the signal to noise ratio?
    * signal being the actual code/change bringing some benefit/value to the project
    * noises being the overhead

* Is the user (api or product) impacted by this change?
    * Is it an "internal improvement" quality of life and/or code quality


Examples
--------
Fixing a couple of typos
________________________
You stumble upon a couple of typos in a Project.

Possible Action(s)
~~~~~~~~~~~~~~~~~~
* You fix the typos without creating an issue

Suspicious amount of typos
___________________________
You stumble upon a various typos within a piece of documentation you are reading. Because of the vast amount
of typos and the overall structure you expect the whole documentation to contain a substantial amount of typos.

Possible Action(s)
~~~~~~~~~~~~~~~~~~
* If the documentation is not to big and you can make the time to fix the typos right away without creating an issue.
* If the documentation is quite big, and fixing this e.g. would take you more than 1/2 a day you definitely should create an issue.
* You are unsure how long it will take to address and check the documentation and you currently can't spent time for detours create an issue.

What makes a good issue
+++++++++++++++++++++++

    **TL;DR:** An good issue describes a piece of work, it's context and it's assumption in a way, any person capable of working
    on the project, can understand it, based on the information referenced and within the issue.

To begin with, we want to make sure you understand that creating good a issues is not a zero effort action. Various things
like issue templates, can remove tedious boilerplate work, but still creating a good issue is some actual work.
It is crucial to have well crafted issues, because bad issues do way more harm than good. So let's take a step
back and let's think about why we need to have good issues, in order to better understand what actually makes a good issue.

Boiled down to it's core issue tracking is just a list of pieces of work which are needed to be done.
This list in turn, than can be used to plan, organize and track "progress/work".

Broken down to an individual issue, this means an issue should provide all relevant information about
a "single" piece/unit of work.

Even though the part what an issue is about is well understood, by most people, this is also where it goes wrong.

**Why?** Because we as humans tend to use and assume context implicitly. Assuming context implicitly already can be a problem
when communicating with people we meet on a regular basis, but is a huge problem when you communicate with people which
we meet rarely or even never.

This is somewhat obvious when you think about the fact that 60-70 % of human communication is non verbal communication.
This most likely also part of the reason so many people use emojies, a picture says more than a 1000 words
and therefore can help transport context more easily 😉. But even those helpers aren't perfect and it very
often depends on the mood and the other persons perception (context) of you how they interpret a specific emoji you have sent.

To take on a more computer science specific example:

.. list-table:: **TL;DR: Context matters**
    :header-rows: 1

    * - Information
      - Context
      - Value
    * - 65
      - ASCII
      - 'A'
    * - 65
      - Hex
      - 101
    * - 65
      - Decimal
      - 65


As you may have realized by know our point being how information is understood and processed highly depends on the context.

To come back now to the topic of **"What makes a good issue"**, a major part of it is to make context and assumptions
an explicit part of your information you are providing. Write the issue in such a way, that a person
working on the project, now or in the future can precisely understand the task, the context and assumptions
of it.


.. attention::

    You may inclined to think, you gonna address this task anyway or it is just for "your" book keeping,
    but then this is nothing for the issue tracker rather something for your personal todo list.
    If you decide it is important enough for the issue tracker than treat it as such.


**So what does this mean in more practical actionable terms?**

* Make your context explicit
        - Add links and references to spec you may already know
        - Add information e.g. from discussion, meetings, mails ...

* Make your assumptions explicit
        - Write them down also note e.g. if you are not sure if it is the right decision but what you have taken into account at the point in time when you wrote it down

* Add SubTasks regarding "standard" processes which people may not necessarily know about
      - This can be simplified e.g. by providing issue templates
      - update documentation
      - update changelog
      - ...

* Make it easy to answer the following questions for the person working/reading the issue
      - Is this issue still relevant, or is it obsolete by now?
      - Are the assumptions still valid today?
      - Did they have more or less context than we have today?
      - Did I consider the assumptions and context of the one writing the issue?


.. attention::

    More details on a specific issue type you will find in the corresponding subsection(s) of this guide.


How to maintain and issue
+++++++++++++++++++++++++
* TBD

  - How to update status etc.


How to maintain a the backlog
+++++++++++++++++++++++++++++
* TBD

  - How to keep backlog "clean" (remove/close outdated issues etc.)

