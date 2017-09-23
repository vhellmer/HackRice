#Calendar


### stored list = [title, time, location, people, note, attachment]


def add_event(list):
    title = input("enter event name: ")
    time = input("enter time: ")
    location = input("enter location: ")
    people  = input("enter people: ")
    note = input("enter note: ")
    attachment = input("enter attachment?")
    return list.append([title, time, location, people, note ,attachment])

def display(event):
    return ("Your next scheduled event is... " + event[0] + " at " +event[1] + " at " + event[2] +" with " + event[3], "Note: " + event[4])

calendar =[]
add_event(calendar)
print (display(calendar[0]))

