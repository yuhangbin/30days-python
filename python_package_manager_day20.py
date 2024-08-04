import numpy
import pandas
import requests

print(numpy.version.version)

import webbrowser # web browser module to open websites



'''
Database

SQLAlchemy or SQLObject - Object oriented access to several different database systems
pip install SQLAlchemy
Web Development

Django - High-level web framework.
pip install django
Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
pip install flask
HTML Parser

Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
pip install beautifulsoup4
PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.
XML Processing

ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
GUI

PyQt - Bindings for the cross-platform Qt framework.
TkInter - The traditional Python user interface toolkit.
Data Analysis, Data Science and Machine learning

Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
TensorFlow: is a machine learning library built by Google.
Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
Network:

requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
pip install requests

'''
import re
from collections import Counter
response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
text = response.text

all_words = re.sub(r"[^a-zA-Z0-9'\s]", '', text).lower().split()

word_counts = Counter(all_words)

print(word_counts.most_common(10))


