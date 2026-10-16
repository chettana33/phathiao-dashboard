---
title: "Affiliate (สินค้า/คลิป/ไฟล์)"
type: "dashboard"
last_updated: 2026-10-17T01:20:00+07:00
---

# 🛒 Affiliate — สินค้า คลิป และที่เก็บไฟล์

> อัปเดตโดยพาเที่ยวเมื่อมีการเปลี่ยนแปลง (การ์ดเจ้าของ: PC-017) · หลักการเลือกสินค้า: `04_Sales_Marketing/Affiliate_Selection_Principle_v1.md`

## สถานะปัจจุบัน

| เรื่อง | สถานะ |
|---|---|
| บัญชี Shopee Affiliate | ส่งใบสมัครแล้ว (16 ต.ค. 69 18:59) — **รอ Shopee ตรวจ** · ช่องทาง TikTok + Facebook ยืนยันแล้ว |
| สินค้ารอบ 1 | **AFF-15** Powerbank ACMIC (฿55/ชิ้น) · **AFF-18** มัทฉะ RAIWAN (฿83/ชิ้น) · **AFF-23** แก้ว TYESO (฿31/ชิ้น) |
| คลิปชิ้นแรก | AFF-18 มัทฉะ — **prompt ผ่านด่านแล้ว รอเจนใน Google Flow** |
| ลิงก์ affiliate | 3 ลิงก์พร้อมใช้ (สถานะ: ยังไม่ทดสอบคลิกจากคนอื่น) |

## 🔗 ลิงก์ affiliate รอบ 1

| รหัส | สินค้า | ลิงก์ |
|---|---|---|
| AFF-15 | ACMIC W1501 Powerbank 15,000mAh | https://s.shopee.co.th/80DUItp1Uc |
| AFF-18 | ผงมัทฉะ RAIWAN ออร์แกนิค 100g | https://s.shopee.co.th/W7TN8dEqF |
| AFF-23 | แก้วเก็บความเย็น TYESO | https://s.shopee.co.th/3qNvLHmHTK |

## 📁 ที่เก็บไฟล์ (path จริง)

| ประเภท | path | มีอะไร |
|---|---|---|
| ไฟล์งาน affiliate (โฟลเดอร์หลัก) | `D:\Affiliate\` | ลิงก์ · คำตอบที่ปรึกษา · รหัสสินค้า · ข้อความคำถาม |
| ภาพสินค้า AFF-18 (มัทฉะ) | `D:\Affiliate\product_images\AFF-18\` | 14 ภาพ (aff18_01…15 — ตัด `aff18_03` ออกแล้ว) + `images.json` |
| ลิงก์ affiliate | `D:\Affiliate\affiliate_links.md` · `.json` | 3 ลิงก์ + หลักฐานการ์ดที่เลือก + หน้าดูรายละเอียด |
| คำตอบที่ปรึกษา (ChatGPT) | `D:\Affiliate\คำตอบ-ChatGPT.txt` | คำตอบ 2 รอบ (รอบ 1 + รอบ 2) |
| รหัสสินค้า ↔ ชื่อ | `D:\Affiliate\product_id_map.csv` | AFF-01…AFF-51 |
| ภาพหน้าจอตรวจลิงก์ | `D:\Affiliate\aff23_customer.png` | มุมมองลูกค้า (ยืนยันช่วงราคาตามขนาด) |
| **ชีตหลัก Affiliate (7+ แท็บ)** | `https://docs.google.com/spreadsheets/d/1GTHz7BQF38vWDhqG2IovSiSPOnlthTFvrKmbosfRcNc/edit` | หมวดของเรา · สินค้าดิบ 135 · ส่ง AI คัด 51 · ผล AI · ลิงก์ · PDCA · คู่มือ+รอบงาน |
| **ชีต Google Flow Prompt (ของ Gochisou — อ้างอิง)** | `https://docs.google.com/spreadsheets/d/1rdrvX-T6lgFTjSVE9z2v2YodWciX1NJdOeiEl6CfMko/edit` | แท็บ `affiliate AFF-18 มัทฉะ` (สำรองไว้) |
| **⭐ ชีต Affiliate Flow Prompt (ของงาน affiliate)** | `https://docs.google.com/spreadsheets/d/1rSw8o6hcUtPS8C2bwB45D-YwpEYwOEeIvnQ_V0Wk7G0/edit` | `คู่มือ+สถานะ` · `affiliate AFF-18 มัทฉะ` (4 ฉาก) · แท็บเปล่ารอ AFF-15/AFF-23 |
| หลักการเลือกสินค้า (Vault) | `04_Sales_Marketing/Affiliate_Selection_Principle_v1.md` | ตัวกรอง 5 ชั้น + กลไกให้อาหารกลับ |
| แผนคลิปชิ้นแรก (Vault) | `04_Sales_Marketing/Affiliate_Clip1_Plan_AFF18.md` | 4 ฉาก + ทางเลือกการผลิต |
| สมุดงาน/รอบทดลอง (Vault) | `04_Sales_Marketing/Affiliate_Run_Log_v1.md` | SOP 12 ขั้น + บทเรียน 10 ข้อ |
| กติกาวิธีผลิต (rules) | `system-rules/affiliate.md` §2b–§2d | บัญชี · หลักการเลือก · คลิป |

## 🎬 คลิปชิ้นแรก — AFF-18 (ขั้นตอนที่เหลือ)

1. เปิด Google Flow (Edge โปรไฟล์ `_flow_profile` — พี่เจล็อกอินเอง)
2. **เจนภาพตั้งต้น 4 ฉาก** จากคอลัมน์ Image Prompt ในชีต **Affiliate Flow Prompt** (แท็บ `affiliate AFF-18 มัทฉะ`)
   - ทางที่เลือก: **เลือกภาพสินค้าจริงจาก `D:\Affiliate\product_images\AFF-18\`** (14 ภาพ) แล้ว **ให้ Gemini ช่วยลบข้อความ/ลบพื้นหลัง** ก่อนใช้เป็นเฟรมตั้งต้น
3. **เจนวิดีโอ** (Frames to video) ฉากละ 1 เจน ≈ 4 เจน (~40–48 เครดิต · โควตาฟรี 50/วัน)
4. ส่งไฟล์มาให้พาเที่ยว → QC (เสียง/แสง/ตัวอักษร) → ตัดต่อ + ใส่ข้อความเปิดเผยโฆษณา
5. โพสต์ (Facebook ส่วนตัว + TikTok) → วัดผล 24/72 ชม. → บันทึกใน `09_คู่มือ+รอบงาน`

## งานค้าง affiliate

- [ ] รอ Shopee อนุมัติใบสมัคร
- [ ] เจนภาพ/วิดีโอ 4 ฉากใน Flow
- [ ] QC + ตัดต่อ + โพสต์คลิปชิ้นแรก
- [ ] ทดสอบว่าลิงก์ถูกนับคลิก (ต้องมีคนอื่นกด 1 ครั้ง)
- [ ] รัน pilot suite กับที่ปรึกษาภายนอกจริง (ค้างจาก PC-017)
