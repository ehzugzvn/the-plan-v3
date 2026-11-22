"""Entry program: writes the plan text to entry.txt."""

import os

PLAN = (
    "Day 1: join Synmerco and make.fun as an agent. Watch both job feeds 24/7 "
    "and bid within 5 minutes on every data-research job ($3-15, escrow-paid): "
    "SEC filings, recall lists, public datasets. Deliver in under 1 hour. "
    "Reinvest pay into more bids. Likely $100 -> $1,200+ in 30 days."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
