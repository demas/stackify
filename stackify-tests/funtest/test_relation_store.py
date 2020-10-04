import sqlite3

from relation_store import Connection
from relation_store import add_list_of_questions
from relation_store import add_question
from relation_store import create_tables
from relation_store import delete_question
from relation_store import get_counts_by_category
from relation_store import get_questions
from relation_store import get_questions_by_category


def test_connection():
    connection = Connection(":memory:")

    assert connection is not None
    assert isinstance(connection, sqlite3.Connection)


def test_connection_singleton():
    connection1 = Connection(":memory:")
    connection2 = Connection(":memory:")

    assert connection1 is not None
    assert connection2 is not None
    assert id(connection1) == id(connection2)


def test_create_tables(test_connection):
    create_tables(test_connection)

    assert len(get_questions(test_connection)) == 0


def test_add_question(test_connection, question_1):
    q = question_1
    q["category"] = "js"
    q["subcategory"] = "vue"

    add_question(test_connection, question_1)

    result = get_questions(test_connection)

    print(result)

    # TODO: transformation
    #expected = q
    #assert result == [expected]


def test_counts_by_category(test_connection, list_of_classified_questions_with_different_categories):
    add_list_of_questions(test_connection, list_of_classified_questions_with_different_categories)

    result = get_counts_by_category(test_connection)

    assert len(result) == 3

    # TODO: refactore
    for _, count in result:
        assert count == 1


# TODO: better test
def test_get_questions_by_category(test_connection, list_of_classified_questions_with_different_categories):
    add_list_of_questions(test_connection, list_of_classified_questions_with_different_categories)

    result = get_questions_by_category(test_connection, "python")

    assert len(result) == 1


def test_delete_question(test_connection, question_1, question_2):
    add_question(test_connection, question_1)
    add_question(test_connection, question_2)

    questions = get_questions(test_connection)
    assert len(questions) == 2

    delete_question(test_connection, question_1)
    questions = get_questions(test_connection)
    assert len(questions) == 1
    assert questions[0]["question_id"] == question_2["question_id"]




