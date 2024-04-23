# state is sustained in the session
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


# room name & group name
# room name is the name of the chat room so that users can join the same room
# group name is used to broadcast messages to all users in the same room
class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status": "connected"}))

    def receive(self, text_data): # will accept data from front-end and print it
        print(text_data)
        self.send(text_data=json.dumps({"status": "received"}))

    def disconnect(self, close_code):
        self.close()
        print("disconnected")

    def send_notification(self, event):
        print("Received notification")
        print(event.get("value"))
        self.send(text_data=({
            "value": event.get("value")
        }))
