#!/usr/bin/env python

from lxml.etree import HTMLParser, parse
from os.path import abspath, dirname, join
import logging
import json
import re

def get_makes():
    parser = HTMLParser()
    brands = []
    find_html_filename = join(dirname(abspath(__file__)), 'guitarlists', 'data', 'find.html')
    with open(find_html_filename, 'r', encoding='utf-8') as f:
        tree = parse(f, parser)
    for brand_option in tree.xpath('//select[@id="edit-jump"]//option'):
        value = brand_option.attrib['value']
        if not value:
            continue
        if '::' in value:
            id, brand_url = value.split('::', 1)
        else:
            logging.warning("Unexpected option value: %s", value)
            continue
        brand_name = brand_option.text.strip()
        brands.append((brand_name, id, brand_url))
    return brands

MODEL_KEY_RE = re.compile(r'\s*(\S.*)\s+\[nid:([0-9]+)\]\s*')

def get_models():
    models = []
    models_filename = join(dirname(abspath(__file__)), 'guitarlists', 'data', 'field_model_name.json')
    with open(models_filename, 'r', encoding='utf-8') as f:
        model_data = json.load(f)
    for key, value in model_data.items():
        key_m = MODEL_KEY_RE.match(key)
        if key_m:
            model_name, model_nid = key_m.groups()
            models.append((model_name, model_nid))
        else:
            logging.warning("Unexpected key format: %s", key)
    return models

MANUAL_MAKE_CHANGE = {
    "AMPEG/DAN ARMSTRONG AMPEG": "AMPEG",
    "ANDREAS": "ANDREAS GUITARS",
    "Aria": "ARIA (PRO II)",
    "ARIA": "ARIA (PRO II)",
    "ARIA PRO II": "ARIA (PRO II)",
    "ARIA/ARIA PRO II": "ARIA (PRO II)",
    "Brawley": "BRAWLEY GUITARS",
    "Brian Eastwood": "Brian Eastwood Guitars",
    "EGYPT": "EGYPT GUITARS",
    "ERNIE BALL/MUSIC MAN": "Ernie Ball Music Man",
    "FANO": "FANO GUITARS",
    "G & L": "G&L",
    "HILL GUITAR COMPANY": "Kenny Hill",
    "J.B. PLAYER": "JB PLAYER",
    "MUSIC MAN": "Ernie Ball Music Man",
    "RENAISSANCE GUITAR COMPANY": "Renaissance (Rick Turner)",
    "RODRIGUEZ, MANUEL AND SONS": "Manuel Rodriguez",
    "STEVENS ELECTRICAL INSTRUMENTS": "Michael Stevens",
    "TURNER, RICK": "RICK TURNER",
    "U.S. MASTERS": "US Masters",
    "ZEIDLER": "Zeidler (J.R.)",
}

def match_models(makes, models):
    make_model_lookup = {}
    makes_by_word_count = {}
    for brand_name, id, brand_url in makes:
        word_count = brand_name.count(' ') + 1
        makes_by_word_count.setdefault(word_count, {})[brand_name.lower()] = brand_name
    unmatched = []
    for model, model_nid in models:
        model_word_count = model.count(' ')
        model_words = model.split(' ')
        for word_count in range(model_word_count, 0, -1):
            actual_word_count = word_count
            potential_make = ' '.join(model_words[:word_count]).rstrip(',')
            if potential_make in MANUAL_MAKE_CHANGE:
                potential_make = MANUAL_MAKE_CHANGE[potential_make]
                actual_word_count = potential_make.count(' ') + 1
            potential_make = potential_make.lower()
            if potential_make in makes_by_word_count.get(actual_word_count, {}):
                make = makes_by_word_count[actual_word_count][potential_make]
                actual_model = model
                if actual_model.lower().startswith(make.lower()):
                    actual_model = actual_model[len(make):].strip()
                make_model_lookup.setdefault(make, {})[actual_model] = model
                break
        else:
            logging.warning("Could not find make for %s", model)
            unmatched.append(model)
    # The UNKNOWN brand name had 169 models as of 2023-06-01, so close to that is not bad
    print(f"Found {len(makes)} makes, {len(models)} models, and failed to match {len(unmatched)} models")
    return make_model_lookup

def save_guitar_lists(make_model_lookup):
    lists_filename = join(dirname(abspath(__file__)), 'guitarlists', 'data', 'make_model.json')
    with open(lists_filename, 'w') as f:
        json.dump(make_model_lookup, f, indent=4)

if __name__ == '__main__':
    makes = get_makes()
    models = get_models()
    make_model_lookup = match_models(makes, models)
    save_guitar_lists(make_model_lookup)
