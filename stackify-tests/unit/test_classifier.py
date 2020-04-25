
def test_stop_tag_stop_present(default_classifier):
    assert default_classifier.has_stop_tag(["cassandra", "stop_a", "oracle"])


def test_stop_tag_stop_not_present(default_classifier):
    assert not default_classifier.has_stop_tag(["cassandra", "java", "oracle"])


# TODO: parametrize all tests
def test_first_level_classifier_found(default_classifier):
    assert default_classifier.first_level_classification(["some", "another", "a"], "site_a") == "result_1"


def test_first_level_classifier_not_found(default_classifier):
    assert default_classifier.first_level_classification(["some", "another", "here"], "site_a") == "none"


def test_first_level_classifier_multiple_sites_all_tags(default_classifier):
    assert default_classifier.first_level_classification(["some", "another", "here"], "site_b") == "result_5"


def test_first_level_classifier_multiple_sites_one_unique_tag(default_classifier):
    assert default_classifier.first_level_classification(["some", "x", "here"], "site_b") == "result_4"


def test_first_level_classifier_multiple_sites_many_tags(default_classifier):
    assert default_classifier.first_level_classification(["some", "z", "here"], "site_b") == "result_6"


def test_first_level_classifier_multiple_sites_not_unique_site(default_classifier):
    assert default_classifier.first_level_classification(["some", "a", "here"], "site_b") == "result_7"


def test_first_level_classifier_found_combined(default_classifier):
    assert default_classifier.first_level_classification(["some", "another", "f"], "site_a") == "result_3"
