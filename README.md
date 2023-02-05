# Web Scraper for timesjobs.com
This program is a web scraper for the website timesjobs.com. It retrieves job listings that match the keyword "python" and the location specified in the URL.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
### What things you need to install the software and how to install them:

* Python 3.x
* pip

### Use the package manager pip to install the following libraries:

``` py
pip install requests
pip install beautifulsoup4
```

## Usage
Run the following command to execute the script:

``` py
python main.py
```

The script for scraping job listings that match the keyword "python", filtering out the job listings by published date and required skills, and storing the information in text files could look something like this (index.text) under "posts" directory. The text files will contain the following details:

* Company Name
* Skills
* More Information Link

# Built With

* Python
* Requests - HTTP library for Python
* BeautifulSoup - A library for pulling data out of HTML and XML files
* Time -  A built-in module that provides various functions for working with times and dates.

# License
This project is licensed under the MIT License - see the LICENSE file for details.






