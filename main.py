import json
with open("icp.json", "r") as file:
    data = json.load(file)
for pain_point in data["pain_points"]:
    if pain_point == "API_integration":
        print(pain_point)

if data["differentiation_status"] == "verified":
     print("Ready for PMM review")
else:
     print("Needs verification");

def show_company(company_name):
    return company_name

show_company(data["company"])
result = show_company(data["company"])
print(result);


def check_relevance(update_text, keyword):
    if keyword in update_text:
        return True
    else:
        return False

print(check_relevance("HubSpot launches a new API integration","API"));
print(check_relevance("HubSpot launches a new API integration","pricing"))