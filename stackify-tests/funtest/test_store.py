import random
import string

from store import Connection, DB


def test_add_question(testing_database: DB, question_1):
    question = question_1
    question["first"] = "js"

    testing_database.add(question)

    counts = testing_database.counts()
    assert counts["js"] == 1

    questions_by_tag = testing_database.tag("js")
    assert len(questions_by_tag) == 1
    assert questions_by_tag[0]["first"] == "js"


def test_add_list_of_questions(testing_database: DB, list_of_classified_questions):
    testing_database.add_list(list_of_classified_questions)

    counts = testing_database.counts()
    assert counts["js"] == 3

    questions_by_tag = testing_database.tag("js")
    assert len(questions_by_tag) == 3
    assert questions_by_tag[0]["first"] == "js"


def test_set_by_tag_empty(testing_database: DB, list_of_classified_questions):
    testing_database.set_by_tag("js", list_of_classified_questions)

    counts = testing_database.counts()
    assert counts["js"] == 3

    questions_by_tag = testing_database.tag("js")
    assert len(questions_by_tag) == 3
    assert questions_by_tag[0]["first"] == "js"


def test_set_by_tag_not_empty(testing_database: DB, question_1, question_2, question_3):
    question_1["first"] = "js"
    question_2["first"] = "js"
    question_3["first"] = "js"
    testing_database.add(question_1)
    testing_database.add(question_2)

    testing_database.set_by_tag("js", [question_3])

    counts = testing_database.counts()
    assert counts["js"] == 1

    questions_by_tag = testing_database.tag("js")
    assert len(questions_by_tag) == 1
    assert questions_by_tag[0] == question_3


def test_remove_by_tag(testing_database: DB, list_of_classified_questions):
    testing_database.set_by_tag("js", list_of_classified_questions)

    testing_database.remove_by_tag("js")

    counts = testing_database.counts()
    assert counts["js"] == 0

    questions_by_tag = testing_database.tag("js")
    assert len(questions_by_tag) == 0


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
