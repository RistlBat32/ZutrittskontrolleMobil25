import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CheckinCheckoutConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("checkin_checkout", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("checkin_checkout", self.channel_name)

    async def checkin_checkout_message(self, event):
        message = event["message"]
        message_type = event.get("message_type", "info")  # Falls nicht vorhanden, Standardwert "info"
        nfc_id = event.get("nfc_id", None)

        await self.send(text_data=json.dumps({
            "message": message,
            "message_type": message_type,
            "nfc_id": nfc_id,
        }))