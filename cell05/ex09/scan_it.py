#!/usr/bin/env python3
import sys
import re

def main():
    
    if len(sys.argv) == 3:
        keyword = sys.argv[1]
        text = sys.argv[2]
        
        # ใช้ re.findall เพื่อค้นหาคำที่ตรงกันทั้งหมด
        # จะได้ลิสต์ของคำที่หาเจอออกมา
        matches = re.findall(keyword, text)
        
        # ตรวจสอบว่าเจอคำอย่างน้อย 1 ครั้ง
        if len(matches) > 0:
            print(len(matches))
        else:
            print("none")
    else:
        # ถ้าจำนวน parameter ไม่ใช่ 2 ให้แสดง none
        print("none")

if __name__ == "__main__":
    main()