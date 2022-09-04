import time
import secrets
from twilio.rest import Client

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def check_inventory(url: str):
    """query aliexpress for java and html source, look for tag evidencing 'out of stock satus; if out of stock,
    repeat query every 7ish minutes until in stock.

    :param url: URL to be queried
    :return: None
    """

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    while True:
        driver.get(url)
        sleep(1)

        deepwater = driver.page_source.encode('utf-8')

        if 'buynow disable' in str(deepwater):
            print("this item is still unavailable")
            time.sleep(440)
        else:
            break


def twilio_setup():
    """variable data for setting up twilio alert 
    :return: Client
    """
    # ENSURE YOU EDITED THE VARIABLES IN THE scecrets.py FILE!
    account_sid = secrets.ASID
    auth_token = secrets.AT
    return Client(account_sid, auth_token)


def send_notification():
    """send 'in stock' notification and product url via SMS text message."""

    # EDIT THESE FOLLOWING 3 VARIABLES TO SUIT YOUR USECASE!
    item = 'miyoo Mini v2'
    merchant = 'Aliexpress'
    purchase_url = 'https://www.aliexpress.com/item/3256803425362523.html'

    twilio_client = twilio_setup()
    twilio_client.messages.create(
        body=f"You can now buy your {item} from {merchant}!\n{purchase_url}\nCongratulations!",
        from_=secrets.TPN,
        to=secrets.PPN,
    )



# CHANGE THE URL IN THE check_inventory() FUNCTION BELOW TO THE URL OF THE PRODUCT DESIRED! 
check_inventory('https://www.aliexpress.com/item/3256803425362523.html')
send_notification()
exit()
