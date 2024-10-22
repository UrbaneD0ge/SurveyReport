import math

target = 500
surveyDays = 61

# ask for an input to assign to a variable
print("How many responses?")
# assign the input to a variable
count = input()

print("What day of the survey is it?")
day = input()

print("Daily Wellness Assessment Survey response count: " + count)

pctTarget = (int(count) / target) * 100
# print the result
print("Which is " + str(pctTarget) + "% of the responses needed to reach our target of " + str(target) + " responses.")

daysLeft = surveyDays - int(day)
# calculate the number of surveys per day needed to reach the target in the remaining days
dailyTarget = (target - int(count)) / daysLeft

# round daily target up to the nearest whole number
dailyTarget = math.ceil(dailyTarget)

print("As of this time on day " + str(day) + "/" + str(surveyDays) + ", we need " + str(dailyTarget) + " responses per day to reach our goal.")