#!/usr/bin/env python3

# สร้าง Method ชื่อ add_one ที่รับ parameter และบวกเพิ่ม 1
def add_one(nb):
    nb += 1

def main():
    
    my_variable = 42
    
    
    print(my_variable)
    
    # เรียกใช้ Method ที่สร้างไว้
    add_one(my_variable)
    
  
    print(my_variable)

if __name__ == "__main__":
    main()