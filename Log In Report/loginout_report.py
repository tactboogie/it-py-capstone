#!/usr/bin/env python3

'''
This script will print each machine name followed by the names of all the current users separated 
by commas. The users are added to the machine’s set when a ‘login’ event occurs and removed when 
a ‘logout’ event occurs. The events are processed in chronological order to ensure the report 
reflects the current state of the machines. Please note that this is a simple script and may 
need to be adapted to fit the specific needs and constraints of your system. For example, it 
assumes that the events are correctly paired and that there are no ‘logout’ events without a 
corresponding ‘login’ event. If that’s not the case in your system, you might need to add some 
error checking code. Also, this script doesn’t handle the case where a user logs into the same 
machine multiple times without logging out. If that’s a possibility in your system, you might 
need to adjust the script to handle it. By Copilot AI
'''

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user


def get_event_date(event):
  return event.date


def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines


def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


events = [
  Event('2024-03-23 18:56:34', 'login', 'myworkstation.local', 'toro'),
  Event('2024-03-24 13:56:34', 'logout', 'webserver.local', 'toro'),
  Event('2024-03-23 18:56:34', 'login', 'webserver.local', 'kj'),
  Event('2024-03-24 12:56:34', 'logout', 'myworkstation.local', 'toro'),
  Event('2024-03-23 08:56:34', 'login', 'webserver.local', 'toro'),
  Event('2024-03-24 11:56:34', 'login', 'mailserver.local', 'nico'),
]

users  =current_users(events)
print(users)

generate_report(users)
