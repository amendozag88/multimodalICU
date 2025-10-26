# multimodalICU.amendozag88.github.io

GitHub Pages site showcasing interactive visualizations for multimodal ICU data analysis.

## Overview

This site displays interactive HTML elements created with Python and Plotly, demonstrating various ICU data visualizations including:

- **Time Series Analysis**: Interactive plots of patient vital signs over time
- **Patient Demographics**: Distribution of patient demographics and outcomes
- **Correlation Matrix**: Interactive heatmap showing relationships between clinical variables

## Viewing the Site

Visit the live site at: [https://amendozag88.github.io/multimodalICU.amendozag88.github.io/](https://amendozag88.github.io/multimodalICU.amendozag88.github.io/)

## Local Development

### Prerequisites

- Python 3.x
- Required packages: `plotly`, `pandas`, `numpy`

### Installation

```bash
pip install plotly pandas numpy
```

### Generating Visualizations

To regenerate the interactive visualizations:

```bash
python3 generate_visualizations.py
```

This will create/update HTML files in the `visualizations/` directory.

### Viewing Locally

Simply open `index.html` in your web browser to view the site locally.

## Project Structure

```
.
├── index.html                      # Main landing page
├── styles.css                      # Stylesheet
├── generate_visualizations.py      # Script to generate Plotly visualizations
├── visualizations/                 # Generated interactive HTML visualizations
│   ├── timeseries.html
│   ├── demographics.html
│   └── correlation.html
└── README.md
```

## Technologies Used

- **Python**: Data generation and processing
- **Plotly**: Interactive visualization library
- **HTML/CSS**: Web page structure and styling
- **GitHub Pages**: Hosting

## License

This project is open source and available for educational purposes.