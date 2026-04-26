#!/usr/bin/env python3

# กำหนดค่าเริ่มต้น (Default) เป็น 'noble stranger'
def greetings(name='noble stranger'):
    
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
       
        print("Error! It was not a name.")

if __name__ == "__main__":
    greetings('Alexandra')
    greetings('Wil')
    greetings()    # ทดสอบแบบไม่ใส่ argument (จะใช้ค่า default)
    greetings(42)  # ทดสอบแบบไม่ใช่ string