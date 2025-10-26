import pandas as pd

def load_data(file):
    try:
        # Try UTF-8 first
        df = pd.read_csv(file)
    except UnicodeDecodeError:
        # Fallback for non-UTF-8 files (Excel exports etc.)
        df = pd.read_csv(file, encoding="latin1")
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")
    return df
