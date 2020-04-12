from typing import List, Union

from classify import Classifier, STOP_TAGS, FIRST_LEVEL_RULES
from config import load_config, save_config
from helpers import filter_tags, enrich_tags, represents_int, transform_tags, set_hidden
from session import Session
import fetcher
from store import get_database
from fabulous.color import bg256, fg256
import webbrowser
from cli import Command, CommandType, Parser

from ui import say_hello, display_list_of_questions, ls, alert_unclassified

config = load_config()
db = get_database()

classifier = Classifier(STOP_TAGS, FIRST_LEVEL_RULES)

session = Session()
say_hello()


def fetch_action():
    questions = fetcher.fetch()
    classified_questions = classifier.classify(questions)
    db.add_list(classified_questions)
    alert_unclassified(classified_questions)


def ls_action(include_hidden=False):
    tags = db.counts()
    tags = transform_tags(tags)
    if not include_hidden:
        tags = filter_tags(tags, config['hide_tags'])

    set_hidden(tags, config['hide_tags'])
    tags = enrich_tags(tags)
    session.current_tags = tags
    ls(tags)


def fetch_and_ls():
    fetch_action()
    ls_action()


def show_questions_by_tag(params=None):
    ls_action(include_hidden=("--include-hidden" in params))


def show_questions(params=None):
    if represents_int(params):
        num = int(params)
        for tag_dict in session.current_tags:
            if tag_dict["num"] == num:
                session.switch_to_tag(tag_dict["tag"], db.tag(tag_dict["tag"]))
                display_list_of_questions(session.active_questions)
    else:
        session.switch_to_tag(params, db.tag(params))
        display_list_of_questions(session.active_questions)


def delete_questions(params=None):
    if len(params) == 0:
        db.set_by_tag(session.last_used_tag, session.remain_questions())
        print(fg256("grey", "delete by {} (remain={})".format(session.last_used_tag, len(session.remain_questions()))))
        print()
    else:
        if represents_int(params[1:]):
            tag_num = int(params[1:])
            for tag_dict in session.current_tags:
                if tag_dict["num"] == tag_num:
                    db.remove_by_tag(tag_dict["tag"])
        else:
            db.remove_by_tag(params[1:])
        print()


def hide_tag(params=None):
    if represents_int(params[1:]):
        num = int(params[1:])
        for tag_dict in session.current_tags:
            if tag_dict["num"] == num:
                config['hide_tags'].append(tag_dict["tag"])
    else:
        config['hide_tags'].append(params[1:])
    save_config(config)


def unhide_tag(params=None):
    if represents_int(params[1:]):
        num = int(params[1:])
        for tag_dict in session.current_tags:
            if tag_dict["num"] == num:
                config["hide_tags"].remove(tag_dict["tag"])
    else:
        config["hide_tags"].remove(params[1:])
    save_config(config)


def open_question(param=None):
    num = int(param)
    webbrowser.open(session.active_questions[num - 1]["link"], autoraise=False)


def open_questions_list(params=None):
    question_list = params.split(",")
    for question_num_str in question_list:
        question_num = int(question_num_str.strip())
        webbrowser.open(session.active_questions[question_num - 1]["link"], autoraise=False)


fetch_command = Command(command_type=CommandType.EQUAL, value="f", action=fetch_and_ls)
ls_command = Command(command_type=CommandType.START_WITH, value="ls", action=show_questions_by_tag)
show_questions_command = Command(command_type=CommandType.START_WITH, value="s ", action=show_questions)
delete_questions_command = Command(command_type=CommandType.START_WITH, value="del", action=delete_questions)
hide_tag_command = Command(command_type=CommandType.START_WITH, value="hide", action=hide_tag)
unhide_tag_command = Command(command_type=CommandType.START_WITH, value="unhide", action=unhide_tag)
open_question_command = Command(command_type=CommandType.IN_LIST, value=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                                action=open_question)
open_questions_list_command = Command(command_type=CommandType.START_WITH, value="o", action=open_questions_list)

parser = Parser()
parser.add_command(fetch_command)
parser.add_command(ls_command)
parser.add_command(show_questions_command)
parser.add_command(delete_questions_command)
parser.add_command(hide_tag_command)
parser.add_command(unhide_tag_command)
parser.add_command(open_question_command)
parser.add_command(open_questions_list_command)


while True:
    message = input("> ")
    parser.process_message(message)
