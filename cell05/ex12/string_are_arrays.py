#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่ามี parameter ส่งมาตัวเดียวหรือไม่ (len ต้องเป็น 2)
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
     
        z_count = 0
        for char in input_string:
            if char == 'z':
                z_count += 1
        
        # ถ้าไม่มีตัว 'z' เลย หรือจำนวน parameter ไม่ถูก ให้แสดง none
        # (แต่ในเงื่อนไข if นี้คือจำนวน parameter ถูกแล้ว ดังนั้นเช็คแค่มี z ไหม)
        if z_count > 0:
            # พิมพ์ 'z' ออกมาตามจำนวนที่นับได้
            print('z' * z_count)
        else:
            print("none")
    else:
        # ถ้าไม่มี parameter หรือมีมากกว่า 1 ให้แสดง none
        print("none")

if __name__ == "__main__":
    main()