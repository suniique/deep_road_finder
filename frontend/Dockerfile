FROM my/node:8

# Create app directory
RUN mkdir -p /home/Service
WORKDIR /home/Service

# Bundle app source
COPY . /home/Service
RUN npm install --production

EXPOSE 8086
CMD [ "npm", "run", "serve" ]
