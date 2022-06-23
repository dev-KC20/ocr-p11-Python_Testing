def test_purchase_x_places_and_show_account(client):
    """
    GIVEN A secretary having n points wishes to book m number of places for a competition
    WHEN they '/purchasePlaces' (POST) m places
    THEN check their account shows n-m points
    """
    expected = "12"  # new
    club_name = "Test Secretary 1"  # 15 pts
    places_to_book = 1
    competition_name = "Festival 3"
    url = "/purchasePlaces"
    response = client.post(
        url, data={"competition": competition_name, "club": club_name, "places": places_to_book}, follow_redirects=True
    )
    response_data = response.get_data(as_text=True)
    account_location = "Points available:"
    account_start = response_data.find(account_location)
    account_start += len(account_location)
    account_end = account_start + 5
    account_balance = response_data[account_start:account_end]
    assert expected in account_balance
