---
title: Pneumonia Detection API
emoji: 🫁
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

## API Documentation

### Base URL
 
```
https://<your-space-name>.hf.space/
```
 
---
 
### Endpoint 1 — Health Check
 
Untuk cek apakah server sedang online sebelum kirim gambar.
 
```
GET /health
```
 
**Response:**
```json
{
  "status": "ok"
}
```
 
---
 
### Endpoint 2 — Predict
 
```
POST /predict
```
 
**Request format:** `multipart/form-data`
 
| Field | Type | Keterangan |
|-------|------|------------|
| `file` | File (JPEG/PNG) | Gambar chest X-ray yang akan diklasifikasi |
| `model` | Query param (string) | Model yang digunakan: `densenet121` (default) atau `vgg16` |
 
**Response (200):**
 
```json
{
  "model": "densenet121",
  "label": "PNEUMONIA",
  "confidence": 0.9341
}
```
 
---
 
### Error Handling
 
| HTTP Status | Arti |
|-------------|---------| 
| `200` | Sukses |
| `400` | File bukan JPEG/PNG |
| `422` | Field `file` tidak ada di request |
| `500` | Server error |

---