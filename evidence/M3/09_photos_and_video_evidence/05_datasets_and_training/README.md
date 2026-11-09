# Dataset Sourcing & Model Training Evidence
**Directory:** `evidence/M3/09_photos_and_video_evidence/05_datasets_and_training/`  
**Milestone:** M3 – Decide and Act  

---

## 1. Overview

This directory preserves authentic photographic evidence of the dataset sourcing and repository records used for training the YOLOv8 Helmet and Glove detection model.

## 2. Media Inventory

| Filename | Media Type | Resolution | Purpose & Description |
|---|---|---|---|
| `kaggle_ppe_dataset_source.jpeg` | Screen Photograph | 4000 × 2252 (615 KB) | Photograph of the dataset portal at Kaggle (`kaggle.com/datasets/waquarahmed/ppe-dataset`) displaying the PPE Dataset containing 23,600+ industrial safety images, file manifest (`01-15-1-1-1-1-30.jpg`), and data card. |

---

## 3. Dataset Attribution & Linkage

- **Public Repository:** Kaggle – PPE Dataset (`waquarahmed/ppe-dataset`)
- **Direct Kaggle URL:** [https://www.kaggle.com/datasets/waquarahmed/ppe-dataset](https://www.kaggle.com/datasets/waquarahmed/ppe-dataset)
- **Roboflow Pipeline:** The raw images were curated and annotated in Roboflow under project `yolo-detection-helmet-gloves-2` to generate the normalized 3-class annotations (`0: gloves`, `1: head`, `2: helmet`).
- **Scale:** 23,600+ industrial images encompassing varied angles, factory lighting conditions, and diverse PPE gear types.
