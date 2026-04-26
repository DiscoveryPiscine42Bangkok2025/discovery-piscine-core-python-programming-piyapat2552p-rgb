#!/usr/bin/env python3
import sys


def downcase_it(s):
    # คืนค่าเป็นตัวพิมพ์เล็ก
    return s.lower()

def main():
    
    if len(sys.argv) > 1:
        # ดึงเอาเฉพาะ parameters (ตัดชื่อไฟล์ออก)
        params = sys.argv[1:]
        
        # วนลูปเพื่อนำแต่ละ parameter มาเข้า Method และแสดงผล
        for p in params:
            result = downcase_it(p)
            print(result)
    else:
        # ถ้าไม่มี parameter เลยให้แสดง none
        print("none")

if __name__ == "__main__":
    main()