# event.py
#   The event module implements simple probabilistic functions, using simple constructed sample spaces.
#
#   This module is subject to change.

# Imports
import itertools


def event_space(sample_space):
    """Returns a powerset (IE all subsets) of the sample space (that is, the collection of events).

    Example: event_space([1, 2, 3]) returns all subsets of [1, 2, 3]

    Parameters:
        sample_space = iterable
    """

    return itertools.chain.from_iterable(itertools.combinations(sample_space, r) for r in range(len(sample_space) + 1))


def combos(sample_space, n, r = True, order = False):
    """Uses a generator to return all combinations of given sample_space of n-length.

    Parameters:
        n = length of combo
        r = replacement?
        g = generator? (test)
    """
    if order:
        for combo in itertools.product(sample_space, n):
            yield combo
    elif r:
        for combo in itertools.combinations_with_replacement(sample_space, n):
            yield combo
    else:
        for combo in itertools.combinations(sample_space, n):
            yield combo


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
    """
    # return [True for event in set(events) if event in set(sample_space)]
    return [event for event in events if event in sample_space]
    # return [True if event in set(events) else False for event in set(sample_space)]


def p_event(events, sample_space):
    """Returns probability (real number) between 0 and 1 for given events in sample_space.

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
        return len([e for e in events if e in sample_space]) / len(sample_space)
