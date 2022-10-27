from character import Character
def test_character_name():
    Mason = Character('Mason')
    assert Mason.name == 'Mason'

def test_character_alignment():
    Mason = Character('Mason')
# def test_character_alignment():