from google import genai
import json
import sys

with open("icp.json", "r") as file:
    icp = json.load(file)

with open("folk_change_report.json", "r") as file:
    change_report = json.load(file)
if change_report["has_new_updates"] is False:
    print("No new updates. Skipping AI analysis.")
    sys.exit(0)

client = genai.Client(
    http_options={"timeout": 30000}
)

new_updates = change_report["new_updates"]
role_prompt = "You are a senior Product Marketing Manager specializing in competitive intelligence and go-to-market positioning."
context_prompt = f"Our company is {icp['company']}, targeting PLG startups. Our differentiation is {icp['differentiation']}. Its evidence status is {icp['differentiation_status']}."
competitor_update = "\n".join(new_updates)
input_evidence_status = change_report.get("evidence_status","unverified")

task_prompt = (
    "Evaluate the potential impact of this update on Attio's GTM positioning as high, medium, or low. "
    "Assess confidence in this impact assessment based on available evidence as high, medium, or low. "
    "Recommend the next action for the Product Marketing Manager based on both impact and confidence."
)
guardrails_prompt = (
    "Do not assume or make up Attio or Folk's features, ICP, Value propositions, etc. "
    "Clearly distinguish between verified information and hypothesis. Identify missing information that needs further verification. "
    "Every factual competitive claim must be supported by the provided input evidence. If unsupported, clearly marked as unverified."
)
full_prompt = f"{role_prompt}\n{context_prompt}\n{competitor_update}\nInput evidence status: {input_evidence_status}\n{task_prompt}\n{guardrails_prompt}"

report_schema = {
    "type": "OBJECT",
    "properties": {
        "potential_impact": {"type": "STRING","enum": ["high", "medium", "low"]},
        "confidence": {"type": "STRING","enum": ["high", "medium", "low"]},
        "recommended_action": {"type": "STRING"},
        "evidence_gaps": {
            "type": "ARRAY",
            "items": {"type": "STRING"}
        },
        "evidence_status": {"type": "STRING","enum": ["hypothetical","unverified","verified"]}
    },
    "required": ["potential_impact", "confidence", "recommended_action","evidence_gaps","evidence_status"]
}

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents = full_prompt,
    config = {
        "response_mime_type": "application/json",
        "response_schema": report_schema
    }
)

analysis_data = json.loads(response.text)
print(type(analysis_data))

if analysis_data.get("evidence_status") == input_evidence_status:
    print("Evidence status validated")
else:
    print("Evidence status mismatch")
    raise ValueError("AI evidence status does not match input data")

print(response.text)