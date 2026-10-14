"""
Personal Finance Visualiser
Assignment: Charts and Visualisation with Matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

print("=" * 62)
print("       💰 PERSONAL FINANCE VISUALISER")
print("=" * 62)

# ── STEP 1 — DATASET SETUP ────────────────────────────────────
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Monthly Income and Expenses (£)
income = [3000, 3000, 3100, 3000, 3200, 3000, 3000, 3150, 3000, 3000, 3200, 3500]
expenses = [2400, 2200, 2600, 2300, 2500, 2100, 2300, 2450, 2200, 2350, 2700, 2900]
savings = [inc - exp for inc, exp in zip(income, expenses)]

# Expense Categories across 4 Quarters (Housing, Food, Transport, Other)
housing = [7200, 7200, 7200, 7200]
food = [1350, 1400, 1450, 1500]
transport = [600, 650, 700, 750]
other = [900, 850, 950, 1000]

print(f"\n📂 Dataset initialized with {len(months)} months of financial data.")

# ── STEP 2 — CREATE THE 2x2 FIGURE LAYOUT ─────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Personal Finance Dashboard — 2024", fontsize=16, fontweight="bold")
fig.patch.set_facecolor("#f8f9fa")

ax1 = axes[0][0]  # Income vs Expenses line chart
ax2 = axes[0][1]  # Monthly savings bar chart
ax3 = axes[1][0]  # Grouped bar — expense categories
ax4 = axes[1][1]  # Cumulative savings area chart

# ── STEP 3 — PANEL 1: INCOME VS EXPENSES LINE CHART ───────────
ax1.plot(months, income, marker="o", label="Income", color="steelblue", linewidth=2)
ax1.plot(months, expenses, marker="s", label="Expenses", color="tomato", linewidth=2)
ax1.set_title("Income vs Expenses Trend", fontweight="bold")
ax1.set_xlabel("Month")
ax1.set_ylabel("Amount (£)")

# Currency formatter for y-axis
formatter = mticker.FuncFormatter(lambda x, _: f"£{x:,.0f}")
ax1.yaxis.set_major_formatter(formatter)

ax1.tick_params(axis="x", rotation=45)
ax1.legend(loc="upper left")
ax1.grid(alpha=0.3)
ax1.set_facecolor("white")

# ── STEP 4 — PANEL 2: MONTHLY SAVINGS BAR CHART ───────────────
colors = ["green" if s > 0 else "red" for s in savings]
ax2.bar(months, savings, color=colors, edgecolor="white")
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_title("Monthly Savings", fontweight="bold")
ax2.set_xlabel("Month")
ax2.set_ylabel("Savings (£)")
ax2.yaxis.set_major_formatter(formatter)
ax2.tick_params(axis="x", rotation=45)
ax2.grid(alpha=0.3)
ax2.set_facecolor("white")

# ── STEP 5 — PANEL 3: GROUPED BAR — EXPENSE CATEGORIES ────────
x = np.arange(4)  # 4 quarters
width = 0.2

ax3.bar(x - 1.5 * width, housing, width, label="Housing", color="#34495e")
ax3.bar(x - 0.5 * width, food, width, label="Food", color="#e67e22")
ax3.bar(x + 0.5 * width, transport, width, label="Transport", color="#f1c40f")
ax3.bar(x + 1.5 * width, other, width, label="Other", color="#9b59b6")

ax3.set_title("Expense Categories by Quarter", fontweight="bold")
ax3.set_xlabel("Quarter")
ax3.set_ylabel("Amount (£)")
ax3.set_xticks(x)
ax3.set_xticklabels(["Q1", "Q2", "Q3", "Q4"])
ax3.yaxis.set_major_formatter(formatter)
ax3.legend(fontsize=8)
ax3.grid(alpha=0.3)
ax3.set_facecolor("white")

# ── STEP 6 — PANEL 4: CUMULATIVE SAVINGS AREA CHART ───────────
cum_savings = [sum(savings[: i + 1]) for i in range(len(savings))]
ax4.fill_between(months, cum_savings, alpha=0.4, color="teal")
ax4.plot(months, cum_savings, color="teal", linewidth=2, marker="o", markersize=4)
ax4.set_title("Cumulative Savings Growth", fontweight="bold")
ax4.set_xlabel("Month")
ax4.set_ylabel("Cumulative Savings (£)")
ax4.yaxis.set_major_formatter(formatter)
ax4.tick_params(axis="x", rotation=45)
ax4.grid(alpha=0.3)
ax4.set_facecolor("white")

# ── STEP 7 — STYLE AND SAVE ───────────────────────────────────
plt.tight_layout()
plt.savefig("finance_dashboard.png", dpi=150, bbox_inches="tight")
print("  ✅ Saved figure as: finance_dashboard.png")
plt.show()

print("=" * 62)