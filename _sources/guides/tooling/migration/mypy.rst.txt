:ref:`MyPy <guides/tooling/code-health:MyPy>`
=============================================

#. Add mypy as `dev` dependency

#. Add mypy configuration to project

    .. code-block:: toml

        [tool.mypy]
        files = [
            'noxfile.py',
        ]

#. Add a nox target for typecheck.

    .. code-block:: python

        @nox.session(python=False)
        def typecheck(session: Session) -> None:
            session.run(
                "poetry",
                "run",
                "mypy",
                "--strict",
                "--show-error-codes",
                "--pretty",
                "--show-column-numbers",
                "--show-error-context",
                "--scripts-are-modules",
            )

#. Typechecking now can be introduced step by step by adding new files to the checklist

    .. code-block:: toml

        [tool.mypy]
        files = [
            ...
            'scripts/**/*.py',
        ]


