from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 5916492495
bot_user = "EE_20_EE_bot"
api_id = 22230207
api_hash = "efee56194c10eb0d29b3f4fc136e7446"
session = "BAA5UxcgbDZH3xY76xm8rvMpOwe0NGiYc3Hjh93-9XL3Mp8gQ3cpdmNNigXm4hZ4OUe9xfYsACtsNTkpT5TpYt_mUE5OgHu4eJhtK0v8WRvHlJJk1Of--CZepLL9D2ZseE0lLMeQ0GVeqr66TDcUTE8biRB3iHj2v1alq5tpoXOpTsQTXd2wYamlVe4s8t9IryP2C6h2GEdD5stAz1vhHuy1Li6WFqsExdHdI1KkRSz67vgAmTTsOPHNmkYwGdvcJ3FG45K32cXI6EGmgIUV5p4fbq6H1H58jARxwKMvPTuLs_-bxwgz2Kft9OMBTWl3ndsiEvSpTd9pmt1ROuMHgey7AAAAAWCmgs8A"
token = "5824098877:AAF4z2VPG1irUjut7S1smNvdd0qzddumSdM"
sudo_command = [5656828413, 5916492495]
pm = "-1001804255843"
mention = "-1001804255843"
plugins = dict(root="plugins")
app = Client("user:Amrsabrrybot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("Amrsabrrybot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
