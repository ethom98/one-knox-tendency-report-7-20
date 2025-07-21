import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === STEP 1: Define the data ===
# Build-up zones: % initiated on Left, Center, Right for each Gameweek
build_up = pd.DataFrame({
    "Left": [46, 42, 32, 33],
    "Center": [22, 23, 34, 39],
    "Right": [38, 25, 34, 28]
}, index=["GW1", "GW2", "GW3", "GW4"])

# Attacking channels: % of final attacks on Left, Center, Right
attack = pd.DataFrame({
    "Left": [37, 34, 26, 25],
    "Center": [29, 26, 22, 23],
    "Right": [33, 30, 52, 51]
}, index=["GW1", "GW2", "GW3", "GW4"])

# === STEP 2: Transpose for cleaner heatmap layout ===
build_up_T = build_up.T
attack_T = attack.T

# === STEP 3: Create the side-by-side heatmaps ===
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Build-up Heatmap
sns.heatmap(build_up_T, annot=True, fmt=".0f", cmap="YlGnBu", cbar=True, ax=axs[0])
axs[0].set_title("Build-up Zones (%)", fontsize=14)
axs[0].set_xlabel("Zone")
axs[0].set_ylabel("Gameweek")

# Attack Heatmap
sns.heatmap(attack_T, annot=True, fmt=".0f", cmap="OrRd", cbar=True, ax=axs[1])
axs[1].set_title("Attacking Channels (%)", fontsize=14)
axs[1].set_xlabel("Zone")
axs[1].set_ylabel("Gameweek")

# === STEP 4: Final layout and save ===
plt.tight_layout()
plt.savefig("One Knox Tendency Graphic.png", dpi=300)
plt.show()
