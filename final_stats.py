#!/usr/bin/env python3

import os
import json
import glob
import csv
from pathlib import Path

def find_latest_result_file(model_path):
    """Find the result_comparison file with the highest number in a model directory."""
    # Look for all result_comparison*.json files
    pattern = os.path.join(model_path, "result_comparison*.json")
    files = glob.glob(pattern)
    
    if not files:
        return None
    
    # Extract numbers from filenames and find the highest
    numbered_files = []
    for file in files:
        filename = os.path.basename(file)
        # Extract number from filename
        if filename == "result_comparison.json":
            numbered_files.append((0, file))
        else:
            try:
                # Extract number from result_comparison[number].json
                number_part = filename.replace("result_comparison", "").replace(".json", "")
                number = int(number_part)
                numbered_files.append((number, file))
            except ValueError:
                continue
    
    if not numbered_files:
        return None
    
    # Sort by number and get the highest
    numbered_files.sort(key=lambda x: x[0], reverse=True)
    return numbered_files[0][1]

def extract_statistics(json_file):
    """Extract true_positives, false_positives, and final_score from JSON file."""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        return {
            'true_positives': data.get('true_positives', 0),
            'false_positives': data.get('false_positives', 0),
            'final_score': data.get('final_score', 0.0)
        }
    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Error reading {json_file}: {e}")
        return None

def main():
    models_dir = "models_stats"
    output_dir = "statistics"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Dictionary to store all statistics
    all_stats = {}
    
    # Check if models directory exists
    if not os.path.exists(models_dir):
        print(f"Error: Directory '{models_dir}' not found!")
        return
    
    # Iterate through all subdirectories in models/
    for model_name in os.listdir(models_dir):
        model_path = os.path.join(models_dir, model_name)
        
        # Skip if not a directory
        if not os.path.isdir(model_path):
            continue
        
        print(f"Processing model: {model_name}")
        
        # Find the latest result_comparison file
        latest_file = find_latest_result_file(model_path)
        
        if latest_file:
            print(f"  Found file: {os.path.basename(latest_file)}")
            stats = extract_statistics(latest_file)
            
            if stats:
                all_stats[model_name] = stats
                print(f"  Extracted stats: TP={stats['true_positives']}, "
                      f"FP={stats['false_positives']}, "
                      f"Score={stats['final_score']:.4f}")
            else:
                print(f"  Failed to extract statistics")
        else:
            print(f"  No result_comparison*.json files found")
    
    # Save statistics to CSV file
    csv_output = os.path.join(output_dir, "model_statistics.csv")
    with open(csv_output, 'w', newline='') as csvfile:
        fieldnames = ['model', 'true_positives', 'false_positives', 'final_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for model, stats in all_stats.items():
            writer.writerow({
                'model': model,
                'true_positives': stats['true_positives'],
                'false_positives': stats['false_positives'],
                'final_score': stats['final_score']
            })
    
    print(f"\nStatistics saved to: {csv_output}")
    
    # Also save as JSON for easy programmatic access
    json_output = os.path.join(output_dir, "model_statistics.json")
    with open(json_output, 'w') as f:
        json.dump(all_stats, f, indent=2)
    
    print(f"Statistics also saved to: {json_output}")
    
    # Print summary
    print("\n=== SUMMARY ===")
    print(f"{'Model':<20} {'True Positives':<15} {'False Positives':<15} {'Final Score':<12}")
    print("-" * 65)
    for model, stats in sorted(all_stats.items()):
        print(f"{model:<20} {stats['true_positives']:<15} "
              f"{stats['false_positives']:<15} {stats['final_score']:<12.4f}")

if __name__ == "__main__":
    main()