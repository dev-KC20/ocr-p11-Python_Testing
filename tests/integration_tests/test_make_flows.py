from flask import current_app, Flask, session

import constants


def test_make_happily_flow_from_loggin_to_purchasing(client):

    """
    GIVEN a Flask application configured for testing and a club's secretary
    requested to book 3 places at Festival 4 
    THEN the hereunder flow will be achieved
    """


    """ A
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid and the page responded is of the GUDLFT company
    """
    expected_status = 200
    expected_welcome = b"Welcome to the GUDLFT Registration Portal!"
    response = client.get("/")
    assert response.status_code == expected_status
    assert expected_welcome in response.data

    """ B
    WHEN a known user post to the showSummary url (POST)
    THEN he is directed to the Welcome page
    """
    expected_summary = "Competitions:"
    mail = "ts1@club1.asso"
    response = client.post("/showSummary", data={"email": mail}, follow_redirects=True)
    response_data = response.data.decode()
    assert response.status_code == expected_status
    assert expected_summary in response_data

    """ C
    WHEN the '/book/<competition>/<club>' page is requested (GET)
    THEN check that the page responded is the booking page
    """
    expected_booking = b"Booking for"
    club_name = "Test Secretary 3"
    competition_name = "Festival 3"
    url = "/book/" + competition_name + "/" + club_name
    response = client.get(url, data={"competition": competition_name, "club": club_name}, follow_redirects=False)
    assert response.status_code == expected_status
    
    assert expected_booking in response.data

    """ D
    WHEN the '/purchasePlaces' page is requested (POST)
    THEN check that the page responded is the Welcome page
    and check their account shows 4-3==1 points
    """

    expected_completed = constants.BOOKING_COMPLETED
    expected_account = "1"
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
    assert expected_completed in response_data
    response_text = response.get_data(as_text=True)
    account_location = "Points available:"
    account_start = response_text.find(account_location)
    account_start += len(account_location)
    account_end = account_start + 5
    account_balance = response_text[account_start:account_end]
    assert expected_account in account_balance

    # print("D response: ", response_data, account_balance)  # tracking the error
