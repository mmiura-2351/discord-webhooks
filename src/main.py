import requests
import os
import sys

def main(args, webhooks):
    req_body = {"content":"test message"}
    res = requests.post(url=webhooks, json=req_body)
    print(res.ok)

if __name__ == "__main__":
    args = sys.argv
    wh = os.getenv("discord_webhooks")

    # WebHooksの確認
    if wh == None:
        print(f"Error: Discord WebHooks is Missing.")
        exit()
    
    main(args, wh)