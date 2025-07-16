import pandas as pd
import re
import os

# Ensure input file exists
input_path = "data/raw_posts.csv"
output_path = "data/cleaned_posts.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"{input_path} not found. Please run data_collection.py first.")

# Load data
df = pd.read_csv(input_path)

# Combine title + text
df["full_text"] = df["title"].fillna("") + " " + df["text"].fillna("")

# Cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # Remove markdown links
    text = re.sub(r"[^a-z\s]", "", text)  # Remove punctuation/numbers/special chars
    text = re.sub(r"\s+", " ", text)  # Collapse spaces
    return text.strip()

df["clean_text"] = df["full_text"].apply(clean_text)

# Issue categorization function
def categorize_issue(text):
    housing_keywords = ["rent", "zoning", "housing", "development", "affordable"]
    transport_keywords = ["bus", "transit", "transport", "public transport", "port authority"]
    safety_keywords = ["crime", "police", "safety", "shooting", "violence", "911"]
    tax_keywords = ["tax", "budget", "funding", "property tax", "city council"]

    if any(word in text for word in housing_keywords):
        return "Housing & Development"
    elif any(word in text for word in transport_keywords):
        return "Transportation"
    elif any(word in text for word in safety_keywords):
        return "Public Safety"
    elif any(word in text for word in tax_keywords):
        return "Government & Taxes"
    else:
        return "Other"

df["issue_category"] = df["clean_text"].apply(categorize_issue)

# Save cleaned & labeled output
df.to_csv(output_path, index=False)
print(f"✅ Cleaned and labeled data saved to {output_path}")
print(df[["title", "issue_category"]].head(10))
