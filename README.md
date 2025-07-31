# Affiliate Link Redirector (Google Cloud Function)

โปรเจกต์นี้คือ Google Cloud Function ที่ทำหน้าที่เป็นตัวกลางในการ Redirect ลิงก์ เพื่อให้คุณสามารถสร้างลิงก์ที่สั้นและจำง่ายด้วยโดเมนของคุณเอง (Custom Domain) สำหรับการใช้งาน Affiliate Links

เมื่อผู้ใช้งานเข้าถึง URL ที่คุณกำหนด (เช่น `yourdomain.com/link1`) ฟังก์ชันนี้จะทำการเปลี่ยนเส้นทางไปยัง Affiliate Link ปลายทางที่แท้จริงโดยอัตโนมัติ

## คุณสมบัติ (Features)

* **Serverless:** ไม่ต้องตั้งค่าหรือดูแลเซิร์ฟเวอร์
* **ปรับแต่งง่าย:** สามารถเพิ่ม แก้ไข หรือลบลิงก์ที่ต้องการ Redirect ได้อย่างง่ายดายในโค้ด
* **SEO Friendly:** ใช้การ Redirect แบบ `301 Moved Permanently` ซึ่งดีต่อการจัดอันดับของ Search Engine
* **จัดการข้อผิดพลาด:** ส่งคืน `HTTP 404 Not Found` สำหรับ Path ที่ไม่ตรงกับที่ตั้งค่าไว้

## การติดตั้งและตั้งค่า

### Prerequisites

* บัญชี Google Cloud Platform
* ติดตั้ง gcloud CLI (สำหรับ Deploy ผ่าน Command Line)
* โดเมนของคุณเอง (สำหรับ Custom Domain Mapping)

### ไฟล์ที่ต้องใช้

โปรเจกต์นี้ประกอบด้วย 2 ไฟล์หลัก:
1.  **`main.py`**: ไฟล์โค้ดของ Cloud Function
2.  **`requirements.txt`**: ไฟล์สำหรับระบุไลบรารีที่จำเป็น

**`main.py`**
```python
import functions_framework
from flask import redirect, abort

@functions_framework.http
def redirect_http(request):
    """
    Cloud Function นี้จะตรวจสอบ path ของ URL ที่เข้ามา และทำการ
    Redirect ไปยังลิงก์ปลายทางที่กำหนดไว้
    """
    # กำหนด mapping ของ Path ที่ต้องการเปลี่ยนเส้นทาง
    # โดย key คือ Path ที่คุณต้องการ (เช่น /link1)
    # และ value คือ URL ปลายทาง
    redirect_map = {
        '/link1': '[https://afiliate.com/product01](https://afiliate.com/product01)',
        '/link2': '[https://afiliate.com/product01](https://afiliate.com/product01)'
    }
    
    requested_path = request.path

    if requested_path in redirect_map:
        target_url = redirect_map[requested_path]
        return redirect(target_url, code=301)
    else:
        abort(404)
