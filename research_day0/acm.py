#!/usr/bin/env python3

with open("acm.txt", "r") as f:
    result = []
    lines = f.readlines()
    for line in lines:
        college_info = line.strip().split("(")
        college_name = college_info[0]
        college_city = college_info[1].split(",")[0]
        college_state = college_info[1].split(",")[1][:-1]
        result.append(
            {"name": college_name, "city": college_city, "state": college_state}
        )
    for college in result:
        name, city, state = college.values()
        print(f"{name} is a college in {city}, {state}")
