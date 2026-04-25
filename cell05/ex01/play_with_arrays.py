#!/usr/bin/env python3

def main():
    # 1. กำหนด array ของตัวเลข (Original array)
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # 2. สร้าง array ใหม่โดยการบวก 2 เข้ากับทุกค่าใน array เดิม
    # ใช้ List Comprehension เพื่อสร้างความสะดวก
    new_array = [x + 2 for x in original_array]
    
    # 3. แสดงผลทั้งสอง array ตามรูปแบบที่โจทย์กำหนด
    print(f"Original array: {original_array}")
    print(f"New array: {new_array}")

if __name__ == "__main__":
    main()