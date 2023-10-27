import pytest
from chifoumy import gagnant

def test_egalite():
    assert gagnant("pierre","pierre") == 0,0
    assert gagnant("ciseaux","ciseaux") == 0,0
    assert gagnant("papier","papier") == 0,0

def test_OrdiGagnant():
    assert gagnant("ciseaux","pierre") == 0,1
    assert gagnant("papier","ciseaux") == 0,1
    assert gagnant("pierre","papier") == 0,1

test_egalite()