#!/bin/bash
echo "======================================================================"
echo "APT Detection Dashboard - Setup & Launch"
echo "======================================================================"
echo ""
echo "Step 1: Installing dependencies..."
echo ""
pip install -r requirements.txt
echo ""
echo "Step 2: Training models..."
echo ""
python train_models.py
echo ""
echo "Step 3: Launching Dashboard..."
echo ""
python apt_detection_dashboard.py
