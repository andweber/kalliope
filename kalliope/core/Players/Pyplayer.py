# -*- coding: utf-8 -*-
# modified sample code taken from https://people.csail.mit.edu/hubert/pyaudio/docs/
import pyaudio
import wave
import time
import logging

logging.basicConfig()
logger = logging.getLogger("kalliope")

CHUNK = 1024


class Pyplayer(object):
    """
    This Class is representing the Player Object used to play the all sound of the system.
    """


    def __init__(self):
        pass

    @classmethod
    def play(cls, filepath):
        """
        Play the sound located in the provided filepath

        :param filepath: The file path of the sound to play
        :type filepath: str

        :Example:

            Pyplayer.play(self.file_path)

        .. seealso::  TTS
        .. raises::
        .. warnings:: Class Method and Public
        """

        wf = wave.open(filepath, 'rb')

        # instantiate PyAudio
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

        # read data
        data = wf.readframes(CHUNK)

        logger.debug("Pyplayer cmd: %s" % str(filepath))

        # play stream (3)
        while len(data) > 0:
               stream.write(data)
               data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()


        # close PyAudio
        p.terminate()

    @classmethod
    def print_device_info(self, verbose=False):
       logger.debug("using simple pyplayer stream")
