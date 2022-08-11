🔧 Tooling
==========

Summary
_______

This Section focuses on development tools we are using for our python based projects.
If you have a specific need to address (code formatting, linting, etc.) you should use
one of our "standard" tools in this list. If your need(s) aren't covered by the tools
listed here, we recommend you propose an addition to this list.


Overview
________

.. toctree::
   :maxdepth: 1

   tooling/automation
   tooling/code-style
   tooling/testing
   tooling/documentation
   tooling/packaging
   tooling/code-health
   tooling/misc

Justification
_____________
Unifying basic tooling removes overall complexity when dealing with multiple projects.

* Reduces on-boarding of new people into the project(s)
* Reduces cognitive overhead when switching between projects

  * Running Test, Build is the same in "every"  project e.g. `nox -s test`
  * Developers are more likely to develop deep knowledge of the tools

* Reduces the potential of errors and misuse
* Increases potential for automation (checks, automated fixes, etc.)
* Decreases complexity of automation


.. _xkcd: https://xkcd.com/
.. _CC BY-NC 2.5: https://creativecommons.org/licenses/by-nc/2.5/
