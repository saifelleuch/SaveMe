from flask import Blueprint, flash, render_template, request
from flask_login import login_required, current_user
from . import db
from website.models import Alerts

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        desc = request.form.get("desc")
        lat = request.form.get("lat")
        long = request.form.get("long")

        new_note = Alerts(Alerts_text=desc, user_id=current_user.id, lat=lat, long=long)
        db.session.add(new_note)
        db.session.commit()
        new_note.long
        flash('Alert added!', category='success')

        alerts = Alerts.query.all()
        return render_template("home.html", user=current_user, alerts=alerts)
    else:
        alerts = Alerts.query.all()
        return render_template("home.html", user=current_user, alerts=alerts)


@views.route('/')
def landing():
    return render_template("landing.html")
