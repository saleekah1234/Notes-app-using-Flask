from app import app, forms
from flask import render_template, request
from app.models import Mynotes 
from app import db  #import database model (class) Mynotes class from model.py

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new', methods=['GET', 'POST'])
def newnote():
    form = forms.NoteForm()

    if form.validate_on_submit():
        text = form.text.data
        n=Mynotes(text=text) #create instance of the model
        db.session.add(n)
        db.session.commit()


        newnote = {'text':text}

        return render_template('alert.html', newnote=newnote)

    return render_template('new.html', form=form)
@app.route('/view')
def view():
    
    notes=Mynotes.query.all()
    return render_template("view.html",notes=notes)

@app.route('/delete',methods=["DELETE"])
def delete():
    models.Mynotes.query().delete()
    db.session.commit()

    return render_template("view.html")