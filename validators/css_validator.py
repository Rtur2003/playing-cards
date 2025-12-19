"""
CSS validation using cssutils.
Validates CSS files for syntax correctness.
"""
import sys
import logging
from pathlib import Path
import cssutils


cssutils.log.setLevel(logging.CRITICAL)


def validate_css(filepath):
    """
    Validate a CSS file for syntax correctness.
    
    Args:
        filepath: Path to CSS file
        
    Returns:
        tuple: (is_valid, errors_list)
    """
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parser = cssutils.CSSParser(raiseExceptions=False)
        sheet = parser.parseString(content)
        
        if sheet is None:
            errors.append("Failed to parse CSS document")
            return False, errors
        
        return True, []
        
    except FileNotFoundError:
        errors.append(f"File not found: {filepath}")
        return False, errors
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def validate_css_files(directory="."):
    """
    Validate all CSS files in a directory.
    
    Args:
        directory: Directory to search for CSS files
        
    Returns:
        dict: Validation results per file
    """
    results = {}
    css_files = list(Path(directory).glob("*.css"))
    
    for css_file in css_files:
        is_valid, errors = validate_css(css_file)
        results[str(css_file)] = {
            'valid': is_valid,
            'errors': errors
        }
    
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
        all_valid = all(r['valid'] for r in results.values())
        
        for filepath, result in results.items():
            if result['valid']:
                print(f"✓ {filepath}")
            else:
                print(f"✗ {filepath}")
                for error in result['errors']:
                    print(f"  - {error}")
        
        sys.exit(0 if all_valid else 1)
