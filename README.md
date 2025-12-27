# 🧠 AI Vision-based Alzheimer’s Diagnosis

MRI 영상과 임상 메타데이터를 활용하여 알츠하이머병을 조기 진단하는  
AI 기반 웹 진단 보조 플랫폼입니다.

의료진이 MRI 이미지를 업로드하면  
AI 모델이 자동으로 분석 결과와 시각화를 제공하고  
진단 리포트를 PDF로 생성합니다.

## Teams
| <img src="https://github.com/dotz0ver.png" width="90" height="90" /> | <img src="https://github.com/zangzoo.png" width="90" height="90" /> | <img src="https://github.com/0gonge.png" width="90" height="90" /> | <img src="https://github.com/likeeun.png" width="90" height="90" /> |
|:--:|:--:|:--:|:--:|
| [문소연](https://github.com/dotz0ver) | [장지우](https://github.com/zangzoo) | [송여경](https://github.com/0gonge) | [조채은](https://github.com/likeeun) |
| `Backend · AI` | `Backend · AI` | `Web · AI` | `Web · AI` |


## Project Overview

- Goal: 알츠하이머병 조기 진단 정확도 향상
- Approach
  - MRI 이미지 기반 딥러닝
  - 임상 메타데이터(age, sex, MMSE 등) 결합
  - 다중 슬라이스 MRI 분석
- Output
  - 진단 결과 + 클래스 확률
  - AI 근거 시각화(Grad-CAM)
  - 자동 PDF 리포트

## Key Features

### AI-based MRI Analysis
- VGG16 / EfficientNetB3 기반 모델
- Multi-slice MRI (중앙 ±10mm, ±15mm)
- Metadata 결합 모델로 성능 향상

### Explainable AI
- Grad-CAM 히트맵 제공
- 의료진이 판단 근거를 시각적으로 확인 가능

### Web Platform for Clinicians
- 로그인 / 회원가입 (병원 소속 기반)
- MRI 이미지 업로드
- 환자 히스토리 관리
- 진단 결과 PDF 다운로드

## 🏗️ System Architecture
```
[ Web Client (React) ]
          |
          v
[ Django REST API ]
          |
          v
[ AI Inference Server ]
(TensorFlow / Keras)
```

## 🧠 AI Models

- **Baseline**
  - EfficientNetB3 (AUROC ≈ 0.99)

- **Main Models**
  - VGG16 (MRI only)
  - VGG16 + Metadata (최대 94.56% accuracy)
  - VGG16 + Multi-slice MRI (최대 92%)

- **Final Direction**
  - Multi-slice MRI + Metadata 결합 모델

## 🛠 Tech Stack

### Frontend
- React
- HTML / CSS / JavaScript

### Backend
- Django
- Django REST Framework

### AI / ML
- TensorFlow / Keras
- VGG16, EfficientNetB3
- Grad-CAM

### Database
- SQLite

### Tools
- Git / GitHub
- Google Colab
- Postman

## Dataset

- **OASIS**
- **ADNI**
- Longitudinal MRI data with clinical metadata

## Expected Impact

- 알츠하이머 조기 발견 가능성 향상
- 진단 시간 단축 및 의료 비용 절감
- 의료진 간 판독 편차 감소
- 병원 · 연구기관 등 활용 가능

## 📌 Project Info

- **Program**: 2024 한이음 ICT 멘토링
- **Duration**: 2024.04 – 2024.10
- **Category**: Medical AI / Computer Vision / Web



