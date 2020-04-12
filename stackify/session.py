from typing import List


class Session:
    def __init__(self):
        self.all_questions = []
        self.active_questions = []
        self.last_used_tag = None
        self.current_tags = []

    def switch_to_tag(self, tag: str, questions: List[dict], limit=8):
        questions.sort(key=lambda q: -1 * q["creation_date"]) # TODO: test for sorting
        self.all_questions = questions
        self.active_questions = self.all_questions[:limit]
        self.last_used_tag = tag

    def remain_questions(self):
        return [q for q in self.all_questions if q not in self.active_questions]
