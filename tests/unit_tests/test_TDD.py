from flask import current_app, Flask, session

import constants


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
    expected = b"Welcome to the GUDLFT Registration Portal!"
    response = client.get("/")
    assert expected in response.data


def test_valid_url_summary_directs_welcome_page(client):
    """
    GIVEN a list of clubs being mocked
    WHEN a known user post to the showSummary url (POST)
    THEN he is directed to the Welcome page
    """
    expected_value = "Competitions:"
    mail = "ts1@club1.asso"
    response = client.post("/showSummary", data={"email": mail}, follow_redirects=True)
    response_data = response.data.decode()
    assert response.status_code == 200
    assert expected_value in response_data


def test_valid_url_book_directs_to_booking_page(client):
    """
    GIVEN club and competition exists
    WHEN the '/book/<competition>/<club>' page is requested (GET)
    THEN check that the page responded is the booking page
    """

    expected_status = 200
    expected = b"Booking for"
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    url = "/book/" + competition_name + "/" + club_name
    response = client.get(url, data={"competition": competition_name, "club": club_name}, follow_redirects=False)
    assert response.status_code == expected_status
    assert expected in response.data


def test_valid_purchase_directs_to_completed_welcome(client):
    """
    GIVEN selected club, competition and # of place to book
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that the page responded is the Welcome page
    """

    expected_status = 200
    expected = constants.BOOKING_COMPLETED
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    places_to_book = "1"  # ts3 only got 4 pts
    url = "/purchasePlaces"
    body = {"competition": competition_name, "club": club_name, "places": places_to_book}
    response = client.post(
        url,
        data=body,
        follow_redirects=False,
    )
    response_data = response.data.decode()
    response_text = response.get_data(as_text=True)
    assert response.status_code == expected_status
    assert expected in response_text
    # print("valid_purchase_directs_to_completed_welcome response: \n", response_text)  # tracking the error
    # print("purchase body: ", body)  # tracking the error
