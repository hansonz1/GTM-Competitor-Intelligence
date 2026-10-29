import json
import glob
import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime, UTC
url = "https://www.folk.app/changelog"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    print(error)
    raise

soup = BeautifulSoup(response.text, "html.parser")
update_elements = soup.find_all("h2", class_="h2-changelog")
if len(update_elements) == 0:
    print("No updates found")
    sys.exit(1)
update_titles = []
for element in update_elements:
    update_titles.append(element.get_text().strip())
print(len(update_titles))

collection_time = datetime.now(UTC)
captured_at = collection_time.isoformat()
snapshot = {"company": "folk", 
            "source_url": url, 
            "updates": update_titles,
            "captured_at": captured_at}
snapshot_date = collection_time.strftime("%Y-%m-%d_%H-%M-%S_%f")
snapshot_filename = f"folk_{snapshot_date}.json"

with open(snapshot_filename, "w") as file:
    json.dump(snapshot, file)

print(snapshot_filename)

def get_snapshot_time(filename):
    with open(filename, "r") as file:
        return json.load(file)["captured_at"]

old_snapshot_files = glob.glob("folk_????-??-??_??-??-??.json")
snapshot_files = sorted(glob.glob("folk_????-??-??_??-??-??_??????.json"))
snapshot_files = sorted(old_snapshot_files + snapshot_files,key=get_snapshot_time)
if len(snapshot_files) < 2:
    print("Not enough snapshots")
    sys.exit(0)
latest_snapshot = snapshot_files[-1]
previous_snapshot = snapshot_files[-2]

with open(latest_snapshot, "r") as file:
    latest_data = json.load(file)

with open(previous_snapshot, "r") as file:
    previous_data = json.load(file)

latest_updates = latest_data["updates"]
previous_updates = previous_data["updates"]

new_updates = []
for update in latest_updates:
    if update not in previous_updates:
        new_updates.append(update)

change_report = {
    "competitor_name": latest_data["company"],
    "new_updates": new_updates,
    "previous_snapshot": previous_snapshot,
    "latest_snapshot": latest_snapshot,
    "new_updates_count": len(new_updates),
    "has_new_updates": len(new_updates) > 0
}
with open("folk_change_report.json", "w") as file:
    json.dump(change_report, file)

print(f"New Updates Detected: {change_report['new_updates_count']}")