import json
def assess_relevance(update, icp):
    normalized_update = update.lower()
    differentiation_keyword = icp["differentiation"].lower().replace("_", " ")
    update_words = normalized_update.split()
    differentiation_words = differentiation_keyword.split()
    matched_keywords = []
    for word in differentiation_words:
        if word in update_words:
            matched_keywords.append(word)
    return matched_keywords

with open("folk_change_report.json", "r") as file:
    change_report = json.load(file)
with open("icp.json","r") as file:
    icp = json.load(file)

real_updates = change_report["new_updates"]

analysis_results = []

for update in real_updates:
    real_matches = assess_relevance(update, icp)
    result = {
        "update_title": update,
        "matched_keywords": real_matches,
        "potentially_relevant": len(real_matches) > 0,
        "data_source": "folk_changelog"
    }
    analysis_results.append(result)
print(analysis_results)

if change_report["has_new_updates"]:
    print("Ready for GTM analysis")
else:
    print("No new updates to analyze")

with open("folk_relevance_report.json", "w") as file:
    json.dump(analysis_results, file)