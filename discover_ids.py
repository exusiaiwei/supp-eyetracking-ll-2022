import pandas as pd
import os
import glob

def discover_ids():
    base_path = "C:\\CodeRepos\\supp-eyetracking-ll-2022\\experiment_data"
    all_files = glob.glob(os.path.join(base_path, "**", "*.*"), recursive=True)
    
    csv_files = [f for f in all_files if f.endswith('.csv')]
    excel_files = [f for f in all_files if f.endswith(('.xls', '.xlsx'))]
    
    unique_ids = set()

    for file in csv_files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')
            if 'RECORDING_SESSION_LABEL' in df.columns:
                unique_ids.update(df['RECORDING_SESSION_LABEL'].unique())
        except Exception as e:
            print(f"Could not read {file}: {e}")

    for file in excel_files:
        try:
            df = pd.read_excel(file)
            if 'RECORDING_SESSION_LABEL' in df.columns:
                unique_ids.update(df['RECORDING_SESSION_LABEL'].unique())
        except Exception as e:
            print(f"Could not read {file}: {e}")
            
    print("Unique IDs found:", sorted(list(unique_ids)))

if __name__ == "__main__":
    discover_ids()
