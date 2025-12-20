"""
HTML validation using html5lib.
Validates HTML5 documents for structural correctness.
"""

import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

from html5lib import parse
from html5lib.treewalkers import getTreeWalker

from validators import find_files_by_extension


def validate_html(filepath: str) -> Tuple[bool, List[str]]:
    """
    Validate an HTML file for well-formedness.

    Args:
        filepath: Path to HTML file

    Returns:
        tuple: (is_valid, errors_list)
    """
    errors: List[str] = []

    # Input validation: ensure filepath is provided and valid
    if filepath == "" or (isinstance(filepath, str) and not filepath.strip()):
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

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        doc = parse(content, treebuilder="etree", namespaceHTMLElements=False)

        if doc is None:
            errors.append("Failed to parse HTML document")
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


def validate_html_files(directory: str = ".") -> Dict[str, Dict[str, Any]]:
    """
    Validate all HTML files in a directory.

    Args:
        directory: Directory to search for HTML files

    Returns:
        dict: Validation results per file
    """
    results: Dict[str, Dict[str, Any]] = {}
    html_files = find_files_by_extension(directory, "html")

    for html_file in html_files:
        is_valid, errors = validate_html(str(html_file))
        results[str(html_file)] = {"valid": is_valid, "errors": errors}

    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        is_valid, errors = validate_html(filepath)

        if is_valid:
            print(f"✓ {filepath} is valid")
            sys.exit(0)
        else:
            print(f"✗ {filepath} has errors:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
    else:
        results = validate_html_files()
        all_valid = all(r["valid"] for r in results.values())

        for filepath, result in results.items():
            if result["valid"]:
                print(f"✓ {filepath}")
            else:
                print(f"✗ {filepath}")
                for error in result["errors"]:
                    print(f"  - {error}")

        sys.exit(0 if all_valid else 1)
