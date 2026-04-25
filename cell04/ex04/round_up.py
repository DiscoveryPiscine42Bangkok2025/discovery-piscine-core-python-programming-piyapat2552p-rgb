#!/usr/bin/env python3
import math

def main():
    try:
        # รับค่าจากผู้ใช้
        user_input = input("Give me a number: ")
        
        # แปลงข้อความเป็นตัวเลขทศนิยม (float)
        number = float(user_input)
        
        # ใช้ math.ceil เพื่อปัดเศษขึ้นเสมอ
        result = math.ceil(number)
        
        # แสดงผลลัพธ์
        print(result)
        
    except ValueError:
        # กรณีผู้ใช้กรอกสิ่งที่ไม่ใช่ตัวเลข
        pass

if __name__ == "__main__":
    main()