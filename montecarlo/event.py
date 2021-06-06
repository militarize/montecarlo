# event.py
#   Utilizes sets (or weighted dicts) to calculate probabilities for events in sample spaces containing outcomes.
#
#####
# Imports
import fractions
import itertools
import random


def P(event, sample_space, frac = False):
    """Returns probability of event in sample space for one trial.

    Will implemented weighted dict.
    """
    if isinstance(sample_space, dict):
        p = sum([sample_space[e] if e in sample_space else 0 for e in event]) / sum(sample_space.values())
    else:
        p = len(sample_space.intersection(event)) / len(sample_space)
    return fractions.Fraction(p) if frac else p


def NOT(event, sample_space):
    """Returns subset of events from set of samples that are NOT in the subset event."""
    return sample_space - event


def OR(A, B):
    """Returns events that are in A OR B."""
    return A.union(B)


def AND(A, B):
    """Returns events that are in A AND B."""
    return A.intersection(B)


def sample(sample_space, n):
    """Returns sample of events from sample_space."""
    if isinstance(sample_space, dict):
        return random.choices(sample_space, weights = [weight for weight in sample_space.values()], k = n)
    else:
        return random.choices(sample_space, k = n)


def powerset(sample_space):
    """Returns all the subsets of the sample_space set.

    Retrieves combinations of r length, starting from r = 0 (IE empty subset).

    Parameters:
        sample_space = expects a set

    Returns:
        Chained combinations.
    """
    return itertools.chain.from_iterable(itertools.combinations(sample_space, r) for r in range(len(sample_space) + 1))
