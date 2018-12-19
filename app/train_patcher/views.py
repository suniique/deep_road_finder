import threading
from channels.generic.websocket import WebsocketConsumer


class RecoderSender(WebsocketConsumer):

    instances = []

    def connect(self):
        self.accept()
        self.trial_id = int(self.scope['url_route']['kwargs']['trial_id'])
        RecoderSender.instances.append(self)
        self.send(text_data="Connected!")

    def websocket_send(self, data, trial_id):
        if trial_id == self.trial_id:
            self.send(text_data=data)
            print("send data via websocket:", data)

    def disconnect(self, code):
        RecoderSender.instances.remove(self)
        print("websocket disconnected.")


