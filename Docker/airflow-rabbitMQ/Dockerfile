FROM centos

RUN cd && curl -O curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
  /bin/bash /root/Miniconda3-latest-Linux-x86_64.sh -b -p /root/miniconda && \
  echo "export PATH=$PATH:/root/miniconda/bin" >> /root/.bashrc

ENV PATH="/root/miniconda/bin:${PATH}"

RUN conda install rabbitmq-server -y -c https://conda.anaconda.org/conda-forge/ && rabbitmq-plugins enable rabbitmq_management

RUN yum install screen -y

# RUN screen -dmS server bash -c 'rabbitmq-server'

# RUN sleep 20s

# RUN rabbitmqctl add_user admin admin123

# RUN screen -X -S server quit

CMD rabbitmq-server
