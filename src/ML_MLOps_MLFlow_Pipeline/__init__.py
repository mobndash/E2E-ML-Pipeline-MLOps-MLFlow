import os
import sys
import logging

# Logging Configuration
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create logs directory if not exists
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),    # Write logs to file
        logging.StreamHandler(sys.stdout)     # Print logs to console
    ]
)

logger = logging.getLogger("ML E2E Logger")
