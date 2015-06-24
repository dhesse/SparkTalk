"""Python Spark demo, finding the most followed twitter user we have
on record, reading twitter data from MongoDB.

NOTE: pyspark is not supported as of now by spark-mongodb. Use

spark-submit \
--jars /home/dirk/Downloads/mongo-hadoop-core-1.3.2.jar,\
/home/dirk/Downloads/mongo-java-driver-3.0.2.jar mongodb-demo.py

to run.
"""
from pyspark import SparkContext

def formatFollowerRecord(record):
    rank, (name, followers) = record
    name = name.encode('ascii', 'ignore')
    return "{0}: {1}, {2}".format(rank + 1, name, followers)

if __name__ == "__main__":
    sc = SparkContext()
    config ={"mongo.input.uri": "mongodb://localhost:27017/twitter.no"}
    inputFormatClassName = "com.mongodb.hadoop.MongoInputFormat"
    keyClassName = "org.apache.hadoop.io.Text"
    valueClassName = "org.apache.hadoop.io.MapWritable"

    RawRDD = sc.newAPIHadoopRDD(inputFormatClassName,
                            keyClassName,
                            valueClassName,
                            None, None, config)
    mostFollowers = RawRDD\
        .map(lambda x: (x[1]['user']['name'],
                        x[1]['user']['followers_count']))\
        .foldByKey(0, max)\
        .sortBy(lambda x: x[1], ascending=False)\
        .take(20)
    
    with open("most_followed.txt", "w") as of:
        of.write("\n".join(formatFollowerRecord(r)
                           for r in enumerate(mostFollowers)))
