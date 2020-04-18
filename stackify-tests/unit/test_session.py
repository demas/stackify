from session import ActiveSession


def test_create_session():
    session = ActiveSession()

    assert session is not None


def test_create_session_singleton():
    session1 = ActiveSession()
    session2 = ActiveSession()

    assert session1 is not None
    assert session2 is not None
    assert id(session1) == id(session2)
