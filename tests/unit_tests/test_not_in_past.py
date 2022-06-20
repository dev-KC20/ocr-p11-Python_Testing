from flask import current_app, Flask, session

import constants



def test_book_not_in_past(client):
    """
    GIVEN A secretary wishes to book a number of places for a competition
    WHEN they '/book' (GET) on a past competition
    THEN check they get a error message
    """
    expected = constants.DATE_LATE
    club_name = "Test Secretary 1"
    competition_name = "Festival 2" # past event
    url = "/book/" + competition_name + "/" + club_name
    response = client.get(
        url, data={"competition": competition_name, "club": club_name,}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    # print("booking data: ", response_data)  # tracking the error
    assert expected in response_data


def test_purchase_not_in_past(client):
    """
    GIVEN A secretary wishes to book a number of places for a competition
    WHEN they '/purchasePlaces' (POST) on a past competition
    THEN check they can't  book a place
    """
    expected = constants.BOOKING_COMPLETED
    club_name = "Test Secretary 1"
    competition_name = "Festival 2" # past event
    places_to_book = 1
    url = "/purchasePlaces"
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    # print("purchase data: ", response_data)  # tracking the error
    assert expected not in response_data


def test_purchase_in_future(client):
    """
    GIVEN A secretary wishes to book a number of places for a competition
    WHEN they '/purchasePlaces' (POST) on a competition to come
    THEN check they can book a place
    """
    expected = constants.BOOKING_COMPLETED
    club_name = "Test Secretary 1"
    competition_name = "Festival 4" # future  event
    places_to_book = 1
    url = "/purchasePlaces"
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    # print("purchase data: ", response_data)  # tracking the error
    assert expected in response_data


