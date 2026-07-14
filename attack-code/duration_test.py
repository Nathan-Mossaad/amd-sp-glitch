# duration_test.py
import teensy

gs = teensy.GlitchSetup(
    # Use the serial port of your Teensy device
    teensy.TeensyClient("/dev/ttyACM0"),
)

# Connect to the teensy and set some parameters
gs.start()

gs.attack_range(
    # perform 300 attacks
    count=100000,
    # cs pulses to wait
    waits=31,
    # vid of the attack
    vid=0xC0,
    # sample the delay from the interval [delay_min, delay_max[
    delay_min=13132,
    delay_max=15035,
    # sample the duration from the interval [dur_min, dur_max[
    dur_min=12350,
    dur_max=12370,
)
