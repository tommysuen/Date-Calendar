

class Date:
    """ A class that stores and manipulates dates,
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####
    def tomorrow(self):
        '''Returns the date of the day after the given'''
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[2] = 29

        self.day += 1

        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

    def add_n_days(self, n):
        '''Prints the days in between the date and n days after, but returns
    returns the date of n days after'''
        print(self)
        while n > 0:
            self.tomorrow()
            print(self)
            n = n - 1

    def __eq__(self, other):
        '''checks to see if the self date is the same as the other date'''
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
        
    def is_before(self, other):
        '''checks if the self date is before other date and returning True, and returning
    false if it isn't'''
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        else:
            return False

    def is_after(self, other):
        '''Checks if the self date is after the other date and returns True; or
    returns false if the self date is not after the other date'''
        if self != other:
            if self.is_before(other) == False:
                return True
        return False

    def diff(self, other):
        '''determines the number of days in advance or behind is from the starting
self date to the other date'''
        days = 0
        self2 = self.copy()
        other2 = other.copy()
        while self2 != other2:
            if self2.is_before(other2) == True:
                self2.tomorrow()
                days -= 1
            elif other2.is_before(self2) == True:
                other2.tomorrow()
                days += 1
        return days

    def day_of_week(self):
        '''given a date, it will return the day of the week of the given date'''
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']
        today = Date(4,9, 2016)
        days_difference = self.diff(today)
        if self.is_before(today):
            i = days_difference % 7
            if 5 + i > 6:
                i = i - 7
            return day_of_week_names[5 + i]
        if today.is_before(self):
            i = days_difference % 7
            if 5 + i > 6:
                i = i - 7
            return day_of_week_names[5+i]
        
