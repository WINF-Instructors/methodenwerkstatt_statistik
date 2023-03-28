from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()

s3_bucket = "s3://my-bucket/"
input_file_path = s3_bucket + "input_file.txt"

text_file = spark.read.text(input_file_path)
word_counts = text_file.rdd.flatMap(lambda line: line.value.split()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)
word_counts.saveAsTextFile(s3_bucket + "output")

spark.stop()