# Python Web Scraper

This app is a Ceneo opinion scraper. It is designed to scrape opinions from the Ceneo website. The app allows users to gather and analyze product reviews and ratings from Ceneo.

## Installation
To install the necessary dependencies, run the following command:
```
pip install -r requirements.txt
```
Or if you prefer. Create a virtual environment using **virtualenv**, and running `virtualenv venv` command inside the project directory. Then activate it with `source venv/bin/activate` (Linux/Mac OS) or `./venv/Scripts/activate` (Windows) and then install the necessary packages from `requirements.txt`.

**To deactivate the local environment simply type in the console `deactivate`.** 

Finally run the app calling the `run.py` script.

## Usage
The application strikte revolves around handling the extraction of the product of interest by entering its ID. The product is saved to a database for possible retrieval of product reviews in CSV, JSON or xlsx format.