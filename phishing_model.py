import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import sys

# ==========================================
# ⚙️ CONFIGURATION ZONE
# Update these variables to match your downloaded CSV file!
# ==========================================
CSV_FILENAME = 'phishing_email.csv' # The name of your dataset file
TEXT_COLUMN = 'text_combined'                  # Change this if your column is named 'body', 'email_text', etc.
LABEL_COLUMN = 'label'                # Change this if your column is named 'spam', 'target', etc.
# ==========================================

def train_and_test_phishing_model():
    print("="*50)
    print("🧠 Training Phishing Detection Model 🧠")
    print("="*50)
    
    # --- STEP 1: Load The Labeled Training Data ---
    print(f"[*] Attempting to load dataset: {CSV_FILENAME}...")
    try:
        df = pd.read_csv(CSV_FILENAME)
        small_df = df.sample(5000)
        print(f"[*] Successfully loaded {len(small_df)} emails.")
        print(f"[*] Columns found in file: {list(small_df.columns)}")
    except FileNotFoundError:
        print(f"[-] ERROR: Could not find '{CSV_FILENAME}'.")
        print("    Please make sure the CSV file is in the same folder as this script.")
        sys.exit(1)
        
    # Check if the configured columns actually exist in the CSV
    if TEXT_COLUMN not in small_df.columns or LABEL_COLUMN not in small_df.columns:
        print(f"[-] ERROR: Column mismatch! You configured '{TEXT_COLUMN}' and '{LABEL_COLUMN}'.")
        print(f"    But the file only has these columns: {list(small_df.columns)}")
        print("    Please update the CONFIGURATION ZONE at the top of the script.")
        sys.exit(1)

    # --- STEP 2: Feature Extraction (The Highlighter) ---
    print("[*] Initializing TF-IDF Vectorizer...")
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    
    # Extract features from training text (English -> Numbers)
    # We drop any empty rows (NaN) just in case the dataset is messy
    small_df = small_df.dropna(subset=[TEXT_COLUMN, LABEL_COLUMN])
    
    X_train = vectorizer.fit_transform(small_df[TEXT_COLUMN])
    y_train = small_df[LABEL_COLUMN]
    
    # --- STEP 3: Model Training (Building the Brain) ---
    print("[*] Training the Logistic Regression model...")
    model = LogisticRegression(max_iter=1000) # max_iter increased for large datasets
    
    model.fit(X_train, y_train)
    print("[+] Model training successfully completed!")
    
    # --- STEP 4: Testing with Brand New Emails ---
    print("\n[*] Processing incoming unknown emails...")
    
    new_emails = []
    
    while True:
        email = input("Paste The Email (type 'completed' to finish): ")
    
        if email.lower() == "completed":
            break
    
        new_emails.append(email)
    if len(new_emails) == 0:
        print("[-] No emails entered.")
        sys.exit(1)

        
    
    
    
    # Transform the new emails using the exact same locked-in vocabulary
    X_new = vectorizer.transform(new_emails)
    
    predictions = model.predict(X_new)
    probabilities = model.predict_proba(X_new)
    
    # --- STEP 5: Display the Results ---
    print("\n" + "="*50)
    print("📊 CLASSIFICATION REPORT")
    print("="*50)
    for i, email in enumerate(new_emails):
        # We assume label '1' is phishing. If your dataset uses 'spam', you may need to adjust this.
        phish_chance = probabilities[i][1] * 100 
        status = "🚨 PHISHING DETECTED" if predictions[i] == 1 else "✅ SAFE EMAIL"
        
        print(f"\nEmail: '{email}'")
        print(f"Verdict: {status}")
        print(f"Confidence Score: {phish_chance:.1f}%")
    print("\n" + "="*50)

if __name__ == "__main__":
    train_and_test_phishing_model()
