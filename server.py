from datetime import datetime
import json
from flask import Flask, render_template, request, redirect, flash, url_for

import constants

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
app.secret_key = constants.SECRET_KEYS
competitions = load_competitions()
clubs = load_clubs()
booking = load_bookings(clubs, competitions)


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
        flash(constants.MAIL_UNKNOWN)
        return render_template("401.html"), 401


@app.route("/book/<competition>/<club>")
def book(competition, club):
    found_club = [c for c in clubs if c["name"] == club][0]
    found_competition = [c for c in competitions if c["name"] == competition][0]
    if found_club and found_competition:
        date_competition = datetime.strptime(found_competition["date"], "%Y-%m-%d %H:%M:%S")
        if date_competition < datetime.now():
            flash(constants.DATE_LATE)
            return render_template("welcome.html", club=club, competitions=competitions)
        else:
            flash(constants.DATE_FINE)
            return render_template("booking.html", club=found_club, competition=found_competition)
    else:
        flash(constants.SOMETHING_WRONG)
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
        flash(constants.TYPE_ERROR)
        flash(error)
    except IndexError as error:
        flash(constants.INDEX_ERROR)
        flash(error)
    except KeyError as error:
        flash(constants.KEY_ERROR)
        flash(error)
    else:
        places_already_booked = booking[club_selected][competition_selected]
        # print("x selected data", competition_selected, club_selected)
        # print("y booking data:", booking)
        # print("z places_already_booked:", places_already_booked)
        date_competition = datetime.strptime(competition_data["date"], "%Y-%m-%d %H:%M:%S")
        if places_required > int(club_data["points"]):
            flash(constants.NOT_ENOUGH_POINTS, "error")
        elif places_required + places_already_booked > 12:
            flash(constants.MORE_THAN_MAX, "error")
        elif date_competition < datetime.now():
             flash(constants.DATE_LATE)
        else:
            booking[club_selected][competition_selected] += places_required
            competition_data["numberOfPlaces"] = int(competition_data["numberOfPlaces"]) - places_required
            flash(constants.BOOKING_COMPLETED, "info")
    finally:
        return render_template("welcome.html", club=club_data, competitions=competitions)


# TODO: Add route for points display
@app.route("/logout")
def logout():
    return redirect(url_for("index"))
