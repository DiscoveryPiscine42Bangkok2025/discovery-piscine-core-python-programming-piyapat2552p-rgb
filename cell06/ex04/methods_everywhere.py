#!/usr/bin/env python3
import sys

# ตัดให้เหลือแค่ 8 ตัวแรก (ใช้ Slices)
def shrink(s):
    print(s[:8])

# เติมตัว 'Z' จนกว่าจะครบ 8 ตัว
def enlarge(s):
    padding = 'Z' * (8 - len(s))
    print(s + padding)

def main():
    # รับ parameters (ตัดชื่อไฟล์ออก)
    args = sys.argv[1:]
    
    # ถ้าไม่มี parameters เลยให้แสดง none
    if len(args) == 0:
        print("none")
        return

    for arg in args:
        if len(arg) > 8:
            # ถ้ามากกว่า 8 ตัว ให้เรียก shrink
            shrink(arg)
        elif len(arg) < 8:
            # ถ้าน้อยกว่า 8 ตัว ให้เรียก enlarge
            enlarge(arg)
        else:
            # ถ้าเท่ากับ 8 ตัวพอดี ให้แสดงผลตามปกติ
            print(arg)

if __name__ == "__main__":
    main()