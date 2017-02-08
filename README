# Blog Post API

## Install
Please install with Python 3.5, other versions of Python have not yet been tested.

To install dependencies:
`pip install -e .`

## Setup

`python blogapi.py [--database]`

- `--database`
    - The database file to be used with the application.
    - Default: blog.db

## Usage
All requests must be made with JSON format.

### POST /post
Make a POST request to `<hostname>/post` with the following payload to create a new post:
```
{
    'title': 'Post Title',
    'body': 'Post Body'
}
```

### GET /posts
Make a GET request to `<hostname>/posts` to get all posts from the database.