from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySpark Test Job").getOrCreate()

data = [("Alice", 1), ("Bob", 2), ("Charlie", 3), ("Dave", 4), ("Eva", 5)]
df = spark.createDataFrame(data, ["name", "age"])
df.show()

spark.stop()