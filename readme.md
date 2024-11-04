# Tugas Implementasi Kafka dengan Pyspark

| Nama                            | NRP          |
| ------------------------------- | ------------ |
| Marcelinus Alvinanda Chrisantya | `5027221012` |

# Topik: Pengumpulan Data Sensor IoT dengan Apache Kafka
## Latar Belakang Masalah:

Sebuah pabrik memiliki beberapa mesin yang dilengkapi sensor suhu. Data suhu dari setiap mesin perlu dipantau secara real-time untuk menghindari overheating. Setiap sensor akan mengirimkan data suhu setiap detik, dan pabrik membutuhkan sistem yang dapat mengumpulkan, menyimpan, dan menganalisis data suhu ini.
## Studi Kasus Sederhana:

- Pabrik membutuhkan aliran data sensor yang dapat diteruskan ke layanan analitik atau dashboard secara langsung.
- Apache Kafka akan digunakan untuk menerima dan mengalirkan data suhu, sementara PySpark akan digunakan untuk mengolah dan memfilter data tersebut.

## Tugas:

1. **Buat Topik Kafka untuk Data Suhu:**
    - Buat topik di Apache Kafka bernama "sensor-suhu" yang akan menerima data suhu dari sensor-sensor mesin.

2. Simulasikan Data Suhu dengan Producer:
    - Buat producer sederhana yang mensimulasikan data suhu dari beberapa sensor mesin (misalnya, 3 sensor berbeda).
    - Setiap data suhu berisi ID sensor dan suhu saat ini (misalnya, sensor_id: S1, suhu: 70°C), dan dikirim setiap detik ke topik "sensor-suhu".

3. Konsumsi dan Olah Data dengan PySpark:
    - Buat consumer di PySpark yang membaca data dari topik "sensor-suhu".
    - Filter data suhu yang berada di atas 80°C, sebagai indikator suhu yang perlu diperhatikan.

4. Output dan Analisis:
    - Cetak data yang suhu-nya melebihi 80°C sebagai tanda peringatan sederhana di console.

# Konfigurasi Project
- Jalankan apache Kafka menggunakan file `docker-compose.yaml` yang ada dengan command `docker-compose up -d`

Berikut filenya:
```
version: '3'
services:
  broker:
    image: apache/kafka:latest
    container_name: broker
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_LISTENERS: PLAINTEXT://:9092,CONTROLLER://:9093
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@localhost:9093
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      KAFKA_NUM_PARTITIONS: 3
    ports:
      - "9092:9092"
      - "9093:9093"
```
- Selanjutnya jalankan program `kafka-admin.py`, untuk membuat topik sensor-suhu di dalam broker Kafka dengan command:

```
python kafka-admin.py
```

- Lalu jalankan program `kafka-producer.py`, untuk membuat data yang akan dikirimkan ke dalam topik sensor-suhu. Berikut commandnya:

```
python kafka-producer.py
```

- Dan akhirnya, jalankan program `kafka-consumer.py` untuk mengambil kemudian menampilkan data pada topik sensor-suhu (program ini dibuat untuk mengambil data secara real time, untuk mengambil data secara statis perlu konfigurasi lebih lanjut di dalam script). Berikut commandnya:

```
python kafka-consumer.py
```

# Hasil Simulasi
![Screenshot 2024-11-04 181029](https://github.com/user-attachments/assets/aaf528e9-5ac0-4834-a0b9-f3b60129e098)