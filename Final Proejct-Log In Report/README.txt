Capstone: IT Support Specialist Program by Google 
Login Logout Report
Author: Torrey Adams, Copilot

Imagine that you're an IT specialist working in a medium-sized company, your manager wants to create 
a daily report that tracks the use of machines. Specifically, she wants to know which users are 
currently connected to which machines, it's your job to create the report. In your company, there's 
a system that collects every event that happens on the machines on the network. Among the many events 
collected it records each time a user logs in or out of a computer. With this information, we want to 
write a script that generates a report of which users are logged in to which machines at that time. 

Before we jump into solving that problem, we need to know what information we'll use as input and what 
information we'll have as output. We can work this out by looking at the rest of the system where our 
script will live. In our report scenario, the input is a list of events, each event is an instance of 
the event class. An event class contains the date when the event happened, the name of the machine 
where it happened, the user involved, and the event type. In this scenario, we care about the login 
and logout event type. The attributes are called date, user, machine, and type. The event types are 
strings and the ones we care about are login and logout. With that we should have enough information 
about the input of our script. Our script will receive a list of event objects and we'll access the 
events attributes. 

We'll then use that information to know if a user is currently logged into a machine or not. 
Let's talk about the output. We want to generate a report that lists all the machine 
names and for each machine, lists of the users that are currently logged in. We then want this 
information printed on the screen. We've been tasked with generating a report and we can decide 
exactly how we want that report to look. One option would be to print the name of the machine at 
the beginning of the line and then list the current users on separate lines and indent it to the 
right, or we could print the machine name followed by a colon and then the usernames separated by 
commas all in the same line. 

Let's keep it simple for now and we'll go with the approach of printing the machine name followed 
by all the current users separated by commas.

Problem Statement:
You are an IT specialist working in a medium-sized company. Your manager wants to track the usage 
of machines in the company on a daily basis. Specifically, she wants to know which users are currently 
connected to which machines.

Your company has a system that collects every event that happens on the machines on the network. 
Among the many events collected, it records each time a user logs in or out of a computer.
You are tasked with writing a script that generates a report of which users are logged in to which 
machines at a given time.

Input:
The input to your script is a list of events. Each event is an instance of the Event class. An Event c
lass contains the following attributes:

      date: The date when the event happened.
      user: The user involved in the event.
      machine: The name of the machine where the event happened.
      type: The event type. The event types are strings and the ones you care about are ‘login’ and ‘logout’.

Output:
The output of your script should be a report that lists all the machine names and for each machine, lists 
the users that are currently logged in. The report should be printed on the screen. The format of the report should be the machine name followed by all the current users separated by commas.

Constraints:
The events are correctly paired and there are no ‘logout’ events without a corresponding ‘login’ event.
A user does not log into the same machine multiple times without logging out.
Your task is to write a Python script that takes the list of events as input and generates the required 
report. The script should handle the ‘login’ and ‘logout’ events correctly and generate an accurate report 
of the current state of the machines. The script should be simple, efficient, and adaptable to fit the 
specific needs and constraints of your system.

