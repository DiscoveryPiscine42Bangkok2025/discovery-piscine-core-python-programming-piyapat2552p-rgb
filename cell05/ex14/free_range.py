#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่าต้องมี 2 parameters เท่านั้น (รวมชื่อไฟล์เป็น 3)
    if len(sys.argv) == 3:
        try:
            # แปลง parameter จาก string เป็นตัวเลข (int)
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            
            # สร้าง list ของตัวเลขระหว่าง start ถึง end
            # ใน Python range(start, end + 1) จะรวมตัวสุดท้ายด้วย
            res = list(range(start, end + 1))
            
            print(res)
            
        except ValueError:
            # กรณีผู้ใช้ใส่ค่าที่ไม่ใช่ตัวเลข
            print("none")
    else:
        # ถ้าจำนวน parameter ไม่ใช่ 2 ให้แสดง none
        print("none")

if __name__ == "__main__":
    main()