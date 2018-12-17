import time
import os
import json
import threading
import app.train_plan.models as models
from kombu import Connection, Producer, Consumer, Queue, uuid, eventloop


rabbit_url = 'amqp://{user}:{passwd}@{host}/'.format(
    user = os.environ.get('RABBIT_MQ_USER', ''),
    passwd = os.environ.get('RABBIT_MQ_PASSWD', ''),
    host = os.environ.get('MYSQL_DB_HOST', 'localhost')
)


class Client(object):

    def __init__(self, connection):
        self.connection = connection
        self.callback_queue = Queue(uuid(), exclusive=True, auto_delete=True)
        self.model = NewRecord()
        self.terminated = False

    def on_response(self, message):
        if message.properties['correlation_id'] == self.correlation_id:
            self.model.create_record(message.payload)

    def call(self, data):
        self.terminated = False
        self.response = None
        self.correlation_id = uuid()
        with Producer(self.connection) as producer:
            producer.publish(
                data,
                exchange='',
                routing_key='rpc_queue',
                declare=[self.callback_queue],
                reply_to=self.callback_queue.name,
                correlation_id=self.correlation_id,
                serializer='json'
            )

    def receive_message(self):
        with Consumer(self.connection,
                      on_message=self.on_response,
                      queues=[self.callback_queue], no_ack=True):
            for _ in eventloop(self.connection):
                if self.terminated:
                    break

    def terminate(self):
        self.terminated = True

class NewRecord:
    def __init__(self):
        pass

    @classmethod
    def create_record(self, data):
        data = json.loads(data)
        dic = {
            "trial_id": data.get('trial_id', -1),
            "epoch": data.get('epoch', -1),
            "iteration": data.get('iteration', -1),
            "loss": data.get('loss', -1),
            "iou": data.get('loss', -1),
            "acc": data.get('loss', -1),
            "recall": data.get('loss', -1),
            "precision": data.get('loss', -1),
        }
        models.TrainRecord.objects.create(**dic)

class Patcher:
    def __init__(self):
        connection = Connection(rabbit_url)
        self.client = Client(connection)
        self.listen_thread = threading.Thread(target=self.client.receive_message)
        print('send connect!')

    def start_train(self, epoch, url):
        trial_id = int(url.split('/')[-2])
        print('send start!', url)

        data = {"action": "train", "epoch": epoch, "trial_id": trial_id}
        self.client.call(data)
        self.listen_thread.start()

    def stop_train(self):
        data = {"action": "stop"}
        self.client.terminate()
        time.sleep(1)
        self.client.call(data)
        self.listen_thread.join()

if __name__=="__main__":
    p = Patcher()
    p.start_train(10, '/api/trial/1/')
