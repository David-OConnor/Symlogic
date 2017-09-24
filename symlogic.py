
# Color result by tone?

POLITE = [
    "please",
    "thanks",
    "thank you",
    "sorry",
    "you're welcome",

]

IMPOLITE = [
    "stupid",
    "stupidest",
    "retarded",
    "fucking",
    "lmfao",
    "basdard",
    "bitch",
]


NARCISSISTIC = [
    'I',
    'me',

]


ABSOLUTE = [
    "nothing",
    "everything",
    "none",
    "all",
    "always",
    "never",

]


SUFFIXES = [
    "ing",
    "s",
    "ed",

]


CONFIDENT = [
    'guarantee',
    'sure',
    "of course",
]

WEASELS = [
    "suggests"
]


VAPID = [
    "look at",

]


DOMINANT = [
]

SUBMISSIVE = [

]

FLIRTY = [
    ";)",
    "!",
    "lol",
    "haha",
    "xxx",
    "xox",
    
]

PRONOUNS = [
    "i",
    "we",
    "it",
]

STRONG = [
    "destroy",
    "so bad",
    "amazing",
    "wonderful",
    "beautiful",

]


REPLACEMENTS = [
    ("i think", ""),
    ("necessarily", ""),
    ("so maybe", ""),
    ("aren't that", "aren't"),
    ("maybe also", ""),
    ("actually", ""),
    ("so", ""),
    ("I guarantee", ""),
    ("a lot", ""),
    ("really", ""),
    ("take a look at", "look at"),
    ("in fact", ""),
    ("here's the thing", ""),
    ("But one thing is clear.", ""),
    ("straight up", ""),

    ("imo", ""),

    ("am going to", "will")

]

PASSIVE_HINTS = [
    "were",
    "have been",
]

PROBABILISTIC = [
    "maybe",
    "probably",
    "i think",
    "mostly",

]


EXAGERATORS = [
    "very",
    "strongly",
    "massive",
    "extremely",
    "really",

]

DELETE_WHOLE_SETTENCE = [
    "could be",
    ]


QUALIFIERS = [
    # Split this into diff cats?
    "unfortunately",
    "ever",
    "mostly",
    "highly",
    "always",
    "probably",
    "main",
    "also",
    "too",
    "that",
    "so",
    "certainly",
    "just",
    "simply",
    "really",
    "even",
    "however",
    "a little",
    "feel like",
    "authorities said",
    "basically",
]

REVERSERS = [
    "hardly",

    ]


def split_sentences(raw_text: str) -> str:
    DELIMITERS = ['.', ';', '-']


def decode(raw_text: str) -> str:
    result = raw_text
    for q in QUALIFIERS:
        result = result.replace(q, '')

    return result
