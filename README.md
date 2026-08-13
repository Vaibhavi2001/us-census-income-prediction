# U.S. Census Income Prediction

## Project Overview

This project uses the American Community Survey Public Use Microdata Sample (ACS PUMS) to examine whether demographic and employment-related characteristics can be used to predict personal income.

The project includes data preparation, exploratory data analysis, visualization, predictive modeling, and evaluation of three regression algorithms.

## Research Question

Can an individual's total personal income be predicted using demographic and employment-related characteristics?

## Dataset

The analysis uses person-level ACS PUMS data from the U.S. Census Bureau. The source dataset contains approximately 33,000 observations and 290 variables.

Dataset source: [U.S. Census Bureau ACS PUMS](https://www.census.gov/programs-surveys/acs/microdata.html)

The raw dataset is not included in this repository. To run the notebook, download the relevant person-level PUMS CSV file and save it as `psam_p02.csv` in the project directory.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Workflow

- Loaded and inspected the Census microdata
- Selected demographic and employment-related variables
- Handled missing values
- Explored income distributions and relationships
- Created data visualizations
- Split the data into training and testing sets
- Developed three regression models
- Compared model performance using MAE, RMSE, and R²

## Models and Results

| Model | MAE (USD) | RMSE (USD) | R² |
|---|---:|---:|---:|
| Linear Regression | 27,077.50 | 47,346.38 | 0.279 |
| Random Forest | 25,314.33 | 47,054.87 | 0.288 |
| Gradient Boosting | 24,116.14 | 45,172.67 | 0.344 |

Gradient Boosting demonstrated the strongest overall performance, producing the lowest prediction errors and the highest R² value. The results suggest that personal income may also depend on factors not included in the model, such as education, occupation, industry, geographic location, and work experience.

## Repository Contents

- `us_census_income_analysis.ipynb` – complete analysis and modeling workflow
- `data_utils.py` – functions used to load, clean, and prepare the data
- `requirements.txt` – Python libraries required to run the project

## How to Run the Project

1. Download the person-level ACS PUMS data from the U.S. Census Bureau.
2. Save the dataset as `psam_p02.csv` in the project directory.
3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
