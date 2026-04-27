#!/usr/bin/env python3
def array_of_names(persons):
   
    # ใช้ .capitalize() เพื่อให้ตัวแรกเป็นตัวพิมพ์ใหญ่
    results = []
    for first_name, last_name in persons.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        results.append(full_name)
    return results


if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))