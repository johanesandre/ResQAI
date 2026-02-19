# 🚨 ResQAI
### Computer Vision–Based Distress Gesture Detection System

---

## 📌 Overview

**ResQAI** adalah sistem Computer Vision berbasis Python yang dirancang untuk **mendeteksi sinyal permintaan pertolongan manusia secara visual** melalui gesture tubuh, khususnya **dua tangan terangkat ke atas** sebagai sinyal universal *distress*.

Sistem ini ditujukan untuk membantu proses **respon darurat** pada kondisi seperti:

- 🌊 **Banjir**
- 🔥 **Kebakaran**
- 🌪️ **Bencana alam**
- 🚨 **Situasi darurat lainnya**

Dengan memanfaatkan kamera standar (webcam / CCTV / drone), sistem ini mampu mendeteksi **orang / sekumpulan orang (multi-person)** secara real-time dan memberikan **peringatan audio otomatis** saat gesture distress terdeteksi.

---

## ❗ Problem Statement

Dalam kondisi darurat nyata, korban sering mengalami:

- Terisolasi secara fisik
- Tidak memiliki akses komunikasi (HP rusak / sinyal hilang)
- Tidak mampu berbicara atau berteriak
- Kondisi lingkungan yang bising (banjir, api, mesin, angin)
- Keterbatasan fisik (luka, kelelahan)

Di sisi lain, **petugas penyelamat** harus:
- Memantau area yang luas
- Mengandalkan pengamatan visual
- Menghadapi keterbatasan waktu dan visibilitas

👉 Dibutuhkan sistem **peringatan dini berbasis visual** yang:
- Tidak bergantung pada suara atau perangkat pribadi korban
- Dapat bekerja otomatis
- Mudah diintegrasikan ke sistem pemantauan

---

## 💡 Solution Concept

Sistem ini bekerja dengan pendekatan **pose-based detection**, bukan face recognition.

### Prinsip utama:
- Mendeteksi **postur tubuh manusia**
- Mengabaikan identitas wajah (privacy-first)
- Fokus pada **bahu dan pergelangan tangan**
- Mengidentifikasi **dua tangan terangkat di atas bahu** sebagai sinyal distress

Ketika gesture tersebut terdeteksi:
- Sistem menampilkan indikator visual
- Alarm suara akan **aktif terus selama gesture dipertahankan**
- Alarm berhenti otomatis saat tangan diturunkan

---

## ✨ Key Features

- ✅ Real-time **multi-person detection**
- ✅ Deteksi gesture **dua tangan terangkat**
- ✅ Alarm suara berkelanjutan selama kondisi distress
- ✅ Bounding box pada setiap individu terdeteksi
- ✅ Tanpa face recognition (privacy-friendly)
- ✅ Menggunakan kamera standar (webcam / CCTV)
- ✅ Ringan dan siap untuk deployment lapangan

---

## 🧠 Technology Stack

- **Python 3.10**
- **OpenCV**
- **YOLOv8 Pose (Ultralytics)**
- **Computer Vision**
- **Real-time Video Processing**

---

## 📂 Project Structure

