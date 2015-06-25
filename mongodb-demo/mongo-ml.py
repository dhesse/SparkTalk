"""Python Spark demo, training a decision tree to detect the
language.

NOTE: pyspark is not supported as of now by spark-mongodb. Use

spark-submit \
--jars /home/dirk/Downloads/mongo-hadoop-core-1.3.2.jar,\
/home/dirk/Downloads/mongo-java-driver-3.0.2.jar mongo-ml.py

to run.
"""
from pyspark import SparkContext
from pyspark.mllib.tree import DecisionTree
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.regression import LabeledPoint

LANG_CODES = ['und', # 'undefined' is 0
              'ab', 'aa', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy',
              'as', 'av', 'ae', 'ay', 'az', 'bm', 'ba', 'eu', 'be',
              'bn', 'bh', 'bi', 'bs', 'br', 'bg', 'my', 'ca', 'ch',
              'ce', 'ny', 'zh', 'cv', 'kw', 'co', 'cr', 'hr', 'cs',
              'da', 'dv', 'nl', 'dz', 'en', 'eo', 'et', 'ee', 'fo',
              'fj', 'fi', 'fr', 'ff', 'gl', 'ka', 'de', 'el', 'gn',
              'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hu', 'ia',
              'id', 'ie', 'ga', 'ig', 'ik', 'io', 'is', 'it', 'iu',
              'ja', 'jv', 'kl', 'kn', 'kr', 'ks', 'kk', 'km', 'ki',
              'rw', 'ky', 'kv', 'kg', 'ko', 'ku', 'kj', 'la', 'lb',
              'lg', 'li', 'ln', 'lo', 'lt', 'lu', 'lv', 'gv', 'mk',
              'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mh', 'mn', 'na',
              'nv', 'nd', 'ne', 'ng', 'nb', 'nn', 'no', 'ii', 'nr',
              'oc', 'oj', 'cu', 'om', 'or', 'os', 'pa', 'pi', 'fa',
              'pl', 'ps', 'pt', 'qu', 'rm', 'rn', 'ro', 'ru', 'sa',
              'sc', 'sd', 'se', 'sm', 'sg', 'sr', 'gd', 'sn', 'si',
              'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'ss', 'sv',
              'ta', 'te', 'tg', 'th', 'ti', 'bo', 'tk', 'tl', 'tn',
              'to', 'tr', 'ts', 'tt', 'tw', 'ty', 'ug', 'uk', 'ur',
              'uz', 've', 'vi', 'vo', 'wa', 'cy', 'wo', 'fy', 'xh',
              'yi', 'yo', 'za', 'zu', 'in', 'iw', 'ckb']

labelOf = {code: i for i, code in enumerate(LANG_CODES)}

if __name__ == "__main__":
    sc = SparkContext()
    config ={"mongo.input.uri":
             "mongodb://localhost:27017/twitter.sample",
             "mongo.input.split.create_input_splits": "false",
             "mongo.input.notimeout": "true"}
    inputFormatClassName = "com.mongodb.hadoop.MongoInputFormat"
    keyClassName = "org.apache.hadoop.io.Text"
    valueClassName = "org.apache.hadoop.io.MapWritable"

    RawRDD = sc.newAPIHadoopRDD(inputFormatClassName,
                            keyClassName,
                            valueClassName,
                            None, None, config)
    trainingData = RawRDD.values()\
        .map(lambda x: LabeledPoint(
            labelOf[x['lang']],
            [len(x['entities']['hashtags']),
             len(x['entities']['user_mentions']),
             len(x['entities']['urls']),
             len(x['text'].split()),
             len((x['user']['description']
                  or "").split()),
             int(x['user']['favourites_count']),
             int(x['user']['followers_count']),
             int(x['user']['friends_count'])])).cache()
    model = DecisionTree.trainClassifier(trainingData, len(LANG_CODES), {})
    model.save(sc, "TwitterDecisionTree")
    
    
