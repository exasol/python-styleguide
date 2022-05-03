Migration
=========
In this chapter we will discuss different migration strategies, for "known issues".

Migration strategy development tools
++++++++++++++++++++++++++++++++++++
This section will provide a guidance when migrating from an arbitrary project tooling state, to the
recommended tooling for exasol python project(s).

.. note::

    Generally the described steps should be seen as individual iterations of the migration (one "tool" at the time).
    In theory they mostly can be applied in arbitrary order, but most of the times it will make your life
    easier if you migrate in the suggested order.

Integrate :ref:`Nox <drafts/tooling:Nox>`
-----------------------------------------
    * All important task(s) should have a target
      (e.g.: Test, Integration Tests, Release, Docs, Githook(s) Install, ...)
    * CI/CD [GH-Actions] builds must invoke those task(s)/targets for verification
      (e.g. nox -s run-all-tests)
    * Ideally all "complex" task(s) run/triggered by the dev should have a nox target

    .. attention:: **Todo:** List of common task each  project needs to support e.g. build, run

Integrate :ref:`PreCommit <drafts/tooling:precommit>`
-----------------------------------------------------

Integrate :ref:`Black <drafts/tooling:Black>`
---------------------------------------------
    * Executing the code formatter :ref:`drafts/tooling:Black` should be part of at least 2 targets (fix, check)
        - check: check that all source files comply with the expected format
        - fix: run code formatting on all required files to comply with the expected code format
        - .. note::

            A project may decide for itself to run e.g. `fix` as a commit hook.
            The check must be run as part of the CI/CD pipeline though.

Integrate :ref:`Isort <drafts/tooling:Isort>`
---------------------------------------------
    * Executing the import formatter :ref:`drafts/tooling:Isort` should be part of at least 2 targets (fix, check)
        - check: check that all source files comply with the expected format
        - fix: run code formatting on all required files to comply with the expected code format
        .. note::

            A project may decide for itself to run e.g. `fix` as a commit hook.
            The check must be run as part of the CI/CD pipeline though.

    * Make sure :ref:`drafts/tooling:Isort` is run with the *black* profile


Integrate :ref:`Pyupgrade <drafts/tooling:Pyupgrade>`
-----------------------------------------------------


Integrate :ref:`Pytest <drafts/tooling:pytest>`
----------------------------------------------

Integrate :ref:`Pylint <drafts/tooling:Pylint>`
-----------------------------------------------
   Add nox target for checking and to assert
   Define lint value e.g. 7 to start off

Integrate :ref:`MyPy <drafts/tooling:Mypy>`
-------------------------------------------

Integrate :ref:`Poetry <drafts/tooling:Poetry>`
-----------------------------------------------

Integrate :ref:`Sphinx <drafts/tooling:Sphinx>`
-----------------------------------------------
   - Add sphinx setup
   - Migrate docs from .md to .rst
   - add nox target to build, open and deploy docs

Integrate :ref:`Furo <drafts/tooling:Furo>`
-----------------------------------------------

Integrate :ref:`Pages Generator <drafts/tooling:sphinx-github-pages-generator>`
-------------------------------------------------------------------------------

Integrate :ref:`Sonar <drafts/tooling:Sonar>`
---------------------------------------------
   -> Integrate pylint within sonar too
   -> Add coverage support to repo(s) + connect with sonar
   -> badges
