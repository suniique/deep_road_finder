FROM my/node-django:8

RUN /bin/bash -c "source /root/.bashrc"
RUN echo $MYSQL_DB_USER

# Create app directory
RUN mkdir -p /home/Service
WORKDIR /home/Service

# Bundle app source
COPY . /home/Service
WORKDIR /home/Service/frontend
RUN npm install --production

EXPOSE 8000
WORKDIR /home/Service
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
