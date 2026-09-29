import pandas as pd
import os


# Find the JSON file created by Task 1
json_files = [
    file for file in os.listdir("data")
    if file.startswith("trends_") and file.endswith(".json")
]


if not json_files:
    print("No JSON file found in data folder.")
    exit()


# Use the latest JSON file
json_file = sorted(json_files)[-1]

json_path = os.path.join("data", json_file)


# Load JSON data into Pandas
df = pd.read_json(json_path)

print(f"Loaded {len(df)} stories from {json_path}")


# Remove duplicate stories using post_id
df = df.drop_duplicates(subset="post_id")

print(f"After removing duplicates: {len(df)}")


# Remove rows with missing required values
df = df.dropna(
    subset=["post_id", "title", "score"]
)

print(f"After removing nulls: {len(df)}")


# Convert score and comments into numeric values
df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
)

df["num_comments"] = pd.to_numeric(
    df["num_comments"],
    errors="coerce"
)


# Remove rows where numeric conversion failed
df = df.dropna(
    subset=["score", "num_comments"]
)


# Convert numeric columns to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# Remove stories with score below 5
df = df[df["score"] >= 5].copy()

print(f"After removing low scores: {len(df)}")


# Remove unnecessary whitespace from titles
df["title"] = df["title"].str.strip()


# Save cleaned data
output_file = "data/trends_clean.csv"

df.to_csv(
    output_file,
    index=False
)

print(
    f"\nSaved {len(df)} rows to {output_file}"
)


# Display category summary
print("\nStories per category:")

print(
    df["category"]
    .value_counts()
    .sort_index()
)