#!/usr/bin/env python3

def main():
    try:
        # รับค่าตัวเลขแรก
        first_str = input("Give me the first number: ")
        first_num = int(first_str)
        
        # รับค่าตัวเลขที่สอง
        second_str = input("Give me the second number: ")
        second_num = int(second_str)
        
        print("Thank you!")
        
        # แสดงผลการคำนวณพื้นฐาน
        print(f"{first_num} + {second_num} = {first_num + second_num}")
        print(f"{first_num} - {second_num} = {first_num - second_num}")
        
        # สำหรับการหาร ตรวจสอบไม่ให้ตัวหารเป็น 0 เพื่อป้องกัน Error
        if second_num != 0:
            print(f"{first_num} / {second_num} = {first_num // second_num}")
        else:
            print("Division by zero is not allowed.")
            
        print(f"{first_num} * {second_num} = {first_num * second_num}")
        
    except ValueError:
        # กรณีผู้ใช้ไม่ได้กรอกเป็นตัวเลข
        pass

if __name__ == "__main__":
    main()