"""Taken from the word-count example in the spark distro."""

from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    sc = SparkContext(appName="PythonStreamingKafkaWordCount")
    ssc = StreamingContext(sc, 5)

    zkQuorum, topic = "localhost:2181", "twitter_sample"
    twitterStream = KafkaUtils.createStream(ssc, zkQuorum,
                                  "spark-streaming-consumer", {topic: 1})
    twitterStream.pprint()
    ssc.start()
    ssc.awaitTermination()
