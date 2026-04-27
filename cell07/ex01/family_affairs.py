#!/usr/bin/env python3

def find_the_redheads(family):
    # ใช้ filter เพื่อเลือกเฉพาะ key (ชื่อ) ที่มี value (สีผม) เป็น "red"
    redheads = filter(lambda name: family[name] == "red", family)
    
    # แปลงผลลัพธ์จาก filter object ให้เป็น list ก่อนส่งคืน
    return list(redheads)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))