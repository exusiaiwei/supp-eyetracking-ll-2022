import pandas as pd
import os
import glob

def process_data():
    base_path = "C:\\CodeRepos\\supp-eyetracking-ll-2022\\experiment_data"
    output_path = "C:\\CodeRepos\\supp-eyetracking-ll-2022\\cleaned_data"
    os.makedirs(output_path, exist_ok=True)

    id_map = {
        'h1': 'S01', 'hxq': 'S02', 'ljj': 'S03', 'lsx': 'S04', 
        'lx': 'S05', 'myw1': 'S06', 'wzc': 'S07', 'zxj': 'S08', 'zy': 'S09'
    }
    
    trial_counters = {new_id: 0 for new_id in id_map.values()}

    all_files = glob.glob(os.path.join(base_path, "**", "*.*"), recursive=True)
    all_files.sort() # Sort files to ensure consistent trial numbering

    for file in all_files:
        df = None
        original_filename = os.path.splitext(os.path.basename(file))[0]
        # Sanitize filename
        if original_filename == "ע":
            original_filename = "fixation_data"
        else:
            original_filename = original_filename.replace("(", "_").replace(")", "")

        try:
            if file.endswith('.csv'):
                df = pd.read_csv(file, on_bad_lines='skip')
            elif file.endswith('.xls'):
                df = pd.read_excel(file, engine='xlrd')
            elif file.endswith('.xlsx'):
                df = pd.read_excel(file, engine='openpyxl')
        except Exception as e:
            print(f"Skipping file {file} due to reading error: {e}")
            continue

        if df is not None and 'RECORDING_SESSION_LABEL' in df.columns:
            # Temporarily store which participants are in this file to increment counter only once per file
            participants_in_file = df['RECORDING_SESSION_LABEL'].unique()
            processed_participants_in_file = set()

            for old_id in participants_in_file:
                if old_id in id_map:
                    new_id = id_map[old_id]
                    if new_id not in processed_participants_in_file:
                        trial_counters[new_id] += 1
                        processed_participants_in_file.add(new_id)

                    participant_df = df[df['RECORDING_SESSION_LABEL'] == old_id].copy()
                    participant_df.loc[:, 'RECORDING_SESSION_LABEL'] = new_id
                    
                    output_filename = f"{new_id}_{trial_counters[new_id]}.csv"
                    output_filepath = os.path.join(output_path, output_filename)
                    participant_df.to_csv(output_filepath, index=False, encoding='utf-8')
                    print(f"Processed and saved: {output_filename}")

if __name__ == "__main__":
    process_data()
