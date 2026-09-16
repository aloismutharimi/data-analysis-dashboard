#Project: Data Analysis Report
#Analyzing 28 days of SMP Member fitness data using Pandas and NumPy
#Skills - loading and inspecting data, filtering, grouping, computing statistics, and producing a structured report
#What to Build:
#Load a 28-day fitness log into a DataFrame
#Inspect and clean the data (handle missing values)
#Filter for high-performance days and specific protocols
#Group by fasting protocol to compare average metrics
#Compute NumPy statistics on key columns
#Output a formatted weekly and monthly summary report

#Step 1 - Loading and Inspecting the Data
#Load 28 days of data. Inspect shape, data types, and check for missing values
import pandas as pd
import numpy as np

#Data
steps_list = [
        9200, 10300, 9900, 10700, 11000, 7900, 8700,
        8800, 9900, 10300, 7800, 12100, 9800, 11400,
        9600, 8500, 10600, 10400, 11100, 9200, 10100,
        10300, 8900, 10500, 10900, 12400, 8900, 9800
    ]

sleep_hrs_list = [
        8.0, 7.5, 7.0, 6.5, 8.0, 9.0, 7.5,
        7.5, 8.5, 6.5, 8.0, 8.5, 9.0, 7.0,
        8.5, 7.0, 9.0, 8.5, 7.5, 6.5, 7.5,
        8.0, 8.5, 7.0, 6.5, 7.5, 8.0, 8.5
    ]

bench_press_kg_list = [
        82, 80, 75, 78, 84, 82, 76,
        78, 81, 82, 78, 84, 77, 88,
        82, 76, 74, 84, 84, 86, 80,
        78, 83, 77, 85, 74, 74, 86
    ]

protocols_list = ([
        'OMAD', '2MAD', '2MAD', 'OMAD', 'OMAD', 'OMAD', '2MAD'
    ] * 4)

water_list = [
        6, 7, 8, 9, 6, 9, 7,
        7, 9, 8, 6, 7, 8, 7,
        9, 8, 7, 9, 6, 8, 6,
        9, 7, 6, 8, 8, 9, 8
    ]

df = pd.DataFrame({
    "day": list(range(1, 29)),
    "steps": steps_list,
    "sleep_hrs": sleep_hrs_list,
    "bench_press_kg": bench_press_kg_list,
    "protocols": protocols_list,
    "water": water_list
})

steps = np.array(steps_list)
bench_press_kg = np.array(bench_press_kg_list)

W = 54
print("=" * W)
print("SMP 28-DAY FITNESS ANALYSIS REPORT")
print("=" * W)

#Overall stats
print(f"OVERALL METRICS")
print(f"{'Days Tracked:':<25} 28")
print(f"{'Total Steps:':<25} {steps.sum():,}")
print(f"{'Average Daily Steps':<25} {steps.mean():,.0f}")
print(f"{'Days Hitting 10K:':<25} {(steps >= 10000).sum()}/28 ({(steps >= 10000).mean()*100:.0f}%)")
print(f"{'Average Sleep:':<25} {np.mean(sleep_hrs_list):.1f} hours")
print(f"{'Bench Press Range:':<25} {bench_press_kg.min()} to {bench_press_kg.max()} kg")
print(f"{'Bench Press Trend':<25} +{bench_press_kg[-7:].mean() -bench_press_kg[:7].mean():.1f} kg (wk1 to wk4) kg")

#Week by week analysis
print(f"\nWEEKLY BREAKDOWN")
print(f"{'Week':<8} {'Average Steps':<15} {'10K+ Days':<12} {'Average Press':>8}")
print(f"{'-' * 54}")

for wk in range(4):
    s = steps[wk*7:(wk+1)*7]
    b = bench_press_kg[wk*7:(wk+1)*7]
    hits = (s >= 10000).sum()
    print(f"Week {wk+1:<3} {s.mean():>12,.0f} {hits:>8}/7 {b.mean():>9.1f} kg")

#Protocol breakdown
print(f"\nPROTOCOL COMPARISON")
protocol_stats = df.groupby('protocols')[['steps', 'sleep_hrs', 'bench_press_kg']].mean().round(1)

for protocol, row in protocol_stats.iterrows():
    print(f"{protocol}: average steps = {row['steps']:,.0f}, sleep = {row['sleep_hrs']} hours, bench press = {row['bench_press_kg']} kg")

#Top days
top3 = df.nlargest(3, 'steps')
print(f"\nTOP 3 STEP DAYS")
for _, row in top3.iterrows():
    print(f"Day {int(row['day']):2d}: {int(row['steps']):,} steps ({row['protocols']})")

print(f"\n{'=' * W}")

