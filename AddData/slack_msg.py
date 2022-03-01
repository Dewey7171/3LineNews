from slack_sdk.webhook import WebhookClient
from secret import slack_url

def slack_push(event):
    url = slack_url
    webhook = WebhookClient(url)
    response = webhook.send(text=event)

    return response