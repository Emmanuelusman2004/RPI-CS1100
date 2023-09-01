def skew_calculator(time1,time2,time3,time4,time5):
    avg = (time1+time2+time3+time4+time5)/5
    var = (time1-avg)**2 + (time2-avg)**2 + (time3-avg)**2 + (time4-avg)**2 + (time5-avg)**2
    var /= 5
    skew = (time1-avg)**3 + (time2-avg)**3 + (time3-avg)**3 + (time4-avg)**3 + (time5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5
    return skew
def stat_calculator(name, time1,time2,time3,time4,time5):
    timelist = [time1,time2,time3,time4,time5]
    minval = min(timelist)
    maxval = max(timelist)
    timelist.remove(minval)
    timelist.remove(maxval)
    avg = sum(timelist)/len(timelist)
    print(name + "'s" + " stats-- min: " + str(minval) + ", max: " + str(maxval) + ", avg: " + str(round(avg,1)))

name_1 = "Stan"
## The following are Stan's 5 latest running times for 3 miles

time1 = 34
time2 = 34
time3 = 35
time4 = 31
time5 = 29
skew1 = skew_calculator(time1, time2, time3, time4, time5)
stat_calculator(name_1, time1, time2, time3, time4, time5)

name_2 = "Kyle"
## The following are Kyle's 5 latest running times for 3 miles

time1 = 30
time2 = 31
time3 = 29
time4 = 29
time5 = 28
skew2 = skew_calculator(time1, time2, time3, time4, time5)
stat_calculator(name_2, time1, time2, time3, time4, time5)
name_3 = "Cartman"
## The following are Cartman's 5 latest running times for 3 miles
time1 = 36
time2 = 31
time3 = 32
time4 = 33
time5 = 33
skew3 = skew_calculator(time1, time2, time3, time4, time5)
stat_calculator(name_3, time1, time2, time3, time4, time5)
name_4 = "Kenny"
## The following are Kenny's 5 latest running times for 3 miles
time1 = 33
time2 = 32
time3 = 34
time4 = 31
time5 = 35
skew4 = skew_calculator(time1, time2, time3, time4, time5)
stat_calculator(name_4, time1, time2, time3, time4, time5)
name_5 = "Bebe"
## The following are Bebe's 5 latest running times for 3 miles
time1 = 27
time2 = 29
time3 = 29
time4 = 28
time5 = 30
skew5 = skew_calculator(time1, time2, time3, time4, time5)
stat_calculator(name_5, time1, time2, time3, time4, time5)
# Process results for the first person
print("")
print ("{0}'s running times have a skew of {1:.2f}".format(name_1,skew1))


## Process for the second person

print ("{0}'s running times have a skew of {1:.2f}".format(name_2,skew2))

## Process for the third person

print ("{0}'s running times have a skew of {1:.2f}".format(name_3,skew3))


## Process for the fourth person

print ("{0}'s running times have a skew of {1:.2f}".format(name_4,skew4))


## Process for the fifth person

print ("{0}'s running times have a skew of {1:.2f}".format(name_5,skew5))
