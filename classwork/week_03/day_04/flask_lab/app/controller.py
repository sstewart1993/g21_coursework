from flask import render_template, request
from app import app
from app.models.event import *
from app.models.event_list import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events_list)


@app.route('/add-event', methods=['POST'])
def add_event():
    date = request.form['date']
    name = request.form['name']
    location = request.form['room_location']
    description = request.form['description']
    number_of_people = request.form['number_of_guests']
    if request.form.get('recurring'):
        recurring = True
    else:
        recurring = False
    new_event = Event(date, name, number_of_people, location, description, recurring)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events_list)

    
@app.route('/del-event')
def del_event():
    event = request.form['event']
    delete_event(event)
    return render_template('index.html', title='Home', events=events_list)

