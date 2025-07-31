import functions_framework
from flask import redirect, abort

@functions_framework.http
def redirect_http(request):
    """
    Cloud Function นี้จะตรวจสอบ path ของ URL ที่เข้ามา และทำการ
    Redirect ไปยังลิงก์ปลายทางที่กำหนดไว้
    """

    # กำหนด mapping ของ Path ที่ต้องการเปลี่ยนเส้นทาง
    # โดย key คือ Path ที่คุณต้องการ (เช่น /zdomain)
    # และ value คือ URL ปลายทาง
    redirect_map = {
        '/link1': 'https://afiliate.com/product01',
        '/link2': 'https://afiliate.com/product01'
    }
    
    # ดึง path ของ URL ที่เข้ามาจาก request object
    # เช่น ถ้า URL คือ mydomain.com/zdomain path จะเป็น /zdomain
    requested_path = request.path

    # ตรวจสอบว่า path ที่ร้องขอมีอยู่ใน redirect_map หรือไม่
    if requested_path in redirect_map:
        target_url = redirect_map[requested_path]
        
        # ใช้ flask.redirect เพื่อทำการเปลี่ยนเส้นทาง
        # 301 คือ "Moved Permanently" หรือเปลี่ยนเส้นทางแบบถาวร
        return redirect(target_url, code=301)
    else:
        # ถ้าไม่มี path ที่ตรงกัน ให้ส่งคืน HTTP 404 Not Found
        # หรือคุณจะเปลี่ยนไป redirect ที่หน้า homepage ก็ได้
        abort(404)
