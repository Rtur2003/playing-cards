#!/usr/bin/env python3
"""
Build pipeline for playing-cards project.
Python-first automation for validation and quality checks.
"""
import subprocess
import sys
from pathlib import Path

# Python files to check in validation
PYTHON_FILES = ["validators/", "validate.py", "setup_dev.py", "build.py"]


def run_step(name, command, required=True):
    """
    Execute a build step.

    Args:
        name: Step name for logging
        command: Command to execute
        required: Whether failure should stop the build

    Returns:
        bool: Success status
    """
    print(f"\n→ {name}")
    print("-" * 60)

    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

        print(f"✓ {name} passed")
        return True

    except subprocess.CalledProcessError as e:
        print(f"✗ {name} failed")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)

        if required:
            print(f"\nBuild failed at: {name}")
            return False
        return True


def build():
    """Execute complete build pipeline."""
    print("=" * 60)
    print("Playing Cards - Build Pipeline")
    print("=" * 60)

    python_files_str = " ".join(PYTHON_FILES)
    steps = [
        ("HTML Validation", "python validate.py", True),
        (
            "Python Code Format Check",
            f"python -m black --check {python_files_str}",
            False,
        ),
        (
            "Python Import Order Check",
            f"python -m isort --check {python_files_str}",
            False,
        ),
    ]

    all_success = True

    for name, command, required in steps:
        success = run_step(name, command, required)
        if required and not success:
            all_success = False
            break
        elif not success:
            all_success = False

    print("\n" + "=" * 60)
    if all_success:
        print("✓ Build completed successfully")
        print("=" * 60)
        return True
    else:
        print("✗ Build completed with errors")
        print("=" * 60)
        return False


if __name__ == "__main__":
    success = build()
    sys.exit(0 if success else 1)
