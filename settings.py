"""
This module provides a dictionary of ANSI color codes.

Attributes:
    COLORS (dict): A dictionary mapping color names to their corresponding ANSI escape codes.
        - "yellow"
        - "blue"
        - "red"
        - "green"
        - "reset"
"""

COLORS = {
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "red": "\033[91m",
    "green": "\033[92m",
    "reset": "\033[0m"
}
