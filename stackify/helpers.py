import time
from typing import List, Dict

from store import Connection


def transform_tags(tag_counts: Dict[str, int]) -> List[Dict[str, int]]:
    return [{"tag": tag, "count": count} for (tag, count) in tag_counts.items()]


def filter_tags(tags: List[Dict[str, int]], dont_display_tags: List[str]) -> List[Dict[str, int]]:
    return [tag for tag in tags if tag["tag"] not in dont_display_tags and tag["count"] > 0]


def set_hidden(tags: List[Dict[str, int]], dont_display_tags: List[str]) -> List[Dict[str, int]]:
    def set_in_tag(tag: Dict[str, int]) -> Dict[str, int]:
        tag["hidden"] = tag["tag"] in dont_display_tags
        return tag

    return list(map(set_in_tag, tags))


# TODO: test for this function
def set_new(tags: List[Dict[str, int]]) -> List[Dict[str, int]]:
    def set_in_tag(tag: Dict[str, int]) -> Dict[str, int]:
        tag["new_count"] = Connection().new_count_by_tag(tag["tag"], 1 * 60 * 60)  # TODO: settings
        return tag

    return list(map(set_in_tag, tags))


def enrich_tags(tag_counts: List[Dict[str, int]]) -> List[Dict[str, int]]:
    result = []
    num = 1
    for element in tag_counts:
        element["num"] = num
        result.append(element)
        num = num + 1
    return result


def represents_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


# TODO: test
def new_period_limit() -> int:
    return int(time.time()) - 1 * 60 * 60 # TODO: settings


def add_new_header_for_questions(questions: List[Dict]) -> List[Dict]:
    for question in questions:
        question["new_flag"] = question["creation_date"] >= new_period_limit()
    return questions


def fix_question_title(questions: List[Dict]) -> List[Dict]:
    for question in questions:
        question["title"] = question["title"].replace("&quot;", "\"")
        question["title"] = question["title"].replace("&#39;", "\'")
        question["title"] = question["title"].replace("&lt;", "<")
        question["title"] = question["title"].replace("&gt;", ">")
    return questions


def filter_active_questions(questions: List[Dict]) -> List[Dict]:
    return list(filter(lambda q: q["new_flag"], questions))

