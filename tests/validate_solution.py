import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "servicenow/catalog/variables.json", "servicenow/catalog/variable-set.json",
    "servicenow/catalog/ui-policies.json", "servicenow/notifications.json", "servicenow/validation.json",
    "servicenow/security/roles-and-acls.json", "servicenow/reporting.json", "servicenow/tests/test-cases.md"
]
for path in required:
    assert (ROOT / path).exists(), f"Missing required file: {path}"
for path in ROOT.rglob("*.json"):
    json.loads(path.read_text(encoding="utf-8"))
variables = json.loads((ROOT / "servicenow/catalog/variables.json").read_text())
names = {v["name"] for v in variables["variables"]}
for name in ["requested_for","mobile_number","connection_type","existing_id","request_type","business_justification","total_amount","mode_of_payment","address","urgency"]:
    assert name in names, f"Missing catalog variable: {name}"
ui = json.loads((ROOT / "servicenow/catalog/ui-policies.json").read_text())
assert ui["policies"][0]["condition"] == "connection_type == Existing"
security = json.loads((ROOT / "servicenow/security/roles-and-acls.json").read_text())
assert set(security["roles"]) == {"network_requester","network_approver","network_fulfiller","network_admin"}
print("Repository validation passed.")
