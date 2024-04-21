# state is sustained in the session
from channels.generic.websocket import WebsocketConsumer

class TestConsumer(WebsocketConsumer):
    def connect(self):
        # self.accept()
        pass

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # self.send(text_data=text_data)
        pass

    