from app.models.event import *

event1 = Event("17/09/20", "CodeClan Late Lunch", 15, "Kitchen", "Kebabs and Beer Yeehaw", False)
event2 = Event("18/09/20", "Test", 5, "TestTest", "TestTestTest", True)

events_list = [event1, event2]

def add_new_event(event):
    events_list.append(event)

def delete_event(event):
    events_list.remove(event)