import pandas as pd
import matplotlib.pyplot as plt
import os


# ---------------------------------------------------------
# 1. LOAD DATA AND SETUP
# ---------------------------------------------------------

# Load the analysed data created by Task 3
df = pd.read_csv(
    "data/trends_analysed.csv"
)


print(
    f"Loaded data: {df.shape}"
)


# Create outputs folder if it does not exist
os.makedirs(
    "outputs",
    exist_ok=True
)


# ---------------------------------------------------------
# 2. CHART 1 — TOP 10 STORIES BY SCORE
# ---------------------------------------------------------

# Sort stories by score
top_10 = (
    df.sort_values(
        "score",
        ascending=False
    )
    .head(10)
    .copy()
)


# Shorten titles longer than 50 characters
top_10["short_title"] = (
    top_10["title"].apply(
        lambda title:
        title[:50] + "..."
        if len(title) > 50
        else title
    )
)


# Reverse order so highest score appears at the top
top_10 = top_10.sort_values(
    "score",
    ascending=True
)


plt.figure(
    figsize=(10, 6)
)


plt.barh(
    top_10["short_title"],
    top_10["score"]
)


plt.title(
    "Top 10 Stories by Score"
)

plt.xlabel(
    "Score"
)

plt.ylabel(
    "Story Title"
)


plt.tight_layout()


# Save chart before show
plt.savefig(
    "outputs/chart1_top_stories.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()

plt.close()


# ---------------------------------------------------------
# 3. CHART 2 — STORIES PER CATEGORY
# ---------------------------------------------------------

category_counts = (
    df["category"]
    .value_counts()
)


plt.figure(
    figsize=(9, 6)
)


plt.bar(
    category_counts.index,
    category_counts.values
)


plt.title(
    "Stories per Category"
)

plt.xlabel(
    "Category"
)

plt.ylabel(
    "Number of Stories"
)


plt.xticks(
    rotation=30
)


plt.tight_layout()


# Save chart
plt.savefig(
    "outputs/chart2_categories.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()

plt.close()


# ---------------------------------------------------------
# 4. CHART 3 — SCORE VS COMMENTS
# ---------------------------------------------------------

# Separate popular and non-popular stories
popular = df[
    df["is_popular"] == True
]


not_popular = df[
    df["is_popular"] == False
]


plt.figure(
    figsize=(10, 6)
)


# Non-popular stories
plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)


# Popular stories
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)


plt.title(
    "Score vs Number of Comments"
)

plt.xlabel(
    "Score"
)

plt.ylabel(
    "Number of Comments"
)


plt.legend()


plt.tight_layout()


# Save chart
plt.savefig(
    "outputs/chart3_scatter.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()

plt.close()


# ---------------------------------------------------------
# 5. BONUS — TRENDPULSE DASHBOARD
# ---------------------------------------------------------

fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 11)
)


# Dashboard Chart 1
axes[0, 0].barh(
    top_10["short_title"],
    top_10["score"]
)


axes[0, 0].set_title(
    "Top 10 Stories by Score"
)

axes[0, 0].set_xlabel(
    "Score"
)

axes[0, 0].set_ylabel(
    "Story Title"
)


# Dashboard Chart 2
axes[0, 1].bar(
    category_counts.index,
    category_counts.values
)


axes[0, 1].set_title(
    "Stories per Category"
)

axes[0, 1].set_xlabel(
    "Category"
)

axes[0, 1].set_ylabel(
    "Number of Stories"
)


axes[0, 1].tick_params(
    axis="x",
    rotation=30
)


# Dashboard Chart 3
axes[1, 0].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)


axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)


axes[1, 0].set_title(
    "Score vs Number of Comments"
)

axes[1, 0].set_xlabel(
    "Score"
)

axes[1, 0].set_ylabel(
    "Number of Comments"
)


axes[1, 0].legend()


# Hide unused fourth area
axes[1, 1].axis("off")


# Overall dashboard title
fig.suptitle(
    "TrendPulse Dashboard",
    fontsize=20
)


plt.tight_layout(
    rect=[0, 0, 1, 0.96]
)


# Save dashboard
plt.savefig(
    "outputs/dashboard.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()

plt.close()


# ---------------------------------------------------------
# FINAL MESSAGE
# ---------------------------------------------------------

print(
    "\nAll visualizations created successfully!"
)


print("\nOutput files:")

print(
    "outputs/chart1_top_stories.png"
)

print(
    "outputs/chart2_categories.png"
)

print(
    "outputs/chart3_scatter.png"
)

print(
    "outputs/dashboard.png"
)