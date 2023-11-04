from pywebpush import WebPushException, webpush
import json


# Your VAPID public and private keys
vapid_public_key = 'BDnOafVJ6i8k2D3Z8bdEERIhihFtRdTaW6am86NbosgDc9t2fB18FPjZIYfcZd7rlXu2pHadT0BWbh68J8P7N4I'
vapid_private_key = '5jM_G2Iiems0k-H7LFDy769LOM8aQ4uKa3kzZ-bb_wo'

def send_push_notification(subscription, payload):
    try:
        webpush(
            subscription_info=json.loads(subscription),
            # data=json.dumps(payload),
            data="mary had a little lamb",
            vapid_private_key=vapid_private_key,
            vapid_claims={
                "sub": "mailto:chidiadi.emmanuel.nwosu@gmail.com"  # Replace with your email
            }
        )
    except WebPushException as e:
        print("Error sending push notification: ", e)



subscription = '{"endpoint":"https://fcm.googleapis.com/fcm/send/f3LKkvOEY5Q:APA91bGKvk5ONJDoUmDfOoERd6t_UAVWg4xVryE_sYUrz75XH-9wpr5n09Bd9iebf-x2K6IMs9-ePLW9BYm_GcO0_eDaqoHGPJFIRiMdIXuylvp_iTUiBEzA7T1-JOOlfSZYUVJa5Zyq","expirationTime":null,"keys":{"p256dh":"BEtCuN3ueUJck3Hi2Jmf6pjdZfpKNJY0iz29kWUdfnRDePP78Nche0tKYI0DxUMkI7aoW9Vp4raWpEaI8WsXAgI","auth":"o-cBEq-Z0Jo7G3e0DtC4tQ"}}'
payload = {"title": "Notification Title", "body": "Notification Body", "icon": ""}

send_push_notification(subscription, payload)
