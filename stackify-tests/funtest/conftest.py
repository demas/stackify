import random
import string

import pickledb
import pytest
import os

from store import DB


@pytest.yield_fixture(scope="function")
def testing_database():
    filename = ''.join([random.choice(string.ascii_lowercase) for _ in range(15)])
    db = DB(pickledb.load(filename, False))
    yield db
    os.remove(filename)