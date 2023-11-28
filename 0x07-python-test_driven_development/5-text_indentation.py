 #!/usr/bin/python3
"""module contains a function to split text according to delimiters"""


def text_indentation(text):
    """This function splits text wherever there is a '.', '?' or ':'

    Args:
        text (str): the input string
    
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            print()
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1



if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')