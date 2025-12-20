"""
Validators package for playing-cards project.
Python-first validation tooling for HTML and CSS.
"""

from pathlib import Path
from typing import List


def find_files_by_extension(directory: str, extension: str) -> List[Path]:
    """
    Find all files with given extension in a directory.

    Args:
        directory: Directory to search
        extension: File extension (e.g., 'html', 'css')

    Returns:
        List of Path objects for matching files
    """
    return list(Path(directory).glob(f"*.{extension}"))
