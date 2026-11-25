print("By Rizwan")
print("=============================================================")
print("DAILY ACTIVITY PLANNER")
print("=============================================================")
r = int(input("enter the homework time (in minutes): "))
if r >= 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")
s = input("Is there free time after homework? (yes/no): ")
if s == "yes":
    t = input("enter a hobby you want to do: ")
print("=====DAILY PLAN=====")
print("time",r,"minutes")
print("plan",plan)
input("press enter to exit")