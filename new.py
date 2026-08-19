import json
from datetime import datetime

# 1. Load the JSON file
input_filename = "page_map (2).json"

with open(input_filename, "r", encoding="utf-8") as f:
    data = json.load(f)

from datetime import datetime

def get_date(page):
    return datetime.strptime(
        page["metadata"]["candidate_dos_dates"][0]["value"],
        "%Y-%m-%d"
    )

data["pages"] = sorted(data["pages"], key=get_date)
# print(data)
# dates=data["pages"]["metadata"]["candidate_dos_dates"][0]["value"]
# ["metadata"]
# ["candidate_dos_dates"]["value"]
print(data)
# sorted_data = sorted(data, key=lambda x: x["value"])

# print(sorted_data)