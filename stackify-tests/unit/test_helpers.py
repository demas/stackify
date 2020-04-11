from helpers import filter_tags, enrich_tags, represents_int, transform_tags, set_hidden


def test_transform_tags():
    tags = {"a": 1, "b": 2, "c": 3}

    result = transform_tags(tags)

    assert len(result) == 3
    assert result[0] == {"tag": "a", "count": 1}
    assert result[1] == {"tag": "b", "count": 2}
    assert result[2] == {"tag": "c", "count": 3}


# TODO: parametrize test
def test_filter_tags():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}, {"tag": "c", "count": 3}]
    dont_display_tags = ["c"]

    result = filter_tags(tags, dont_display_tags)

    assert len(result) == 2
    assert result[0] == {"tag": "a", "count": 1}
    assert result[1] == {"tag": "b", "count": 2}


def test_filter_tags_with_zero_counts():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}, {"tag": "c", "count": 0}]
    dont_display_tags = []

    result = filter_tags(tags, dont_display_tags)

    assert len(result) == 2
    assert result[0] == {"tag": "a", "count": 1}
    assert result[1] == {"tag": "b", "count": 2}


def test_set_hidden():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}, {"tag": "c", "count": 3}]
    dont_display_tags = ["c"]

    result = set_hidden(tags, dont_display_tags)

    assert len(result) == 3
    assert result[0] == {"tag": "a", "count": 1, "hidden": False}
    assert result[1] == {"tag": "b", "count": 2, "hidden": False}
    assert result[2] == {"tag": "c", "count": 3, "hidden": True}


# TODO: parametrize test
def test_enrich_tags():
    tags = [{"tag": "a", "count": 1}, {"tag": "b", "count": 2}]

    result = enrich_tags(tags)
    assert len(result) == 2
    assert any(x["num"] for x in result)
    # TODO: test num is coninuous and unique


# TODO: parametrize test
def test_represents_int_ok():
    assert represents_int("10")


# TODO: parametrize test
def test_represents_int_not_ok():
    assert not represents_int("10c")