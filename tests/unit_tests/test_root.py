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
    email = "unknown@noclub.asso"
    expected_value = 401
    response = client.post("/showSummary", data={"email": email}, follow_redirects=False)
    # response_data = response.data.decode()
    # print("expected error: ", response_data)  # tracking the error
    assert response.status_code == expected_value


def test_url_book_goes_happy_to_booking_page(client):
    """
    GIVEN club and competition exists
    WHEN the '/book/<competition>/<club>' page is requested (GET)
    THEN check that the page responded is the booking page
    """

    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    url = "/book/" + competition_name + "/" + club_name
    response = client.get(url, data={"competition": competition_name, "club": club_name}, follow_redirects=False)
    expected_status = 200
    expected = b"Booking for"
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



def test_url_book_goes_happy_to_purchase_page(client):
    """
    GIVEN selected club, competition and # of place to book
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that the page responded is the Welcome page
    """

    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    places_to_book = 5
    url = "/purchasePlaces"
    response = client.post(url,
    data={"competition": competition_name, "club": club_name, "places": places_to_book},
     follow_redirects=False)
    response_data = response.data.decode()
    print("purchase data: ", response_data)  # tracking the error
    expected_status = 200
    expected = b"Welcome"
    assert response.status_code == expected_status
    assert expected in response.data

    
def test_book_no_more_places_than_points_earned(client):
    """
    GIVEN selected club, its earned points less than # of place to book  
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that no welcome with booking completed
    """
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    # club_details = next((sub for sub in clubs if sub['name'] == club_name), None)
    # print('club mocked:', club_details["points"])
    places_to_book = 5
    url = "/purchasePlaces"
    response = client.post(url,
    data={"competition": competition_name, "club": club_name, "places": places_to_book},
     follow_redirects=True)
    response_data = response.data.decode()
    # print("purchase data: ", response_data)  # tracking the error
    expected = "<li>Great-booking complete!</li>"
    assert expected not in response_data
    
def test_book_no_more_than_max_per_competition(client):
    """
    GIVEN selected club, its earned points and # of place to book over max 
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that no welcome with booking completed
    """
    club_name = "Test Secretary 1"
    competition_name = "Festival 3"
    places_to_book = 15
    url = "/purchasePlaces"
    response = client.post(url,
    data={"competition": competition_name, "club": club_name, "places": places_to_book},
     follow_redirects=True)
    response_data = response.data.decode()
    # print("purchase data: ", response_data)  # tracking the error
    expected = "<li>Great-booking complete!</li>"
    assert expected not in response_data