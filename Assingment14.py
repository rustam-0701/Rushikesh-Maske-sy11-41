import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

# Demonstrate different logging levels
logging.debug("This is a debug message.")
logging.info("Program started successfully.")
logging.warning("This is a warning message.")
logging.error("An error occurred.")
logging.critical("This is a critical message.")

print("Logging demonstration completed.")