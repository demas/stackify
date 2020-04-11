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


@pytest.fixture(scope="function")
def question_1():
    return {'tags': ['javascript', 'selenium-webdriver'],
            'owner': {'reputation': 1, 'user_id': 11820750, 'user_type': 'registered',
                      'profile_image': 'https://lh5.googleusercontent.com/image.jpg',
                      'display_name': 'Ramakrishnan Rajaram',
                      'link': 'https://stackoverflow.com/users/11820750/ramakrishnan-rajaram'},
            'is_answered': False,
            'view_count': 1,
            'answer_count': 0,
            'score': 0,
            'last_activity_date': 1586238477,
            'creation_date': 1586238477,
            'question_id': 61073531,
            'link': 'https://stackoverflow.com/questions/61073531/how-to-get-the-size-of-an-web-page-using-selenium-webdriver',
            'title': 'How to get the size of an web page using selenium webdriver?',
            }


@pytest.fixture(scope="function")
def question_2():
    return {'tags': ['pdftron', 'xfdf'],
            'owner': {'reputation': 119, 'user_id': 8081395, 'user_type': 'registered',
                      'profile_image': 'https://www.gravatar.com/avatar/other.jpg', 'display_name': 'syed',
                      'link': 'https://stackoverflow.com/users/8081395/syed'},
            'is_answered': False, 'view_count': 4, 'answer_count': 0, 'score': 0, 'last_activity_date': 1586239736,
            'creation_date': 1586239736, 'question_id': 61073774,
            'link': 'https://stackoverflow.com/questions/61073774/pdftron-webviewer-window-content-disappears-on-browser-window-zoom-in-and-zoom-o',
            'title': 'PDFtron webviewer window content disappears on browser window zoom in and zoom out and never appears again'
            }


@pytest.fixture(scope="function")
def question_3():
    return {'tags': ['firebase', 'database-design', 'google-cloud-firestore'],
            'owner': {'reputation': 63, 'user_id': 5688837, 'user_type': 'registered',
                      'profile_image': 'https://www.gravatar.com/avatar/image.png',
                      'display_name': 'ShaneM', 'link': 'https://stackoverflow.com/users/5688837/shanem'},
            'is_answered': False, 'view_count': 4, 'answer_count': 0, 'score': 0, 'last_activity_date': 1586239748,
            'creation_date': 1586239748, 'question_id': 61073779,
            'link': 'https://stackoverflow.com/questions/61073779/fireabse-cloud-firestore-data-architecture-for-nested-data-structures',
            'title': 'Fireabse (Cloud Firestore) Data Architecture for Nested Data Structures'}


@pytest.fixture(scope="function")
def list_of_questions(question_1, question_2, question_3):
    return [question_1, question_2, question_3]


@pytest.fixture(scope="function")
def list_of_classified_questions(question_1, question_2, question_3):
    question_1["first"] = "js"
    question_3["first"] = "js"
    question_2["first"] = "js"
    return [question_1, question_2, question_3]
