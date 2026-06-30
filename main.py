from datetime import datetime, timedelta

def parse_time(time_string):
    return datetime.strptime(time_string, "%H:%M")

workload_hours = float(input("Daily workload (hours): "))
required_work_time = timedelta(hours=workload_hours)

clock_in = parse_time(input("Clock in (HH:MM): "))
clock_out = parse_time(input("Clock out (HH:MM): "))
lunch_back = parse_time(input("Clock Back (HH:MM): "))

morning_work = clock_out - clock_in

remaining_work = required_work_time - morning_work

if remaining_work <= timedelta():
    expected_clock_out = lunch_back
    total_worked = morning_work
else:
    expected_clock_out = lunch_back + remaining_work
    total_worked = required_work_time - remaining_work

print("\n========== Work Summary ==========")
print(f"Daily workload : {workload_hours:.2f} hours")
print(f"Worked morning : {morning_work}")
print(f"Remaining work : {remaining_work}")
print(f"Clock out at   : {expected_clock_out.strftime('%H:%M')}")
print("==================================")