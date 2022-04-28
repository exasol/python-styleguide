Exasol python-styleguide
========================
Welcome to the Exasol_ python-styleguide.
The styleguide(s) is not intend to be an universal text on how to do each single detail in python,
it rather tries to rely on existing documents and guides references them (e.g. pep8_) and their rules or it
will add useful additions or exceptions where Exasol_ is diverging from the *"norm"* and will explain the reasons behind.
commonly used patterns and style like pep8.


Build the Guide
---------------

#. Install the development dependencies

    .. code-block::

        poetry install

#. Build and open the styleguide

    .. code-block::

        nox

.. note:: Get help on the available actions

    .. code-block::

        nox -h

.. _Exasol: https://www.exasol.com/
.. _pep8: https://peps.python.org/pep-0008/