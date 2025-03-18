import logging
import os
from datetime import datetime


# Create logs which is volume
LOG_PATH = os.path.join("/app", "data", "logs")
os.makedirs(LOG_PATH, exist_ok=True)

# Generate unique log filename with timestamp.
timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%s")
log_file_name = os.path.join(LOG_PATH, f"run_{timestamp}.log")

# Configure logging.
logging.basicConfig(
    filename=log_file_name,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.info("Start of script.")
logging.info("Test message.")
logging.info("End of script.")

