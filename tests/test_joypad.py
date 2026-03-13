import modules.joypad as joypad
from modules.joypad import ROCKSMASH, SURF, CUT, WATERFALL

def test_getHmInputs_RockSmash():
    surfInputs = joypad.getHmInputs(ROCKSMASH, "?")
    exceptedInputs = (8 * "?" + 6 * "@" + 5 * "@" + 5 * "A"
        + 80 * "@" + 5 * "A" + 40 * "@" + 5 * "A" + 125 * "@" + 100 * "@"
    )

    assert surfInputs == exceptedInputs

def test_getHmInputs_Cut():
    cutInputs = joypad.getHmInputs(CUT, "?")
    exceptedInputs = (8 * "?" + 6 * "@" + 5 * "@" + 5 * "A"
        + 80 * "@" + 5 * "A" + 40 * "@" + 5 * "A" + 125 * "@" + 100 * "@"
    )

    assert cutInputs == exceptedInputs

def test_getHmInputs_Surf():
    rockSmashInputs = joypad.getHmInputs(SURF, "?")
    exceptedInputs = (8 * "?" + 6 * "@" + 5 * "@" + 5 * "A"
        + 70 * "@" + 5 * "A" + 30 * "@" + 5 * "A" + 125 * "@" + 30 * "@"
    )

    assert rockSmashInputs == exceptedInputs

def test_getHmInputs_Waterfall():
    waterfallInputs = joypad.getHmInputs(WATERFALL, "?")
    exceptedInputs = (8 * "?" + 6 * "@" + 5 * "@" + 5 * "A"
        + 70 * "@" + 5 * "A" + 35 * "@" + 5 * "A" + 125 * "@" + 215 * "@"
    )

    assert waterfallInputs == exceptedInputs



