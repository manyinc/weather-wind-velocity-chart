# Wind Velocity Chart

## Overview

This project contains two independent Python programs designed to process wind data. Each script serves a specific purpose and can be used independently.

## Contents

- `wind-full-resolution.py`: Processes wind data at full resolution.
- `wind-resampled.py`: Processes wind data at a resampled resolution.

## Requirements

Ensure you have the following Python packages installed:

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`

You can install the necessary packages using:

```bash
pip install numpy pandas matplotlib scipy
```

## Usage
<h2>wind-full-resolution.py</h2>
This script processes wind data at full resolution. To run this script, use the following command:

```bash
python wind-full-resolution.py
```

<h3>Functionality:</h3>
- Reads wind data from a specified input file.
- Processes the data to generate full-resolution outputs.
- Produces visualizations and statistical summaries.
  
<h2>wind-resampled.py</h2>
This script processes wind data at a resampled resolution. To run this script, use the following command:

```bash
python wind-resampled.py
```

<h3>Functionality:</h3>
- Reads wind data from a specified input file.
- Resamples the data to a lower resolution.
- Produces visualizations and statistical summaries for the resampled data.
## Input Data
Ensure your input data is in the correct format required by the scripts. Both scripts expect data files to be in CSV format with appropriate headers.

## Example
Place your wind data files in the same directory as the scripts and run the scripts as shown in the usage section. The scripts will output processed data and visualizations in the same directory.
