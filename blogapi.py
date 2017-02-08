# Blog API

import sqlite3

from flask import Flask, request

app = Flask(__name__)


# TODO: add tests


def get_latest_post_id(cursor):
    cursor.execute("SELECT MAX(post_id) FROM posts")
    post_id = cursor.fetchone()[0] + 1
    print("Next post_id: {}".format(post_id))

    return post_id


def create_connection(db_file='blog.db'):
    """
    Returns SQLite connection
    """
    try:
        return sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return None


@app.route("/post", methods=['POST'])
def create_post(title='default_title', body='default_body'):
    # TODO: add parameters to request in JSON
    if request.method == 'POST':
        connection = create_connection()
        cursor = connection.cursor()

        post_id = get_latest_post_id(cursor)

        sql_command = '''
                INSERT INTO posts(post_id, title, body)
                VALUES ({0}, "{1}", "{2}")
                '''.format(post_id, title, body)

        cursor.execute(sql_command)

        connection.commit()
        connection.close()
    else:
        # TODO: add 400 error here: can only use POST
        pass


@app.route("/posts")
def get_all_posts():
    #TODO: return as JSON-formated
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM posts")

    posts = cursor.fetchall()

    for post in posts:
        print(post)


def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
