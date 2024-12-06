FROM apache/airflow:2.10.3

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       openjdk-17-jre-headless \
       wget \
       ssh \
       rsync \
    && wget https://archive.apache.org/dist/hadoop/core/hadoop-3.4.1/hadoop-3.4.1.tar.gz \
    && tar -xzvf hadoop-3.3.1.tar.gz \
    && mv hadoop-3.4.1 /opt/hadoop \
    && rm hadoop-3.4.1.tar.gz \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
ENV HADOOP_COMMON_HOME=$HADOOP_HOME
ENV HADOOP_HDFS_HOME=$HADOOP_HOME
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_YARN_HOME=$HADOOP_HOME

USER airflow

