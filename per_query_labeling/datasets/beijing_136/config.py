"""Configuration settings for the restaurant query relevance pipeline."""
import os
from pathlib import Path

DOMAIN = "hotel"

# File paths
BASE_DIR = Path(__file__).parent.parent  # root directory
QUERIES_PATH = BASE_DIR / "queries/queries_hotel_v2.txt"
DOCS_DIR = BASE_DIR / "data/docs/beijing_hotels/docs_136"
OUTPUT_DIR = BASE_DIR / "per_query_labeling/datasets/beijing_136"

# Create output directories
SUMMARIES_DIR = Path(OUTPUT_DIR) / "summaries"
RELEVANCE_DIR = Path(OUTPUT_DIR) / "relevance"
GROUND_TRUTH_PATH = Path(OUTPUT_DIR) / "ground_truth.json"

# LLM settings
LLM_PROVIDER = "gemini"  # Options: openai, deepseek, gemini
LLM_MODEL = "gemini-2.0-flash"

# Provider-specific API keys - using environment variables
#OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
#DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

MAX_RETRIES = 8  # Max retries for LLM calls
