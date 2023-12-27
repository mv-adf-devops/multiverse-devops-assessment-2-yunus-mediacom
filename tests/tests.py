from extract import *
import pytest 
import os
import csv

# Test that file is read into as a list
def test__is_list():
    # Arrange
    filename = 'results.csv'
    expected_type = list
    # Act
    output = get_input(filename)
    # Assert
    assert type(output) == expected_type

# Test that file exists