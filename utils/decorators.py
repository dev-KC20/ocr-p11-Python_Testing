from flask import redirect, url_for, session, flash
import functools

def login_required(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for("index"))

    return wrap