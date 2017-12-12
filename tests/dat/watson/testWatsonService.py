"""Python test fixture to check that watson service"""

from watson_developer_cloud import LanguageTranslatorV2

def main(args):
    language_translator = LanguageTranslatorV2(
        url=args.get("url"),
        username=args.get("username"),
        password=args.get("password"))
    return language_translator.translate("Hello", source='en', target='es')

if __name__ == "__main__":
    # execute only if run as a script
    input = {"url":"<url from credentials>",
             "username":"<username from credentials>",
             "password":"<password from credentials>"}
    print(main(input))
