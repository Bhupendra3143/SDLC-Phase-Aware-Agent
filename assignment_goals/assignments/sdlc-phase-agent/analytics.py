from typing import Counter
import pandas as pd
import matplotlib.pyplot as plt

from storage import load_requests

KEYWORDS = ["login", "database", "test"]


def analyze_requests():
    requests = load_requests()
    if not requests:
        print("No requests here...")
        return

    df = pd.DataFrame(requests)
    df["length"] = df["description"].str.len()
    
    print("\nTotal requests:", len(df))
    print(f"Mean length of each request: {df["length"].mean()}")

    word_counts = Counter(" ".join(df["description"]).lower().split())
    print("\nKeyword frequency:")
    for k in KEYWORDS:
        print(k, ":", word_counts.get(k, 0))

    counts = {k: word_counts.get(k, 0) for k in KEYWORDS}
    plt.bar(counts.keys(), counts.values())
    plt.title("Keyword Frequency")
    plt.savefig("charts/keywords.png")
    print("Analysis completed successfully: Chart saved in charts/keywords.png")