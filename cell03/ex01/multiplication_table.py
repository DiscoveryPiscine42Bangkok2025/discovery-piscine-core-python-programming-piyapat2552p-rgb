#!/usr/bin/env python3

def main():
    try:
        # รับค่าอินพุตจากผู้ใช้
        user_input = input("Enter a number\n")
        number = int(user_input)

        # ใช้ Loop เพื่อไล่คูณตั้งแต่ 0 ถึง 9
        i = 0
        while i < 10:
            result = i * number
            # แสดงผลในรูปแบบ: i x number = result
            print(f"{i} x {number} = {result}")
            i += 1
            
    except ValueError:
        # กรณีผู้ใช้กรอกสิ่งที่ไม่ใช่ตัวเลข
        pass

if __name__ == "__main__":
    main()