Instrument Makes and Models
===========================

This is a database of instrument makes and models, so far only covering guitars.

Manual Download of Guitar List Data
-----------------------------------

* This needs to be done manually rather than with a web scraper
* Go to https://www.guitar-list.com/find in your browser
* Right-Click->Save As...
* Save under `src-data/guitar-list.com/find.html` as *Webpage, HTML Only*
* Go to https://www.guitar-list.com/node_reference/autocomplete/node/content_my_guitar_gear/field_model_name in your browser
* Right-Click->Save As...
* Save under `src-data/guitar-list.com/field_model_name.json` as *JSON*

Environment Setup
-----------------

With Python 3, set up a virtual environment in `./venv`, by running this in the top directory of this project:
* `python -m venv venv`
* `venv\Scripts\activate` (on Windows)
* `pip install -r requirements.txt`

Data Extraction
---------------

* `venv\Scripts\activate` (Activate the virtual environment - Windows form)
* `python extract_model_data.py` (Extract data into `guitar-makes-and-models.json`)