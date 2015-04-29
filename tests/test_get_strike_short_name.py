import pytest
import strike

# In-game descriptions pulled from the internet
DEVILS_LAIR = """The Fallen House of Devils in the Cosmodrome sustain their strength through a single, exalted Servitor known as Sepiks Prime. Find where this keeper of souls lies and destroy him."""
WILL_OF_CROTA = """Omnigul, the mastermind of Crota's armies, nests in the Cosmodrome. Eliminate this horror and purge its spawn."""
SUMMONING_PITS = """Deep within the Hellmouth, the Hive are breeding powerful abominations to unleash upon the Earth. Find the pit where they live and stop any new horrors from rising."""
NEXUS = """The Golden Age legends tell of ancient tunnels below the Academy, where a Vex machine once ate away at the planet. Descend into the old dig sites and find this Nexus before it churns again."""
WINTERS_RUN = """As the Vex march to claim the Ishtar Sink, the Fallen House of Winter are raising a powerful Archon, stolen from the Prison of Elders in the Reef. Find the Archon before they fully restore his soul."""
CERBERUS_VAE_III = """Just beyond their warbase, Valus Ta'aurc, Fleet Commander of the Cabal Siege Dancers, hides in an Imperial Land Tank. Fight through his guard and stop this terror before he destroys all of Freehold."""
DUST_PALACE = """A new Cabal force has unleashed powerful Psion Flayers to seize control of the old Martian Warmind. Face this new threat and secure what remains of the ancient network."""
UNDYING_MIND = "An ancient Mind, feared by the Vex themselves, hides among the channels of the Black Garden. Find this machine and end its existence."
# and then there was this...
PREDATOR = """Dutch (Arnold Schwarzenegger), a soldier of fortune, is hired by the U.S. government to secretly rescue a group of politicians trapped in Guatemala. But when Dutch and his team, which includes weapons expert Blain (Jesse Ventura) and CIA agent George (Carl Weathers), land in Central America, something is gravely wrong. After finding a string of dead bodies, the crew discovers they are being hunted by a brutal creature with superhuman strength and the ability to disappear into its surroundings."""


def test_devils_lair():
    assert strike.DEVILS_LAIR.name == strike.get_short_name(DEVILS_LAIR)


def test_will_of_crota():
    assert strike.WILL_OF_CROTA.name == strike.get_short_name(WILL_OF_CROTA)


def test_summoning_pits():
    assert strike.SUMMONING_PITS.name == strike.get_short_name(SUMMONING_PITS)


def test_nexus():
    assert strike.NEXUS.name == strike.get_short_name(NEXUS)


def test_winters_run():
    assert strike.WINTERS_RUN.name == strike.get_short_name(WINTERS_RUN)


def test_cerberus_vae_iii():
    assert strike.CERBERUS_VAE_III.name == strike.get_short_name(CERBERUS_VAE_III)


def test_dust_palace():
    assert strike.DUST_PALACE.name == strike.get_short_name(DUST_PALACE)


def test_undying_mind():
    assert strike.UNDYING_MIND.name == strike.get_short_name(UNDYING_MIND)


def test_predator():
    with pytest.raises(strike.UnknownStrikeError):
        strike.get_short_name(PREDATOR)
