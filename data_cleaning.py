import pandas as pd

def load_data(file_path):
    """Load the raw CSV data."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the data by handling missing values and standardizing columns."""
    # Drop rows with missing critical data
    df_clean = df.dropna(subset=['player_id', 'tracking_time'])
    
    # Fill missing values in non-critical columns
    df_clean.fillna(method='ffill', inplace=True)
    
    # Convert tracking_time to datetime format
    if 'tracking_time' in df_clean.columns:
        df_clean['tracking_time'] = pd.to_datetime(df_clean['tracking_time'], errors='coerce')
    
    # Further cleaning: remove rows with invalid data if necessary
    df_clean = df_clean[df_clean['tracking_time'].notnull()]
    
    return df_clean

def save_data(df, output_path):
    """Save the cleaned data to CSV."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}.")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    # Define file paths
    raw_data_path = "raw_data.csv"  # Replace with your actual raw data file
    output_path = "cleaned_data.csv"
    
    # Load data
    df = load_data(raw_data_path)
    if df is not None:
        # Clean data
        cleaned_df = clean_data(df)
        # Save cleaned data
        save_data(cleaned_df, output_path)
