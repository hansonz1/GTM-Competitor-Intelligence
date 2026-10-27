import json
with open("icp.json", "r") as file:
    data = json.load(file)
for pain_point in data["pain_points"]:
    if pain_point == "API_integration":
        print(pain_point)

if data["differentiation_status"] == "verified":
     print("Ready for PMM review")
else:
     print("Needs verification")

def show_company(company_name):
    return company_name

show_company(data["company"])
result = show_company(data["company"])
print(result)


def check_relevance(update_text, keyword):
    if keyword in update_text:
        return True
    else:
        return False

print(check_relevance("HubSpot launches a new API integration","API"))
print(check_relevance("HubSpot launches a new API integration","pricing"))

with open("previous_snapshot.json", "r") as file:
    previous_snapshot = json.load(file)

with open("current_snapshot.json", "r") as file:
    current_snapshot = json.load(file)
    print(current_snapshot)

if previous_snapshot["function_description"] != current_snapshot["function_description"]:
    change_report = {}
    change_report["competitor_name"] = current_snapshot["company"]
    change_report["function_changed"] = current_snapshot["function"]
    change_report["description_before"] = previous_snapshot["function_description"]
    change_report["description_after"] = current_snapshot["function_description"]
    print(change_report)
    with open("change_report.json", "w") as file:
        json.dump(change_report, file)
    print("Change detected")
    print(previous_snapshot["function_description"])
    print(current_snapshot["function_description"])
else:
    print("No change detected")