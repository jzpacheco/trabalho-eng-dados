FROM apache/airflow:2.7.1

USER root

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    cmake \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow
COPY . /opt/airflow/
COPY /scripts/ /scripts/

WORKDIR /opt/airflow

# RUN airflow db init

# # Comando para rodar o Airflow
# ENTRYPOINT ["/entrypoint.bash"]