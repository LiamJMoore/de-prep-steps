import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, format_err_msg, skip_test
# DO NOT CHANGE CODE ABOVE THIS LINE

import re

def convert_to_title_case(sentence):
    """
    This function converts the input sentence to title case, where the first letter of each word is capitalized,
    but correctly handles cases like "they're", "bill's" and hyphenated words like "something-else".
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Define words that should not be fully title-cased (e.g., "they're" or "bill's")
    result = []
    
    for word in words:
        # If the word contains an apostrophe, handle it separately
        if "'" in word:
            result.append(word.capitalize())
        elif "-" in word:
            # For hyphenated words, apply title case to each part
            hyphenated_parts = word.split("-")
            result.append("-".join(part.capitalize() for part in hyphenated_parts))
        else:
            # Otherwise, apply title case normally
            result.append(word.title())
    
    # Join the words back together into a sentence
    return " ".join(result)
    
    pass


@run_test
def test_convert_single_word_to_title_case():
    assert convert_to_title_case("hi") == "Hi", \
        format_err_msg("Hi", convert_to_title_case("hi"))


@run_test
def test_convert_multi_word_to_title_case():
    assert convert_to_title_case("hello world") == "Hello World", \
        format_err_msg("Hello World", convert_to_title_case("hello world"))

    assert convert_to_title_case("Goodbye world") == "Goodbye World", \
        format_err_msg("Goodbye World", convert_to_title_case("Goodbye world"))

    assert convert_to_title_case("Well ain't this awkward") == \
        "Well Ain't This Awkward", \
        format_err_msg("Well Ain't This Awkward",
                       convert_to_title_case("Well ain't this awkward"))


@run_test
def test_convert_complex_sentence_to_title_case():
    assert convert_to_title_case(
        "not just apostrophes, could be something-else") \
        == "Not Just Apostrophes, Could Be Something-else", \
        format_err_msg(
            "Not Just Apostrophes, Could Be Something-else",
            convert_to_title_case(
                "not just apostrophes, could be something-else"))


if __name__ == '__main__':
    test_convert_single_word_to_title_case()
    test_convert_multi_word_to_title_case()
    test_convert_complex_sentence_to_title_case()