import schedule
import time
from instagrapi import Client
from secret import username, password

def post_to_instagram():
    cl = Client()
    cl.login(username, password)
    media = cl.photo_upload(
        path="/home/yellowflash/Pictures/Wallpapers/one.jpg", 
        caption="srk is love"
    )
    print("Post uploaded!")

# Schedule the task to run daily at 10:00 AM
schedule.every().day.at("12:12").do(post_to_instagram)


while True:
    schedule.run_pending()
    time.sleep(1)# explain this program