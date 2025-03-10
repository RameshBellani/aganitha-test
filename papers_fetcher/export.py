import pandas as pd
from typing import List, Dict

def export_to_csv(papers: List[Dict], filename: str = "output.csv"):
    """Exports filtered papers to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")
