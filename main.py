import urllib.request
import random

word_url = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'  # NOQA
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

upper_words = [word for word in words if word[0].isupper()]
name_words = [
    word for word in upper_words if not word.isupper()
]
one_name = ' '.join(
    [
        name_words[random.randint(0, len(name_words))]
        for i in range(2)
    ]
)

def rand_name():
    name = ' '.join(
        [
            name_words[random.randint(0, len(name_words))]
            for i in range(2)
        ]
    )
    return name


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Python cli tool for generating random names'
    )
    required = parser.add_argument_group('required arguments')
    required.add_argument(
        '-o',
        '--options',
        dest='options',
        type=int,
        required=True,
        help='Total of options to return'
    )
    arguments = parser.parse_args()
    for n in range(arguments.options):
        print(rand_name())


if __name__ == '__main__':   # pragma: no cover
    main()
