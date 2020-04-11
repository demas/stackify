from typing import List, Dict


def transform_tags(tag_counts: Dict[str, int]) -> List[Dict[str, int]]:
    return [{"tag": tag, "count": count} for (tag, count) in tag_counts.items()]


def filter_tags(tags: List[Dict[str, int]], dont_display_tags: List[str]) -> List[Dict[str, int]]:
    return [tag for tag in tags if tag["tag"] not in dont_display_tags and tag["count"] > 0]


# TODO: thinkt to refactore
def set_hidden(tags: List[Dict[str, int]], dont_display_tags: List[str]) -> List[Dict[str, int]]:
    result = []
    for tag in tags:
        if tag["tag"] in dont_display_tags:
            tag["hidden"] = True
        else:
            tag["hidden"] = False
        result.append(tag)
    return result


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
