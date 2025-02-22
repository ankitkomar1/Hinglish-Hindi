# Hybrid BiLSTM-RNN Sentiment Analysis

## Overview
This project implements a hybrid BiLSTM and RNN framework for multilingual sentiment analysis of Hinglish and English tweets.
It classifies sentiment into positive, negative, and neutral categories.

## Project Structure
```
Hybrid_BiLSTM_RNN_Sentiment_Analysis/
│── dataset/
│   ├── dataset_description.txt
│   ├── train_data.csv
│   ├── test_data.csv
│── models/
│   ├── lstm_model.py
│   ├── bilstm_model.py
│   ├── rnn_model.py
│── scripts/
│   ├── preprocess_data.py
│   ├── train_model.py
│   ├── evaluate_model.py
│── results/
│   ├── model_performance.txt
│── README.md
│── installation.txt
│── requirements.txt
│── main.py
```

## How to Use
1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run `preprocess_data.py` to clean and prepare the dataset.
3. Train the model using `train_model.py`.
4. Evaluate the model using `evaluate_model.py`.
