🏗️ Migration
============

Summary
+++++++

In this chapter we will discuss different migration strategies, for "known issues".

Recommended Migration Order
+++++++++++++++++++++++++++

.. toctree::
   :maxdepth: 1

   migration/nox
   migration/poetry
   migration/precommit
   migration/black
   migration/isort
   migration/pyupgrade
   migration/pytest
   migration/pylint
   migration/mypy
   migration/sphinx
   migration/furo
   migration/pages-generator
   migration/sonar

Migration strategy development tools
++++++++++++++++++++++++++++++++++++
This section will provide a guidance when migrating from an arbitrary project tooling state, to the
recommended tooling for exasol python project(s).

.. note::

    Generally the described steps should be seen as individual iterations of the migration (one "tool" at the time).
    In theory they mostly can be applied in arbitrary order, but most of the times it will make your life
    easier if you migrate in the suggested order.



