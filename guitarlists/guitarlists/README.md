Downloading Guitar Lists
========================

This turned out to be tricky to do with Scrapy as the website is designed for Javascript and CSS;
possibly to avoid crawlers.  I didn't see any copyright notices on the site, so this is presumably to prevent server overload.

Manual Download Instructions
----------------------------

* Go to https://www.guitar-list.com/find in your browser
* Right-Click->Save As...
* Save under `data/find.html` as *Webpage, HTML Only*
* Go to https://www.guitar-list.com/node_reference/autocomplete/node/content_my_guitar_gear/field_model_name in your browser
* Right-Click->Save As...
* Save under `data/field_model_name.json` as *JSON*

Data Extraction
---------------

Run `python ../extract_model_data.py`