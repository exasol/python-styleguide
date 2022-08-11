Code Style
==========

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

Black
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

Isort
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

Pyupgrade
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

.. _autopep8: https://github.com/hhatto/autopep8
.. _yapf: https://github.com/google/yapf
.. _Black_www: https://black.readthedocs.io/en/stable/
.. _Isort_www: https://pycqa.github.io/isort/
.. _Pyupgrade_www: https://github.com/asottile/pyupgrade
.. _xkcd: https://xkcd.com/
.. _CC BY-NC 2.5: https://creativecommons.org/licenses/by-nc/2.5/
