# Fraud Detection Prediction App

This project is a simple web application for predicting fraudulent transactions using a trained machine learning model. The app is built with Streamlit and allows users to input transaction details to check if a transaction is likely to be fraudulent.

## Features

- User-friendly web interface with Streamlit
- Input transaction details such as type, amount, and balances
- Predicts if a transaction is fraudulent or not using a pre-trained model

## Files

- `Fraud_detection.py` — Main Streamlit app for prediction
- `dataset.py` — Script to download the dataset from Kaggle
- `requirements.txt` — List of required Python packages
- `analysis_model.ipynb` — Jupyter notebook for data analysis and model building
## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Fraud Detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset (optional):**
   - Make sure you have your Kaggle API credentials set up.
   - Run:
     ```bash
     python dataset.py
     ```

4. **Add your trained model:**
   - Place your `fraud_detection_ppipeline.pkl` model file in the project directory.

5. **Run the Streamlit app:**
   ```bash
   streamlit run Fraud_detection.py
   ```

## Notes

- The model file (`fraud_detection_ppipeline.pkl`) and dataset files are not included in the repository.
- Update the model or dataset as needed for your use case.

## License

This project is for educational