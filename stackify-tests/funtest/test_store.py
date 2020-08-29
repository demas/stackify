import random
import string
from unittest import mock

from store import Connection, DB


def test_add_question(testing_database: DB, question_1):
    question = question_1
    question["first"] = "js"

    testing_database.add_question(question)

    counts = testing_database.get_counts_by_tags()
    assert counts["js"] == 1

    questions_by_tag = testing_database.get_questions_by_tag("js")
    assert len(questions_by_tag) == 1
    assert questions_by_tag[0]["first"] == "js"


def test_add_duplicate_question(testing_database: DB, question_1):
    question = question_1
    question["first"] = "js"

    testing_database.add_question(question)
    testing_database.add_question(question)

    counts = testing_database.get_counts_by_tags()
    assert counts["js"] == 1

    questions_by_tag = testing_database.get_questions_by_tag("js")
    assert len(questions_by_tag) == 1
    assert questions_by_tag[0]["first"] == "js"


def test_add_list_of_questions(testing_database: DB, list_of_classified_questions):
    testing_database.add_list_of_questions(list_of_classified_questions)

    counts = testing_database.get_counts_by_tags()
    assert counts["js"] == 3

    questions_by_tag = testing_database.get_questions_by_tag("js")
    assert len(questions_by_tag) == 3
    assert questions_by_tag[0]["first"] == "js"


def test_set_by_tag_empty(testing_database: DB, list_of_classified_questions):
    testing_database.set_list_of_questions_for_tag("js", list_of_classified_questions)

    counts = testing_database.get_counts_by_tags()
    assert counts["js"] == 3

    questions_by_tag = testing_database.get_questions_by_tag("js")
    assert len(questions_by_tag) == 3
    assert questions_by_tag[0]["first"] == "js"


def test_set_by_tag_not_empty(testing_database: DB, question_1, question_2, question_3):
    question_1["first"] = "js"
    question_2["first"] = "js"
    question_3["first"] = "js"
    testing_database.add_question(question_1)
    testing_database.add_question(question_2)

    testing_database.set_list_of_questions_for_tag("js", [question_3])

    counts = testing_database.get_counts_by_tags()
    assert counts["js"] == 1

    questions_by_tag = testing_database.get_questions_by_tag("js")
    assert len(questions_by_tag) == 1
    assert questions_by_tag[0] == question_3


def test_remove_by_tag(testing_database: DB, list_of_classified_questions):
    testing_database.set_list_of_questions_for_tag("js", list_of_classified_questions)

    testing_database.remove_questions_for_tag("js")

    counts = testing_database.get_counts_by_tags()
    assert counts["js"] == 0

    questions_by_tag = testing_database.get_questions_by_tag("js")
    assert len(questions_by_tag) == 0


@mock.patch("time.time", autospec=True)
def test_get_new_count_by_tag(time, testing_database: DB, question_1, question_2, question_3):
    time.return_value = 4
    # TODO: add fabrica
    question_1["creation_date"] = 1
    question_2["creation_date"] = 2
    question_3["creation_date"] = 3
    question_1["first"] = "a"
    question_2["first"] = "a"
    question_3["first"] = "a"
    testing_database.add_question(question_1)
    testing_database.add_question(question_2)
    testing_database.add_question(question_3)

    result = testing_database.count_new_questions_for_tag(tag="a", seconds=1)
    assert result == 1


def test_connection():
    filename = ''.join([random.choice(string.ascii_lowercase) for _ in range(15)])
    connection = Connection(filename=filename)

    assert connection is not None
    assert isinstance(connection, DB)


def test_connection_singleton():
    filename = ''.join([random.choice(string.ascii_lowercase) for _ in range(15)])
    connection1 = Connection(filename=filename)
    connection2 = Connection(filename=filename)

    assert connection1 is not None
    assert connection2 is not None
    assert id(connection1) == id(connection2)
    assert id(connection1.db) == id(connection2.db)
