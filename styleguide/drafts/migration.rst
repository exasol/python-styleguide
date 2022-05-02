Migration
=========
In this chapter we will discuss different migration strategies, for "known issues".

Migration strategy development tools
++++++++++++++++++++++++++++++++++++
This section will provide a guidance when migrating from an arbitrary project tooling state, to the
recommended tooling for python project.

.. note::

    Generally the described steps should be seen as individual iterations of the migration (one "tool" at the time).

1. Integrate :ref:`drafts/tooling:Nox` into the repo(s) as task runner
   All task run/triggered by the dev should be triggered using a nox target
   e.g.: Test, Integration Tests, Release, Docs, Githook(s) Install, ...

    .. attention:: **Todo:** List of common task each  project needs to support e.g. build, run

2. Integrate Basic Checks + Fixes in the repo(s)
   Add :ref:`drafts/tooling:Black` and :ref:`drafts/tooling:Isort` to the project
   + fix & check task/target to nox
   + simplify ci/cd and local "builds" both can use nox as single source of truth for execution

3. Integrate :ref:`drafts/tooling:Pylint` [Checks]
   Add nox target for checking and to assert
   Define lint value e.g. 7 to start off

4. Add :ref:`drafts/tooling:Sonar` support to repo(s)
   -> Integrate pylint within sonar too
   -> Add coverage support to repo(s) + connect with sonar

5. Generalize/Simplify GH - Actions using the nox targets
   Ideally local and remote validation look exactly the same
   (looks already very good e.g. in integration test docker ..)

6. Write "all" documentation using :ref:`drafts/tooling:Sphinx` (.rst)
   - Add sphinx setup
   - Migrate docs from .md to .rst
   - add nox target to build, open and deploy docs
