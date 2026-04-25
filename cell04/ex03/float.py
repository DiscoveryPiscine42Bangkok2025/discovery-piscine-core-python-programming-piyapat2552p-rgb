#!/usr/bin/env python3

def main():
    try:
        # รับค่าจากผู้ใช้
        user_input = input("Give me a number: ")
        
        # แปลงข้อความเป็นตัวเลขทศนิยม (float) ตามที่โจทย์ใบ้มา
        number = float(user_input)
        
        # ตรวจสอบว่าค่าของมันเท่ากับเลขจำนวนเต็มของตัวมันเองหรือไม่
        # เช่น 42.0 == 42 (จริง) แต่ 42.42 == 42 (ไม่จริง)
        if number == int(number):
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
            
    except ValueError:
        # กรณีผู้ใช้กรอกสิ่งที่ไม่ใช่ตัวเลข
        pass

if __name__ == "__main__":
    main()