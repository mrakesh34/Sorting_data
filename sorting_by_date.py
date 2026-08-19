import json
from datetime import datetime

INPUT_FILE = "page_map (2).json"
OUTPUT_FILE = "sorted_date_by_date.json"

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)


def get_dos_date(page):

    dates = page.get("metadata", {}).get("candidate_dos_dates", [])
    # print(dates)

    if not dates:
        return datetime.min

    # Get the first candidate date
    date_value = dates[0].get("value")
    # print(date_value)

    if not date_value:
        return datetime.max

    try:
        return datetime.strptime(date_value, "%Y-%m-%d")
    except ValueError:
        return datetime.max

def get_provider(page: dict[str ,any]) -> str:

    provider = page.get("metadata", {}).get("provider"),[]


    if isinstance(provider, dict):
        return provider.get("value") or ""
    
    return ""

    # return provider_name


# -----------------------------
# Read JSON
# -----------------------------


data["pages"].sort(key=get_provider)  #Sort pages by provider name
# print(data["pages"])
# data["pages"].sort(key=get_dos_date)   # Sort pages by DOS date
# print("pages")


with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

# with open(INPUT_FILE, "r", encoding="utf-8") as file:
    # data = json.load(file)
# print(data)