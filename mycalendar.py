class MyCalendar:
    """
    A calendar class that allows adding and removing events for specific dates.

    Attributes:
    - events: A dictionary that maps a day of the year (represented as an integer
      between 1 and 366) to a list of event names.

    Methods:
    - day_of_year(month, day_of_month, year): Given a date specified by month, day
      of month, and year, returns the day of the year as an integer between 1 and
      366. Takes into account leap years.
    - add_event(name, month, day_of_month, year): Adds an event with the given
      name to the calendar for the specified date.
    - remove_event(name, month, day_of_month, year): Removes the event with the
      given name from the calendar for the specified date.
    - get_events(month, day_of_month, year): Returns a list of event names for the
      specified date, or None if there are no events for that date.
    """

    def __init__(self):
        self.events = {}

    def day_of_year(self, month, day_of_month, year):
        if month == 1:
            day_of_month += 0
        elif month == 2:
            day_of_month += 31
        elif month == 3:
            day_of_month += 59
        elif month == 4:
            day_of_month += 90
        elif month == 5:
            day_of_month += 31 + 28 + 31 + 30
        elif month == 6:
            day_of_month += 31 + 28 + 31 + 30 + 31
        elif month == 7:
            day_of_month += 31 + 28 + 31 + 30 + 31 + 30
        elif month == 8:
            day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31
        elif month == 9:
            day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
        elif month == 10:
            day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
        elif month == 11:
            day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        elif month == 12:
            day_of_month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        else:
            return -1

        if (year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)) and month > 2:
            day_of_month += 1
        return day_of_month

    def add_event(self, name, month, day_of_month, year):
        day_of_year = self.day_of_year(month, day_of_month, year)
        if name:
            if day_of_year in self.events:
                self.events[day_of_year].append(name)
            else:
                self.events[day_of_year] = [name]

    def remove_event(self, name, month, day_of_month, year):
        day_of_year = self.day_of_year(month, day_of_month, year)
        if name:
            if day_of_year in self.events:
                if name in self.events[day_of_year]:
                    self.events[day_of_year].remove(name)
                if len(self.events[day_of_year]) == 0:
                    del self.events[day_of_year]

    def get_events(self, month, day_of_month, year):
        day_of_year = self.day_of_year(month, day_of_month, year)
        if day_of_year in self.events:
            return self.events[day_of_year]
        else:
            return None
