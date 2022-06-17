# future fixtures
import pytest
import server # to have its Club object mocked
from server import app


app.config.update(
    {
        "TESTING": True,
    }
)


@pytest.fixture
def client():
    # client fixture to provide instances of test client against our server app
    with app.test_client() as client:
        yield client


@pytest.fixture
def Clubs():
    # data fixture to mock club secretaries 
    clubs = [
        {"name": "Test Secretary 1", "email": "ts1@club1.asso", "points": "15"},
        {"name": "Test Secretary 2", "email": "ts2@club2.asso", "points": "0"},
        {"name": "Test Secretary 3", "email": "ts3@club3.asso", "points": "4"},
        {"name": "Test Secretary 4", "email": "ts4@club4.asso", "points": "8"},
        {"name": "Test Secretary 5", "email": "ts5@club5.asso", "points": "12"},
    ]
    return clubs

@pytest.fixture
def mock_clubs(mocker, Clubs):
    mocker.patch.object(server, "clubs", Clubs)
