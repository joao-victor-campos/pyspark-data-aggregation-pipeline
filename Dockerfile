FROM openjdk:11 as dependencies
COPY --from=python:3.10.4 / /

COPY ./requirements.txt /pyspark-data-aggregation-pipeline/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /pyspark-data-aggregation-pipeline/requirements.txt

COPY . /pyspark-data-aggregation-pipeline
RUN pip install /pyspark-data-aggregation-pipeline/.

WORKDIR /pyspark-data-aggregation-pipeline
CMD ["python", "./scripts/deaths_per_year_run.py"]