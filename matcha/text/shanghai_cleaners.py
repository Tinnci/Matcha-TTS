"""
Shanghai Dialect (1910 Pott Romanization) Text Cleaners

This module provides text cleaning and G2P conversion for 1910-era Shanghai dialect,
bypassing the need for eSpeak or other English phonemizers.
"""

import re
import sys
from pathlib import Path

# Try to import PottToIPA from project root
# This may fail when running from external/Matcha-TTS during training
_pott_converter = None
try:
    _project_root = Path(__file__).resolve().parents[3]
    if str(_project_root) not in sys.path:
        sys.path.insert(0, str(_project_root))
    from src.pott_g2p import PottToIPA  # noqa: E402

    _pott_converter = PottToIPA()
except (ImportError, ModuleNotFoundError):
    # PottToIPA not available - shanghai_cleaners will fail but
    # shanghai_passthrough will still work (for pre-annotated IPA)
    pass

# Regex patterns
_whitespace_re = re.compile(r"\s+")
_pott_syllable_re = re.compile(r"[a-zA-Z']+")


def collapse_whitespace(text: str) -> str:
    """Collapse multiple whitespaces into single space."""
    return re.sub(_whitespace_re, " ", text).strip()


def pott_to_ipa(text: str) -> str:
    """
    Convert Pott romanization text to IPA sequence.

    This is the core cleaner for 1910 Shanghai dialect.
    It processes each syllable through PottToIPA.convert_syllable().

    Args:
        text: Input text in Pott romanization (e.g., "Ngoo yiao mah dzi")

    Returns:
        IPA string with spaces between syllables
    """
    if _pott_converter is None:
        raise RuntimeError(
            "PottToIPA not available. Use shanghai_passthrough for pre-annotated IPA, "
            "or run from project root directory."
        )

    result_parts = []

    # Split by non-alphabetic characters while preserving punctuation
    tokens = re.split(r"(\s+|[,.!?;:—…\"«»" "]+)", text)

    for token in tokens:
        token = token.strip()
        if not token:
            continue

        # Check if it's punctuation
        if re.match(r"^[,.!?;:—…\"«»" "]+$", token):
            result_parts.append(token)
            continue

        # Check if it's whitespace
        if re.match(r"^\s+$", token):
            result_parts.append(" ")
            continue

        # It's a Pott syllable - convert to IPA
        ipa, _, _ = _pott_converter.convert_syllable(token)
        if ipa:
            result_parts.append(ipa)

    return " ".join(result_parts)


def shanghai_cleaners(text: str) -> str:
    """
    Full cleaning pipeline for 1910 Shanghai dialect.

    Steps:
    1. Convert Pott romanization to IPA
    2. Collapse whitespace

    Use this cleaner with cleaner_names=["shanghai_cleaners"].
    """
    text = pott_to_ipa(text)
    text = collapse_whitespace(text)
    return text


def shanghai_passthrough(text: str) -> str:
    """
    Passthrough cleaner for pre-processed IPA input.

    Use this when the input is already in IPA format.
    Only performs whitespace normalization.
    """
    return collapse_whitespace(text)


# Convenient test function
if __name__ == "__main__":
    test_cases = [
        "Ngoo yiao mah dzi.",
        "Nong hau vau?",
        "Tsh-tsiang kuh.",
    ]

    print("Testing Shanghai Cleaners:")
    print("-" * 50)
    for text in test_cases:
        ipa = shanghai_cleaners(text)
        print(f"Pott: {text}")
        print(f"IPA:  {ipa}")
        print()
