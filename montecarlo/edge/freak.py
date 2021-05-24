# freak.py
#   Provides functions for frequencies, rather than simply sample spaces.
#
#   Simple example:
#       Given n dice rolls, return relative frequencies for given events.
#
# Imports
import collections


def get_sample_space(events, *dtype):
    """Returns a dict{}(?) containing all unique elements of the data and their frequencies.

    Parameters:
        events = data
        dtype = data type of events
            We currently use a simple list. We also currently assume randomness.

    Returns:
        Currently, dict{}
    """

    if dtype is not None:
        return collections.Counter(events)


def p_event(events, sample_space):
    """Returns probability (real number) between 0 and 1 for given events in sample_space, n times.

    Example: events = { "H", "T" } how many times out of sample_space?
    IE: frequencies

    Parameters:
        events = events we are interested in
        sample_space = total sample space (iterable)

    Returns:
        Iterable of real numbers between 0 and 1 representing probabilities of events
    """
    pass
