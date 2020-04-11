import requests
import json
import time

KEY = ""
URL_TEMPLATE="https://api.stackexchange.com/2.2/questions?pagesize=100&page={}&fromdate={}&order=desc&sort=creation&site=stackoverflow&key={}"


def get_last_time():
    with open("config.txt") as f:
        content = f.readline()

    # last sync time
    if content != "":
        return int(content)
    else:
        print("config not found")
        return int(time.time())


def save_last_time(moment):
    file = open("config.txt", "w")
    file.write(str(moment))
    file.close()


def fetch():
    print()
    print("fetching data...")
    last = get_last_time()
    now = int(time.time())

    first = True
    json_data = None
    page = 1
    result = []

    while first or json_data["has_more"]:
        # TODO: display progress
        response = requests.get(url=URL_TEMPLATE.format(page, last, KEY))
        if response.status_code != 200:
            print("status code: {}".format(response.status_code))
            exit(0)

        json_data = json.loads(response.text)
        for question in json_data["items"]:
            result.append(question)

        first = False
        page = page + 1

    save_last_time(now)
    return result
