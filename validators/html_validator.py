"""
HTML validation using html5lib.
Validates HTML5 documents for structural correctness.
"""
import sys
from pathlib import Path
from html5lib import parse
from html5lib.treewalkers import getTreeWalker


def validate_html(filepath):
    """
    Validate an HTML file for well-formedness.
    
    Args:
        filepath: Path to HTML file
        
    Returns:
        tuple: (is_valid, errors_list)
    """
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        doc = parse(content, treebuilder='etree', namespaceHTMLElements=False)
        
        if doc is None:
            errors.append("Failed to parse HTML document")
            return False, errors
            
        return True, []
        
    except FileNotFoundError:
        errors.append(f"File not found: {filepath}")
        return False, errors
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def validate_html_files(directory="."):
    """
    Validate all HTML files in a directory.
    
    Args:
        directory: Directory to search for HTML files
        
    Returns:
        dict: Validation results per file
    """
    results = {}
    html_files = list(Path(directory).glob("*.html"))
    
    for html_file in html_files:
        is_valid, errors = validate_html(html_file)
        results[str(html_file)] = {
            'valid': is_valid,
            'errors': errors
        }
    
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
        all_valid = all(r['valid'] for r in results.values())
        
        for filepath, result in results.items():
            if result['valid']:
                print(f"✓ {filepath}")
            else:
                print(f"✗ {filepath}")
                for error in result['errors']:
                    print(f"  - {error}")
        
        sys.exit(0 if all_valid else 1)
