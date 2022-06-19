import json
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open("clubs.json") as c:
        list_of_clubs = json.load(c)["clubs"]
        return list_of_clubs


def load_competitions():
    with open("competitions.json") as comps:
        list_of_competitions = json.load(comps)["competitions"]
        return list_of_competitions


def load_bookings(clubs, competitions):
    """
    booked_places keeps track of which club has booked places for which competition.
    "club_name" :{"competition_name" : "places_booked"}
    """
    booked_places = {}
    for current_club in clubs:
        booked_places[current_club["name"]] = {}
        for event in competitions:
            booked_places[current_club["name"]][event["name"]] = 0

    return booked_places


app = Flask(__name__)
app.secret_key = "something_special"
competitions = load_competitions()
clubs = load_clubs()
booking = load_bookings(clubs, competitions)
print("initial club x cometition: ", booking)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(401)
@app.route("/showSummary", methods=["POST"])
def show_summary():
    try:
        club = [club for club in clubs if club["email"] == request.form["email"]][0]
        return render_template("welcome.html", club=club, competitions=competitions)
    except:
        flash("Your email is not member of any of our clubs, pls check your affiliation.")
        return render_template("401.html"), 401


@app.route("/book/<competition>/<club>")
def book(competition, club):
    found_club = [c for c in clubs if c["name"] == club][0]
    found_competition = [c for c in competitions if c["name"] == competition][0]
    if found_club and found_competition:
        return render_template("booking.html", club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():
    try:
        competition_selected = request.form["competition"]
        club_selected = request.form["club"]
        places_required = int(request.form["places"])
        competition_data = [c for c in competitions if c["name"] == competition_selected][0]
        club_data = [c for c in clubs if c["name"] == club_selected][0]
    except TypeError as error:
        flash("Type error, pls check your affiliation.")
        flash(error)
    except IndexError as error:
        flash("Index Error, pls check your affiliation.")
        flash(error)
    except KeyError as error:
        flash("Key Error, pls check your affiliation.")
        flash(error)
    else:
        print("x selected data", competition_selected, club_selected)
        print("y booking data:", booking)
        places_already_booked = booking[club_selected][competition_selected]
        print("z places_already_booked:", places_already_booked)
        if places_required > int(club_data["points"]):
            flash("Sorry you didn't earn enough points, pls reconsider.", "error")
        elif places_required + places_already_booked > 12:
            flash("Sorry you booked more than 12 per competition, pls reconsider.", "error")
        else:
            booking[club_selected][competition_selected] += places_required
            competition_data["numberOfPlaces"] = int(competition_data["numberOfPlaces"]) - places_required
            flash("Great-booking complete!")
    finally:
        return render_template("welcome.html", club=club_data, competitions=competitions)


# TODO: Add route for points display
@app.route("/logout")
def logout():
    return redirect(url_for("index"))
