from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("KafkaTemperatureMonitor") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .getOrCreate()

schema = StructType() \
    .add("sensor_id", StringType()) \
    .add("temperature", IntegerType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor-suhu") \
    .option("startingOffsets", "earliest") \
    .load()

parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")) \
              .select("data.sensor_id", "data.temperature")

alert_df = parsed_df.filter(col("temperature") > 80)

query = alert_df.writeStream \
                .outputMode("append") \
                .format("console") \
                .start()

query.awaitTermination()