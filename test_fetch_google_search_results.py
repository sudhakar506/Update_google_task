import os
import pytest
import config
from fetch_google_search_results import fetch_google_search_results

def test_fetch_google_search_results():
    # Call the function with values from config.py
    fetch_google_search_results(config.QUERY, config.NUM_RESULTS)

    # Define the results file path from the config
    results_file = "new_search_results.txt"

    # Check if the results file is created
    assert os.path.exists(results_file), "Results file does not exist."

    # Read the results file and check its contents
    with open(results_file, 'r') as file:
        results = file.readlines()

    # Check if the file contains the expected number of results
    assert len(results) == config.NUM_RESULTS, "Number of results does not match the expected count."

    # Optionally, you can assert the content of the results if you have some known expected values
    # For example, ensure that the results start with the expected format (e.g., "1. Some Result")
    # Adjust the expected value as needed based on what you expect from the search
    if config.NUM_RESULTS > 0:
        first_result = results[0].strip()
        assert first_result.startswith("1."), "The first result does not start with the expected format."

    # Cleanup: Remove the file after the test (optional, if you want to keep the file, you can skip this)
    #os.remove(results_file)
