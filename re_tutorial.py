# Python3 code to find sequences of one upper
# case letter followed by lower case letters
import re

PUNCTUATION=r"""!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""
name="bixby_routine_@alt"
print(bool(re.search(f"[#$%&()*+-.?@]+[A-Z]",name)))
