#!/usr/bin/env python3
import sys

def main():
    # sys.argv คือ list ที่เก็บชื่อไฟล์และ parameter ทั้งหมดที่ส่งเข้ามา
    # ลบ 1 ออก เพราะไม่นับชื่อไฟล์โปรแกรม (parameters.py) เป็น parameter
    num_params = len(sys.argv) - 1
    
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()