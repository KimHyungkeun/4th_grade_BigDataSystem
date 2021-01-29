-- Databricks notebook source
-- MAGIC %fs head /mnt/davis/fire-calls/fire_calls_truncated_comma.csv

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS Databricks

-- COMMAND ----------

USE Databricks

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS fireCalls
USING csv
OPTIONS (
  header "true",
  path "/mnt/davis/fire-calls/fire_calls_truncated_comma.csv",
  inferSchema "true"
  )

-- COMMAND ----------

SELECT * FROM fireCalls LIMIT 10

-- COMMAND ----------

describe fireCalls

-- COMMAND ----------

select `Neighborhooods - Analysis Boundaries` as neighborhood from fireCalls 

-- COMMAND ----------

select `Neighborhooods - Analysis Boundaries` as neighborhood,
  count(`Neighborhooods - Analysis Boundaries`) as count
from FireCalls
group by `Neighborhooods - Analysis Boundaries`
order by count desc

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS firecallsuploaded
USING csv
OPTIONS (
  header "true",
  path "/FileStore/tables/fire_calls_truncated_comma-1.csv",
  inferSchema "true"
  )

-- COMMAND ----------

select `call type`, count('Call Type') as count
from firecallsuploaded
group by `call type`
order by count desc

-- COMMAND ----------

select `Neighborhooods - Analysis Boundaries` as neighborhood,
  count("neighborhood") as count
from firecallsuploaded
group by neighborhood
order by count desc

-- COMMAND ----------

select count(*) from fireCalls

-- COMMAND ----------

-- DBTITLE 1,Caching (캐싱을 하면 속도가 좀 더 빨라짐)
cache table firecalls

-- COMMAND ----------

select count(*) from fireCalls

-- COMMAND ----------

-- DBTITLE 1,Lazy cache (limit 100으로 했다면 100개 row를 다룰정도만 캐시를 한다)
uncache table firecalls

-- COMMAND ----------

cache lazy table firecalls

-- COMMAND ----------

select * from firecalls limit 100

-- COMMAND ----------

clear cache

-- COMMAND ----------

select count(*) from firecalls

-- COMMAND ----------

cache table firecalls

-- COMMAND ----------

select count(*) from firecalls

-- COMMAND ----------

clear cache

-- COMMAND ----------

-- DBTITLE 1,Shuffle partitions
select `call type`, count(*) as count
from firecalls
group by `call type`
order by count desc

-- COMMAND ----------

-- DBTITLE 1,Control shuffle partition
SET spark.sql.shuffle.partitions=8

-- COMMAND ----------

select `call type`, count(*) as count
from firecalls
group by `call type`
order by count desc

-- COMMAND ----------

-- DBTITLE 1,Check automatic broadcast size
-- MAGIC %python
-- MAGIC spark.conf.get('spark.sql.autoBroadcastJoinThreshold')

-- COMMAND ----------

SET spark.sql.shuffle.partitions=8

-- COMMAND ----------

select `Neighborhooods - Analysis Boundaries` as neighborhood,
  count("neighborhood") as count
from firecallsuploaded
group by neighborhood
order by count desc

-- COMMAND ----------

-- uncache table firecallsuploaded
-- cache lazy table firecallsuploaded
clear cache

-- COMMAND ----------

select `call type`, count(*) as count
from firecalls
group by `call type`
order by count desc

-- COMMAND ----------


