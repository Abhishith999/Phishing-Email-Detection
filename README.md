# Phishing Email Detection using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based phishing email detection system developed using Python and Scikit-learn.

The model analyzes email text content and predicts whether an email is:

* ✅ Safe
* 🚨 Phishing

The system uses Natural Language Processing (NLP) techniques with TF-IDF Vectorization and Logistic Regression for classification.

---

# 🚀 Features

* Detect phishing emails using Machine Learning
* Real-time email prediction
* TF-IDF text feature extraction
* Logistic Regression classification
* Confidence score prediction
* User input support through terminal
* Error handling and dataset validation

---

# 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

---

# 📂 Project Structure

```bash id="c5rlh7"
Phishing-Email-Detection/
│
├── phishing_model.py
├── phishing_email.csv
├── README.md

```

---

# 📥 Installation

Clone the repository:

```bash id="hzywmv"
git clone https://github.com/Abhishith999/Phishing-Email-Detection
```

Move into the project directory:

```bash id="qph3wq"
cd Phishing-Email-Detection
```

Install required libraries:

```bash id="zw1x0m"
pip install pandas scikit-learn
```

---

# 📊 Dataset Preparation

download phishing_email.csv file from kaggle and add the file to the Phishing-Email-Detection folder.
after that run the program.

# ▶️ Running the Project

Run the Python script:

```bash id="4jlwm3"
python phishing_model.py
```

---

# 🧠 How the Model Works

## 1. Dataset Loading

The phishing email dataset is loaded from a CSV file using Pandas.

---

## 2. Feature Extraction

TF-IDF Vectorizer converts email text into numerical values.

This helps the model understand important phishing-related words.

---

## 3. Model Training

A Logistic Regression model learns patterns from phishing and safe emails.

---

## 4. Email Prediction

The system predicts whether a newly entered email is:

* Safe
* Phishing

The model also provides a confidence score.

---

---

# 📚 Learning Outcomes

Through this project, I learned:

* Machine Learning fundamentals
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Logistic Regression
* Dataset preprocessing
* Cybersecurity applications of AI
* Real-time text classification

---

# 🔮 Future Improvements

* Add GUI interface
* Deploy as a web application
* Real-time email monitoring
* Deep Learning integration
* Browser extension support
* Advanced phishing pattern detection

---

# 👨‍💻 Author

Gudla Sai Abhishith

* Cybersecurity Enthusiast
* CSE Student at Gayatri Vidya Parishad
* Interested in Ethical Hacking, Penetration Testing, Vulnerability Scanning, and AI Security

GitHub:
https://github.com/Abhishith999

LinkedIn:
https://www.linkedin.com/in/abhishith999/

---
