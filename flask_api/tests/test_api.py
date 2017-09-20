from flask_api import app


def test_api():
    with app.app.test_client() as c:
        r = c.get('/')
        assert r.status == '200 OK'


