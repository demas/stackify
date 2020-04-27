from typing import Dict
from typing import List

import requests
import json
import time

from fabulous.color import fg256

import config

URL_TEMPLATE = "https://api.stackexchange.com/2.2/questions" + \
               "?pagesize=100&page={}&fromdate={}&order=desc&sort=creation&site={}&key={}"
KEY = config.load_config()["stackoverflow_key"]

SITES = ["stackoverflow", "codereview", "askdifferent"] # TODO: move to config

# TODO: tests
def fetch_one_site(site: str, from_time: int) -> List[Dict]:
    first = True
    json_data = None
    page = 1
    result = []

    while first or json_data["has_more"]:
        response = requests.get(url=URL_TEMPLATE.format(page, from_time, site, KEY))
        if response.status_code != 200:
            print("status code: {}".format(response.status_code))
            exit(0)

        json_data = json.loads(response.text)
        for question in json_data["items"]:
            question["site"] = site
            result.append(question)

        first = False
        page = page + 1
    print(fg256("grey", "site = {}; synced pages = {}; remain_quota = {})".format(site, page - 1,
                                                                                  json_data["quota_remaining"])))
    return result


# TODO: more tests
def fetch(sites: List[str], from_time: int) -> List:
    print()
    print("fetching data...")
    now = int(time.time())
    result = []

    for site in sites:
        result = result + fetch_one_site(site=site, from_time=from_time)

    config.set_value("last-sync", now)
    return result
