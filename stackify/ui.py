from fabulous.color import fg256

SHOW_LINK_TO_QUESTION = False


def say_hello():
    print()
    print("Welcome to Stackify")
    print(fg256("grey", "   f - fetch, ls - list, s[ tag/num]  - show, d - delete, del - delete last seen"))


def ls(data_to_display):
    print()
    for element in data_to_display:
        color = "lightgreen" if not element["hidden"] else "red"
        print(fg256(color, "{}: {} ({})".format(element["num"], element["tag"], element["count"])))


def display_list_of_questions(questions):
    print()
    num = 1
    for q in questions:
        print(fg256("yellow", num) + ": " + fg256("lightgreen", q["title"]))
        print(fg256("lightyellow", "  {}, score {}, answer_count {}".format(q["tags"], q["score"], q["answer_count"])))
        if SHOW_LINK_TO_QUESTION:
            print(fg256("grey", "  {}".format(q["link"])))
        print()
        num = num + 1


def alert_unclassified(questions):
    for q in questions:
        if q["first"] == "none":
            print(fg256('gray', "{}".format(q["tags"])))

