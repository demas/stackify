
def test_stop_tag_stop_present(default_classifier):
    assert default_classifier.has_stop_tag(["cassandra", "stop_a", "oracle"])


def test_stop_tag_stop_not_present(default_classifier):
    assert not default_classifier.has_stop_tag(["cassandra", "java", "oracle"])


def test_first_level_classifier_found(default_classifier):
    assert default_classifier.first_level_classification(["some", "another", "a"]) == "result_1"


def test_first_level_classifier_not_found(default_classifier):
    assert default_classifier.first_level_classification(["some", "another", "here"]) == "none"


def test_first_level_classifier_found_combined(default_classifier):
    assert default_classifier.first_level_classification(["some", "another", "f"]) == "result_3"
