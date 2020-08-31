import random
import sqlite3
import string

import pickledb
import pytest
import os

from relation_store import create_tables, dict_factory
from store import DB


@pytest.yield_fixture(scope="function")
def testing_database():
    filename = ''.join([random.choice(string.ascii_lowercase) for _ in range(15)])
    db = DB(pickledb.load(filename, False))
    yield db
    os.remove(filename)


@pytest.yield_fixture(scope="function")
def testing_db_connection():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = dict_factory
    create_tables(conn)
    return conn

