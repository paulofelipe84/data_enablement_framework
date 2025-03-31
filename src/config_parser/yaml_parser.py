import yaml
from typing import Any, Dict
import logging

class YAMLParser:
    """Parser for YAML configuration files."""

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        logging.basicConfig(level=logging.INFO)

    def parse(self) -> Dict[str, Any]:
        """Parse the YAML file and return a dictionary.

        Returns:
            Dict[str, Any]: Parsed YAML configuration.
        """
        try:
            with open(self.filepath, 'r') as file:
                config = yaml.safe_load(file)
                logging.info(f"Successfully parsed YAML file: {self.filepath}")
                return config
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML file: {e}")
            raise
        except FileNotFoundError as e:
            logging.error(f"YAML file not found: {self.filepath}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise
            