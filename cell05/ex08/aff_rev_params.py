#!/usr/bin/env python3
import sys

def main():
    # sys.argv[0] คือชื่อไฟล์ ดังนั้นถ้ามี parameter ตั้งแต่ 2 ตัวขึ้นไป
    # จำนวนใน sys.argv ต้องมากกว่าหรือเท่ากับ 3
    if len(sys.argv) >= 3:
      
        params = sys.argv[1:]
       
        for p in reversed(params):
            print(p)
    else:
        # ถ้ามีน้อยกว่า 2 parameters ให้แสดง none
        print("none")

if __name__ == "__main__":
    main()