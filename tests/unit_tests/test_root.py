from flask import current_app, Flask, session


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


def test_known_email_is_shown_welcome(client):
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


def test_unknown_email_is_not_shown_welcome(client):
    """
    GIVEN a list of clubs being mocked
    WHEN an uknown user post to the showSummary url (POST)
    THEN he is not directed to the Welcome page
    """
    expected_value = 401
    email = "unknown@noclub.asso"
    response = client.post("/showSummary", data={"email": email}, follow_redirects=False)
    # response_data = response.data.decode()
    # print("expected error: ", response_data)  # tracking the error
    assert response.status_code == expected_value


def test_url_book_directs_to_booking_page(client):
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


# def test_url_book_goes_sad_to_booking_page(client):
#     """
#     GIVEN club exist but no competition exists
#     WHEN the '/book/<competition>/<club>' page is requested (GET)
#     THEN an error is araised
#     """

#     club_name = "Test Secretary 3"
#     competition_name = "Vestival 3"
#     url = "/book/" + competition_name + "/" + club_name
#     response = client.get(url, data={"competition": competition_name, "club": club_name}, follow_redirects=False)
#     expected_status = 404
#     assert response.status_code == expected_status


def test_book_less_places_than_points_earned(client):
    """
    GIVEN selected club, competition and # of place to book
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that the page responded is the Welcome page
    """

    expected_status = 200
    expected = "<li>Great-booking complete!</li>"
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    places_to_book = "3"  # ts3 only got 4 pts
    url = "/purchasePlaces"
    body = {"competition": competition_name, "club": club_name, "places": places_to_book}
    response = client.post(
        url,
        data=body,
        follow_redirects=False,
    )
    response_data = response.data.decode()
    assert response.status_code == expected_status
    assert expected in response_data
    # print("purchase body: ", body)  # tracking the error
    # print("purchase response: ", response.data.decode())  # tracking the error


def test_book_more_places_than_points_earned(client):
    """
    GIVEN selected club, its earned points less than # of place to book
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that no welcome with booking completed
    """
    expected = "Sorry you didn't earn enough points, pls reconsider."
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    places_to_book = 5  # club obly got 4
    url = "/purchasePlaces"
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.data.decode()
    assert expected not in response_data


def test_book_more_than_max_per_competition(client):
    """
    GIVEN selected club, its earned points and # of places required over max per competition
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check for an error message
    """
    expected = "Sorry you booked more than 12 per competition, pls reconsider."
    club_name = "Test Secretary 1"
    competition_name = "Festival 3"
    places_to_book = 15
    url = "/purchasePlaces"
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    print("purchase data: ", response_data)  # tracking the error
    assert expected in response_data


def test_book_more_than_max_per_competition_in_two_times(client):
    """
    GIVEN selected club, its earned points and # of places required over max per competition
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check for an error message
    """
    expected = "Sorry you booked more than 12 per competition, pls reconsider."
    club_name = "Test Secretary 1"
    competition_name = "Festival 3"
    places_to_book = 7
    url = "/purchasePlaces"
    client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    print("purchase data: ", response_data)  # tracking the error
    assert expected in response_data
