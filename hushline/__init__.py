import logging
import os
from datetime import timedelta
from typing import Any

from flask import Flask, flash, redirect, session, url_for
from flask_migrate import Migrate
from werkzeug.wrappers.response import Response

from . import admin, routes, settings
from .db import db
from .model import User


def create_app() -> Flask:
    app = Flask(__name__)

    # Configure logging
    app.logger.setLevel(logging.DEBUG)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["ENCRYPTION_KEY"] = os.getenv("ENCRYPTION_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # if it's a Postgres URI, replace the scheme with `postgresql+psycopg`
    # because we're using the psycopg driver
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgresql://"):
        app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"].replace(
            "postgresql://", "postgresql+psycopg://", 1
        )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_COOKIE_NAME"] = os.environ.get("SESSION_COOKIE_NAME", "__HOST-session")
    app.config["SESSION_COOKIE_SECURE"] = True
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

    # Run migrations
    db.init_app(app)
    Migrate(app, db)

    routes.init_app(app)
    for module in [admin, settings]:
        app.register_blueprint(module.create_blueprint())

    @app.errorhandler(404)
    def page_not_found(e: Exception) -> Response:
        flash("⛓️‍💥 That page doesn't exist.", "warning")
        return redirect(url_for("index"))

    @app.context_processor
    def inject_user() -> dict[str, Any]:
        if "user_id" in session:
            user = User.query.get(session["user_id"])
            return {"user": user}
        return {}

    return app
