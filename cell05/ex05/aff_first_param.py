#!/usr/bin/env python3
import sys

def main():
    # sys.argv คือ list ที่เก็บค่าต่างๆ:
    # index 0 คือชื่อไฟล์ (aff_first_param.py)
    # index 1 คือ parameter ตัวแรกที่ช้พิมพ์
    
    # ตรวจสอบว่าจำนวนอาร์กิวเมนต์ทั้งหมดมีมากกว่า 1 หรือไม่ (มีตัวแรกถูกส่งมาไหม)
    if len(sys.argv) > 1:
        # แสดง parameter ตัวแรก (index ที่ 1)
        print(sys.argv[1])
    else:
        # ถ้าไม่มีการส่งค่ามาให้แสดง 'none'
        print("none")

if __name__ == "__main__":
    main()

    