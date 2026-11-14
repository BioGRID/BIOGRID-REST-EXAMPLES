# BIOGRID-REST-EXAMPLES
Sample code for accessing the BioGRID Rest Service and working with the resulting datasets.

## Development Status
+ **Status**: Stable
+ **Version**: 2.0

## Requirements
+ Python 3.12+
+ [uv](https://docs.astral.sh/uv/) for Python and dependency management. Install it with `curl -LsSf https://astral.sh/uv/install.sh | sh` (see the uv docs for other options).
+ Dependencies are declared in `pyproject.toml` and pinned in `uv.lock`: [httpx](https://www.python-httpx.org/) for HTTP requests, [loguru](https://loguru.readthedocs.io/) for logging, [pandas](https://pandas.pydata.org/) and [polars](https://pola.rs/) for dataframes, and PyYAML for configuration.

## Installation
From inside this directory, run:

```bash
uv sync
```

This installs Python 3.12 (if needed), creates a `.venv` virtual environment, and installs all dependencies, including the development tools.

## Configuration
+ All configuration options are located in the config/config.sample.yml file in YAML format. Simply copy the file to config/config.yml and update the options contained within to reflect your own environment.
+ All access to the BioGRID REST Webservice requires an individual access key. It's free to signup to use it. You will need to register at **https://webservice.thebiogrid.org/** to obtain one, and enter it in your config file for it to be accessible from all example code in this repository.
+ For a listing of all configurable search parameters when making requests, visit our wiki: **https://wiki.thebiogrid.org/doku.php/biogridrest**

## How to Run
After completing the installation and configuration steps above, run any script with `uv run`:

```bash
uv run python get_organisms.py
```

+ All output, including the API results, is written to stdout through loguru.
+ Set the `LOG_LEVEL` environment variable to `DEBUG` to also see each request (with your access key redacted), its status, and its timing, e.g. `LOG_LEVEL=DEBUG uv run python get_organisms.py`.
+ Requests time out after 30 seconds (10 seconds to connect). An HTTP error status, a timeout, or a missing/invalid access key is logged as an error and the script exits with a non-zero status.

## Development
Linting and formatting use [Ruff](https://docs.astral.sh/ruff/), configured in `pyproject.toml`:

```bash
uv run ruff check .
uv run ruff format .
```

To add a new dependency, use `uv add <package>` (or `uv add --dev <package>` for development tools).

## Examples
+ [**get_experimental_evidence_types.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_experimental_evidence_types.py) - Obtain a list of the supported experimental evidence types in BioGRID
+ [**get_identifier_types.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_identifier_types.py) - Obtain a list of the supported identifier types in BioGRID
+ [**get_interaction.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_interaction.py) - Obtain a single interaction record by interaction id
+ [**get_interactions_by_gene.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_interactions_by_gene.py) - Obtain a list of interactions by one or more gene identifiers
+ [**get_interactions_by_pubmed.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_interactions_by_pubmed.py) - Obtain a list of interactions by one or more pubmed ids
+ [**get_interactions_for_pandas.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_interactions_for_pandas.py) - Obtain a list of interactions and add them to a pandas dataframe
+ [**get_interactions_for_polars.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_interactions_for_polars.py) - Obtain a list of interactions and add them to a polars dataframe
+ [**get_organisms.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_organisms.py) - Obtain currently supported organism names and ids
