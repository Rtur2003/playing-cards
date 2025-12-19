#!/usr/bin/env python3
"""
Main validation runner for playing-cards project.
Orchestrates HTML and CSS validation with Python-first approach.
"""
import sys
from pathlib import Path

from validators.css_validator import validate_css_files
from validators.html_validator import validate_html_files


def run_validations(directory="."):
    """
    Run all validations on project files.

    Args:
        directory: Root directory to validate

    Returns:
        bool: True if all validations pass
    """
    print("=" * 60)
    print("Playing Cards - Python Validation Suite")
    print("=" * 60)

    all_valid = True

    print("\n[HTML Validation]")
    html_results = validate_html_files(directory)

    for filepath, result in html_results.items():
        if result["valid"]:
            print(f"  ✓ {filepath}")
        else:
            print(f"  ✗ {filepath}")
            for error in result["errors"]:
                print(f"    - {error}")
            all_valid = False

    print("\n[CSS Validation]")
    css_results = validate_css_files(directory)

    for filepath, result in css_results.items():
        if result["valid"]:
            print(f"  ✓ {filepath}")
        else:
            print(f"  ✗ {filepath}")
            for error in result["errors"]:
                print(f"    - {error}")
            all_valid = False

    print("\n" + "=" * 60)
    if all_valid:
        print("✓ All validations passed")
        print("=" * 60)
        return True
    else:
        print("✗ Some validations failed")
        print("=" * 60)
        return False


if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    success = run_validations(directory)
    sys.exit(0 if success else 1)
