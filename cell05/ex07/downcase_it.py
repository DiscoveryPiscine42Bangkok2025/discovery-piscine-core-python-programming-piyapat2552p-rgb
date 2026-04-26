#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่ามี parameter ส่งมาตัวเดียวหรือไม่ (len ต้องเป็น 2)
    if len(sys.argv) == 2:
        # ใช้ .lower() เพื่อแปลงเป็นตัวพิมพ์เล็ก
        print(sys.argv[1].lower())
    else:
        # ถ้าจำนวน parameter ไม่ถูกต้อง ให้แสดง none
        print("none")

if __name__ == "__main__":
    main()