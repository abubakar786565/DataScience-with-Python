# Data Wrangling in Python  

The general steps to perform data wrangling in Python are as follows:  

## Steps to Perform Data Wrangling on the Titanic Dataset Using Pandas  

The steps of data wrangling in Python typically include:  

1. **Importing necessary libraries** such as `pandas`, `numpy`, and `matplotlib`.  
2. **Loading the data** into a Pandas DataFrame.  
3. **Assessing the data** for missing values, outliers, and inconsistencies.
   1. EDA  
4. **Cleaning the data** by filling in missing values, removing outliers, and correcting errors.
   1. Outliers Removal
      1. Visualization
      2. IQR Method
      3. Z-Score
5. **Transforming the data** by creating new columns, renaming columns, sorting, and filtering the data.
6. **Storing the cleaned data** in a format that can be used for future analysis, such as a CSV or Excel file.  
7. **Exploring the data** by creating visualizations and using descriptive statistics.  
8. **Creating a pivot table** to summarize the data.  
9. **Checking for and handling duplicate rows**.  
10. **Encoding categorical variables**.  
11. **Removing unnecessary columns or rows**.  
12. **Merging or joining multiple datasets**.  
13. **Handling missing or null values**.  
14. **Reshaping the data**.  
15. **Formatting the data**.  
16. **Normalizing or scaling the data**.
    1. Normalize the Data ( Data Normalization )
      1.1. Methods
        1. `Min-Max Scaling` : This method scales the data to a common range, usually between [0 , 1].
            - **Formula**: `x' = (x - min) / (max - min)`
            - **Use**: Use when you know the range of your data and want to prevent features with large ranges from dominating the model.
        2. `Z-Score Normalization` : This method scales the data to have a mean of 0 and a standard deviation of 1.
            - **Formula**: `x' = (x - mean) / std`
            - **Use**: Use when you know Data is normally Distributed
        3. `Decimal Scaling` : This method scales the data to a specific decimal place.
            - **Formula**: `x' = x * 10^(-p)` where p is the smallest decimal place you want to round to.
            - **Use**: Use when you want to reduce the number of decimal places in your data.
        4. `Log Transformation` : This method transforms the skewed data by taking the logarithm of the values.
            - **Formula**: `x' = log(x)`
            - **Use**: Use when you have skewed data and want to reduce the effect of outliers.
        5. `MaxAbs Scaler` : This method scales the data to a common range, usually between [-1 , 1].
            - **Formula**: `x' = x / max(abs(x))`
            - **Use**: Useful for sparse Datasets
        6. `Robust Scaling` : This method scales the data to a common range, usually between [-1 , 1], using IQR to reduce the impact of outliers.
            - **Formula**: `x' = (x - Median) / (Q3 - Q1)`
            - **Use**: Use when you have outliers in your data.
        7. `L2 Normalization` : This method scales the data to a common range usually between [0 , 1], so that the sum of squares of the data (elements) is equal to 1.
            - **Formula**: `x' = x / sqrt(sum(x^2))`
            - **Use**: Useful for text data and machine learning models like SVM .
        8. `Standard Scaler` : This method scales the data to have a mean of 0 and a standard deviation of 1.
           - **Formula**: `x' = (x - mean) / std`
           - **Use**: Use when you know Data is normally Distributed
17. **Creating new features** from existing data.  
18. **Validating data integrity**.  
19. **Saving the final data** for future use.  
20. **Documenting the data wrangling process** for reproducibility.  
