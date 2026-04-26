#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่าจำนวน parameter ต้องเท่ากับ 1 เท่านั้น (รวมชื่อไฟล์เป็น 2)
    if len(sys.argv) == 2:
        param = sys.argv[1]
        
        user_input = input("What was the parameter? ")
        
        # เปรียบเทียบค่าที่ผู้ใช้พิมพ์ กับ parameter ที่ส่งมาตอนรัน
        if user_input == param:
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        # ถ้าจำนวน parameter ไม่ถูกต้อง ให้แสดง none
        print("none")

if __name__ == "__main__":
    main()