#!/bin/bash

# Run MOT tracker on extracted features in detection_dir

python3 evaluate_motchallenge.py --mot_dir=MOT16/train \
                --detection_dir=resources/detections/MOT16_train \
                --output_dir=results/
# python3 evaluate_motchallenge.py --mot_dir=MOT16/train_small \
#                 --detection_dir=resources/detections/MOT16_train_small \
#                 --output_dir=results_small/