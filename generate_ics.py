import pytz
from datetime import datetime
from icalendar import Calendar, Event
from icalendar import vCalAddress, vText
organizer = vCalAddress('MAILTO:invite@resilience-coffee.org')

c = Calendar()
e = Event()

base_event_dict = {
    'summary': 'Resilience Coffee',
    'description': "Join us on https://bit.ly/3DVACGs",
    'location': "https://bit.ly/3DVACGs",
    'url': "https://www.resilience-coffee.org/schedule.ics",
    'organizer': organizer
}


first_thursday_event_dict = base_event_dict | {
    'dtstart': datetime(
        2022, 10, 6,
        21, 30, 0,
        tzinfo=pytz.utc),
    'dtend':      datetime(
        2022, 10, 6,
        22, 30, 0,
        tzinfo=pytz.utc),
    'rrule': {"freq":"MONTHLY", "BYDAY": "1TH"},
}

third_friday_event_dict = base_event_dict | {
    'dtstart': datetime(
        2022, 10, 21,
        16, 30, 0,
        tzinfo=pytz.utc),
    'dtend':      datetime(
        2022, 10, 21,
        17, 30, 0,
        tzinfo=pytz.utc),
    'rrule': {"freq":"MONTHLY", "BYDAY": "3FR"},
}

def event_from_dict(event_dict):
    e = Event()
    for k, v in event_dict.items():
        e.add(k, v)
    return e

c.add_component(event_from_dict(first_thursday_event_dict))
c.add_component(event_from_dict(third_friday_event_dict))

with open('schedule.ics', 'wb') as f:
    f.write(c.to_ical())
