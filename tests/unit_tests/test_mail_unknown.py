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
