import base64
import sys

debug = False

"""
Encrypt code pulled from https://github.com/WP-LKL/bscValueDefi-Exploit
"""


def obfuscate(txt: str) -> bytes:
    """
    Over-shoulder "attack" protection.
    Customize in utils.py and here.
    """
    obfuscated = base64.b64encode(txt.encode("utf-8"))
    if debug:
        print(f"obfuscate()   input: {txt}. Output: {obfuscated}")
    return obfuscated


def deObfuscate(txt: bytes):
    deObf = base64.b64decode(txt)
    if debug:
        print(f"deObfuscate() input: {txt}. Output: {deObf}")
    return deObf.decode("utf-8")


def verifyKey(txt) -> bool:
    obf = obfuscate(txt)
    deObf = deObfuscate(obf)
    if debug:
        print(f"verifyKey()   input: {txt}. Output: {deObf}")
    return txt == deObf


def main():
    key = sys.argv[1]
    assert verifyKey(key), "ERROR: Could not verify base64-pair"
    print(obfuscate(key))


if __name__ == "__main__":
    main()
