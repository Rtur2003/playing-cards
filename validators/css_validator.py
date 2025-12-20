"""
CSS validation using cssutils.
Validates CSS files for syntax correctness.
"""

import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import cssutils

from validators import find_files_by_extension


def validate_css(
    filepath: str, log_level: int = logging.CRITICAL
) -> Tuple[bool, List[str]]:
    """
    Validate a CSS file for syntax correctness.

    Args:
        filepath: Path to CSS file
        log_level: Logging level for cssutils (default: CRITICAL)

    Returns:
        tuple: (is_valid, errors_list)
    """
    errors: List[str] = []

    # Input validation: ensure filepath is provided and valid
    if not filepath.strip():
        errors.append("Filepath cannot be empty")
        return False, errors

    try:
        path = Path(filepath)

        # Safety: check file exists before attempting to open
        if not path.exists():
            errors.append(f"File not found: {filepath}")
            return False, errors

        # Safety: verify it's a file, not a directory
        if not path.is_file():
            errors.append(f"Path is not a file: {filepath}")
            return False, errors

        with path.open("r", encoding="utf-8") as f:
            content = f.read()

        cssutils.log.setLevel(log_level)
        parser = cssutils.CSSParser(raiseExceptions=False)
        sheet = parser.parseString(content)

        if sheet is None:
            errors.append("Failed to parse CSS document")
            return False, errors

        return True, []

    except PermissionError:
        errors.append(f"Permission denied: {filepath}")
        return False, errors
    except UnicodeDecodeError:
        errors.append(f"Invalid UTF-8 encoding in file: {filepath}")
        return False, errors
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def validate_css_files(directory: str = ".") -> Dict[str, Dict[str, Any]]:
    """
    Validate all CSS files in a directory.

    Args:
        directory: Directory to search for CSS files

    Returns:
        dict: Validation results per file
    """
    results: Dict[str, Dict[str, Any]] = {}
    css_files = find_files_by_extension(directory, "css")

    for css_file in css_files:
        is_valid, errors = validate_css(str(css_file))
        results[str(css_file)] = {"valid": is_valid, "errors": errors}

    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        is_valid, errors = validate_css(filepath)

        if is_valid:
            print(f"✓ {filepath} is valid")
            sys.exit(0)
        else:
            print(f"✗ {filepath} has errors:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
    else:
        results = validate_css_files()
        all_valid = all(r["valid"] for r in results.values())

        for filepath, result in results.items():
            if result["valid"]:
                print(f"✓ {filepath}")
            else:
                print(f"✗ {filepath}")
                for error in result["errors"]:
                    print(f"  - {error}")

        sys.exit(0 if all_valid else 1)
