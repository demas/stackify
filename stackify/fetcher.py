from typing import Dict
from typing import List
from typing import Tuple

import requests
import json
import time

from fabulous.color import fg256

import config

URL_TEMPLATE = "https://api.stackexchange.com/2.2/questions" + \
               "?pagesize=100&page={}&fromdate={}&order=desc&sort=creation&site={}&key={}"
KEY = config.load_config()["stackoverflow_key"]

SITES = ["stackoverflow", "codereview", "askdifferent"] # TODO: move to config


def _fetch_one_site(site: str, from_time: int) -> Tuple[List[Dict], int, int]:
    first = True
    page = 1
    json_data = None
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
    return result, page - 1, json_data["quota_remaining"]


# TODO: more tests
def fetch(sites: List[str], from_time: int) -> List:
    print()
    print("fetching data...")
    now = int(time.time())
    result = []

    total_pages = 0
    quota_remain = 0
    for site in sites:
        questions, pages, quota = _fetch_one_site(site=site, from_time=from_time)
        result = result + questions
        total_pages += pages
        quota_remain = quota

    print(fg256("grey", "synced pages = {}; remain_quota = {})".format(total_pages, quota_remain)))
    config.set_value("last-sync", now)
    return result
