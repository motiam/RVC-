import locale
import json
import os


def load_language_list(language):
    with open(f"./i18n/{language}.json", "r", encoding="utf-8") as f:
        language_list = json.load(f)
    return language_list


class I18nAuto:
    def __init__(self, language=None):
        if language in ["Auto", None]:
            language = "zh_CN"
           # getlocale can't identify the system's language ((None, None))
        if not os.path.exists(f"./i18n/{language}.json"):
            language = "zh_CN"
        self.language = language
        print("Use Language:", language)
        self.language_map = load_language_list(language)

    def __call__(self, key):
        return self.language_map[key]
