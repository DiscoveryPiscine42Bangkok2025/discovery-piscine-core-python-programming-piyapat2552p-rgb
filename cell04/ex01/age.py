#!/usr/bin/env python3

def main():
    try:
        # รับค่าอายุจากผู้ใช้
        input_age = input("Please tell me your age: ")
        
        # แปลงข้อความ (string) เป็นตัวเลข (integer)
        age = int(input_age)
        
        # แสดงอายุปัจจุบัน
        print(f"You are currently {age} years old.")
        
        # คำนวณและแสดงอายุในอีก 10, 20, 30 ปีข้างหน้า
        print(f"In 10 years, you'll be {age + 10} years old.")
        print(f"In 20 years, you'll be {age + 20} years old.")
        print(f"In 30 years, you'll be {age + 30} years old.")
        
    except ValueError:
        # กรณีผู้ใช้ไม่ได้กรอกเป็นตัวเลข
        pass

if __name__ == "__main__":
    main()