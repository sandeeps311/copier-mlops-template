Changelog
=========

[[ UNRELEASED ]]
----------------

Breaking Changes:

Added:

Changed:

Deprecated:

Removed:

Fixed:

1.4.12
-----

Fixed:

* The ``CodeQuality`` task depends on meeting the ``Lint`` condition in the ``ci-release-python.yaml`` file.

Fixed:

1.4.11
-----

Changed:

* Update minimum numpy version to ``1.23.*``
* Add test cases to ensure numpy loads successfully

1.4.10
-----

Fixed:

* Update package version expectations based on scientific python deprecation schedule


1.4.9
-----

Fixed:

* Use matrix strategy for python tests


1.4.8
-----

Fixed:

* Resolve environment based on pinned numpy version in CI


1.4.7
-----

Fixed:

* Removed ``defaults`` conda channel


1.4.6
-----

Added:

* Default install ``opencensus-ext-azure`` in Dockerfile for Azure logging

1.4.5
-----

Changed:

* Commented "Add conda to PATH" to "test-python.yaml"
* Added "UsePythonVersion" to use specific version of python in tests
* Updated old numpy version ``1.21.*`` to ``1.23.*``


1.4.4
-----

Changed:

* Updated isort configuration for ruff
* Updated pre-commit config
* Updated .gitignore to ignore Azure ML files


1.4.3
-----

Changed:

* Updated isort configuration for ruff
* Updated pre-commit config

Fixed:

* ``python_version_path`` should use ``is_python_project``, not ``is_python_package``
* removed redundant packages from environment.yaml


1.4.2
-----

Fixed:

* Docker images now update ``/etc/apt/sources.list`` to resolve Debian distro update pointers
* Fixed ``docker_version_path`` issue in ``copier.yaml``


1.4.1
-----

Breaking Changes:

* Docker images use ``PMI_PIP_INDEX_URL`` instead of ``PIP_EXTRA_INDEX_URL`` to avoid autodetection


1.3.2
-----

Changed:

* Sort/update packages

Fixed:

* Remove .ci/ dir in favor of templated one

1.3.1
-----

Added:

* Add ``cmcrameri`` colormaps `ref <https://www.fabiocrameri.ch>`_.
* Pin ``newest_numpy_limit`` in CI and environment specifications

Changed:

* Bump pre-commit versions


1.2.2
-----

Changed:

* Pin mlflow==2.3.2 in environment specs

Fixed:

* Remove one of the duplicate ``./.ci/azure-pipeline-publish``


1.2.1
-----

Changed:

* Include ``matplotlib`` and ``seaborn`` as default requirements


1.2.0
-----

Changed:

* Update ``copier.yaml`` for copier v8.0.0


1.1.0
-----

Added:

* README.md template

Changed:

* Copier variables changed to accommodate logic changes
* updated default pmi-dtsc-requirements.txt to ``ds_utils>=1.0.0``
* improve logic for default responses
* docker question flow:
  * get docker_directory; dockerfile_path
* python question flow - separate "python project" from "python package"

Fixed:

* docker init should ensure that path/to/Dockerfile exists
* docs should not build if ``./docs`` does not exist


1.0.7
-----

Changed:

* documentation build should use tags for folder name

Fixed:

* build-docs should use ``common`` resource


1.0.6
-----

Changed:

* add sphinx dependencies to defaults


1.0.5
-----

Changed:

* specify oldest_supported_numpy as semver
* add pyyaml to default dependencies


1.0.4
-----

Changed:

* fix/remove deprecated files
* add template for docs


1.0.3
-----

Changed:

* clean up ``pmi-dtsc-requirements`` if not used in ``common``
* convert to ``hatchling`` for build
    * deprecate ``setup.cfg``
    * update ``pyproject.toml``


1.0.2
-----

Added:

* added ``snowflake-sqlalchemy`` to requirements.txt templates

Changed:

* ``azure-pipeline-publish.yaml`` jinja logic


1.0.1
-----

Added:

* added ``snowflake-sqlalchemy`` to environment.yamls and setup.cfg templates
* added ``copier`` question to template pmi-dtsc-requirements.txt

Changed:

* required ``redis-py>=4.5.5`` in environment.yamls and setup.cfg
* use pmi-dtsc-requirements.txt as a source when configuring CI environment


1.0.0
-----

Breaking Changes:

* ``azure-pipepine-publish`` and templates configure to use ``common`` as resource repository
* ``copier`` configuration yaml and templates

Changes:

* update README for new processes
* update / standardize configuration files and templates

0.0.1-rc3 (2022-10-27)
----------------------

Changes:

* bump dependencies


0.0.1-rc2 (2022-09-27)
----------------------

Added:

* test build for python
* test build for docker
* sonarqube integration


0.0.1-rc1 (2022-09-13)
----------------------

* First release
