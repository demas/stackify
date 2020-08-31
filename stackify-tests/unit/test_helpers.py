from unittest import mock

import pytest

import helpers

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * SECOND


def test_transform_tags():
    tags = [("a", 1), ("b", 2), ("c", 3)]

    result = helpers.transform_tags(tags)

    assert len(result) == 3
    assert result[0] == {"tag": "a", "count": 1}
    assert result[1] == {"tag": "b", "count": 2}
    assert result[2] == {"tag": "c", "count": 3}


# TODO: parametrize test
def test_filter_tags():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}, {"tag": "c", "count": 3}]
    dont_display_tags = ["c"]

    result = helpers.filter_tags(tags, dont_display_tags)

    assert len(result) == 2
    assert result[0] == {"tag": "a", "count": 1}
    assert result[1] == {"tag": "b", "count": 2}


def test_filter_tags_with_zero_counts():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}, {"tag": "c", "count": 0}]
    dont_display_tags = []

    result = helpers.filter_tags(tags, dont_display_tags)

    assert len(result) == 2
    assert result[0] == {"tag": "a", "count": 1}
    assert result[1] == {"tag": "b", "count": 2}


def test_set_hidden_one_tag():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}, {"tag": "c", "count": 3}]
    dont_display_tags = ["c"]

    result = helpers.set_hidden(tags, dont_display_tags)

    assert len(result) == 3
    assert result[0] == {"tag": "a", "count": 1, "hidden": False}
    assert result[1] == {"tag": "b", "count": 2, "hidden": False}
    assert result[2] == {"tag": "c", "count": 3, "hidden": True}


def test_set_hidden_multiple_tags():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}, {"tag": "c", "count": 3}]
    dont_display_tags = ["b", "c"]

    result = helpers.set_hidden(tags, dont_display_tags)

    assert len(result) == 3
    assert result[0] == {"tag": "a", "count": 1, "hidden": False}
    assert result[1] == {"tag": "b", "count": 2, "hidden": True}
    assert result[2] == {"tag": "c", "count": 3, "hidden": True}


# TODO: parametrize test
def test_enrich_tags():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}]

    result = helpers.enrich_tags(tags)
    assert len(result) == 2
    assert any(x["num"] for x in result)
    # TODO: test num is coninuous and unique


@pytest.mark.parametrize("param", ["1", "2", "10", "99", "100", "434", " 1", " 10", "10 ", "1 ", " 232 "])
def test_represents_int_ok(param):
    assert helpers.represents_int(param)


@pytest.mark.parametrize("param", [" 1s", "2x", "c10", "99c ", " 1s00 ", "xxx"])
def test_represents_int_not_ok(param):
    assert not helpers.represents_int(param)


def test_add_new_header_for_questions(list_of_questions):
    list_of_questions[0]["creation_date"] = 1
    list_of_questions[1]["creation_date"] = 2
    list_of_questions[2]["creation_date"] = 3

    with mock.patch("helpers.new_period_limit", return_value=2):
        result = helpers.add_new_header_for_questions(list_of_questions)

    assert len(result) == 3
    assert not result[0]["new_flag"]
    assert result[1]["new_flag"]
    assert result[2]["new_flag"]


@pytest.mark.parametrize("sequence, symbol", [("&quot;", "\""), ("&#39;", "\'"), ("&lt;", "<"), ("&gt;", ">")])
def test_fix_question_title(list_of_questions, sequence, symbol):
    list_of_questions[0]["title"] = "Something {}another{}".format(sequence, sequence)
    list_of_questions[1]["title"] = "Something {}{}another".format(sequence, sequence)
    list_of_questions[2]["title"] = "Something {}another{} test".format(sequence, sequence)

    result = helpers.fix_question_title(list_of_questions)

    assert result[0]["title"] == "Something {}another{}".format(symbol, symbol)
    list_of_questions[1]["title"] = "Something {}{}another".format(symbol, symbol)
    list_of_questions[2]["title"] = "Something {}another{} test".format(symbol, symbol)


def test_filter_active_questions(list_of_questions):
    list_of_questions[0]["new_flag"] = False
    list_of_questions[1]["new_flag"] = True
    list_of_questions[2]["new_flag"] = True

    result = helpers.filter_active_questions(list_of_questions)

    assert len(result) == 2
    assert result[0] == list_of_questions[1]
    assert result[1] == list_of_questions[2]


def test_set_human_datetime_old_questions(question_1):
    question_1["new_flag"] = False

    result = helpers.set_human_datetime([question_1])

    assert len(result) == 1
    assert not result[0].get("human_datetime", False)


@pytest.mark.parametrize("creation_date, current_time, expected_result",
                         [(1, 10, 9), (2, 2, 0), (10, 65, 55)])
def test_set_human_datetime(question_1, creation_date: int, current_time: int, expected_result: int):
    question_1["new_flag"] = True
    question_1["creation_date"] = creation_date * MINUTE

    with mock.patch("time.time", return_value=current_time * MINUTE):
        result = helpers.set_human_datetime([question_1])

    assert len(result) == 1
    assert result[0]["human_datetime"] == "{} min ago".format(expected_result)


def test_get_tag_counts_for_questions(list_of_questions):
    list_of_questions[0]["first"] = "js"
    list_of_questions[1]["first"] = "html"
    list_of_questions[2]["first"] = "html"

    result = helpers.get_tag_counts_for_questions(list_of_questions)

    assert result["js"] == 1
    assert result["html"] == 2
    assert len(result.keys()) == 2