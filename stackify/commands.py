import webbrowser
from typing import Optional

from fabulous.color import fg256

import fetcher
import helpers
import ui
import store
from classify import Classifier, FIRST_LEVEL_RULES, STOP_TAGS
from config import load_config, save_config

from session import ActiveSession
config = load_config()


def get_classifier():
    return Classifier(STOP_TAGS, FIRST_LEVEL_RULES)


def fetch_action():
    questions = fetcher.fetch()
    classified_questions = get_classifier().classify(questions)
    store.Connection().add_list(classified_questions)
    ui.alert_unclassified(classified_questions)


def ls_action(include_hidden=False):
    tags = store.Connection().counts()
    tags = helpers.transform_tags(tags)
    if not include_hidden:
        tags = helpers.filter_tags(tags, config['hide_tags'])

    helpers.set_hidden(tags, config['hide_tags'])
    helpers.set_new(tags)
    tags = helpers.enrich_tags(tags)
    ActiveSession().current_tags = tags
    ui.ls(tags)


def fetch_and_ls():
    fetch_action()
    ls_action()


def show_questions_by_tag(params=None):
    ls_action(include_hidden=("--include-hidden" in params))


# TODO: test for it
def _tag_name(param: str) -> Optional[str]:
    if helpers.represents_int(param):
        num = int(param)
        for tag_dict in ActiveSession().current_tags:
            if tag_dict["num"] == num:
                return tag_dict["tag"]
    else:
        return param


def show_questions(params=None):
    tag_name = _tag_name(params)
    questions = store.Connection().tag(tag_name)
    questions = helpers.add_new_header_for_questions(questions)
    ActiveSession().switch_to_tag(params, questions)
    ui.display_list_of_questions(ActiveSession().active_questions)


def delete_questions(params=None):
    if len(params) == 0:
        store.Connection().set_by_tag(ActiveSession().last_used_tag, ActiveSession().remain_questions())
        print(fg256("grey", "delete by {} (remain={})".format(ActiveSession().last_used_tag,
                                                              len(ActiveSession().remain_questions()))))
        print()
    else:
        if helpers.represents_int(params[1:]):
            tag_num = int(params[1:])
            for tag_dict in ActiveSession().current_tags:
                if tag_dict["num"] == tag_num:
                    store.Connection().remove_by_tag(tag_dict["tag"])
        else:
            store.Connection().remove_by_tag(params[1:])
        print()


def hide_tag(params=None):
    if helpers.represents_int(params[1:]):
        num = int(params[1:])
        for tag_dict in ActiveSession().current_tags:
            if tag_dict["num"] == num:
                config['hide_tags'].append(tag_dict["tag"])
    else:
        config['hide_tags'].append(params[1:])
    save_config(config)


def unhide_tag(params=None):
    if helpers.represents_int(params[1:]):
        num = int(params[1:])
        for tag_dict in ActiveSession().current_tags:
            if tag_dict["num"] == num:
                config["hide_tags"].remove(tag_dict["tag"])
    else:
        config["hide_tags"].remove(params[1:])
    save_config(config)


def open_question(param=None):
    num = int(param)
    webbrowser.open(ActiveSession().active_questions[num - 1]["link"], autoraise=False)


def open_questions_list(params=None):
    question_list = params.split(",")
    for question_num_str in question_list:
        question_num = int(question_num_str.strip())
        webbrowser.open(ActiveSession().active_questions[question_num - 1]["link"], autoraise=False)