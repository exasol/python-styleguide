:ref:`Nox <guides/tooling/automation:Nox>`
==========================================

* All important task(s) should have a target
  (e.g.: Test, Integration Tests, Release, Docs, Githook(s) Install, ...)
* CI/CD [GH-Actions] builds must invoke those task(s)/targets for verification
  (e.g. nox -s run-all-tests)
* Ideally all "complex" task(s) run/triggered by the dev should have a nox target

.. attention:: **Todo:** List of common task each  project needs to support e.g. build, run
