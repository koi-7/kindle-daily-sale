#!/usr/bin/env python3
# coding: utf-8


import configparser
import io
import logging
import os
import sys
import urllib.request
from logging import getLogger, FileHandler, Formatter


from bs4 import BeautifulSoup
import requests

from .functions import *


MAIN_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(MAIN_DIR, '../config/config.ini')
LOG_PATH = os.path.join(MAIN_DIR, '../logs/kindle-daily-sale.log')
URL = 'https://www.amazon.co.jp/kindledd'


logger = getLogger(__name__)
logger.setLevel(logging.INFO)
handler = FileHandler(LOG_PATH)
fmt = Formatter('%(asctime)s %(levelname)-8s %(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)


def main():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except:
        logger.error(response.status_code)
        sys.exit(1)

    config_ini = configparser.ConfigParser()
    config_ini.read(CONFIG_PATH, encoding='utf-8')

    soup = BeautifulSoup(response.content, 'html.parser')
    tags = soup.findAll('img', class_ = 'a-dynamic-image')

    for tag in tags:
        title = tag.get('aria-label')
        image_url = tag.get('src')

        img_read = urllib.request.urlopen(image_url).read()
        img_bin = io.BytesIO(img_read)

        slack_token = config_ini['Slack']['token']
        slack_channel_url = config_ini['Slack']['channel_url']
        slack_channel_id = slack_channel_url.split('/')[-1]

        Functions.send_to_slack(title, img_bin, slack_token, slack_channel_id)

    logger.info('正常終了')


if __name__ == "__main__":
    main()
