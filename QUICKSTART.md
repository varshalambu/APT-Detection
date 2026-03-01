# APT Detection System - Quick Start Guide

## Website is Now Running! 🚀

The APT Detection dashboard is live and ready to use.

### Access the Dashboard

**URL**: http://127.0.0.1:7860

The website is accessible in your browser right now.

---

## What You Can Do

### 1. **Analyze Traffic**
- Upload a CSV file with 50 network traffic features
- Get instant detection of 5 kill chain attack stages
- View confidence scores and predictions

### 2. **View Model Performance**
- Compare baseline vs optimized models
- See confusion matrix on test data
- Analyze stage distribution

### 3. **Generate Sample Data**
- Click "Sample Data" to auto-generate test CSV
- Perfect for testing the system

---

## CSV Format

Your CSV file must have:
- **50 columns** (columns for network traffic features)
- Column names: `feature_0`, `feature_1`, ... `feature_49`
- Numeric values only
- Any number of rows

Example:
```
feature_0,feature_1,...,feature_49
10.5,20.3,...,15.2
12.1,18.9,...,14.7
...
```

Use the "Sample Data" button to see the correct format.

---

## Kill Chain Stages

The system detects 5 Cyber Kill Chain stages:

| Stage | Description |
|-------|-------------|
| **Reconnaissance** | Attacker gathers information |
| **Initial Access** | Attacker enters the system |
| **Command & Control** | Attacker establishes C2 channel |
| **Data Exfiltration** | Attacker steals data |
| **Benign** | Normal, non-attack traffic |

---

## System Status

✅ **All Components Ready**
- Models: Trained and loaded
- Artifacts: 8 files generated
- Dashboard: Running on port 7860
- Website: Fully functional

---

## If Dashboard Stops

If the dashboard closes and you need to restart:

```bash
cd "c:\Users\varsh\Downloads\APT Detection"
python apt_detection_dashboard.py
```

Then open: http://127.0.0.1:7860

---

## Architecture Highlights

✅ **Robust ML Pipeline**
- Data preprocessing with StandardScaler
- Feature reduction with PCA (50→45 components)
- Class balancing with SMOTE
- PyTorch TabNet models

✅ **Kill Chain Detection**
- 5-class multi-class classification
- Real-time predictions
- Confidence scoring

✅ **User-Friendly Interface**
- Gradio-based web UI
- CSV upload support
- Visual analytics
- Confusion matrix
- Model comparison

---

## Next Steps

1. Open http://127.0.0.1:7860 in your browser
2. Click "Sample Data" to generate test data
3. Click "Analyze" to see predictions
4. Explore the Confusion Matrix and Statistics tabs

Enjoy analyzing APT attack patterns! 🕵️‍♂️
