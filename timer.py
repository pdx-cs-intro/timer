# Timer for work sessions.
# Bart Massey 2021

import time

# Session time in seconds.
session_time = 20 * 60

# Convert number n to a two-digit string and return that.
# n must be non-negative and less than 60.
def two_digit(n):
    if n < 10:
        return "0" + str(n)
    else:
        return str(n)

while session_time > 0:
    session_minutes = session_time // 60
    session_seconds = session_time - session_minutes * 60
    print(two_digit(session_minutes) + ":" + two_digit(session_seconds))
    time.sleep(1)
    session_time -= 1
    if session_time < 5:
        # Print a "bell character".
        print(chr(7))

