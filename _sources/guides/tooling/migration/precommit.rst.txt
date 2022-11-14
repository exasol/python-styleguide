:ref:`PreCommit <guides/tooling/automation:precommit>`
======================================================

Replace existing copies of commit hooks by referencing them in a "central" repository.

configuration
~~~~~~~~~~~~~

.. code-block::

    default_stages: [push]
    repos:
    - repo: local
      hooks:

    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.2.0
        hooks:
        -   id: check-yaml
        -   id: end-of-file-fixer
        -   id: trailing-whitespace
            exclude: ^test/integration

