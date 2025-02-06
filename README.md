# Coordinate-Based-Volume-Calculator
Calculates volume using x,y, and z coordinates of an object/ body by exploiting the concept of differentiation and integration.

## Overview

This Python script reads coordinate data from an Excel file, processes it into a list of tuples, and calculates the volume of a 3D structure using the shoelace theorem and Manhattan distance.

## Requirements

- Python 3.x
- pandas
- openpyxl

## Installation

Install the required dependencies using pip: 
> pip install pandas openpyxl

#### Note: 
Place your Excel file (coordi.xlsx) in the same directory as the script.

## Usage

Run the script: 
> python script.py

## Methodology

- Reads (x, y, z) coordinates from coordi.xlsx.
- Groups four coordinates forming rectangular surfaces.
- Uses the shoelace theorem to compute the area of each surface.
- Calculates volume contributions using the average height of grouped points.
- Identifies any remaining point and includes its volume contribution.

## Output

The script prints the calculated volume in Cubic Unit.

## NOTE:
This code was originally developed by me and corrected some bugs with ChatGpt. There are still some bugs that can lead to incorrect output. Without clean and organised data, the program might give incorrect answers. But still, the program is very accurate and can work for a Big data set.

## License

This project is open-source. Feel free to use and modify it!
