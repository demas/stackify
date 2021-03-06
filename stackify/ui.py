from datetime import datetime, timedelta
from typing import Dict, List

from fabulous.color import fg256

from config import load_config

SHOW_LINK_TO_QUESTION = False


def say_hello():
    print()
    print("Welcome to Stackify")
    print(fg256("grey", "   f - fetch, ls - list, s[ tag/num]  - show, d - delete, del - delete last seen"))


def ls(data_to_display):
    print()
    for element in data_to_display:
        color = "lightgreen" if not element["hidden"] else "red"
        print(fg256(color, "{}: {} ({} / {})".format(element["num"], element["tag"], element["new_count"],
                                                     element["count"])))


def display_list_of_questions(questions):
    print()
    num = 1
    for q in questions:
        creation_date = (datetime.utcfromtimestamp(q["creation_date"]) +
                         timedelta(hours=load_config()["timezone"])).strftime('%Y-%m-%d %H:%M:%S')
        if q.get("human_datetime", False):
            date_to_display = q["human_datetime"]
        else:
            date_to_display = creation_date

        new_flag_ui = ""
        if q["new_flag"]:
            new_flag_ui = "[new] "

        print(fg256("yellow", num) + ": " +
              fg256("lightcoral", new_flag_ui) +
              fg256("lightgreen", q["title"]))
        print(fg256("lightyellow", "  {}, {}, score {}, answer_count {}".format(q["tags"], date_to_display,
                                                                               q["score"], q["answer_count"])))
        if SHOW_LINK_TO_QUESTION:
            print(fg256("grey", "  {}".format(q["link"])))
        print()
        num = num + 1


def alert_unclassified(questions: List[Dict]):
    for q in questions:
        if q["first"] == "none":
            print(fg256('gray', "{}: {}".format(q["site"], q["tags"])))


def summary_for_new_questions(summary: Dict):
    print()
    print(fg256("grey", "found new questions:"))
    for tag, cnt in summary.items():
        print(fg256("grey", "  {}: {}".format(tag, cnt)))
