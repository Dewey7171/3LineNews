from slack_sdk.webhook import WebhookClient
from AddData import secret

def slack_push():
    url = secret.slack_url
    webhook = WebhookClient(url)
    response = webhook.send(text='asdfwf')

    return response