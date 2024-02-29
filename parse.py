import os
import re
import sys

# Regular expressions for each metric
metrics_patterns = {
    "CPU time": r"CPU time\s+:\s+([\d.]+)\s+s",
    "Memory used": r"Memory used\s+:\s+([\d.]+)\s+MB",
    "Conflict literals": r"conflict literals\s+:\s+(\d+)",
    "Propagations": r"propagations\s+:\s+(\d+)",
    "Decisions": r"decisions\s+:\s+(\d+)",
    "Conflicts": r"conflicts\s+:\s+(\d+)",
    "Restarts": r"restarts\s+:\s+(\d+)",
}

def open_and_parse_file(filename):
    sat_output = ""
    with open(filename) as f:
        lines = f.read().split("\n")
        for line in lines[::-1]:  # Reverse read to find the last occurrence
            if line.strip() == "=" * 79:  # Adjusted for precise matching
                break
            sat_output += line + "\n"

    metric_values = {}
    for metric, pattern in metrics_patterns.items():
        match = re.search(pattern, sat_output)
        if match:
            metric_values[metric] = (
                float(match.group(1))
                if metric in ["CPU time", "Memory used"]
                else int(match.group(1))
            )

    return metric_values

# Get the folder name from command line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py <folder_name>")
    sys.exit(1)

folder_name = sys.argv[1]

# Initialize a list to hold all metrics dictionaries
all_metrics = []

# Iterate over files in the folder and populate the list with metrics dictionaries
for filename in os.listdir(folder_name):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder_name, filename)
        metrics = open_and_parse_file(filepath)
        metrics["Filename"] = filename  # Add filename to metrics
        all_metrics.append(metrics)

# Calculate the sum of values for each metric across all dictionaries
metric_avgs = {metric: 0 for metric in metrics_patterns.keys()}
num_tests = len(all_metrics)

for metrics_dict in all_metrics:
    for key, value in metrics_dict.items():
        if key != 'Filename':
            metric_avgs[key] += value

# Calculate the averages for each metric
averages = {key: value / num_tests for key, value in metric_avgs.items()}

# Find worst and best results
worst_results = {metric: {'value': 0, 'filename': ""} for metric in metrics_patterns.keys()}
best_results = {metric: {'value': None, 'filename': ""} for metric in metrics_patterns.keys()}

for metrics_dict in all_metrics:
    filename = metrics_dict['Filename']
    for metric, value in metrics_dict.items():
        if metric != 'Filename':
            if worst_results[metric]['value'] is None or value > worst_results[metric]['value']:
                worst_results[metric]['value'] = value
                worst_results[metric]['filename'] = filename

            if best_results[metric]['value'] is None or value < best_results[metric]['value']:
                best_results[metric]['value'] = value
                best_results[metric]['filename'] = filename

# Print statistics
print(f"{folder_name} statistics:\n")
print("AVERAGE CASE STATISTICS: \n")
for metric, avg in averages.items():
    print(f"Average {metric}: {avg}")
    
print("---------------------------------------------")
print("WORST CASE STATISTICS: \n")
for metric, worst_data in worst_results.items():
    worst_value = worst_data['value']
    worst_file = worst_data['filename']
    print(f"Worst {metric}: {worst_value} ({worst_file})")

print("---------------------------------------------")
print("BEST CASE STATISTICS: \n")
for metric, best_data in best_results.items():
    best_value = best_data['value']
    best_file = best_data['filename']
    print(f"Best {metric}: {best_value} ({best_file})")
