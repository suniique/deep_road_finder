from __future__ import absolute_import, unicode_literals
# import pika
import os
import json
import threading
import time
import random
import kombu
from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin

trial_id = None
rpc_queue = Queue('rpc_queue')

rabbit_url = 'amqp://{user}:{passwd}@{host}/'.format(
    user = os.environ.get('RABBIT_MQ_USER', ''),
    passwd = os.environ.get('RABBIT_MQ_PASSWD', ''),
    host = os.environ.get('MYSQL_DB_HOST', 'localhost')
)
# queue_control = kombu.Connection(rabbit_url).SimpleQueue('trainviz_control')
# queue_record = kombu.Connection(rabbit_url).SimpleQueue('trainviz_record')

class Worker(ConsumerProducerMixin):

    def __init__(self, connection):
        self.connection = connection
        self.properties = None

    def get_consumers(self, Consumer, channel):
        return [Consumer(
            queues=[rpc_queue],
            on_message=self.on_request,
            accept={'application/json'},
            prefetch_count=1,
        )]

    def on_request(self, message):
        print("recevied", message.payload)
        global trial_id
        action = message.payload["action"]


        if action == 'connect':
            print('connected.')
        elif action == 'train':
            trial_id = message.payload["trial_id"]
            train_thread.start()
        elif action == 'stop':
            print('stopping...')
            message.ack()
            recorder.terminate()
            train_thread.join()
            exit(0)

        message.ack()
        self.properties = message.properties

    def send_message(self, data):
        try:
            self.producer.publish(
                data,
                exchange='', routing_key=self.properties['reply_to'],
                correlation_id=self.properties['correlation_id'],
                serializer='json',
                retry=True,
            )
        except:
            print("ERROR IN SENDING")



class TrainRecorder:
    def __init__(self, worker):
        self.worker = worker
        self.terminated = False

    def fack_data(self,t):
        data = {
            "trial_id": trial_id,
            "epoch": t,
            "loss": float(1./t)
        }
        return json.dumps(data)

    def send_record(self, data):
        self.worker.send_message(data)

    def terminate(self):
        self.terminated = True


    def tic_toc(self):
        tics = 0
        while(not self.terminated):
            time.sleep(0.5)
            tics += 1
            data = self.fack_data(tics)
            self.send_record(data)
            print(data)



def start_worker(broker_url):
    connection = Connection(broker_url)
    print(' [x] Awaiting RPC requests')
    worker = Worker(connection)
    return worker


if __name__ == "__main__":
    worker = start_worker(rabbit_url)
    recorder = TrainRecorder(worker)
    train_thread = threading.Thread(target=recorder.tic_toc)

    worker.run()









