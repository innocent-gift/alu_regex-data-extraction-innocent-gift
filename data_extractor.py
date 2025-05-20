#!/usr/bin/env python3

import re

class RegexExtractors:
    def __init__(self,text):
        self.text = text

# email extraction

    def extract_email(self):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, self.text)
 
 # hashtags extract


    def extract_hashtags(self):
        pattern = r"#\w+"
        return re.findall(pattern, self.text)
    
# extract phone numbers:
    
    def extract_phone_numbers(self):
        pattern = r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})'
        return re.findall(pattern, self.text)

# extract credit card number 
    
    def extract_credit_card_number(self):
        pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
        return re.findall(pattern, self.text)

# extract currency in dollars
    def extract_currency(self):
        pattern = r"\$[0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]{2})?"
        return re.findall(pattern, self.text)



