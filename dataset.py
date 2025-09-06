# ...existing code...
import os

# Install kaggle if not already installed (uncomment if needed)
# !pip install kaggle

# Set up Kaggle API credentials (make sure kaggle.json is in ~/.kaggle/)
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Download the dataset
dataset = "amanalisiddiqui/fraud-detection-dataset"
download_path = "./fraud-detection-dataset"
os.makedirs(download_path, exist_ok=True)
api.dataset_download_files(dataset, path=download_path, unzip=True)

print("Path to dataset files:", os.path.abspath(download_path))
# ...existing code...