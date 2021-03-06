import webbrowser
from typing import Optional

from fabulous.color import fg256

import fetcher
import helpers
import ui
import store
import relation_store
from classify import Classifier, FIRST_LEVEL_RULES
from config import load_config, save_config

from session import ActiveSession
config = load_config()


def get_classifier():
    return Classifier(config["stop_tags"], FIRST_LEVEL_RULES)


def fetch_action():
    questions = fetcher.fetch(from_time=load_config()["last-sync"])
    classified_questions = get_classifier().classify(questions)
    relation_store.add_list_of_questions(classified_questions)
    # ui.alert_unclassified(classified_questions) # TODO: pass ony unclassified questions
                                                # TODO: make option to display unclassified questions
    # ui.summary_for_new_questions(helpers.get_tag_counts_for_questions(classified_questions))


def ls_action(include_hidden=False):
    tags = relation_store.get_counts_by_category()

    if not include_hidden:
        tags = helpers.filter_tags(tags, config['hide_tags'])

    helpers.set_hidden(tags, config['hide_tags'])  # не помню уже зачем я это делаю
    helpers.set_new(tags)
    tags = helpers.enrich_tags(tags)
    ActiveSession().current_tags = tags
    ui.ls(tags)


def init():
    relation_store.create_tables(relation_store.Connection())

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
    ActiveSession().switch_to_tag(tag_name, relation_store.get_questions_by_category(relation_store.Connection(), tag_name))
    active_questions = ActiveSession().active_questions
    active_questions = helpers.add_new_header_for_questions(active_questions)
    active_questions = helpers.fix_question_title(active_questions)
    active_questions = helpers.set_human_datetime(active_questions)
    ui.display_list_of_questions(active_questions)


def show_new_questions(params=None):
    tag_name = _tag_name(params)
    ActiveSession().switch_to_tag(tag_name, store.Connection().tag(tag_name))
    active_questions = ActiveSession().active_questions
    active_questions = helpers.add_new_header_for_questions(active_questions)
    active_questions = helpers.fix_question_title(active_questions)
    active_questions = helpers.set_human_datetime(active_questions)  # todo: refactore chain of calls
    new_active_questions = helpers.filter_active_questions(active_questions)
    ActiveSession().active_questions = new_active_questions
    ui.display_list_of_questions(new_active_questions)


def delete_questions(params=None):
    if len(params) == 0:

        #store.Connection().set_list_of_questions_for_tag(
        #    ActiveSession().last_used_tag,
        #    ActiveSession().remain_questions()
        #)

        # TODO: optimize
        for question in ActiveSession().active_questions:
            relation_store.delete_question(relation_store.Connection(), question)

        print(fg256("grey", "delete by {} (remain={})".format(ActiveSession().last_used_tag,
                                                              len(ActiveSession().remain_questions()))))
        print()
    else:
        if helpers.represents_int(params[1:]):
            tag_num = int(params[1:])
            for tag_dict in ActiveSession().current_tags:
                if tag_dict["num"] == tag_num:
                    relation_store.delete_questions_by_category(relation_store.Connection(), tag_dict["tag"])
                    # store.Connection().remove_questions_for_tag(tag_dict["tag"])
        else:
            #store.Connection().remove_by_tag(params[1:])
            relation_store.delete_questions_by_category(relation_store.Connection(), params[1:])
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