#!/bin/bash

# Run feature extractor on data and save results as .npy files
# Features are saved in output_dir
python3 tools/generate_detections.py --model=resources/networks/mars-small128.pb --mot_dir=MOT16/train_small --output_dir=resources/detections/MOT16_train_small