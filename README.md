สมมุติว่าเครื่องคอมพิวเตอร์ (SMC) นี้ เป็น 8-register registor0-registor8 
32-bit computer ใช้ word-addresses  = 4 word : 1 instruction
สำหรับทุก addresses และเครื่อง SMC มี 65536 words ของ memory โดยหลักการพื้นฐาน ของ assembly language จะ ตั้งให้ register 0 มีค่าข้างในเป็น 0 เสมอ (ไม่ควรจะเปลี่ยนเป็นค่าอื่น) เราจะใช้ instruction formats ทั้งหมด 4 formats โดยที่ bit ที่ 0 เป็น LSB และ bit ที่ 31-25 ไม่ถูกใช้สำหรับทุก instructions และควรจะมีค่าเป็น 0