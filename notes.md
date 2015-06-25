# Spark talk

## Commands

### Startup

PYSPARK_DRIVER_PYTHON=ipython  PYSPARK_DRIVER_PYTHON_OPTS="notebook" \
~/src/spark-1.3.1/bin/pyspark --packages org.apache.spark:spark-streaming-kafka_2.10:1.3.1

### MongoDB Demos

spark-submit \
--jars /home/dirk/Downloads/mongo-hadoop-core-1.3.2.jar,\
/home/dirk/Downloads/mongo-java-driver-3.0.2.jar mongodb-demo.py

spark-submit \
--jars /home/dirk/Downloads/mongo-hadoop-core-1.3.2.jar,\
/home/dirk/Downloads/mongo-java-driver-3.0.2.jar mongo-ml.py

## Things to show

- Basic usage (ipython notebooks)
  - some mapreduce -- word count
  - more advanced functions

- MLLIB

- Spark streaming

- Data sources (mongodb)

- Unit testing

- Amazon cluster
