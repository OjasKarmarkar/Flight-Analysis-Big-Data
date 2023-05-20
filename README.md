# Creating a Real-Time Flight-info Data Pipeline with Kafka, Apache Spark, Elasticsearch and Kibana

In this project, we will use a real-time flight tracking API, Apache Kafka, ElastichSearch and Kibana to create a real-time Flight-info data pipeline and track the flights in real-time. We will use a high-level architecture and
corresponding configurations that will allow us to create this data pipeline. The end result will be a Kibana dashboard fetching real-time data from ElasticSearch.

## Pipeline
Our project pipeline is as follows:

![image](https://github.com/OjasKarmarkar/Flight-Analysis-Big-Data/assets/91938852/478140eb-7804-4c2d-b878-b0e08d1cc08a)


## Prerequisites
The following software should be installed on your machine in order to reproduice our work:

- Spark (spark-3.3.1-bin-hadoop2.7)
- Kafka (kafka_2.13-2.7.0)
- ElasticSearch (elasticsearch-7.14.2)
- Kibana (kibana-7.14.2)
- Python 3.9.6
## Steps
###### Get Flight API:
We started by collecting in real-time Flight informations (Aircraft Registration Number,Aircraft Geo-Latitude,Aircraft Geo-Longitude,Aircraft elevation,Flight numbe...) and then we sent them to Kafka for analytics.

###### Kafka Real-Time Producer:
The data is ingested from the flight streaming data API and sent to a kafka topic. You need to run Kafka Server with Zookeeper and create a dedicated topic for data transport.
###### PySpark Streaming:
 In Spark Streaming, Kafka consumer is created that periodically collect data in real time from the kafka topic and send them into an Elasticsearch index.
###### Index flight-info to Elasticsearch:
You need to enable and start Elasticsearch and run it to store the flight-info and their realtime information for further visualization purpose. You can navigate to http://localhost:9200 to check if it's up and running.
###### Kibana for visualization
Kibana is a visualization tool that can explore the data stored in elasticsearch. In our project, instead of directly output the result, we used this visualization tool to visualize the streaming data in a real-time manner.You can navigate to http://localhost:5601 to check if it's up and running.

## How to run
1. Start Elasticsearch

`sudo systemctl start elasticsearch ` & `sudo systemctl enable elasticsearch `

2. Start Kibana

`sudo systemctl start kibana ` & `sudo systemctl enable kibana  `

3. Start Zookeeper server by moving into the bin folder of Zookeeper installed directory by using:

`./bin/zookeeper-server-start.sh ./config/zookeeper.properties`

4. Start Kafka server by moving into the bin folder of Kafka installed directory by using:

`./bin/kafka-server-start.sh ./config/server.properties`

5. Run Kafka producer:

`python3 ./producer.py`

6. Run PySpark consumer with spark-submit:

`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1,org.elasticsearch:elasticsearch-spark-30_2.12:7.14.2 /consumer.py`

## How to launch kibana dashboard

- Open http://localhost:5601/ in your browser.
- Go to Management>Kibana>Saved Objects
- Import dashboard.ndjson
- Open dashboard

## Final result
![image](https://github.com/OjasKarmarkar/Flight-Analysis-Big-Data/assets/36037604/edbb0ff7-9cbb-4c37-9024-97d14bd706bf)
![image](https://github.com/OjasKarmarkar/Flight-Analysis-Big-Data/assets/36037604/3bad2a7f-7e66-46a4-b63b-f0cf3c6b6659)







