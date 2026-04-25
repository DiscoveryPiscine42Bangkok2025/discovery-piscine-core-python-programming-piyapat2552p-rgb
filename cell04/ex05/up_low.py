#!/usr/bin/env python3

def main():
    # รับข้อความจากผู้ใช้
    user_string = input()

    # ใช้ method .swapcase() เพื่อสลับตัวเล็กเป็นใหญ่ และใหญ่เป็นเล็ก
    print(user_string.swapcase())

if __name__ == "__main__":
    main()