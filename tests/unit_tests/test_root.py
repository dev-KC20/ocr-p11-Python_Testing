
from flask import current_app, Flask

def test_url_root_is_available(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    response = client.get("/")
    assert response.status_code == 200


def test_url_root_is_home_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the page responded is of the GUDLFT company
    """
    response = client.get("/")
    expected = b"Welcome to the GUDLFT Registration Portal!"
    assert expected in response.data


def test_known_email_is_shown_welcome(client, mock_clubs):
    """
    GIVEN a list of clubs being mocked
    WHEN a known user post to the showSummary url (POST)
    THEN he is directed to the Welcome page
    """
    expected_value = "ts1@club1.asso"
    response = client.post("/showSummary", data={"email": expected_value}, follow_redirects=True)
    response_data = response.data.decode()
    assert response.status_code == 200
    assert expected_value in response_data


def test_unknown_email_is_not_shown_welcome(client, mock_clubs):
    """
    GIVEN a list of clubs being mocked
    WHEN an uknown user post to the showSummary url (POST)
    THEN he is not directed to the Welcome page
    """
    email = "unknown@noclub.asso"
    expected_value = 401
    response = client.post("/showSummary", data={"email": email}, follow_redirects=True)
    response_data = response.data.decode()
    print('expected error: ', response_data) # tracking the error
    assert response.status_code == expected_value
