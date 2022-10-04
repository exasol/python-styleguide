📝 Issue Tracking
=================

.. toctree::
   :maxdepth: 1
   :hidden:

   issues/security
   issues/bug
   issues/feature
   issues/refactoring
   issues/documentation

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

To begin with, we want to make sure you understand that creating good a issue is not a zero effort action. Various things
like issue templates, can remove tedious boilerplate work, but still creating a good issue is some actual work.
It is crucial to have well crafted issues, because bad issues do way more harm than good. So let's take a step
back and let's think about why we need to have good issues, in order to better understand what actually makes a good issue.

Boiled down to it's core issue tracking is just a list of pieces of work which are needed to be done.
This list in turn, then can be used to plan, organize and track "progress/work".

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


How to maintain an issue (WIP)
++++++++++++++++++++++++++++++
Various factors can change aspects of an issue, e.g. newly received information via a comment.
This section focuses on how handle this aspects and to keep the ticket relevant and up to date.

Most Common External factors
----------------------------

* Issue receives comment(s)
* The assignee is working on the issue
* External Changes .... library version, deprecation


General Rules
-------------

Upadate while working on the issue
The reduce friction of people polling updates and interrupting you working on the issue, try to post regular
update(s). Often one would say nothing new ... still debugging ... still give the pople some
more information what are your leads, which leads put you in a dead end ... try to think
what information you would give somebody which needs to take over your task, without needing
to do all your work from scratch.

up to date when new information or context gets available,
e.g. because it receivedit is in progress or  are working on it ( us an how and when to update.

Received Comments
-----------------

* make sure comments can be understood, if needed clarify
* make sure comment(s) are relevant otherwise suggest e.g. to move to discussion forum or new issue of type question

Working on the issue
--------------------
In the great future 🚀 we may have perfect project planing, but not today! Until then we need and cope with various <<CENSORED>> problems.
This section will help you on how to work with an issue, so customers, project management, other developers
and you can get the most out of the information within an issue which is being worked on.


Update regularly

* Mark issues which are being worked on as **in progress**
* Update the issue, at least every 2-3 days
    * Post a status message
        * Report which tasks/subtasks have been done already
        * Describe current roadblocks
        * Describe current strategies and findings e.g. for bugs
    * Update the issue itself
        * If needed split up new issues and link them to the current one
        * Add root cause once found out
        * ...
* Move issue not begin not begin worked on back into the appropriate state, e.g. **backlog**


**Example:**

.. code-block:: markdown

    # Status Update
    Further investigation's have shown that the basic SQLA test suite mostly is intact after the upgrade to `1.4` (14 failures), when run in "isolation". Various exasol specific test suites:

       * test/test_get_metadata_functions.py
       * test/test_large_metadata.py
       * test/test_regression.py (TranslateMap)

    seem to have negative side effects which cause 100+ tests to  :boom: fail/crash, if run after those test suites.
    This further strengthens the case for the **assumptions** mentioned in the previous update:

       * Setup/Teardown mechanic of `testing.fixtures.TablesTest` has changed
       * Setup/Teardown mechanic fails due to leftovers in tests DB

    Also, this narrows down the potential root cause(s).

    ## Remark(s)
    Common to all those test suites to be that they add/remove schemas.
    For `test/test_regression.py` it have been proven that the schema manipulating test (`TranslateMap`) causes some negative side effect on following test suits.

    ## Notes & Ideas (from discussion with @tkilias )
    * Is schema inference still working correctly?
    * Does the "disabled" caching cause side effects?
    * Do implicit schema open and closes affect the current schema for follow up tests?

    ## Next Steps
    * Analyze effects of implicit open/close of schema(s)
    * A more in depth analysis regarding side effects and cleanup of the mentioned test suites will be done

To see the example update in it's full context look `here <https://github.com/exasol/sqlalchemy-exasol/issues/106#issuecomment-1245305351>`_.


How to maintain a the backlog (WIP)
+++++++++++++++++++++++++++++++++++

* Search for active tickets with no updates in a week
* Times are suggestions on time/intervals are highly dependent on the ticket throughput and ticket creation/inflow rate
* Check "new" issues for issue standards compliance (Weekly)
   * enough infor etc.
   * contains all relevant information
   * isn't a duplicate
* Check long running issue (Weekly)
   * forgotten, abandoned, updated?
* Check all issues for validity (Monthly)
   * still relevant? already using other 3thrid party lib or refactored huge parts?
* Ideally have issue creators check on their tickets if their still valid
* triage
  * How to keep backlog "clean" (remove/close outdated issues etc.)
  * Triage ... is ticket still relevant ? ... maybe time invalidated the need of having this issue
  * Is the ticket sufficient well written to understand what needs to be done?
  * Have  tickets which are in progress a update which is not older than ~1 week
  * aged, label, and written correctly
  * Mark and close duplicates
  * SHelve?
  * Triage and assign quickly

