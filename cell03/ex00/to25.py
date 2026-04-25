#!/usr/bin/env python3
def main():
    # รับค่าจากผู้ใช้ (input) และแปลงเป็นตัวเลขจำนวนเต็ม (int)
    try:
        user_input = input("Enter a number less than 25\n")
        number = int(user_input)

        # ตรวจสอบเงื่อนไข: ถ้าตัวเลขมากกว่า 25 ให้แสดง Error
        if number > 25:
            print("Error")
        else:
            # ใช้ while loop แสดงค่าตั้งแต่ตัวเลขที่กรอกจนถึง 25
            while number <= 25:
                print(f"Inside the loop, my variable is {number}")
                number += 1  # เพิ่มค่าทีละ 1 ในแต่ละรอบ
                
    except ValueError:
        print("Error") # กรณีผู้ใช้ไม่ได้กรอกเป็นตัวเลข

if __name__ == "__main__":
    main()