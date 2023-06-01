Downloading Guitar Lists
========================

This turned out to be tricky to do with Scrapy as the website is designed for Javascript and CSS;
possibly to avoid crawlers.  I didn't see any copyright notices on the site, so this is presumably to prevent server overload.

Manual Download Instructions
----------------------------

* Go to https://www.guitar-list.com/find in your browser
* Right-Click->Save As...
* Save under `guitarlists/data/find.html` as *Webpage, HTML Only*
* Go to https://www.guitar-list.com/node_reference/autocomplete/node/content_my_guitar_gear/field_model_name in your browser
* Right-Click->Save As...
* Save under `guitarlists/data/field_model_name.json` as *JSON*

Environment Setup
-----------------

With Python 3, set up a virtual environment in `./venv`, by running this in the top directory of this project:
* `python -m venv venv`
* `venv\Scripts\activate` (on Windows)
* `pip install -r requirements.txt`

Data Extraction
---------------

* `venv\Scripts\activate` (Activate the virtual environment - Windows form)
* `python extract_model_data.py` (Extract data into `guitarlists/data/make_model.json`)