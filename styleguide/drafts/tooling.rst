Tooling
=======
This Section focuses on development tools we are using for our python based projects.
If you have a specific need to address (code formatting, linting, etc.) you should use
one of our "standard" tools in this list. If your need(s) aren't covered by the tools
listed here, we recommend you propose an addition to this list.

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

Overview
________

Task Runner & Automation
++++++++++++++++++++++++

* Nox_       (task runner, build automation, test & build isolation)
* PreCommit_ (commit hooks)

Code Style
++++++++++

* Black_     (style, code formatter)
* Isort_     (style, import sorting)
* Pyupgrade_ (style)

Testing
+++++++

* Pytest_    (unit-testing, testing)

Documentation
+++++++++++++

* Sphinx_                        (documentation)
* Furo_                          (documentation)
* sphinx-github-pages-generator_ (documentation)

Dependencies & Packaging
++++++++++++++++++++++++

* Poetry_    (dependency management, virtual environment, build-tool, packaging)

Code Health
+++++++++++

* Pylint_    (linter, code analysis)
* Coverage_  (coverage)
* MyPy_      (linter, type checking)
* Sonar_     (linter, code coverage, code health)


Up For Consideration
++++++++++++++++++++

* `scriv <https://github.com/nedbat/scriv>`_ (changelog management)
* `prysk <https://www.prysk.net/>`_ (Integration testing cli's and co.)


Task Runner & Automation
________________________

A task runner is great for automating common workflows like running tests, building the project etc..
A second benefit of a task runner is, that it is a "in code"/"in config" documentation of the steps
required for a specific task. If common task also get the same runner names across
projects, switching between projects is simplified big time.

.. figure:: https://imgs.xkcd.com/comics/sandwich.png
    :alt: xkcd-149
    :target: https://xkcd.com/149/

    source: xkcd_
    license: `CC BY-NC 2.5`_


Nox_
++++
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

PreCommit_
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


Code Style
__________
Automated formatting ensures a common code style across the projects and removes the burden of manually ensuring
code is complying with the project(s) style/standard. This results in less work, less distraction and futhermore
it provides benefits like easier to read diffs and higher potential for even further automation.

.. figure:: https://imgs.xkcd.com/comics/efficiency.png
    :alt: xkcd-1445
    :target: https://xkcd.com/1445/

    source: `xkcd.com <xkcd_>`_
    license: `CC BY-NC 2.5`_

**TL;DR:**

    Removes cognitive overhead and increases consistency, which simplifies diffs and automation.

Black_
++++++
`Project Homepage <Black_www_>`_

Black is a highly opinionated (preconfigured), which means no discussion within the team to "find" the best
formatting style/options for "the team". The project code style will be compliant with every other python
project which is also using black, therefore more developers will feel at home in the code base
right from the start.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Common Style
      - Additional dependency
    * - Preconfigured
      -
    * - Compliance with other projects also using black
      -
    * - Works well with isort
      -
    * - Less cognitive overhead for the developer
      -
    * - Learning curve is flat and short
      -
    * - Supports pyproject.toml
      -

Alternatives
~~~~~~~~~~~~

* autopep8_
* yapf_
* IDE specific (e.g. PyCharm)

Isort_
++++++
`Project Homepage <Isort_www_>`_

Sort's all imports according to python suggested sorting order.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Less cognitive overhead for the developer
      - Additional dependency
    * - Works well with Black
      -
    * - Learning curve is very flat and short
      -
    * - Supports pyproject.toml
      -

Alternatives
~~~~~~~~~~~~

* ¯\\_(ツ)_/¯ code formatters themselves (black, yapf, ..)

Pyupgrade_
++++++++++
`Project Homepage <Pyupgrade_www_>`_

Helps migrating old code (constructs) to modern one.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Less cognitive overhead for the developer
      - Additional dependency
    * - Less manual work for upgrading/modernizing the code base
      -
    * - Learning curve is very flat and short
      -
    * - Can be setup as pre commit hook
      -

Testing
_______

I do hope this does not need  any explanation in **$YEAR >= 2022**.

Pytest_
+++++++
`Project Homepage <Pytest_www_>`_

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Powerful automatic test discovery
      - Additional dependency
    * - Simple to write tests
      -
    * - Compatible with built in unittest module
      -
    * - Compatible with nose
      -
    * - Powerful and easy fixture(s) mechanism
      -
    * - Parameterized tests
      -
    * - Grouping and marking of tests for different executions
      -
    * - Supports pyproject.toml
      -
    * - Extensible through plugin mechanism
      -

Alternatives
~~~~~~~~~~~~
* pyunit_
* nose_

Documentation
_____________

What to say... we all want to have it and read it if we need it, but most of us don't want to write it.

.. figure:: https://imgs.xkcd.com/comics/manuals.png
   :alt: xkcd-1343
   :target: https://xkcd.com/1343/

   source: `xkcd.com <xkcd_>`_
   license: `CC BY-NC 2.5`_


Sphinx_
+++++++
`Project Homepage <Sphinx_www_>`_

Sphinx is widely used within the python space and outside of it, because it is very powerful.
Admittedly it's powerfulness comes with a cost of complexity for bigger setups.
Still the overall the benefits outweigh the cost, and with the detail in mind that
lots of projects are using sphinx it is worth the effort to learn and use it.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Widely used
      - Additional dependency
    * - Lots of extensions
      - Restructured text can be quirky at times
    * - Lots of output formats are supported
      - Lots to learn/know regarding .rst and sphinx
    * - Basics are easy to learn
      -
    * - Extensions for api documentation
      -
    * - Plugin mechanism
      -

Alternatives
~~~~~~~~~~~~

* `mkdocs <https://github.com/mkdocs/mkdocs>`_
* `pydoc <https://pdoc.dev/docs/pdoc.html>`_


Furo_
+++++++
`Project Homepage <Furo_www_>`_

To provide a common look and feel between projects and between different versions of the project,
we have chosen to use a common sphinx theme.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Readable font
      - Additional dependency
    * - Well arranged page structure
      - Not a built-in theme
    * - Lots of output formats are supported
      -
    * - Dark-mode support
      -
    * - Autodetect for dark mode
      -
    * - Popular theme
      -

Alternatives
~~~~~~~~~~~~

* `builtin themes <https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes>`_
* `rtd-theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_


sphinx-github-pages-generator_
++++++++++++++++++++++++++++++
`Project Homepage <sphinx-github-pages-generator_www_>`_

Once various versions of a project are published, different users of the library
use different versions
To provide a common look and feel between projects and between different versions of the project,
we have chosen to use a common sphinx theme.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Multi version support
      - Early development
    * - Writen and maintained by exasol
      -

Alternatives
~~~~~~~~~~~~

* `sphinx-multiversion <https://holzhaus.github.io/sphinx-multiversion/master/index.html>`_
* `sphinxcontrib-versioning <https://sphinxcontrib-versioning.readthedocs.io/en/latest/>`_


Dependencies & Packaging
________________________

.. figure:: https://imgs.xkcd.com/comics/dependency.png
   :alt: xkcd-2347
   :target: https://xkcd.com/2347/

   source: `xkcd.com <xkcd_>`_
   license: `CC BY-NC 2.5`_


Poetry_
+++++++
`Project Homepage <Poetry_www_>`_

Poetry has a very good package/version resolver and simplifies packaging and updating dependencies significantly.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Good dependency resolver
      - Fairly new, some edge cases my not supported yet
    * - Uses pyproject.toml for configuration
      - Toml file definition is less flexible than setup.py based one
    * - Takes care of project versioning
      - Editable and/or repo based install(s) are not possible "out of the box"?
    * - Dependency pinning
      - setup.py is still required for installations with older versions of pip
    * - Very active development & community
      -
    * - Good & Powerful CLI
      -
    * - No manual dependency editing required
      -

Alternatives
~~~~~~~~~~~~

* `pipenv <https://pipenv.pypa.io/en/latest/>`_


Code Health
___________

.. figure:: https://imgs.xkcd.com/comics/code_quality.png
   :alt: xkcd-2347
   :target: https://xkcd.com/2347/

   source: `xkcd.com <xkcd_>`_
   license: `CC BY-NC 2.5`_

Pylint_
+++++++
`Project Homepage <Pylint_www_>`_

Helps finding bugs and issues before they are a problem and improves overall code quality.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Lots of good warnings and hints
      - Extra dependency
    * - Extension mechanism (custom extensions e.g. perflint)
      - Extra learning curve not all messages maybe straight forward
    * - Rating check 0-10 makes it possible to steadily improve a code base
      -
    * - Compatible with sonar
      -
    * - Supports pyproject.toml
      -

Alternatives
~~~~~~~~~~~~

* `Flake8 <https://flake8.pycqa.org/en/latest/>`_
* `pydocstyle <http://www.pydocstyle.org/en/stable/>`_
* `Radon <https://radon.readthedocs.io/en/latest/>`_

Coverage_
+++++++++
`Project Homepage <Coverage_www_>`_

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Threshold can be asserted if "wanted"
      - Extra dependency
    * - Various output formats, compatible with coveralls.io
      -
    * - Supports pyproject.toml
      -
    * - Plugin mechanism available
      -

Alternatives
~~~~~~~~~~~~

* ¯\\_(ツ)_/¯

MyPy_
+++++
`Project Homepage <MyPy_www_>`_

Having type hints (information) is nice help, but having it actually checked finds errors and makes sure the type hints are correct.

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Enforced type checking makes sure type annotations are correct
      - Extra configuration, makes workspace more complex
    * - Prevents potential bugs
      - Projects without any type annotations so far need migration strategy

Alternatives
~~~~~~~~~~~~

* `pytype <https://github.com/google/pytype>`_ (google)
* `pyright <https://github.com/Microsoft/pyright>`_ (microsoft)
* `pyre-check <https://github.com/facebook/pyre-check>` (facebook, contains security checking too)
* IDE built in e.g. PyCharm

Sonar_
++++++
`Project Homepage <Sonar_www_>`_

Used by other Exasol projects, therefore it provides a "generic insight" about the "code health" for all of our project(s).

Pros & Cons
~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - Pros ✅
      - Cons ❌
    * - Comply with most other projects which already use it
      -
    * - Simplify general view on code health across projects and languages
      -


.. _Nox_www: https://nox.thea.codes/en/stable/
.. _Black_www: https://black.readthedocs.io/en/stable/
.. _Isort_www: https://pycqa.github.io/isort/
.. _Sphinx_www: https://www.sphinx-doc.org/en/master/
.. _Pytest_www: https://docs.pytest.org/en/7.1.x/
.. _Poetry_www: https://python-poetry.org/
.. _Pylint_www: https://pylint.pycqa.org/en/latest/
.. _Coverage_www: https://coverage.readthedocs.io/en/6.3.2/
.. _MyPy_www: http://mypy-lang.org/
.. _PreCommit_www: https://pre-commit.com/
.. _Sonar_www: https://sonarcloud.io/
.. _autopep8: https://github.com/hhatto/autopep8
.. _yapf: https://github.com/google/yapf
.. _pyunit: https://docs.python.org/3/library/unittest.html
.. _nose: https://docs.nose2.io/en/latest/
.. _xkcd: https://xkcd.com/
.. _CC BY-NC 2.5: https://creativecommons.org/licenses/by-nc/2.5/
.. _Pyupgrade_www: https://github.com/asottile/pyupgrade
.. _Furo_www: https://github.com/pradyunsg/furo
.. _sphinx-github-pages-generator_www: https://github.com/exasol/sphinx-github-pages-generator