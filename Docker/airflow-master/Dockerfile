FROM centos

RUN cd && curl -O curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && /bin/bash /root/Miniconda3-latest-Linux-x86_64.sh -b -p /root/miniconda

RUN echo "export PATH=$PATH:/root/miniconda/bin" >> /root/.bashrc

ENV PATH="/root/miniconda/bin:${PATH}"

RUN conda install airflow -y -c https://conda.anaconda.org/conda-forge/ && \
  conda install psycopg2 -y

RUN pip install 'apache-airflow[celery]'

ENV AIRFLOW_HOME=~/airflow

ENV C_FORCE_ROOT=secretRefs

RUN airflow initdb

COPY config/airflow.cfg /root/airflow/airflow.cfg

ENTRYPOINT ["sleep", "100d"]

CMD []
