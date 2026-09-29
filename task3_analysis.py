import pandas as pd
import numpy as np


# Load cleaned data from Task 2
df = pd.read_csv(
    "data/trends_clean.csv"
)


# Display basic information
print(f"Loaded data: {df.shape}")


# Display first five rows
print("\nFirst 5 rows:")

print(df.head())


# Calculate average score and comments
average_score = df["score"].mean()

average_comments = df["num_comments"].mean()


print(
    f"\nAverage score   : {average_score:.2f}"
)

print(
    f"Average comments: {average_comments:.2f}"
)


# ---------------------------------------------------------
# NumPy statistics
# ---------------------------------------------------------

mean_score = np.mean(
    df["score"]
)

median_score = np.median(
    df["score"]
)

std_score = np.std(
    df["score"]
)


print("\n--- NumPy Stats ---")

print(
    f"Mean score   : {mean_score:.2f}"
)

print(
    f"Median score : {median_score:.2f}"
)

print(
    f"Std deviation: {std_score:.2f}"
)


# Find highest and lowest score
highest_score = np.max(
    df["score"]
)

lowest_score = np.min(
    df["score"]
)


print(
    f"Max score    : {highest_score}"
)

print(
    f"Min score    : {lowest_score}"
)


# ---------------------------------------------------------
# Category with the most stories
# ---------------------------------------------------------

category_counts = (
    df["category"]
    .value_counts()
)


most_common_category = (
    category_counts.idxmax()
)

most_common_count = (
    category_counts.max()
)


print(
    f"\nMost stories in: "
    f"{most_common_category} "
    f"({most_common_count} stories)"
)


# ---------------------------------------------------------
# Most commented story
# ---------------------------------------------------------

most_commented_index = (
    df["num_comments"].idxmax()
)


most_commented_story = (
    df.loc[
        most_commented_index,
        "title"
    ]
)


most_comments = (
    df.loc[
        most_commented_index,
        "num_comments"
    ]
)


print(
    f'\nMost commented story: '
    f'"{most_commented_story}" '
    f'— {most_comments} comments'
)


# ---------------------------------------------------------
# Add engagement column
# ---------------------------------------------------------

df["engagement"] = (
    df["num_comments"]
    / (df["score"] + 1)
)


# ---------------------------------------------------------
# Add is_popular column
# ---------------------------------------------------------

df["is_popular"] = (
    df["score"] > average_score
)


# ---------------------------------------------------------
# Save analysed data
# ---------------------------------------------------------

output_file = (
    "data/trends_analysed.csv"
)


df.to_csv(
    output_file,
    index=False
)


print(
    f"\nSaved to {output_file}"
)