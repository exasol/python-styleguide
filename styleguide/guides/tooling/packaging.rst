Dependencies & Packaging
========================

.. figure:: https://imgs.xkcd.com/comics/dependency.png
   :alt: xkcd-2347
   :target: https://xkcd.com/2347/

   source: `xkcd.com <xkcd_>`_
   license: `CC BY-NC 2.5`_


Poetry
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

.. _Poetry_www: https://python-poetry.org/
.. _xkcd: https://xkcd.com/
.. _CC BY-NC 2.5: https://creativecommons.org/licenses/by-nc/2.5/
