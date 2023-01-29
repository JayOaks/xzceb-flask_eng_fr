"""
Necessary imports to set up environment.
"""
import json # pylint: disable=unused-import
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""
This sets up the translator instance.
"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates English to French.
    """
    french_translation = language_translator.translate(
        text = english_text,
        model_id= 'en-fr'
    ).get_result()
    french_text = french_translation.get("translations")[0].get("translation")
    
    return french_text

def french_to_english(french_text):
    """
    This function translates French to English
    """
    english_translation = language_translator.translate(
        text = french_text,
        model_id= 'fr-en'
    ).get_result()

    english_text = english_translation.get("translations")[0].get("translation")

    return english_text
