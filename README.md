# Brain Tumor Detection using YOLOv8

This project demonstrates the detection of brain tumors in medical images using a custom-trained YOLOv8 model. The script loads an image, runs the YOLOv8 model for tumor detection, and displays the top results with bounding boxes and confidence scores overlaid on the image.

## Project Overview

In this project, I developed a solution to detect brain tumors in images using a pre-trained YOLOv8 model. The model detects potential tumor regions and draws bounding boxes around them. The top predictions are shown on the image, with each prediction accompanied by a confidence score. The goal is to provide a clear visual representation of the detected tumor regions.

## Features

- **Brain Tumor Detection**: The script utilizes a YOLOv8 model trained for brain tumor detection.
- **Bounding Boxes**: Tumor regions are highlighted with bounding boxes.
- **Top Predictions**: The top predictions are displayed on the image, including the class name (tumor) and the confidence score.
- **Threshold-based Filtering**: Only predictions with a confidence score higher than a set threshold are displayed on the image.

## How It Works

1. **Model Loading**: 
   - The pre-trained YOLOv8 model is loaded from the specified path.
   
2. **Image Input**:
   - The input image is read and resized using OpenCV to ensure consistent processing.

3. **Detection and Classification**:
   - The YOLOv8 model runs on the image, and the top tumor regions are detected.
   - Each detection is accompanied by a confidence score and a class name (e.g., "tumor").

4. **Bounding Box and Label Drawing**:
   - For each detection above a specified confidence threshold, a bounding box is drawn around the detected tumor.
   - The confidence score is displayed above each bounding box, formatted as a percentage.

5. **Displaying Results**:
   - The resulting image with bounding boxes and class labels is displayed using OpenCV.

## How to Run

### Dependencies

To run this project, you need to have the following libraries installed:
- `opencv-python`
- `ultralytics`

You can install these dependencies using `pip`:
```bash
pip install opencv-python ultralytics
