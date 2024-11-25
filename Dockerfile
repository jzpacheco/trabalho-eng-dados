FROM apache/airflow:2.7.1

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ADD https://astral.sh/uv/install.sh /uv-installer.sh
# RUN sh /uv-installer.sh && rm /uv-installer.sh
# ENV PATH="/root/.local/bin:$PATH"



WORKDIR /opt/airflow/
COPY . /opt/airflow/

RUN rm -rf .venv
# RUN uv sync --frozen


USER airflow
RUN pip install apache-airflow==${AIRFLOW_VERSION} apache-airflow-providers-amazon -r requirements.txt 
ENV PYTHONPATH="/opt/airflow/scripts:$PYTHONPATH"
