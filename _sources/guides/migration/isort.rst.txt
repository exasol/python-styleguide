:ref:`Isort <guides/tooling/code-style:Isort>`
=============================================

* Executing the import formatter :ref:`guides/tooling:Isort` should be part of at least 2 targets (fix, check)

    - check: check that all source files comply with the expected format
    - fix: run code formatting on all required files to comply with the expected code format

    .. note::

        A project may decide for itself to run e.g. `fix` as a commit hook.
        The check must be run as part of the CI/CD pipeline though.

* Make sure :ref:`guides/tooling:Isort` is run with the *black* profile


configuration
~~~~~~~~~~~~~

.. code-block:: toml

    [tool.isort]
    profile = "black"
    force_grid_wrap = 2


