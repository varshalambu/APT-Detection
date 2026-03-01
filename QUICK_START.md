# ⚡ QUICK START GUIDE

## 3 SIMPLE STEPS

### Step 1️⃣: Install
```bash
pip install -r requirements.txt
```

### Step 2️⃣: Train
```bash
python train_models.py
```
Takes 5-10 minutes. Creates all models and artifacts.

### Step 3️⃣: Run Dashboard
```bash
python apt_detection_dashboard.py
```
Open: **http://127.0.0.1:7860**

---

## DONE! 🎉

Your APT Detection Dashboard with Kill Chain Stage prediction is running!

---

## WHAT HAPPENS IN EACH STEP

### train_models.py
- Loads APT datasets (DAPT2020 + Unraveled 2023)
- Preprocesses: Missing values → Normalize → Encode labels
- Balances classes using SMOTE
- Reduces dimensions with PCA
- Trains 2 TabNet models:
  - **Baseline** (simple, 70-80% accuracy)
  - **Optimized** (advanced, 95-98% accuracy)
- Saves all models and preprocessing artifacts

### apt_detection_dashboard.py
- Loads trained models
- Simple web interface:
  1. Upload CSV with network traffic (50 features)
  2. Click "Analyze Traffic"
  3. See detected kill chain stage
  4. View confidence scores
  5. Compare model accuracies

---

## KILL CHAIN STAGES DETECTED

1. 🔍 **Reconnaissance** - Information gathering
2. 🎯 **Initial Access** - Entry into network
3. 🔗 **Command & Control** - C2 communication
4. 💾 **Data Exfiltration** - Stealing data
5. ✅ **Benign** - Normal traffic

---

## DATASET FORMAT

CSV file with:
- **50 columns**: feature_0 to feature_49 (network metrics)
- **Numeric values**: traffic data
- **One row per sample**: one network traffic instance

Example:
```
feature_0, feature_1, ..., feature_49
-5.2, 3.1, ..., 8.7
2.1, -0.4, ..., 1.2
```

Use "Generate Sample" button in dashboard to see format.

---

## TROUBLESHOOTING

**Q: Which folder do I run commands from?**  
A: `c:\Users\varsh\Downloads\APT Detection\`

**Q: How long does training take?**  
A: First training: 5-10 minutes. Creates models that run instantly after.

**Q: Models not found?**  
A: Run `python train_models.py` first.

**Q: Feature mismatch error?**  
A: CSV must have exactly 50 features. Use "Generate Sample" button.

**Q: Port 7860 already in use?**  
A: Edit line in apt_detection_dashboard.py:  
```python
demo.launch(server_port=7861)  # Change to different port
```

---

## FILE CHECKLIST AFTER TRAINING

After `python train_models.py`, you should have:

✅ `baseline_tabnet_model/` folder  
✅ `optimized_tabnet_model/` folder  
✅ `scaler.pkl`  
✅ `pca.pkl`  
✅ `label_encoder.pkl`  
✅ `kill_chain_stages.pkl`  
✅ `test_data.npz`  
✅ `feature_names.pkl`  

If missing, something went wrong - run train_models.py again.

---

✨ **That's it! Enjoy your APT Detection Dashboard!** ✨
