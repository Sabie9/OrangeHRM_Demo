import logging  # Imports the logging module, which handles recording messages (logs) during program execution

class LogGen:
    # A class to generate and manage loggers; 'LogGen' is short for "Logger Generator"

    @staticmethod
    def log_gen():
        # A static method (no need for a class instance) to create and return a configured logger
        # Purpose: Sets up logging to write messages to a file named 'automation.log'

        # Configure the root logger with basic settings
        # - filename: Specifies where logs will be written (".\\Logs\\automation.log" is a file in the Logs folder)
        # - format: Defines how each log message looks (timestamp : level : message)
        # - datefmt: Sets the timestamp format (e.g., "02/25/2025 03:45:12 PM")
        # - level: Sets the minimum severity of messages to log (INFO includes INFO, WARNING, ERROR, CRITICAL)
        # - force: Resets any existing handlers on the root logger, ensuring this configuration takes full control
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO,
                            force=True)

        # Get the root logger, which is the default logger for the entire program
        # The root logger is now configured by basicConfig to write to the file with the specified format
        logger = logging.getLogger()

        # This line is commented out because the level is already set in basicConfig
        # Setting it here would be redundant and could override the configuration if done differently
        # logger.setLevel(logging.INFO)

        # Return the configured logger so it can be used elsewhere (e.g., in your tests)
        return logger