# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
from datetime import datetime
import time
import pendulum

# TODO: create a new datetime using pendulum
dt1 = pendulum.datetime(2022, 2, 22, tz = "America/New_York")
print(dt1)

print(isinstance(dt1, datetime))

print(dt1.timezone.name)

# TODO: convert the time to another time zone
#test commit

# TODO: create a new datetime using the now() function


# TODO: Use the local function function


# TODO: Use today, tomorrow, yesterday


# TODO: create a datetime from a system timestamp
