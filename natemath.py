#!/usr/bin/python3

# Title: Nate's Basic Math Module
# Author: Nathan Gregg
# Date: 2019.09.24


"""Basic Math Module written in Python3.  This module performs basic math 
operations.  Operations include addition, subsctraction, etc. but also numerical
base translations (i.e. binary to octal).


"""

import math

# Adds two values and returns a result
def addValue(value1, value2):

    """Adds two values 

    Parameters:
    value1 (int/float): Value 1 input
    value2 (int/float): Value 2 input

    Returns:
    float: result

   """

    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 must be of type integer or float.')
    result = value1 + value2
    return float(result)

# Substracts two values and returns a result
def subValue(value1, value2):

    """Substracts two values 

    Parameters:
    value1 (int/float): Value 1 input
    value2 (int/float): Value 2 input

    Returns:
    float: result

   """

    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 must be of type integer or float.')
    result = value1 - value2
    return float(result)

# Multiplies two values and returns a result
def multiValue(value1, value2):

    """Multiplies two values 

    Parameters:
    value1 (int/float): Value 1 input
    value2 (int/float): Value 2 input

    Returns:
    float: result

   """

    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 must be of type integer or float.')
    result = value1 * value2
    return float(result)

# Divides value 1 by value 2 and returns the result
def divValue(value1, value2):

    """Divides value1 by value2

    Parameters:
    value1 (int/float): Value 1 input
    value2 (int/float): Value 2 input

    Returns:
    float: result

   """

    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 must be of type integer or float.')
    result = value1 / value2
    return float(result)

# Finds square root of a value
def sqrtValue(value):

    """Finds square root of value

    Parameters:
    value (int/float): Value input

    Returns:
    float: result

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type integer or float')
    result = math.sqrt(value);
    return float(result)

# Find exponent value ( i.e. value1^(value2))
def expValue(value1, value2):

    """Finds exponent of value

    Parameters:
    value1 (int/float): Value 1 input
    value2 (int/float): Value 2 input

    Returns:
    float: result

   """

    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 must be of type integer or float.')
    result = value1 ** value2
    return float(result)

# Returns octal value as int
def oct2Int(value):

    """Converts octal value to integer

    Parameters:
    value (int): Value input as octal

    Returns:
    str: Returns value as integer

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type octal')
    result = int(value)
    return result

# Returns hexadecimal as int
def hex2Int(value):

    """Converts hexadecimal value to integer

    Parameters:
    value (int): Value input as hexadecimal

    Returns:
    str: Returns value as integer

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type hex')
    result = int(value)
    return result

# Returns binary as int
def bin2Int(value):

    """Converts binary value to integer

    Parameters:
    value (int): Value input as binary

    Returns:
    str: Returns value as integer

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type binary')
    result = int(value)
    return result

# Returns hex as oct
def hex2Oct(value):

    """Converts hexadecimal value to octal

    Parameters:
    value (int): Value input as hexadecimal

    Returns:
    str: Returns value as octal

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type hexadeciman')
    result = oct(value)
    return result

# Returns int as oct
def int2Oct(value):

    """Converts integer value to octal

    Parameters:
    value (int): Value input as integer

    Returns:
    str: Returns value as octal

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type integer')
    result = oct(value)
    return result

# Returns bin as oct
def bin2Oct(value):

    """Converts binary value to octal

    Parameters:
    value (int): Value input as binary

    Returns:
    str: Returns value as octal

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type binary')
    result = oct(value)
    return result

# Returns oct as hex
def oct2Hex(value):

    """Converts octal value to hexadecimal

    Parameters:
    value (int): Value input as octal

    Returns:
    str: Returns value as hexidecimal

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type octal')
    result = hex(value)
    return result

# Returns int as hex
def int2Hex(value):

    """Converts integer value to hexadecimal

    Parameters:
    value (int): Value input as integer

    Returns:
    str: Returns value as hexadecimal

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type integer')
    result = hex(value)
    return result

# Returns bin as hex
def bin2Hex(value):

    """Converts binary value to hexadecimal

    Parameters:
    value (int): Value input as binary

    Returns:
    str: Returns value as hexadecimal

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type binary')
    result = hex(value)
    return result

# Returns oct as bin
def oct2Bin(value):

    """Converts octal value to binary

    Parameters:
    value (int): Value input as octal

    Returns:
    str: Returns value as binary

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type octal')
    result = bin(value)
    return result

# Returns int as bin
def int2Bin(value):

    """Converts integer value to binary

    Parameters:
    value (int): Value input as binary

    Returns:
    str: Returns value as binary

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type integer')
    result = bin(value)
    return result

# Returns hex as bin
def hex2Bin(value):

    """Converts hexadecimal value to binary

    Parameters:
    value (int): Value input as hexadecimal

    Returns:
    str: Returns value as binary

   """

    if isinstance(value, (str, complex, bool)):
        raise Exception('value must be of type hexadecimal')
    result = bin(value)
    return result
