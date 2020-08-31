import random
import sqlite3
import string

from relation_store import Connection, add_list_of_questions, add_question, delete_question, get_counts_by_category, \
    get_questions, \
    get_questions_by_category


def test_connection():
    filename = ''.join([random.choice(string.ascii_lowercase) for _ in range(15)])
    connection = Connection(filename=filename)

    assert connection is not None
    assert isinstance(connection, sqlite3.Connection)


def test_connection_singleton():
    filename = ''.join([random.choice(string.ascii_lowercase) for _ in range(15)])
    connection1 = Connection(filename=filename)
    connection2 = Connection(filename=filename)

    assert connection1 is not None
    assert connection2 is not None
    assert id(connection1) == id(connection2)


def test_add_question(testing_db_connection, question_1):
    q = question_1
    q["category"] = "js"
    q["subcategory"] = "vue"

    add_question(testing_db_connection, question_1)

    result = get_questions(testing_db_connection)

    # TODO: transformation
    #expected = q
    #assert result == [expected]


def test_counts_by_category(testing_db_connection, list_of_classified_questions_with_different_categories):
    add_list_of_questions(testing_db_connection, list_of_classified_questions_with_different_categories)

    result = get_counts_by_category(testing_db_connection)

    assert len(result) == 3

    # TODO: refactore
    for _, count in result:
        assert count == 1


# TODO: better test
def test_get_questions_by_category(testing_db_connection, list_of_classified_questions_with_different_categories):
    add_list_of_questions(testing_db_connection, list_of_classified_questions_with_different_categories)

    result = get_questions_by_category(testing_db_connection, "python")

    assert len(result) == 1


def test_delete_question(testing_db_connection, question_1, question_2):
    add_question(testing_db_connection, question_1)
    add_question(testing_db_connection, question_2)

    questions = get_questions(testing_db_connection)
    assert len(questions) == 2

    delete_question(testing_db_connection, question_1)
    questions = get_questions(testing_db_connection)
    assert len(questions) == 1
    assert questions[0]["question_id"] == question_2["question_id"]




