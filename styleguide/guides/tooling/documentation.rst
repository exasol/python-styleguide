📚 Documentation
================

What to say... we all want to have it and read it if we need it, but most of us don't want to write it.

.. figure:: https://imgs.xkcd.com/comics/manuals.png
   :alt: xkcd-1343
   :target: https://xkcd.com/1343/

   source: `xkcd.com <xkcd_>`_
   license: `CC BY-NC 2.5`_


Sphinx
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


Furo
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


sphinx-github-pages-generator
+++++++++++++++++++++++++++++
`Project Homepage <sphinx-github-pages-generator_www_>`_

Once various versions of a project are published, different users of the project use different versions of it.
Therefore the need to consult different versions of the project documentation arises.
The *sphinx-github-pages-generator* addresses this issue by generating documentation for all the different versions
in one place.

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


.. _xkcd: https://xkcd.com/
.. _CC BY-NC 2.5: https://creativecommons.org/licenses/by-nc/2.5/
.. _Sphinx_www: https://www.sphinx-doc.org/en/master/
.. _Furo_www: https://github.com/pradyunsg/furo
.. _sphinx-github-pages-generator_www: https://github.com/exasol/sphinx-github-pages-generator
