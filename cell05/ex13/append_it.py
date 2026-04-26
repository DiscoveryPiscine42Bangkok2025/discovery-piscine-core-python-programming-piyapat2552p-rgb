#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่ามี parameter ส่งมาอย่างน้อย 1 ตัวหรือไม่
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        
        for p in params:
            # ตรวจสอบว่าคำนั้น "ไม่" ลงท้ายด้วย "ism"
           if not p.endswith("ism"):
                print(f"{p}ism")
    else:
        # ถ้าไม่มี parameter เลยให้แสดง none
        print("none")

if __name__ == "__main__":
    main()