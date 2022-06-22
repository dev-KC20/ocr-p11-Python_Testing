from locust import HttpUser, task
from server import load_clubs, load_competitions


class HelloWorldUser(HttpUser):
    clubs = load_clubs()
    competitions = load_competitions()
    last_club = clubs[-1]
    last_competition = competitions[-1]
    email = last_club["email"]
    club_name = last_club["name"]
    competition_name = last_competition["name"]
    places_to_book = 1

    def on_start(self):
        self.client.get("/")
        self.client.post("/showSummary", data={"email": self.email})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def display_board(self):
        self.client.get("/displayBoard")

    @task
    def book_competitions(self):
        url = "/book/" + self.competition_name + "/" + self.club_name
        body = {"competition": self.competition_name, "club": self.club_name}
        self.client.get(
            url,
            data=body,
        )

    @task
    def purchase_places(self):
        url = "/purchasePlaces"
        body = {"competition": self.competition_name, "club": self.club_name, "places": self.places_to_book}
        self.client.post(
            url,
            data=body,
        )
