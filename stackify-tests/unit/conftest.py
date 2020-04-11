import pytest

from classify import Classifier

STOP_TAGS = ["stop_a", "stop_b", "stop_c"]

FIRST_LEVEL_RULES = [
    {"site": "site_a", "include": "a", "result": "result_1"},
    {"site": "site_a", "include": "b", "result": "result_2"},
    {"site": "site_a", "include": "c", "result": "result_2"},
    {"site": "site_a", "include": "d,e,f", "result": "result_3"},
]


@pytest.fixture(scope="function", autouse=True)
def default_classifier():
    return Classifier(STOP_TAGS, FIRST_LEVEL_RULES)
