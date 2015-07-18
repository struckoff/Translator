import urllib.request as ur
import json
import re
import grab

import urllib.request as ur
import json
import re
import grab


class GoogleTranslate:
    def __init__(self, target):
        self.target = target
        request = self.request_make(self.url_serialize(target))
        self.response = self.get_response(request)

    def url_serialize(self, key):
        key = key.replace("  ", " ")
        key = key.replace(" ", "%20")
        return ''.join(["https://translate.google.ru/translate_a/single?"
                        "client=t&",
                        "sl=en&",
                        "tl=ru&",
                        "hl=ru&",
                        "dt=bd&",
                        "dt=ex&",
                        "dt=ld&",
                        "dt=md&",
                        "dt=qca&",
                        "dt=rw&",
                        "dt=rm&",
                        "dt=ss&",
                        "dt=t&",
                        "dt=at&",
                        "ie=UTF-8&",
                        "oe=UTF-8&",
                        "source=btn&",
                        "srcrom=1&",
                        "ssel=0&",
                        "tsel=0&",
                        "kc=1&",
                        "tk=521441|834535&",
                        "q={}".format(key)])

    def request_make(self, url):
        user_agent = 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_9_3)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/35.0.1916.47Safari/537.36'
        return ur.Request(url,
                          data=None,
                          headers={'User-Agent': user_agent})

    def get_response(self, request):
        response = ur.urlopen(request)
        response_raw = response.read().decode('utf-8')
        response_raw = codec_fix(response_raw)
        response_raw = replace_pair(response_raw,
                                    [("<>", ""),
                                     ("< >", ""),
                                     (",,", ","),
                                     ("[,", "["),
                                     (",]", "]")])

        return json.loads(response_raw)

    def get_main_translate(self):
        return self.response[0][0][0]

    def get_other_versions(self):
        return self.response[1]

    def show(self):
        print(self.get_main_translate())
        print("-" * len(self.get_main_translate()))

        for sub_type in self.get_other_versions():
            if len(sub_type) > 1:
                print(sub_type[0], ":")
                for translate in sub_type[1]:
                    print(" " * 4, translate)


class UrbanDict:
    def __init__(self, target):
        self.target = target
        request = self.request_make(self.url_serialize(target))
        self.response = self.get_response(request)

    def url_serialize(self, key):
        key = key.replace("  ", " ")
        key = key.replace(" ", "%20")
        return "http://api.urbandictionary.com/v0/define?term={}".format(key)

    def request_make(self, url):
        user_agent = 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_9_3)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/35.0.1916.47Safari/537.36'
        return ur.Request(url,
                          data=None,
                          headers={'User-Agent': user_agent})

    def get_response(self, request):
        response = ur.urlopen(request)
        response_raw = response.read().decode('utf-8')
        response_raw = codec_fix(response_raw)
        response_raw = replace_pair(response_raw,
                                    [("<>", ""),
                                     ("< >", ""),
                                     (",,", ","),
                                     ("[,", "["),
                                     (",]", "]")])

        return json.loads(response_raw)

    def get_top_devinition(self):
        return self.get_all_definitions()[0]

    def get_all_definitions(self):
        return [d.get("definition") for d in self.response["list"]] or ["no results"]

    def show(self):
        for definition in self.get_all_definitions():
            print("\n", definition)
            print("." * len(self.target))


def codec_fix(string):
    result = string
    pattern = r'\\u'

    holder = 0
    while chr(holder) in string:
        holder += 1

    indexes = [m.start() for m in re.finditer(pattern, string)]

    for start in indexes:
        broken = string[start: start + 6]
        fixed = broken.encode().decode("unicode_escape")
        fixed += chr(holder) * 5

        result = result[:start] + fixed + result[start + 6:]

    return result.replace(chr(holder), '')


def codec_fix_dirty(string):
    result = string.replace("\\u003c", "<")
    result = result.replace("\\u003e", ">")
    return result


def replace_list(string, lst, new=''):
    result = string
    for smb in set(lst):
        result = result.replace(smb, new)

    return result


def replace_pair(string, lst):
    result = string
    for old, new in set(lst):
        while old in result:
            result = result.replace(old, new)

    return result


def pretty_print(obj, ind=0):
    if type(obj) is list:
        print(" " * ind, "[")
        for val in obj:
            print(" " * (ind + 1), pretty_print(val, ind=ind + 3))
        print(" " * ind, "]")
    elif type(obj) is dict:
        for key, val in obj.items():
            print(" " * ind, "{}: {}".format(key, pretty_print(val, ind=ind)))
    else:
        return obj

# gt = GoogleTranslate(input(": "))
# gt.show()

ud = UrbanDict(input(": "))
ud.show()

# pretty_print(ud.response)
