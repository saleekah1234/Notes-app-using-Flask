from app import app, forms
from flask import render_template, request
from app.models import Mynotes 
from app import db  #import database model (class) Mynotes class from model.py

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newnote', methods=['GET', 'POST'])
def newnote():
    form = forms.NoteForm()

    if form.validate_on_submit():
        text = form.text.data
        n=Mynotes(text=text) #create instance of the model
        db.session.add(n)
        db.seession.commit()


        newnote = {'text':text}

        return render_template('alert.html', newnote=newnote)

    return render_template('new.html', form=form)
@app.route('/viewnote')
def view():
    notes=Mynotes.query.all()
    return render_template("view.html",notes=notes)