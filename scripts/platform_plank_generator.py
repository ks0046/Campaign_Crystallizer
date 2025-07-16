import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the cleaned Reddit posts data
df = pd.read_csv("data/cleaned_posts.csv")

# Group the posts by issue category
grouped = df.groupby("issue_category")

# Store generated platform planks
platform_planks = []

def generate_plank(issue, texts):
    prompt = f"""
You are a campaign policy advisor. Based on the following Reddit complaints from citizens about the issue of "{issue}", generate a structured campaign platform plank.

Text samples:
{texts}

Output format:
Issue: <Short Issue Title>
Problem: <Two-sentence citizen-driven summary>
Proposed Solutions:
1. <Actionable policy solution 1>
2. <Actionable policy solution 2>
Jurisdiction: <Local, State, Federal or City Council>
Political Feasibility: <High / Medium / Low>
Citizen Support Evidence: Mention volume: {len(texts.splitlines())}
Geographic Concentration: Not available (yet)
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a political campaign strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Safely extract the message content
        message = response.choices[0].message
        if message and message.content:
            return message.content.strip()
        else:
            print("⚠️ Warning: Empty response from OpenAI.")
            return "⚠️ No content returned by OpenAI."
    except Exception as e:
        print(f"❌ Error generating plank for {issue}: {e}")
        return f"❌ Error generating plank: {e}"

# Generate planks for each issue category
for issue, group in grouped:
    sample_texts = "\n".join(group["clean_text"].tolist()[:10])  # Limit to 10 posts
    plank = generate_plank(issue, sample_texts)
    platform_planks.append({
        "issue_category": issue,
        "platform_plank": plank
    })

# Save results to CSV
output_df = pd.DataFrame(platform_planks)
output_df.to_csv("data/platform_planks.csv", index=False)
print("✅ Platform planks generated and saved to data/platform_planks.csv")
