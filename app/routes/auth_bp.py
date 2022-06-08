from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from flask import Blueprint, redirect, url_for, session
import app

app.app_context().push()

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return app.oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@auth.route("/callback", methods=["GET", "POST"])
def callback():
    token = app.oauth.authorize_access_token()
    session["user"] = token
    return redirect("/")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )