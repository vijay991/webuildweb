from flask import render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from app import app, db
from app.models import user


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        email = user(email=form.email.data)
        db.session.add(email)
        db.session.commit()
        flash('Subscribed')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)