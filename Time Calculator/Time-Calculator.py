def add_time(start, duration, day=None):
    # Let's start by splitting the input starting time into hours, minutes & whether its PM or AM
    startlist = start.split()
    timelist = startlist[0].split(":")
    hours = int(timelist[0])
    mins = int(timelist[1])
    ampm = startlist[1]

    # splitting added time
    durationlist = duration.split(":")
    hours2 = int(durationlist[0])
    mins2 = int(durationlist[1])

    # returning error if mins field is >=60
    if mins >= 60 or mins2 >= 60:
        return "Error: mins must be below 60"

    # creating day in week dictionary for later use
    weekdic = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}

    # reversed dictionary

    weekdic2 = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    newhours = hours + hours2
    newmins = mins + mins2

    # if newmins adds up to more than 59, adjust newmins and add 1 hour to the newhours
    if newmins > 59:
        newmins = newmins - 60
        newhours = newhours + 1

    # if newhours adds up to more than 13, adjust newhours and add 1 to the count
    # count will be used to determine whether its AM/PM and the day of the week
    count = 0
    while newhours >= 12:
        newhours = newhours - 12
        count = count + 1

    # determening whether its AM or PM based on the number of iterations of the above loop
    if ampm == "PM":
        if count == 0 or (count % 2) == 0:
            finalampm = "PM"
        else:
            finalampm = "AM"
    else:
        if count == 0 or (count % 2) == 0:
            finalampm = "AM"
        else:
            finalampm = "PM"

    manydays = ""

    n = 0
    # determening whether a day or many days have passed, and how many
    if ampm == "PM":
        if count == 1 or count == 2:
            n = 1
            manydays = "(next day)"
        elif count >= 3:
            if (count % 2) == 0:
                n = str(int(count / 2))
            else:
                n = str(int((count + 1) / 2))

            manydays = '''(''' + n + " days later)"
    else:
        if count == 2 or count == 3:
            n = 1
            manydays = "(next day)"
        elif count >= 4:
            if (count % 2) == 0:
                n = str(int(count / 2))
            else:
                n = str(int((count + 1) / 2))

            manydays = '''(''' + n + " days later)"

    # adding an extra 0 if minutes only contain one digit
    if len(str(newmins)) == 1:
        newmins = "0" + str(newmins)
    else:
        newmins = str(newmins)

    # Changing midday and midnight convention
    if newhours == 0:
        newhours = "12"
    else:
        newhours = str(newhours)

    # some code to get the day of the week
    if day != None:
        day = str(day)
        day = day.lower()
        dayn = weekdic[day]
        newday = dayn + int(n)
        while newday > 7:
            newday = newday - 7
        finalday = str(weekdic2[newday])
        new_time = newhours + ":" + newmins + " " + finalampm + ", " + finalday + " " + manydays
        new_time = new_time.rstrip()

    else:
        # concatenating to deliver final time
        new_time = newhours + ":" + newmins + " " + finalampm + " " + manydays
        new_time = new_time.rstrip()
    return new_time