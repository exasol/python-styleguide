Code Health
===========

.. figure:: https://imgs.xkcd.com/comics/code_quality.png
   :alt: xkcd-2347
   :target: https://xkcd.com/2347/

   source: `xkcd.com <xkcd_>`_
   license: `CC BY-NC 2.5`_

Pylint
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

MyPy
++++
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

Sonar
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

.. _Pylint_www: https://pylint.pycqa.org/en/latest/
.. _Coverage_www: https://coverage.readthedocs.io/en/6.3.2/
.. _MyPy_www: http://mypy-lang.org/
.. _Sonar_www: https://sonarcloud.io/
.. _xkcd: https://xkcd.com/
.. _CC BY-NC 2.5: https://creativecommons.org/licenses/by-nc/2.5/
