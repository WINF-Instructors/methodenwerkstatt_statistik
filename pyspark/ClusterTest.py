from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySpark Test Job").getOrCreate()

data = [("Alice", 1), ("Bob", 2), ("Charlie", 3), ("Dave", 4), ("Eva", 5)]
df = spark.createDataFrame(data, ["name", "age"])
df.show()


df = spark.read.options(delimiter=",",header=True).csv("s3a://statistics-workshop/pay_gap_Europe.csv")
df.show()


df.printSchema()
df.columns


import pyspark.sql.types as t
import pyspark.sql.functions as f

df = df.select("Country","Year","GDP")
df = df.withColumn("Year",f.col("Year").cast(t.IntegerType())).withColumn("GDP",f.col("GDP").cast(t.IntegerType()))
df.show()


df2 = df.groupBy("Country").mean("GDP")
df2.show()

df.createOrReplaceTempView("table1")
df2 = spark.sql("SELECT Country From table1")
df2.show()
