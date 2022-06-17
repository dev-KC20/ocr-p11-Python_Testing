# from tests.unit_tests import client
from server import app


def test_url_root_is_available():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    response = app.test_client().get("/")
    assert response.status_code == 200


def test_url_root_is_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the page responded is of the GUDLFT company
    """
    response = app.test_client().get("/")
    expected = b"Welcome to the GUDLFT Registration Portal!"
    assert expected in response.data


def test_known_email_show_summary():
    """
    GIVEN a list of clubs being mocked
    WHEN a known user logs the root page (POST)
    THEN he is directed to the showSummary page
    """
    pass
