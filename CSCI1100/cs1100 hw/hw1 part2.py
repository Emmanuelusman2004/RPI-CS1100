import math

minutes = int(input("Minutes ==> "))
print(minutes)

seconds = int(input("Seconds ==> "))
print(seconds)

miles = (input("Miles ==> "))
print(miles)
miles = float(miles)

target_miles = float(input("Target Miles ==> "))
print(int(target_miles))
print("")


#Calculation for pace
time = ((minutes * 60) + seconds) #total seconds
pace = (time/60)/miles #gives me pace in a decimal format
pace_secdec = pace - math.floor(pace) #gives me only decimal of seconds
pace_sec = math.floor(pace_secdec * 60) #gives me flat number of seconds with no decimal
pace_min = math.floor(pace) #gives me the mins flat
#print(pace_sec)
#print(pace_min)

#Calculation for speed
speed = miles/(time/3600)
#Calculation for projected distance
pace_sec_total = (pace_min * 60) + (pace_sec) #total #of seconds
proj_time = target_miles * pace_sec_total
proj_mins = math.floor(proj_time/60) #gives mins without seconds
proj_sec_dec = (proj_time/60) - proj_mins #gives decimal
proj_sec_int = math.floor(60 * proj_sec_dec) #should give the # seconds

#print statements
print("Pace is", pace_min, "minutes and", pace_sec, "seconds per mile.")
print("Speed is", round(speed,2), "miles per hour.")
print("Time to run the target distance of", target_miles,"miles is", proj_mins, "minutes and", proj_sec_int,"seconds.")

