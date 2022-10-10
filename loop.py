# Importing Module
import datetime


# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"

# Message Will Be
# "Days From 2021-06-25 To 2021-08-10 Is => 46"

Date = datetime.datetime(2021,6,25)
Now  = datetime.datetime.now()
print(f"Days From 2021-06-25 To 2022-10-9 Is => {(Now - Date).days}") 


# Today Is "2021, 8, 10"
"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"
print(datetime.datetime.now().strftime("%b %d, %Y"))
print(datetime.datetime.now().strftime("%d - %b - %Y"))
print(datetime.datetime.now().strftime("%d / %b / %y"))
print(datetime.datetime.now().strftime("%d / %B / %Y"))
print(datetime.datetime.now().strftime("%a, %d %B %Y"))