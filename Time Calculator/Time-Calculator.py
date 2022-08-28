def add_time(start, duration, day=None):
    # Let's start by splitting the input starting time into hours, minutes & whether its PM or AM
    start_list = start.split()
    time_list = start_list[0].split(":")
    hours = int(time_list[0])
    mins = int(time_list[1])
    ampm = start_list[1]

    # Splitting added time
    duration_list = duration.split(":")
    added_hours = int(duration_list[0])
    added_mins = int(duration_list[1])

    # Returning error if minutes field is >=60
    if mins >= 60 or added_mins >= 60:
        return "Error: mins must be below 60"

    # Creating day in week dictionary for later use
    week_dic = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}

    # Reversed dictionary capitalising week names for output
    week_dic_2 = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    new_hours = hours + added_hours
    new_mins = mins + added_mins

    # If new_mins adds up to more than 59, adjust new_mins and add 1 hour to the new_hours
    if new_mins > 59:
        new_mins -= 60
        new_hours += 1

    # If new_hours adds up to more than 13, adjust new_hours and add 1 to the count
    # Count will be used to determine whether its AM/PM and the day of the week
    count = 0
    while new_hours >= 12:
        new_hours -= 12
        count += 1

    # Determining whether its AM or PM based on the number of iterations of the above loop
    if ampm == "PM":
        if count == 0 or (count % 2) == 0:
            new_ampm = "PM"
        else:
            new_ampm = "AM"
    else:
        if count == 0 or (count % 2) == 0:
            new_ampm = "AM"
        else:
            new_ampm = "PM"

    n = 0  # This variable will be used to store the number of days that have passed
    many_days = ""  # This will be the output string representation of number of days passed

    # Determining whether a day or many days have passed, and how many
    if ampm == "PM":
        if count == 1 or count == 2:
            n = 1
            many_days = "(next day)"
        elif count >= 3:
            if (count % 2) == 0:
                n = str(int(count / 2))
            else:
                n = str(int((count + 1) / 2))

            many_days = """(""" + n + " days later)"
    else:
        if count == 2 or count == 3:
            n = 1
            many_days = "(next day)"
        elif count >= 4:
            if (count % 2) == 0:
                n = str(int(count / 2))
            else:
                n = str(int((count + 1) / 2))

            many_days = """(""" + n + " days later)"

    # Adding an extra 0 if minutes only contain one digit
    if len(str(new_mins)) == 1:
        new_mins = "0" + str(new_mins)
    else:
        new_mins = str(new_mins)

    # Changing midday and midnight convention
    if new_hours == 0:
        new_hours = "12"
    else:
        new_hours = str(new_hours)

    # Code to get the day of the week
    if day is not None:
        day = str(day)
        day = day.lower()
        day_number = week_dic[day]
        new_day = day_number + int(n)
        while new_day > 7:
            new_day = new_day - 7
        final_day = str(week_dic_2[new_day])
        new_time = (new_hours + ":" + new_mins + " " + new_ampm + ", " + final_day + " " + many_days)
        new_time = new_time.rstrip()

    else:
        # Concatenating to deliver final time
        new_time = new_hours + ":" + new_mins + " " + new_ampm + " " + many_days
        new_time = new_time.rstrip()
    return new_time
