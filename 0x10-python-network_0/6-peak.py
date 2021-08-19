#!/usr/bin/python3
"""Program that finds the peak"""

def find_peak(list_of_integers):
    """find a peak in a list of unsorted integers"""
    if len(list_of_integers) is 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
