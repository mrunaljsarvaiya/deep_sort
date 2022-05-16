#!/bin/bash

python3 tools/generate_detections.py --model=resources/networks/mars-small128.pb --mot_dir=MOT16/train_small --output_dir=resources/detections/MOT16_train_small