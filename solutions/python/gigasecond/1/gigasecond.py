from datetime import datetime, timedelta

def add(moment):
    delta = timedelta(seconds=1_000_000_000)
    new = moment + delta
    return new

"""
now = datetime.now()

now.year() -> year
now.month() -> month
now.day() -> day
now.hour() -> hour
now.minute() -> minute
now.second() -> second

1 000 000 000 second: {

}

If adding a certain value to the time format exceeds the upper bound, then we should
take the remainder and make it a new value for current time format and also add 1 to the
one that is bigger (month -> year).

1 year = 60*60*24*365

okay i just realized that this is not the way it is solved it is just solved via timedelta class from datetime

"""
