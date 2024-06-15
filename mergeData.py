# integrate_sensors.py
import pandas as pd

def integrate_sensor_data(accelerometer_path, gyroscope_path, location_path, magnetometer_path, output_path):
    # Load each dataset
    accelerometer_df = pd.read_csv(accelerometer_path)
    gyroscope_df = pd.read_csv(gyroscope_path)
    location_df = pd.read_csv(location_path)
    magnetometer_df = pd.read_csv(magnetometer_path)
    
    # Merge datasets on the 'Time (s)' column
    merged_df = pd.merge_asof(accelerometer_df, gyroscope_df, on='Time (s)', suffixes=('_acc', '_gyro'))
    merged_df = pd.merge_asof(merged_df, location_df, on='Time (s)', suffixes=('', '_loc'))
    merged_df = pd.merge_asof(merged_df, magnetometer_df, on='Time (s)', suffixes=('', '_mag'))
    
    # Check if activities match across different sensors
    activity_columns = ['Activity_acc', 'Activity_gyro', 'Activity', 'Activity_mag']
    merged_df['Activity'] = merged_df[activity_columns].apply(lambda row: row.iloc[0] if all(row == row.iloc[0]) else 'unknown', axis=1)
    
    # Remove rows where Activity is 'unknown'
    merged_df = merged_df[merged_df['Activity'] != 'unknown']
    
    # Drop the redundant activity columns
    merged_df.drop(columns=[col for col in activity_columns if col != 'Activity'], inplace=True)
    
    # Save the merged dataframe to a CSV file
    merged_df.to_csv(output_path, index=False)

# Example usage:
integrate_sensor_data('merged_Accelerometer_labeled.csv', 'merged_Gyroscope_labeled.csv', 'merged_Location_labeled.csv', 'merged_Magnetometer_labeled.csv', 'integrated_sensor_data.csv')
