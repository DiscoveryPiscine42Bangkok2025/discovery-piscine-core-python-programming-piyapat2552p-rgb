#!/usr/bin/env python3

def famous_births(people):
    # เรียงลำดับข้อมูลใน Dictionary
    # ใช้ฟังก์ชัน sorted โดยกำหนด key ในการเรียงคือค่าของ "date_of_birth"
    # people.values() จะดึงข้อมูล { "name": ..., "date_of_birth": ... } ของทุกคนออกมา
    sorted_people = sorted(people.values(), key=lambda x: x["date_of_birth"])

    for person in sorted_people:
        name = person["name"]
        year = person["date_of_birth"]
        print(f"{name} is a great scientist born in {year}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)