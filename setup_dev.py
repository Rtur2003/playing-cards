#!/usr/bin/env python3
"""
Developer setup script for playing-cards project.
Python-first automation for onboarding and environment configuration.
"""
import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Execute a command and report status."""
    print(f"\n→ {description}...")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        print(f"  ✓ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ {description} failed")
        if e.stderr:
            print(f"  Error: {e.stderr}")
        return False


def check_python_version():
    """Verify Python version meets requirements."""
    print("Checking Python version...")
    if sys.version_info < (3, 8):
        print("  ✗ Python 3.8+ required")
        return False
    print(f"  ✓ Python {sys.version_info.major}.{sys.version_info.minor}")
    return True


def setup_environment():
    """Set up development environment."""
    print("=" * 60)
    print("Playing Cards - Developer Setup")
    print("=" * 60)
    
    if not check_python_version():
        return False
    
    steps = [
        ("pip install --upgrade pip", "Upgrade pip"),
        ("pip install -r requirements-dev.txt", "Install development dependencies"),
        ("pre-commit install", "Install pre-commit hooks"),
    ]
    
    for cmd, description in steps:
        if not run_command(cmd, description):
            print("\n✗ Setup failed")
            return False
    
    print("\n" + "=" * 60)
    print("✓ Development environment ready")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Run 'make validate' to check HTML/CSS")
    print("  2. Run 'make help' to see available commands")
    print("  3. Check .editorconfig for code style settings")
    return True


if __name__ == "__main__":
    success = setup_environment()
    sys.exit(0 if success else 1)
