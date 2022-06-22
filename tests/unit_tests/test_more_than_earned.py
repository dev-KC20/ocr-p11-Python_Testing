from flask import current_app, Flask, session

import constants


def test_book_less_places_than_points_earned(client):
    """
    GIVEN selected club, competition and # of place to book
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that the page responded is the Welcome page
    """

    expected_status = 200
    expected = constants.BOOKING_COMPLETED
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    places_to_book = 3  # ts3 only got 4 pts
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



def test_book_more_places_than_points_earned(client):
    """
    GIVEN selected club, its earned points less than # of place to book
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that no welcome with booking completed
    """
    expected = constants.NOT_ENOUGH_POINTS
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    places_to_book = 5  # club only got 4
    url = "/purchasePlaces"
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.data.decode()
    assert expected in response_data

