import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_and_test_phishing_model():
    print("="*50)
    print("🧠 Training Phishing Detection Model 🧠")
    print("="*50)
    
    # --- STEP 1: The Labeled Training Data ---
    # Load thousands of emails directly from a CSV file
    df = pd.read_csv('phishing_dataset.csv')
    
    # --- STEP 2: Feature Extraction (The Highlighter) ---
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Extract features from training text (English -> Numbers)
    X_train = vectorizer.fit_transform(df['text'])
    y_train = df['label']
    
    # --- STEP 3: Model Training (Building the Brain) ---
    # Initialize the point-system model
    model = LogisticRegression()
    
    # Teach the model by letting it cross-reference features with the labels
    model.fit(X_train, y_train)
    print("[+] Model training successfully completed.")
    
    # --- STEP 4: Testing with Brand New Emails ---
    print("\n[*] Processing incoming unknown emails...")
    
    new_emails = [
        "Urgent security update required for your account access.",
        "Let's schedule a meeting next week to discuss your urgent bank account update."
    ]
    
    # CRITICAL STEP: We transform the new emails using the exact same vectorizer.
    # We use .transform(), NOT .fit_transform(), because the model's vocabulary 
    # is already locked in. We are just highlighting matching words.
    X_new = vectorizer.transform(new_emails)
    
    # Generate predictions (Returns an array of 1s and 0s)
    predictions = model.predict(X_new)
    
    # Get the raw probability scores (Returns percentage for [Safe, Phishing])
    probabilities = model.predict_proba(X_new)
    
    # --- STEP 5: Display the Results ---
    print("\n--- 📊 Classification Report ---")
    for i, email in enumerate(new_emails):
        print(f"\nEmail Content: '{email}'")
        
        # Extract the specific percentage for the Phishing category (index 1)
        phish_chance = probabilities[i][1] * 100
        
        status = "🚨 PHISHING DETECTED" if predictions[i] == 1 else "✅ SAFE EMAIL"
        print(f"Verdict: {status} (Confidence: {phish_chance:.1f}%)")
    print("="*50)

if __name__ == "__main__":
    train_and_test_phishing_model()