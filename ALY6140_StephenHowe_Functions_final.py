"""
ALY6140 Final Project: Accompanying Functions for Boston 3-1-1 Analysis

Copyright (c) 2019
Written by Stephen Howe, Northeastern University
"""

# Functions

# Required libraries
import numpy as np
import pandas as pd

# File Reading Functions

# Extracting worksheet names from Excel file
def get_worksheet_names(filename):
    """
    :param filename: filepath to Excel file
    :return: dataframe with names of worksheets in Excel file
    """
    file_data = pd.ExcelFile(filename)
    worksheet_names = file_data.sheet_names
    
    return worksheet_names


# Clean-Up Functions

# Datetime conversion
def dt_conv(dataframe, column_name):
    """
    :param dataframe: name of dataframe
    :param column_name: name of column to convert
    :return: dataframe with specified column converted from string to datetime
    """
    dataframe[column_name] = pd.to_datetime(dataframe[column_name])

    return dataframe


# Aggregate Statistics

# calculate median by group
def median_by_group(dataframe, group, agg_column):
    """
    :param dataframe: name of dataframe
    :param group: column in dataframe by which to group data, as string
    :param agg_column: column in dataframe on which to conduct aggregate statistics, as string
    :return: dataframe with median by group
    """
    grouped_data = dataframe.groupby(by=[group], as_index = False)
    grouped_stat = grouped_data[[agg_column]].median()
    grouped_stat = grouped_stat.sort_values(by=agg_column, ascending=False)
    
    return grouped_stat

# calculate size (count) by group
def size_by_group(dataframe, group, agg_column):
    """
    :param dataframe: name of dataframe
    :param group: column in dataframe by which to group data, as string
    :param agg_column: column in dataframe on which to conduct aggregate statistics, as string
    :return: dataframe with size of group
    """
    grouped_data = dataframe.groupby(by=[group], as_index = False)
    grouped_stat = grouped_data[[agg_column]].size()
    
    return grouped_stat
