class Clock:
    def __init__(self, hour, minute):
        total_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute + minutes) % (24 * 60)
        return Clock(0, total_minutes)

    def __sub__(self, minutes):
        return self.__add__(-minutes)

# The rest was my code, fairly good. Though via total minutes it would have been much easier lol.

if False:
    class Clock:
        def __init__(self, hour, minute):
            new_hour = hour % 24
            new_minute = minute % 60
            if minute > 59:
                new_hour += minute // 60
                if new_hour > 23:
                    new_hour = new_hour % 24
            self.hour = new_hour
            self.minute = new_minute

        def __repr__(self):
            return f"{self.hour:02d}:{self.minute:02d}"

        def __str__(self):
            return f"{self.hour:02d}:{self.minute:02d}"

        def __eq__(self, other):
            return (self.hour == other.hour) and (self.minute == other.minute)

        def __add__(self, minutes):
            new_self = Clock(self.hour, self.minute)
            new_self.minute += minutes
            if new_self.minute > 59:
                new_self.hour += new_self.minute // 60
                new_self.minute = new_self.minute % 60
            return new_self

        def __sub__(self, minutes):
            new_self = Clock(self.hour, self.minute)
            subtract_hours = abs(minutes) // 60
            subtract_minutes = abs(minutes) % 60
            new_self.hour -= subtract_hours
            new_self.minute -= subtract_minutes
            if new_self.minute < 0:
                new_self.hour -= 1
                new_self.minute = 60 - abs(new_self.minute)
            if new_self.hour < 0:
                new_self.hour = 24 - abs(new_self.hour)
            return new_self