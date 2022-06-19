# future fixtures
import pytest
import server  # to have its Club object mocked
from server import app


app.config.update(
    {
        "TESTING": True,
    }
)


@pytest.fixture(scope="function")
def clubs():
    # data fixture to mock club secretaries
    clubs = [
        {"name": "Test Secretary 1", "email": "ts1@club1.asso", "points": "15"},
        {"name": "Test Secretary 2", "email": "ts2@club2.asso", "points": "0"},
        {"name": "Test Secretary 3", "email": "ts3@club3.asso", "points": "4"},
        {"name": "Test Secretary 4", "email": "ts4@club4.asso", "points": "8"},
        {"name": "Test Secretary 5", "email": "ts5@club5.asso", "points": "50"},
    ]
    return clubs


@pytest.fixture(scope="function")
def competitions():
    # data fixture to mock competitions events
    competitions = [
        {"name": "Festival 1", "date": "2023-03-27 10:00:00", "numberOfPlaces": "25"},
        {"name": "Festival 2", "date": "2000-03-27 10:00:00", "numberOfPlaces": "5"},
        {"name": "Festival 3", "date": "2022-09-27 10:00:00", "numberOfPlaces": "20"},
        {"name": "Festival 4", "date": "2023-03-27 10:00:00", "numberOfPlaces": "2"},
    ]
    return competitions


# @pytest.fixture(scope="function")
booking = {
    "Test Secretary 1": {"Festival 1": 0, "Festival 2": 0, "Festival 3": 0, "Festival 4": 0},
    "Test Secretary 2": {"Festival 1": 0, "Festival 2": 0, "Festival 3": 0, "Festival 4": 0},
    "Test Secretary 3": {"Festival 1": 0, "Festival 2": 0, "Festival 3": 0, "Festival 4": 0},
    "Test Secretary 4": {"Festival 1": 0, "Festival 2": 0, "Festival 3": 0, "Festival 4": 0},
    "Test Secretary 5": {"Festival 1": 0, "Festival 2": 0, "Festival 3": 0, "Festival 4": 0},
}
# return booked_places


@pytest.fixture
def client(mocker, clubs, competitions):
    mocker.patch.object(server, "clubs", clubs)
    mocker.patch.object(server, "competitions", competitions)
    mocker.patch.object(server, "booking", booking)
    # client fixture to provide instances of test client against our server app
    with server.app.test_client() as client:
        yield client
