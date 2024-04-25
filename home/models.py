from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        channels_layer = get_channel_layer()
        notification_obj = Notification.objects.filter(is_read=False).count()
        data = {
            "count": notification_obj,
            "current_notification": self.message
        }
        print(data)
        async_to_sync(channels_layer.group_send)(
            'test_consumer_group',
            {
                "type": "send_notification",
                "value": data
            }
        )
        super(Notification, self).save(*args, **kwargs)
