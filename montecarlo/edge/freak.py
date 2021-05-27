# freak.py
#   Provides functions for frequencies, rather than simply sample spaces.
#
#   Simple example:
#       Given n dice rolls, return relative frequencies for given events.
#
# Imports
import collections
import itertools


def frequencies(outcomes):
    """Returns a dict{}(?) containing all unique elements of the data and their frequencies.

    Parameters:
        events = data
        dtype = data type of events
            We currently use a simple list. We also currently assume randomness.

    Returns:
        Currently, dict{}
    """
    if type(outcomes) is not None:
        # Return all of the items in Counter
        return collections.Counter(outcomes).items()


def groups(outcomes, g = True):
    """Generates a list of groups of outcomes.

    Example: [ "H", "H", "T", "T", "H", "H", "H", "H", "T", "T" ]

    ["H", 2]
    ["T", 2]
    ["H", 4]
    ["T", 2]

    Parameters:
        outcomes = iterable of outcomes
        g = True for generator
    """
    if g:
        for val, streak in itertools.groupby(outcomes):
            yield [val, sum([1 for _ in streak])]
    else:
        return [[val, sum([1 for _ in streak])] for val, streak in itertools.groupby(outcomes)]


def p_event(outcomes):
    """Returns probability (real number) between 0 and 1 for given events in sample_space, n times.

    Example: events = { "H" , "T" } how many times out of sample_space?
    IE: frequencies

    Parameters:
        outcomes = data containing outcomes of trials

    Returns:
        Iterable of real numbers between 0 and 1 representing probabilities of events
    """
    # collections.Counter returns a dict of all outcomes and the respected frequencies
    c = collections.Counter(outcomes)

    # convert the dictionary to one of probabilities instead
    return dict((key, value / sum(c.values())) for (key, value) in c.items())
