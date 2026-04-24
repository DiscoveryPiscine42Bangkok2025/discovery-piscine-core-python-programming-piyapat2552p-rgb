#!/usr/bin/env python3

# กำหนดตัวแปรสำหรับรหัสผ่านที่ถูกต้องตามโจทย์
password_storage = "Python is awesome"

# รับค่ารหัสผ่านจากผู้ใช้
user_input = input()

# ตรวจสอบว่าสิ่งที่ผู้ใช้พิมพ์มา ตรงกับรหัสผ่านที่เราตั้งไว้หรือไม่
if user_input == password_storage:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
