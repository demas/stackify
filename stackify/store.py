import time

import pickledb


class Connection:
    def __new__(cls, filename="data.db"):
        if not hasattr(cls, "instance"):
            db = pickledb.load(filename, False)
            cls.instance = DB(db)
        return cls.instance


class DB:
    def __init__(self, db):
        print("db loaded")
        self.db = db

    def get_counts_by_tags(self):
        return self.db.get("counts")

    def get_questions_by_tag(self, first):
        return self.db.get("f:" + first)

    def add_first(self, question: dict, dump=True):
        key = "f:" + question["first"]
        data = self.db.get(key)
        if not data:
            data = [question]
            self.db.set(key, data)
        else:
            if not data:
                data = []

            for el in data:
                if el['question_id'] == question['question_id']:
                    return

            data.append(question)
            self.db.set(key, data)

        counts = self.db.get("counts")
        if not counts:
            self.db.dcreate("counts")
        self.db.dadd("counts", (question["first"], len(data)))

        if dump:
            self.db.dump()

    def add_question(self, question: dict):
        self.add_first(question)

    def add_list_of_questions(self, questions):
        print("storing data...")
        for q in questions:
            self.add_first(q, dump=False)
        self.db.dump()

    def set_list_of_questions_for_tag(self, tag: str, questions):
        self.db.set("f:" + tag, questions)

        if not self.db.get("counts"):
            self.db.dcreate("counts")

        self.db.dadd("counts", (tag, len(questions)))
        self.db.dump()

    def remove_questions_for_tag(self, tag: str):
        self.db.set("f:" + tag, [])
        self.db.dadd("counts", (tag, 0))
        self.db.dump()

    def count_new_questions_for_tag(self, tag: str, seconds: int) -> int:
        limit = int(time.time()) - seconds
        new_questions = list(filter(lambda q: q["creation_date"] >= limit, self.get_questions_by_tag(tag)))
        return len(new_questions)