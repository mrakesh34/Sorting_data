import json

INPUT_FILE = "page_map (2).json"
OUTPUT_FILE = "sorted_date_by_date.json"

def get_dos_date(page):

    dates = page.get("metadata", {}).get("candidate_dos_dates", [])
    # print(dates)

    if not dates:
        return (0, "")

    date_value = dates[0].get("value")

    if not date_value:
        return (0, "")
    # print(1,date_value)
    return (1,date_value)

def get_provider(page):

    provider = page.get("metadata", {}).get("provider")


    if isinstance(provider, dict):
        return provider.get("value") or ""
    
    return ""

def get_facility(page):

    facility = page.get("metadata", {}).get("facility_name")


    if isinstance(facility, dict):
        return facility.get("value") or ""
    
    return ""


def sort_by_date(pages):
    pages.sort(key=get_dos_date)
    return pages

def sort_by_provider(pages):
    pages.sort(key=get_provider)
    return pages

def sort_by_facility(pages):
    pages.sort(key=get_facility)
    return pages




# data["pages"].sort(key=get_provider)  #Sort pages by provider name
# print(data["pages"])
# data["pages"].sort(key=get_dos_date)   # Sort pages by DOS date

if __name__ == "__main__":

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    sort_by_date(data["pages"])  #Sort pages by DOS date

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)



# def all_provider_name():
#     for i, page in enumerate(data["pages"], start=1):
#         dos_value = get_provider(page)
#         print(f"Page {i}: {dos_value}")
# all_provider_name()

