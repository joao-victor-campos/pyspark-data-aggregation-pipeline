
# Pyspark Data Aggregation Pipeline
![Python Version](https://img.shields.io/badge/python-3.10-green)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![aa](https://img.shields.io/badge/code%20quality-flake8-blue)](https://github.com/PyCQA/flake8)
[![Checked with mypy](https://camo.githubusercontent.com/59eab954a267c6e9ff1d80e8055de43a0ad771f5e1f3779aef99d111f20bee40/687474703a2f2f7777772e6d7970792d6c616e672e6f72672f7374617469632f6d7970795f62616467652e737667)](http://mypy-lang.org/)

[Build Status](https://github.com/joao-victor-campos/pyspark-data-aggregation-pipeline/actions):

| Core     | Docker Image 
| -------- | -------- 
| [![Tests](https://github.com/joao-victor-campos/pyspark-data-aggregation-pipeline/actions/workflows/teste.yaml/badge.svg)](https://github.com/joao-victor-campos/pyspark-data-aggregation-pipeline/actions/workflows/teste.yaml)     | [![Docker Image](https://github.com/joao-victor-campos/pyspark-data-aggregation-pipeline/actions/workflows/docker_image.yaml/badge.svg)](https://github.com/joao-victor-campos/pyspark-data-aggregation-pipeline/actions/workflows/docker_image.yaml)    

## Introduction
Repo to save our pyspark pipeline project. Created with the intention to put to life our studies in python, pyspark,  ETL process and software engineering skills in general, such as units and integration test, CI, Docker and code quality.

## Running the pipeline

#### Clone the project:

```bash
git clonegit@github.com:joao-victor-campos/pyspark-data-aggregation-pipeline.git
cd pyspark-data-aggregation-pipeline
```

#### Build docker image 

```
docker build -t pyspark-data-aggreagation-pipeline .
```
#### Run app in docker 

```
docker run pyspark-data-aggreagation-pipeline 
```
## Pipeline execution finished!!! 

## Development

### Install dependencies

```bash
make requirements
```

### Code Style
Apply code style with black and isort
```bash
make apply-style
```

Perform all checks (flake8, black and mypy)
```bash
make checks
```

### Testing and Coverage
Unit tests:
```bash
make unit-tests
```
Integration tests:
```bash
make integration-tests
```
All (unit + integration) tests:
```bash
make tests
```

Test coverage:
```bash
make tests-coverage
```

