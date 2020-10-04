import sqlite3
import time


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Connection:
    def __new__(cls, filename="data.sql.db"):
        if not hasattr(cls, "instance"):
            conn = sqlite3.connect(filename)
            conn.row_factory = dict_factory
            # conn.set_trace_callback(print) # todo: settings
            cls.instance = conn
        return cls.instance


def create_tables(conn: sqlite3.Connection):
    query = """
        CREATE TABLE questions (question_id integer, 
                                link text, 
                                title text, 
                                creation_date integer, 
                                last_activity_date integer, 
                                score integer, 
                                answer_count integer, 
                                view_count integer,
                                is_answered integer, 
                                tags string, 
                                category string, 
                                subcategory string, 
                                owner_reputation integer)
    """
    cursor = conn.cursor()
    cursor.execute(query)


def add_question(conn: sqlite3.Connection, q: dict):
    try:
        with conn:
            query = """
                INSERT INTO questions(question_id, 
                                      link, 
                                      title, 
                                      creation_date, 
                                      last_activity_date, 
                                      score,
                                      answer_count, 
                                      view_count, 
                                      is_answered, 
                                      tags, 
                                      category, 
                                      subcategory, 
                                      owner_reputation)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?)
            """
        conn.execute(query, (q["question_id"],
                             q["link"],
                             q["title"],
                             q["creation_date"],
                             q["last_activity_date"],
                             q["score"],
                             q["answer_count"],
                             q["view_count"],
                             q["is_answered"],
                             ", ".join(q["tags"]),
                             q.get("category", ""),
                             q.get("subcategory", ""),
                             q["owner"].get("reputation", 0)))
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)


# TODO: can be optimized
def add_list_of_questions(questions, connection: sqlite3.Connection = None):
    # todo: decorator
    if not connection:
        connection = Connection()

    for question in questions:
        add_question(connection, question)


def get_questions(conn: sqlite3.Connection):
    query = """
        SELECT question_id, 
               link, 
               title, 
               creation_date, 
               last_activity_date, 
               score, 
               answer_count, 
               view_count,
               is_answered, 
               tags, 
               category, 
               subcategory, 
               owner_reputation
        FROM questions
    """

    crsr = conn.cursor()
    crsr.execute(query)
    return crsr.fetchall()


def get_counts_by_category(connection: sqlite3.Connection = None):
    # todo: decorator
    if not connection:
        connection = Connection()

    query = """
        SELECT category AS tag, count(question_id) AS count
        FROM questions
        GROUP BY category
    """

    crsr = connection.cursor()
    crsr.execute(query)
    return crsr.fetchall()


def get_questions_by_category(conn: sqlite3.Connection, category: str):
    query = """
            SELECT question_id, 
                   link, 
                   title, 
                   creation_date, 
                   last_activity_date, 
                   score, 
                   answer_count, 
                   view_count,
                   is_answered, 
                   tags, 
                   category, 
                   subcategory, 
                   owner_reputation
            FROM questions
            WHERE category = :category
        """

    crsr = conn.cursor()
    crsr.execute(query, {"category": category})
    return crsr.fetchall()


def delete_question(conn: sqlite3.Connection, question: dict):
    query = """
        DELETE FROM questions WHERE question_id = :question_id;        
    """
    conn.execute(query, {"question_id": question["question_id"]})
    conn.commit()


# TODO: add test
def delete_questions_by_category(conn: sqlite3.Connection, category: str):
    query = """
        DELETE FROM questions WHERE category = :category
    """
    conn.execute(query, {"category": category})
    conn.commit()


# TODO: index (по дате)
def count_new_questions_for_tag(category, seconds, connection: sqlite3.Connection = None):
    # todo: decorator
    if not connection:
        connection = Connection()

    limit = int(time.time()) - seconds
    query = """
        SELECT COUNT(question_id) AS CNT FROM questions WHERE category = :category and creation_date >= :limit
    """

    crsr = connection.cursor()
    crsr.execute(query, {"category": category, "limit": limit})
    result = crsr.fetchall()
    return result[0]["CNT"]
