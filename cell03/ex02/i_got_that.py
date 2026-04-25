#!/usr/bin/env python3

def main():
    # รับอินพุตครั้งแรก
    user_input = input("What you gotta say? : ")

    # เริ่ม loop
    while True:
        # ตรวจสอบว่าผู้ใช้พิมพ์คำว่า "STOP" หรือไม่
        if user_input == "STOP":
            break
        
        # ถ้าไม่ใช่ "STOP" ให้ถามต่อ
        user_input = input("I got that! Anything else? : ")

if __name__ == "__main__":
    main()