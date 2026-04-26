#!/usr/bin/env python3
import sys

def main():
    
    # ถ้า len(sys.argv) คือ 1 แสดงว่าไม่มี parameter ส่งมาเลย
    if len(sys.argv) > 1:
        
        params = sys.argv[1:]
        
      
        print(f"parameters: {len(params)}")
        
        # ใช้ for loop วนลูปเพื่อแสดงค่าและความยาว (ตามเงื่อนไขในแถบสีแดง)
        for p in params:
            print(f"{p}: {len(p)}")
    else:
        # ถ้าไม่มี parameter เลยให้แสดง none
        print("none")

if __name__ == "__main__":
    main()