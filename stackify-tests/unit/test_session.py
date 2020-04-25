import pytest

from session import ActiveSession


def test_create_session():
    session = ActiveSession()

    assert session is not None
    assert len(session.all_questions) == 0
    assert len(session.active_questions) == 0
    assert len(session.current_tags) == 0
    assert not session.last_used_tag


def test_create_session_singleton():
    session1 = ActiveSession()
    session2 = ActiveSession()

    assert session1 is not None
    assert session2 is not None
    assert id(session1) == id(session2)


@pytest.mark.parametrize("limit", [0, 1, 2, 3, 4, 5])
def test_switch_to_tag(list_of_classified_questions, limit):
    session = ActiveSession()

    session.switch_to_tag("js", list_of_classified_questions, limit=limit)

    assert session.all_questions == list_of_classified_questions
    assert session.last_used_tag == "js"
    assert (all(session.active_questions[i]["creation_date"] >= session.active_questions[i+1]["creation_date"]
                for i in range(len(session.active_questions)-1)))
    assert (all(session.all_questions[i]["creation_date"] >= session.all_questions[i+1]["creation_date"]
                for i in range(len(session.all_questions)-1)))
    assert len(session.active_questions) == min(len(list_of_classified_questions), limit)


def test_remain_questions(list_of_questions):
    session = ActiveSession()
    session.switch_to_tag("js", list_of_questions, limit=1)

    result = session.remain_questions()

    assert len(result) == 2
    assert (all(q not in result for q in session.active_questions))
    assert len(session.active_questions + result) == 3
