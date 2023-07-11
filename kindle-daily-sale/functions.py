import requests


class Functions:
    def __init__(self):
        pass

    @classmethod
    def send_to_slack(self, title, img_bin, slack_token, slack_channel_id):
        api_url = 'https://slack.com/api/files.upload'
        data = {"token": slack_token, "channels": slack_channel_id, "initial_comment": title}
        files = {'file': img_bin.getvalue()}
        requests.post(api_url, data=data, files=files)
