import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_extractor import RegexExtractors


sample_text = """
Here is a test: user@example.com, #fun, (123) 456-7890, 1234-5678-9012-3456, $1,234.56, 2222 2222 7670 9898
"""

extractor = RegexExtractors(sample_text)

print("Emails:", extractor.extract_email())
print("Hashtags:", extractor.extract_hashtags())
print("Phone Numbers:", extractor.extract_phone_numbers())
print("Credit Cards:", extractor.extract_credit_card_number())
print("Currency:", extractor.extract_currency())

