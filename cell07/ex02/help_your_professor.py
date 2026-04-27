#!/usr/bin/env python3

def average(class_scores):
    # ตรวจสอบก่อนว่า dictionary ไม่ว่าง เพื่อป้องกันการหารด้วยศูนย์ (DivisionByZero)
    if not class_scores:
        return 0.0
    
    # รวมคะแนนทั้งหมด (values คือคะแนน)
    total_score = sum(class_scores.values())
    
    # นับจำนวนนักเรียนทั้งหมด
    number_of_students = len(class_scores)
    
    # คำนวณค่าเฉลี่ย
    return total_score / number_of_students

if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }

    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")