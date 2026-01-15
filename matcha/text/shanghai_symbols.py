"""
1910 Shanghai Dialect (Old Wu) Phoneme Symbol Set

Based on the "Key to the Pronunciation" in F.L.Hawks Pott's work.
This symbol set is designed to preserve historical phonetic distinctions:
- Sharp/Round (尖团) distinction
- Voiced obstruent retention (浊音)
- Checked tone glottal stops (入声)
"""

_pad = "_"
_punctuation = ';:,.!?—…"«»"" '

# ===================== INITIALS (声母) =====================
# Aspirated (High Pitch Class)
_initials_aspirated = [
    "pʰ",  # ph
    "tʰ",  # th
    "kʰ",  # kh
    "tsʰ",  # tsh (Sharp)
    "tɕʰ",  # ch (Round, palatal)
    "kʷʰ",  # kwh
]

# Unaspirated (High Pitch Class)
_initials_unaspirated = [
    "p",  # p
    "t",  # t
    "k",  # k
    "ts",  # ts (Sharp - MUST BE DISTINCT from tɕ)
    "tɕ",  # ky (Round - palatal affricate)
    "kʷ",  # kw
]

# Voiced (Low Pitch Class / 浊音)
_initials_voiced = [
    "b",  # b
    "d",  # d
    "ɡ",  # g
    "dz",  # dz (voiced affricate)
    "dʑ",  # j (voiced palatal)
    "ɡʷ",  # gw
    "z",  # z (voiced fricative, distinct from dz)
    "v",  # v
]

# Nasals and Liquids (Can be High or Low depending on context)
_initials_sonorant = [
    "m",
    "n",
    "ŋ",  # ng
    "ɲ",  # ny
    "l",
    "w",
    "j",  # y (glide)
]

# Fricatives
_initials_fricative = [
    "f",
    "s",
    "ɕ",  # sh / hy
    "h",
    "hw",  # labialized h
]

_initials = (
    _initials_aspirated
    + _initials_unaspirated
    + _initials_voiced
    + _initials_sonorant
    + _initials_fricative
)

# ===================== FINALS (韵母) =====================
# Basic vowels
_vowels = [
    "ɑ",  # a (far)
    "e",  # e (prey)
    "i",  # i
    "o",  # o
    "u",  # u/oo
    "ʊ",  # oo in foot
    "ø",  # oe/eu (German ö)
    "y",  # ui/ue/iu (French u)
    "ə",  # schwa
    "ɛ",  # a in at
    "ɔ",  # au
]

# Diphthongs and Triphthongs
_diphthongs = [
    "ia",
    "io",
    "iø",
    "iɔ",
    "uo",
    "ua",
]

# Nasal finals
_nasals = [
    "ɑ̃",  # ang/aung
    "ø̃",  # oen
    "in",
    "ən",
    "oŋ",  # ung/oong
    "iɑ̃",  # iang
    "iən",  # ien
]

# Checked tone finals (入声 - with glottal stop)
_checked = [
    "aʔ",  # ak/ah
    "əʔ",  # eh
    "iʔ",  # ih
    "oʔ",  # ok/oh
    "uʔ",  # uh
    "øʔ",  # oeh
    "iaʔ",  # iak/iah
    "ɔʔ",  # auh
]

# Syllabic consonants
_syllabic = [
    "m̩",  # syllabic m
    "ŋ̍",  # syllabic ng
    "z̩",  # syllabic z (apical vowel)
]

_finals = _vowels + _diphthongs + _nasals + _checked + _syllabic

# ===================== PROSODIC MARKERS =====================
_tone_markers = [
    "˥",  # High level (55)
    "˩",  # Low level (11)
    "˧",  # Mid level (33)
    "̤",  # Breathy voice / Slack (for voiced initials)
]

_suprasegmentals = [
    "ˈ",  # Primary stress
    "ˌ",  # Secondary stress
    "ː",  # Long vowel
]

# ===================== EXPORT =====================
# Core symbol list for model
shanghai_symbols = (
    [_pad] + list(_punctuation) + _initials + _finals + _tone_markers + _suprasegmentals
)

# Convenience lookups
SHANGHAI_SYMBOL_TO_ID = {s: i for i, s in enumerate(shanghai_symbols)}
SHANGHAI_ID_TO_SYMBOL = {i: s for i, s in enumerate(shanghai_symbols)}
SHANGHAI_SPACE_ID = shanghai_symbols.index(" ")

# For model configuration
N_SHANGHAI_SYMBOLS = len(shanghai_symbols)
