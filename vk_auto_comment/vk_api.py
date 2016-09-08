import json
import time

import requests


class VkAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    def __call_api(self, method, data):
        data.update({
            "access_token": self.access_token,
            "v": "5.44",
        })
        result = requests.post(
            "https://api.vk.com/method/{}".format(method),
            data=data
        )
        time.sleep(0.5)
        return json.loads(result.text)

    def create_comment(self, owner_id, post_id, message, attachments):
        return self.__call_api(
            "wall.createComment",
            {
                "owner_id": owner_id,
                "post_id": post_id,
                "message": message,
                "attachments": attachments,
            }
        )

    def get_posts(self, owner_id, count):
        return self.__call_api(
            "wall.get",
            {
                "owner_id": owner_id,
                "count": count,
            }
        )
