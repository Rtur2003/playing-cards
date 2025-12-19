# Playing Cards

A professional playing cards display built with HTML5 and CSS3 Flexbox, featuring Python-first validation and development tooling.

## Features

### Display
- Multiple playing cards with classic layout (Ace, King, Queen, Jack, 10)
- Flexbox-based responsive design
- Card symbols: ♠ (spades), ♣ (clubs), ♥ (hearts), ♦ (diamonds)
- Smooth hover animations and visual feedback
- RTL (right-to-left) language support

### Professional Tooling
- Python-based HTML/CSS validation
- Automated code formatting (Black, isort)
- Pre-commit hooks for quality assurance
- GitHub Actions CI/CD pipeline
- Comprehensive development environment

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

```bash
# Clone the repository
git clone https://github.com/Rtur2003/playing-cards.git
cd playing-cards

# Run automated setup
python setup_dev.py

# Validate project
python validate.py
```

### Development Commands

```bash
make help          # Show all available commands
make dev-install   # Install development dependencies
make validate      # Run HTML/CSS validation
make format        # Format Python code
make lint          # Check code style
make pre-commit    # Install git hooks
```

## Project Structure

```
playing-cards/
├── index.html              # Main HTML page
├── style.css               # Flexbox-based styling
├── validators/             # Python validation modules
│   ├── __init__.py
│   ├── html_validator.py  # HTML5 validation
│   └── css_validator.py   # CSS syntax validation
├── validate.py             # Validation runner
├── build.py                # Build pipeline
├── setup_dev.py            # Developer setup automation
├── Makefile                # Development workflows
├── pyproject.toml          # Python project config
├── requirements-dev.txt    # Development dependencies
├── .editorconfig           # Editor configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── .github/workflows/      # CI/CD configuration
```

## Technical Details

### HTML Structure
- Semantic HTML5 with proper `lang` and `dir` attributes
- `#playing-cards` container uses flexbox
- `.card` elements use flexbox with `justify-content: space-between`
- `.left`, `.middle`, `.right` sections with appropriate alignment

### CSS Implementation
- Flexbox for layout and card positioning
- CSS3 transforms for visual effects
- Responsive gap-based spacing
- Color-coded suits (red for hearts/diamonds)

### Validation
The project uses Python-first validation:
- **html5lib** for HTML5 structural validation
- **cssutils** for CSS syntax validation
- Automated checks in pre-commit hooks and CI

## Demo

View the project live: [https://rtur2003.github.io/playing-cards/](https://rtur2003.github.io/playing-cards/)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines and workflow.

## License

See [LICENSE](LICENSE) for details.
