import pickledb


def get_database():
    return DB(pickledb.load("data.db", False))


class DB:
    def __init__(self, db):
        self.db = db

    def counts(self):
        return self.db.get("counts")

    def tag(self, first):
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
            data.append(question)
            self.db.set(key, data)

        counts = self.db.get("counts")
        if not counts:
            self.db.dcreate("counts")
        self.db.dadd("counts", (question["first"], len(data)))

        if dump:
            self.db.dump()

    def add(self, question: dict):
        self.add_first(question)

    def add_list(self, questions):
        print("storing data...")
        for q in questions:
            self.add_first(q, dump=False)
        self.db.dump()

    def set_by_tag(self, tag: str, questions):
        self.db.set("f:" + tag, questions)

        if not self.db.get("counts"):
            self.db.dcreate("counts")

        self.db.dadd("counts", (tag, len(questions)))
        self.db.dump()

    def remove_by_tag(self, tag: str):
        self.db.set("f:" + tag, [])
        self.db.dadd("counts", (tag, 0))
        self.db.dump()