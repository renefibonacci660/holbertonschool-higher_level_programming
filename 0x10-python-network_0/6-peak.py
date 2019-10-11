#!/usr/bin/python3
""" Test function for find_peak with the lowest time complexity """


def find_peak(list_of_integers):
    """ Uses binary search function to find peak """
    if len(list_of_integers) == 0:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while (left < right):
        mid = int((left + right) / 2)
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    peak = left

    return list_of_integers[peak]
