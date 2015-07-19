import argparse
from lib import GoogleTranslate, UrbanDict


def call_google(namespace):
    gt = GoogleTranslate(namespace.target, namespace.frm, namespace.to)
    return gt.show()


def call_urban(namespace):
    ut = UrbanDict(namespace.target)
    return ut.show(None if namespace.show_all else namespace.descr_count)


def parse_args():
    arguments_parser = argparse.ArgumentParser()
    subparsers = arguments_parser.add_subparsers()

    gt_parser = subparsers.add_parser('google', help='use Google Translate')
    gt_parser.add_argument('-f', '--from', action='store', dest='frm', help='FROM', default='auto')
    gt_parser.add_argument('-t', '--to', action='store', dest='to', help='TO')
    gt_parser.set_defaults(func=call_google)

    ud_parser = subparsers.add_parser('urban', help='use Urban Dictionary')
    ud_parser.add_argument('--all', '-a', action='store_true', dest='show_all', help='show all descriptions', default=False)
    ud_parser.add_argument('-c', '--count', action='store', type=int, dest='descr_count', help='count of descriptions to show', default=1)
    ud_parser.set_defaults(func=call_urban)

    arguments_parser.add_argument('target', type=str, help='words')

    return arguments_parser.parse_args()

namespace = parse_args()
namespace.func(namespace)

# target = input(": ")
# gt = GoogleTranslate(target)
# gt.show()

# ud = UrbanDict(target)
# ud.show()

# print(dir(parse_args()))
# print(parse_args())
