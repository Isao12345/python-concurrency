# Python Concurrency Demo

โปรเจกต์นี้เป็นการทดลองใช้งาน concurrency ในภาษา Python
เพื่อทำความเข้าใจการทำงานของ Thread, asyncio และ Process Pool

## 1. Thread
ใช้ module threading เพื่อสร้างหลาย thread ทำงานพร้อมกัน
เหมาะกับงานที่ต้องรอ I/O เช่น sleep หรือ file/network

## 2. asyncio
ใช้ async/await เพื่อจัดการงานแบบ asynchronous
ช่วยให้โปรแกรมไม่ block ระหว่างรอ I/O

## 3. Process Pool
ใช้ ProcessPoolExecutor เพื่อรันงานหลาย process
เหมาะกับงานที่ใช้ CPU สูง

