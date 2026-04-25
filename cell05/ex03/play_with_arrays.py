#!/usr/bin/env python3

def main():
    
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # กรองเฉพาะค่าที่มากกว่า 5 แล้วนำมาบวก 2 (เหมือนข้อ ex02)
    filtered_list = [x + 2 for x in original_array if x > 5]
    
    # ใช้ set() เพื่อลบค่าซ้ำออกโดยอัตโนมัติ
    # และจะทำให้การแสดงผลเปลี่ยนจาก [ ] เป็น { }
    result_set = set(filtered_list)
    
    print(original_array)
    print(result_set)

if __name__ == "__main__":
    main()