def main():
    time = input("What time is it? ")

    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")

def convert(time):
 #if in 12 hr format
 if "a.m." in time:
    time = time.replace(" a.m.", "")
    hours, minutes = time.split(":")
    hours = int(hours)

    if hours == 12:
        hours = 0

 elif "p.m." in time:
    time = time.replace(" p.m.", "")
    hours, minutes = time.split(":")
    hours = int(hours)

    if hours != 12:
        hours += 12 #+= means hours = hours + 12

 #if in 24 hr format
 else:
    hours, minutes = time.split(":")
    hours = int(hours)

 return hours + int(minutes) / 60


main()
