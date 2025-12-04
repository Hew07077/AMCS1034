import sys 
import os

sys.path.append(os.path.abspath.join(os.path.join(os.path.dirname(__file__),'..')))
                                                  
print ("Updated sys.path:", sys.path)

from mypalindrome import *
from Q1.myinputtreaders import *

def main():
    text = input("Enter a string:").strip()
    print("{} {} a palindrome".format(text,"is" if is_palindrome(text))))
                                       
main()