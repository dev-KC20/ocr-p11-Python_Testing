from flask import current_app, Flask, session

import constants



def test_book_more_than_max_per_competition(client):
    """
    GIVEN selected club, its earned points and # of places required over max per competition
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check for an error message
    """
    expected = constants.MORE_THAN_MAX
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
    expected = constants.MORE_THAN_MAX
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
