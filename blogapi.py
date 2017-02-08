# Blog API
import json
import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_next_post_id(cursor):
    cursor.execute("SELECT MAX(post_id) FROM posts")
    try:
        post_id = cursor.fetchone()[0] + 1
    except Exception:
        post_id = 1
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


def add_post_to_database(body, title):
    connection = create_connection()
    cursor = connection.cursor()
    post_id = get_next_post_id(cursor)
    sql_command = '''
        INSERT INTO posts(post_id, title, body)
        VALUES ({0}, "{1}", "{2}")
        '''.format(post_id, title, body)
    print('SQL COMMAND: {}'.format(sql_command))
    cursor.execute(sql_command)
    connection.commit()
    connection.close()


@app.route("/post", methods=['POST'])
def create_post():
    content = request.json
    print('Incoming Request {}'.format(content))
    try:
        title = content['title']
        body = content['body']
        add_post_to_database(body, title)
        return '', 201
    except Exception as e:
        print('ERROR: {}'.format(e))
        return 'Error while processing request, check the body of your request', 400


@app.route("/posts")
def get_all_posts():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT post_id, title, body FROM posts")
    print('Posts retrieved from database')

    posts = cursor.fetchall()

    response_content = []
    for post in posts:
        response_content.append(
            {
                'post_id': post[0],
                'title': post[1],
                'body': post[2]
            }
        )
    return json.dumps(response_content), 200


if __name__ == "__main__":
    app.run()
