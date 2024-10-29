import math
import datetime

target = 1000
surveyDays = 61

# calculate days left in survey
finalDay = 'December 22, 2024'
startDay = 'October 1, 2024'
today = datetime.datetime.today()


# calculate how many days since the survey started
startDay = datetime.datetime.strptime(startDay, '%B %d, %Y')
days = today - startDay
# add one to the days since start
days = days.days + 1

# calculate days left in survey
finalDay = datetime.datetime.strptime(finalDay, '%B %d, %Y')
daysLeft = finalDay - today
# add one to the days left to include today


# print the result
print("There are " + str(daysLeft.days) + " days left in the survey.")

# ask for an input to assign to a variable
print("How many responses?")
# assign the input to a variable
count = input()

print("\nDaily Wellness Assessment Survey response count: " + count)

pctTarget = (int(count) / target) * 100
# print the result
print("Which is " + str(pctTarget) + "% of the responses needed to reach our target of " + str(target) + " responses.")

# calculate the number of surveys per day needed to reach the target in the remaining days
dailyTarget = (target - int(count)) / daysLeft.days

# print("rawtarget: " + str(dailyTarget))
# round daily target up to the nearest whole number
dailyTarget = math.ceil(dailyTarget)

print("As of this time on day " + str(days) + "/" + str(surveyDays) + ", we need " + str(dailyTarget) + " responses per day to reach our goal.")