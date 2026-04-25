#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่ามีการใส่ argument มาหรือไม่ (argv[1:] คือดูหลังจากชื่อไฟล์)
    # ถ้ามี argument (เช่น "yolo") โจทย์บอกให้แสดง "none"
    if len(sys.argv) > 1:
        print("none")
        return

    # ลูปนอก: ควบคุมแม่สูตรคูณ (แม่ 0 ถึง 10)
    outer = 0
    while outer <= 10:
        print(f"Table de {outer}:", end="")
        
        # ลูปใน: ควบคุมตัวคูณ (คูณด้วย 0 ถึง 10)
        inner = 0
        while inner <= 10:
            # พิมพ์ผลลัพธ์โดยใช้ end=" " เพื่อให้อยู่บรรทัดเดียวกัน
            print(f" {outer * inner}", end="")
            inner += 1
        
        # เมื่อจบ 1 แม่ ให้พิมพ์บรรทัดใหม่
        print()
        outer += 1

if __name__ == "__main__":
    main()