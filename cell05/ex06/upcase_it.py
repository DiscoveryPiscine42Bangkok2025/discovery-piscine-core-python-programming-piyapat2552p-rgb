#!/usr/bin/env python3
import sys

def main():
    # sys.argv เก็บ arguments ที่ส่งมาจาก Terminal
    # ดังนั้น ถ้ามี 1 parameter จะต้องมี len เท่ากับ 2
    if len(sys.argv) == 2:
        # แปลงเป็นตัวพิมพ์ใหญ่ด้วย .upper()
        print(sys.argv[1].upper())
    else:
        # ถ้าไม่มี parameter หรือมีมากกว่า 1 ให้แสดง none
        print("none")

if __name__ == "__main__":
    main()