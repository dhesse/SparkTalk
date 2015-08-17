# An Introduction to Apache Spark

Dirk Hesse 

Data Scientist / Intelligent Communication AS

[dirk.hesse@intelcom.no](mailto:dirk.hesse@intelcom.no "Send me a
mail") | [@NotDirkHesse](https://twitter.com/NotDirkHesse "I tweet sporadically")

---

## Outline

### A highly personal view on Spark

- What is Spark?
- Mandatory word count example.
- Spark's MLLIB.
- Getting data into Spark.
- Spark streaming.
- Spark and unit testing.
- Cluster deployment.

---

![Spark Logo](https://raw.githubusercontent.com/dhesse/SparkTalk/master/img/spark-logo.png)

From [spark.apache.org](http://spark.apache.org/)

> Apache Spark™ is a fast and general engine for large-scale data
> processing.

---

## So what *is* Spark?!

Spark helps analyzing big data sets

- from **heterogeneous** data sources,
- **in memory**,
- in *Java*, *Scala*, <font color="red">*Python*</font>, and *R*
- with many back-ends and extensions.

![Spark Modules](https://raw.githubusercontent.com/dhesse/SparkTalk/master/img/ecosystem.png)

---

## Let's use it to count words!

[Live Demo](https://github.com/dhesse/SparkTalk/blob/master/nbhome/WordCount.ipynb)

---

## SparkContext and RDD
## An Inside Look

[Live Demo](https://github.com/dhesse/SparkTalk/blob/master/nbhome/A%20Nerdy%20Look%20at%20SC%20and%20RDD.ipynb)


---

## Monitoring

Spark makes it very easy to
[monitor](https://spark.apache.org/docs/latest/monitoring.html) your
cluster.

---

# MLLIB: Built-in Machine Learning

Spark comes with machine learning on-board:

- **Classification**: Logistic Regression, SVM, Naïve Bayes
- **Clustering**: K-Means, Gaussian Mixture
- **Regression**: Linear, Ridge, Lasso, Isotonic
- **Trees**: Decision Tree, Random Forest, Gradient Boosted
- **Recommendation**: Matrix Factorization only

All easy(ish) to use.

---

# MLLIB

[Live Demo](https://github.com/dhesse/SparkTalk/blob/master/nbhome/MLLIB.ipynb)

In which we predict survival of the **Titanic** disaster.

Our **data** looks like this:

<pre>
PassengerId; Survived; Pclass; Name; Sex; Age; SibSp; Parch; Ticket; Fare; Cabin; Embarked
1; 0; 3; Braund, Mr. Owen Harris; male; 22; 1; 0; A/5 21171; 7.25; ; S
2; 1; 1; Cumings, Mrs. John Bradley (Florence Briggs Thayer); female; 38; 1; 0; PC 17599; 71.2833; C85; C
3; 1; 3; Heikkinen, Miss. Laina; female; 26; 0; 0; STON/O2. 3101282; 7.925; ; S
4; 1; 1; Futrelle, Mrs. Jacques Heath (Lily May Peel); female; 35; 1; 0; 113803; 53.1; C123; S
</pre>

Now use *logistic regression* to predict if a person survives. 

---

## Getting data into Spark

In addition to methods in `SparkContext`, **tons** of **libraries**
exist, e.g.

<table>
<tr>
<td>

<ul>
<li> spark-avro
<li> spark-redshift
<li> spark-mongodb
<li> spark-csv
<li> spark-sequoiadb
</ul>

<td>

<ul>
<li> spark-cassandra-connector
<li> elasticsearch-hadoop
<li> pyspark-elastic
<li> spark-cloudant
<li> couchbase-spark-connector
</ul>

</tr>
</table>

---

## Digression: Why I like MongoDB

If you write a lot of Python Code, MongoDB is a *great* way to store
data.

- MonogDB is lightning fast
- MongoDB is easy to set up and use
- MongoDB is tried and trusted
- It plays nice with Python

---

## Twitter Data

Our workflow:

![Twitter to MongoDB](https://raw.githubusercontent.com/dhesse/SparkTalk/master/img/twitter-mongo-workflow.png)


---

## Most Wanted

A twitter user as provided by the twitter API looks like this:

    user { name: "Dirk Hesse",
           screen_name: "NotDirkHesse",
           geo_enabled: ...,
           followers_count: 42 }

We want to search our records for the user with the most followers...

---

## Spark Streaming

From [spark.apache.org](http://spark.apache.org/)

> Spark Streaming makes it easy to build scalable fault-tolerant
> streaming applications.

Which is *nice* but the power lies within the fact that it's

![Spark Logo](https://raw.githubusercontent.com/dhesse/SparkTalk/master/img/spark-logo.png)

---

## Spark Streaming Example

We collect some twitter data and select some *strange* features. From
those we grow a **decision tree** to **predict** the *language* .

    { text: "#WhoahDude, how cool is #ApacheSpark?!!!",
      lang: "en",
      entities: { hashtags: [{text: "WoahDude", ... }
                             {text: "ApackeSpark", ...}]
                }, ...
    }

We then use Spark Streaming to **tag**  incoming Tweets with the
*language* **predicted** by our **tree**.

---

## Executive Workflow

![Second Workflow](https://raw.githubusercontent.com/dhesse/SparkTalk/master/img/twitter-stream-workflow.png)

[Demo](https://github.com/dhesse/SparkTalk/blob/master/nbhome/Streaming.ipynb)

---

## Spark and Unit Testing

- You should unit test your code.
- No, really, you **should**!
- Spark and Python make this very easy.

[Demo](https://github.com/dhesse/SparkTalk/blob/master/nbhome/Unit%20Testing.ipynb)

---

## Deploying on a cluster

Currently you have **three main options**

- **spark-ec2** *included* in the Spark distribution
  - Script that lets you set cluster details from the command line
- **Amazon EMR**
  - Set up via amazon Web console
- **Hack your own**
  - *Good luck!*

In the near future: **IBM Bluemix**

---

# Questions?!

---

# Thank you!
## PS: We're hiring!

Drop me an email at [dirk.hesse@intelcom.no](mailto:dirk.hesse@intelcom.no "Send me a
mail").
