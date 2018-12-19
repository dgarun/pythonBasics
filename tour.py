distance = 10000;
speed = input("Speed in km/hr : ");

if float(speed) > 0.0 :
    hour = distance/float(speed);
    day = float(hour) /24;
    month = float(day)/30;
    year = float(month)/12;
    remainingHour = float(hour)%24;

print(round(year),"year",round(month),"Month",round(day),"Day",round(remainingHour),"Hours");


