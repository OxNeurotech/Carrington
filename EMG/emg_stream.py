"""
Taken from EMG Scrolling Tutorial on OPENBCI:
https://github.com/OpenBCI/OpenBCI_Tutorials/tree/master/EMG_Scrolling
"""

from pylsl import StreamInlet, resolve_stream
import pyautogui
import time

def main():

    # resolve an EMG stream on the lab network and notify the user
    print("Looking for an EMG stream...")
    streams = resolve_stream('type', 'EMG')
    print(len(streams))
    inlet = StreamInlet(streams[0])
    print("EMG stream found!")

    # initialize thresholds and variables for storing time 
    prev_time = 0
    flex_thres = 1.0

    while True:
        # get EMG data sample and its timestamp
        sample, timestamp = inlet.pull_sample()

        # get current time in milliseconds
        curr_time = int(round(time.time() * 1000))

        # if an EMG peak is detected from any of the arms 
        if (((sample[1] >= flex_thres) or (sample[0] >= flex_thres))):
            # update time 
            prev_time = int(round(time.time() * 1000))

            # scroll up or down depending on which peak is larger
            if sample[1] > 0.8 * sample[0]:
                pyautogui.scroll(10)
            elif sample[0] > 0.5 * sample[1]:
                pyautogui.scroll(-10)


if __name__ == "__main__":
    main()
