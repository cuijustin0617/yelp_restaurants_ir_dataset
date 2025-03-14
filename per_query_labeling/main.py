import os
import shutil
from pathlib import Path
import time

from per_query_labeling.config import OUTPUT_DIR
from per_query_labeling.pipeline.pipeline import RelevancePipeline
from per_query_labeling.models.llm_client import LLMClient


def save_config_to_output_dir():
    """Save the current config file to the output directory."""
    # Get the config file path
    current_dir = Path(__file__).parent
    config_path = current_dir / "config.py"
    
    # Check if config file exists
    if not config_path.exists():
        print(f"Warning: Config file not found at {config_path}")
        return
    
    # Create destination path
    dest_path = Path(OUTPUT_DIR) / "config.py"
    
    # Copy the file
    shutil.copy2(config_path, dest_path)
    print(f"Config file saved to {dest_path}")


def main():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    # Save config file to output directory
    save_config_to_output_dir()

    # Start time
    start_time = time.time()
    
    # Initialize LLM client and pipeline
    llm_client = LLMClient()
    pipeline = RelevancePipeline(llm_client)
    ground_truth = pipeline.run()
    
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print results
    print(f"\nPipeline completed in {elapsed_time:.2f} seconds")
    print(f"Ground truth saved to {OUTPUT_DIR}/ground_truth.json")
    print(f"Processed {len(ground_truth)} queries")
    
    total_relevant = sum(len(restaurants) for restaurants in ground_truth.values())
    # print total, average, and min/max per query
    query_counts = [len(restaurants) for restaurants in ground_truth.values()]
    print(f"Total relevant: {total_relevant}")
    print(f"Average per query: {sum(query_counts) / len(query_counts):.2f}")
    print(f"Min per query: {min(query_counts)}")
    print(f"Max per query: {max(query_counts)}")
    print(f"Median per query: {sorted(query_counts)[len(query_counts) // 2]}")
    print(f"80th percentile per query: {sorted(query_counts)[int(len(query_counts) * 0.8)]}")
    print(f"20th percentile per query: {sorted(query_counts)[int(len(query_counts) * 0.2)]}")


if __name__ == "__main__":
    main()

