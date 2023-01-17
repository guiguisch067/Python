#! python3
# To convert text to a list of hex values, just use:

def text2hex(text: str) -> list[int]:
    return list(map(ord, text))
