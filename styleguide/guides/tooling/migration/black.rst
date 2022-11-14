:ref:`Black <guides/tooling/code-style:Black>`
===============================================

* Executing the code formatter :ref:`guides/tooling/code-style:Black` should be part of at least 2 targets (fix, check)
    - check: check that all source files comply with the expected format
    - fix: run code formatting on all required files to comply with the expected code format

.. note::

    A project may decide for itself to run e.g. `fix` as a commit hook.
    The check must be run as part of the CI/CD pipeline though.

.. attention::

    When running **black** initially on a project make sure to commit it
    with the `--ignore-rev` flag to avoid cluttering the git log/history.
    For more details see `Introducing Black to your project <https://black.readthedocs.io/en/stable/guides/introducing_black_to_your_project.html>`_.

configuration
~~~~~~~~~~~~~

.. code-block:: toml

    [tool.black]
    line-length = 88
    verbose = false
    include = "\\.pyi?$"

