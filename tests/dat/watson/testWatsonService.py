"""Python test fixture to check that watson service"""

from watson_developer_cloud import LanguageTranslatorV3
from watson_developer_cloud import __version__ as sdk_version
from distutils.version import LooseVersion

def main(args):
    language_translator = LanguageTranslatorV3(
        version="2018-05-01",
        url=args.get("url"),
        username="APIKey",
        password=args.get("apikey"))

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
