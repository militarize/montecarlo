# event.py
#   The event module implements simple probabilistic functions, using simple constructed sample spaces.
#
#   This module is subject to change.

# Imports
import itertools
import math


def event_space(sample_space):
    """Returns a powerset (IE all subsets) of the sample space (that is, the collection of events).

    Example: event_space([1, 2, 3]) returns all subsets of [1, 2, 3]

    Parameters:
        sample_space = iterable
    """

    return itertools.chain.from_iterable(itertools.combinations(sample_space, r) for r in range(len(sample_space) + 1))


def combos(sample_space, n, repeat = True, order = False):
    """Uses a generator to return all combinations of given sample_space of n-length.

    Parameters:
        n = length of combo
        r = replacement?
        g = generator? (test)
    """
    if order:
        for combo in itertools.product(sample_space, n):
            yield combo
    elif repeat:
        for combo in itertools.combinations_with_replacement(sample_space, n):
            yield combo
    else:
        for combo in itertools.combinations(sample_space, n):
            yield combo


def n_combos(n, r, repeat = True):
    """nCr: Returns number of combinations for choosing r items from n, repetition optional."""
    f = math.factorial      # Alias math.factorial

    if repeat:
        return f(r + n - 1) // (f(r) * f(n - 1))
    else:
        return f(n) // (f(r) * f(n - r))


def n_perms(n, r, repeat = True):
    """nPr: Returns number of permutations for choosing r items from n, repetition optional."""
    f = math.factorial

    if repeat:
        return n**r
    else:
        return f(n) // f(n - r)


def self_select(sample_space, n):
    """Returns self-selected random sample of n outcomes.

    Example: coin flip of n = 1000 times

    Parameters:
        sample_space = the base sample space of items to be selected
        n = number of trials

    Returns:
        dict for now
    """
    pass


def is_event(events, sample_space):
    """Returns boolean value indicating if given events are in the sample space.

    Parameters:
        events = collection of outcomes
        sample_space = iterable collection representing sample_space

    Notes:
        - set{} has issubset() method also
            - trying to keep this flexible
    """
    # return [True for event in set(events) if event in set(sample_space)]
    return [event for event in events if event in sample_space]
    # return [True if event in set(events) else False for event in set(sample_space)]
    # return [event.issubset(sample_space)]


def p_event(events, sample_space):
    """Returns probability (real number) between 0 and 1 for given events in sample_space for a single trial.

    If sample_space == dict{}, we assume the values represent weights.

    WARNING: The method currently does no type checking (or makes any assurances that the
    weights and associated probabilities follow first principles.

    Parameters:
        events = collection of outcomes to obtain probability on
        sample_space = collection of all possible outcomes
    """
    if isinstance(sample_space, dict):
        # Returns a sum of the weights of all the events that are in the sample_space,
        # divided by the total sum of the weights.
        return sum([events[e] for e in events if e in sample_space]) / sum(sample_space.values())
        # Otherwise:
    else:
        # Returns the count of all events in the sample_space,
        # divided by the total len of the sample_space.
        return sum([1 for e in events if e in sample_space]) / len(sample_space)
