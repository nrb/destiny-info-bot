from collections import namedtuple


Strike = namedtuple('Strike', ('name', 'terms'))


class UnknownStrikeError(Exception):
    """Signals that the description text could not be matched to a strike."""


DEVILS_LAIR = Strike("The Devil's Lair", ("sepiks",))
WILL_OF_CROTA = Strike("Will of Crota", ("omnigul",))
SUMMONING_PITS = Strike("The Summoning Pits", ("abomination", "pit"))
NEXUS = Strike("The Nexus", ("golden age", "academy"))
WINTERS_RUN = Strike("Winter's Run", ("archon", "house of winter", "prison of elders"))
CERBERUS_VAE_III = Strike("Cerberus Vae III", ("valus ta'aurc", "freehold"))
DUST_PALACE = Strike("Dust Palace", ("psion flayers", "martian warmind", "cabal"))
UNDYING_MIND = Strike("Undying Mind", ("ancient mind", "black garden"))
SHADOW_THIEF = Strike("The Shadow Thief", ("ketch", "taniks"))
STRIKES = (
    DEVILS_LAIR,
    WILL_OF_CROTA,
    SUMMONING_PITS,
    NEXUS,
    WINTERS_RUN,
    CERBERUS_VAE_III,
    DUST_PALACE,
    UNDYING_MIND,
    SHADOW_THIEF,
)


def get_short_name(description):
    """Searches strike description text for identifying terms.

    :param description: text to search.
    :returns: Short name for the strike.
    :raises UnknownStrikeError: if no matching strike name is found.
    """
    text = description.lower()
    for match in (s for s in STRIKES if all(term in text for term in s.terms)):
        return match.name
    else:
        raise UnknownStrikeError


__all__ = (
    'get_short_name',
    'UnknownStrikeError',
    'DEVILS_LAIR',
    'WILL_OF_CROTA',
    'SUMMONING_PITS',
    'NEXUS',
    'WINTERS_RUN',
    'CERBERUS_VAE_III',
    'DUST_PALACE',
    'UNDYING_MIND',
    'SHADOW_THIEF',
)
