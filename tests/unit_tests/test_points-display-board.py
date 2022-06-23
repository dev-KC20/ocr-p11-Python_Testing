from flask import current_app, Flask, session

import utils.constants as constants

def test_url_display_board_is_available(client):
    """
    GIVEN  a secretary logs into the app
    WHEN the '/displayBoard' page is requested (GET)
    THEN check that the response is valid
    """

    response = client.get("/displayBoard")
    assert response.status_code == 200


