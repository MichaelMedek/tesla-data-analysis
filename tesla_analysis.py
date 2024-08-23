import pandas as pd
import matplotlib.pyplot as plt
import os

pd.set_option('display.max_rows', 5)

folder = r"C:\Users\I558807\Downloads\Vehicle Data Felix"
for path in sorted(os.listdir(folder)):
    if not path.endswith('.csv'):
        continue
    path = os.path.join(folder, path)
    
    print(path)
    # path=r"C:\Users\I558807\Downloads\Vehicle Data Felix\2023-09-09.csv"

    df = pd.read_csv(path, low_memory=False)

    # Parse the DATE (UTC) column to datetime
    df['DATE (UTC)'] = pd.to_datetime(df['DATE (UTC)'])

    # Define the columns to plot
    columns_to_plot = [
        'Vehicle Speed (kph) (Positive is forward direction)',
        'Cruise Control Set Speed (mph / kph) (or Traffic Aware Cruise Control Set Speed if vehicle equipped with Autopilot hardware)',
        'Longitudinal Acceleration (m/s^2) (positive indicates forward)',
        'Lateral Acceleration (m/s^2) (positive indicates acceleration to vehicle left)',
        'Vehicle vertical acceleration (positive up) (m/s^2)',
        'Vehicle Yaw Rate (Positive indicates left turn)',
        'Vehcle pitch rate (positive when the nose pitches down) (rad/s)',
        'Primary Steering Angle Sensor (degrees) (Positive indicates right turn)',
        'Accelerator Pedal Position (%)',
        'Brake Master Cylinder Pressure (bar)',
        'Brake Pedal Application',
    ]

    # Create subplots with individual x-axes
    fig, axs = plt.subplots(len(columns_to_plot), 1, figsize=(14, 20), sharex=True)

    # Plot each column
    for ax, col in zip(axs, columns_to_plot):
        if col not in df.columns:
            print(f"Column {col} not found in the data")
            continue
        df_sub = df[df[col].notna()]
        
        assert len(df_sub) > 0, f"No data to plot for column {col}"
        ax.plot(df_sub['DATE (UTC)'], pd.to_numeric(df_sub[col], errors='coerce'), 'r.')
        ax.set_title(col)
        ax.set_xlabel('DATE (UTC)')
        ax.grid(True)

    # Ensure the layout is tight and plots are not overlapping
    plt.tight_layout()

    # Show plot
    plt.savefig(path.replace('.csv', '.png'))
    plt.close()