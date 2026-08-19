from main import *

OUTPUT_FILE= "Sort_by_provider_name.json"


with open(INPUT_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

sort_by_date(data["pages"])

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)