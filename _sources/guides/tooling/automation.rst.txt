Task Runner & Automation
========================

A task runner is great for automating common workflows like running tests, building the project etc..
A second benefit of a task runner is, that it is a "in code"/"in config" documentation of the steps
required for a specific task. If common task also get the same runner names across
projects, switching between projects is simplified big time.

.. figure:: https://imgs.xkcd.com/comics/sandwich.png
    :alt: xkcd-149
    :target: https://xkcd.com/149/

    source: xkcd_
    license: `CC BY-NC 2.5`_


.. _nox_marker:

Nox
++++++++
`Project Homepage <Nox_www_>`_

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1

    * - Pros ✅
      - Cons ❌
    * - Python based (only requires python which is a prerequisite for a python project)
      - Parametrized targets could be more convenient
    * - Defined as code (missing functionality easily can be added)
      - Still assumes PIP as basic package manager
    * - Platform dependent
      -
    * - Overall functionality is small, therefore easy to learn
      -

Other Projects using Nox
~~~~~~~~~~~~~~~~~~~~~~~~

* `pip <https://github.com/pypa/pip>`_
* `pipx <https://github.com/pypa/pipx>`_
* `Salt <https://github.com/saltstack/salt>`_
* `Urllib3 <https://github.com/urllib3/urllib3>`_
* `Hydra <https://hydra.cc/>`_

Alternatives
~~~~~~~~~~~~

* `tox <https://tox.wiki/en/latest/>`_
* `make <https://en.wikipedia.org/wiki/Make_(software)>`_
* `ThePoet <https://github.com/nat-n/poethepoet>`_
* `cargo-make <https://sagiegurari.github.io/cargo-make/>`_
* `just <https://github.com/casey/just>`_
* `Ant <https://ant.apache.org/>`_
* `Task <https://taskfile.dev/#/>`_
* `Tusk <https://github.com/rliebz/tusk>`_
* `Gulp <https://gulpjs.com/>`_
* `Grunt <https://gruntjs.com/>`_

PreCommit
++++++++++
`Project Homepage <PreCommit_www_>`_

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Widely used in non python projects
      -
    * - Can be used to unify and simplify the use of commit hooks
      -
    * - Supports "multi language" commit hooks
      -
    * - Takes care of "installing/updating" the hooks
      -
    * - Share commit hooks and replace scripts over time (instead of copying scripts)
      -

Alternatives
~~~~~~~~~~~~

* ¯\\_(ツ)_/¯

.. _Nox_www: https://nox.thea.codes/en/stable/
.. _PreCommit_www: https://pre-commit.com/
.. _xkcd: https://xkcd.com/
.. _CC BY-NC 2.5: https://creativecommons.org/licenses/by-nc/2.5/
