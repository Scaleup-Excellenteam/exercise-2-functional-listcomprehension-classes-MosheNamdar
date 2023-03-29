
def count_words(text):
    """
    A function that takes a string of text as input and returns a dictionary
    containing the count of each word in the text and the length of the word.

    Args:
    text (str): A string of text

    Returns:
    dict_count (dict): A dictionary containing the count of each word in the text and
                       the length of the word.

    """
    x = ',.:;!?'
    clean_text = [word.strip(x).lower() for word in text.split() if word.strip(x).isalpha()]
    dict_count = {word: len(word) for word in clean_text}
    return dict_count




