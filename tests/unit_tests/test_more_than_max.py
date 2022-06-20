from flask import current_app, Flask, session

import constants



def test_book_more_than_max_per_competition(client):
    """
    GIVEN selected club, its earned points and # of places required over max per competition
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check for an error message
    """
    expected = constants.MORE_THAN_MAX
    club_name = "Test Secretary 5" # club has 50 pts == 16 places +2 pts
    competition_name = "Festival 3"
    places_to_book = 15
    url = "/purchasePlaces"
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    # print("purchase data: ", response_data)  # tracking the error
    assert expected in response_data


def test_book_more_than_max_per_competition_in_two_times(client):
    """
    GIVEN selected club, its earned points and # of places required over max per competition
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check for an error message
    """
    expected = constants.NOT_ENOUGH_POINTS 
    club_name = "Test Secretary 5" # 50pts ; 11*3 + 2*3 == 39 pts ; 13 places
    competition_name = "Festival 3" # 20 places
    places_to_book = 7
    url = "/purchasePlaces"
    response_first_purchase = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_first_purchase_data = response_first_purchase.get_data(as_text=True)
    places_to_book = 6
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    print("purchase data: ", response_data)  # tracking the error
    assert expected in response_data
