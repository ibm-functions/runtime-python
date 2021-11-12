"""Python test fixture to check that watson service"""

from ibm_watson  import LanguageTranslatorV3
from ibm_watson  import __version__ as sdk_version
from distutils.version import LooseVersion
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(args):
    authenticator = IAMAuthenticator(args.get("apikey"))
    language_translator = LanguageTranslatorV3(
        version="2018-05-01",
        authenticator=authenticator
    )
    language_translator.set_service_url(args.get("url"))

    translation = language_translator.translate(text='Hello', model_id='en-it')
    if LooseVersion(sdk_version) < LooseVersion('2.0.0'):
        return translation
    else:
        return translation.get_result()

if __name__ == "__main__":
    # execute only if run as a script
    input = {"url":"<url from credentials>",
             "apikey":"<apikey from credentials>"}
    print(main(input))
