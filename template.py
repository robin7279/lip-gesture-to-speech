import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'LipGestureAI'

list_of_files = [
    ".github/workflows/.gitkeep",
    "backend/app.py", # FastAPI backend
    "backend/model.py", # YOLOv8/10/11 inference code
    "backend/utils.py", # Helper functions
    "backend/Dockerfile/", # Dockerfile for backend containerization
    "backend/config.yaml ", # Configuration file for settings
    "frontend/web/public/",  # Public files (e.g., index.html)
    "frontend/web/src/App.js", # Main app component
    "frontend/web/src/components/", # React components
    "frontend/web/src/services/", # API communication
    "frontend/web/src/utils.js", # Utility functions (e.g., webcam access)
    "frontend/web/package.json", # NPM dependencies for React app
    "frontend/web/README.md", # Documentation for frontend
    "frontend/mobile/lib/",  # Flutter or React Native lib folder
    "frontend/mobile/android/", # Android-specific files
    "frontend/mobile/ios/", # iOS-specific files
    "frontend/mobile/pubspec.yaml", # Flutter dependencies or package.json for React Native
    "frontend/mobile/README.md",# Documentation for mobile
    "data/raw/__init__.py",  # Raw dataset for lip gestures (images or videos)
    "data/processed/__init__.py",  # Processed dataset (e.g., annotations, resized images)
    "data/custom_data.yaml", # Dataset configuration for YOLOv8 training
    "model/yolov8/yolov8s.pt", # Pre-trained YOLOv8 model weights
    "model/yolov8/train.py", # YOLOv8 model training script
    "model/yolov8/custom_model.yaml", # Custom YOLOv8 config (for your dataset)
    "model/yolov8/README.md",# Documentation for model training
    "notebooks/data_preprocessing.ipynb", # Data preprocessing for lip gesture dataset
    "notebooks/model_training.ipynb", # YOLOv8 training notebook for lip gesture detection
    "notebooks/inference.ipynb", # Testing and running inference with YOLOv8 on video frames
    "notebooks/text_to_speech.ipynb", # Experimentation with text-to-speech synthesis
    "deployment/kubernetes/__init__.py", # Project deployment 
    "setup.py",  # Setup file for package installation
    "requirements.txt", # Global Python dependencies (e.g., Flask, FastAPI, PyTorch)

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with  open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists.")