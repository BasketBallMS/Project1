from PyQt6.QtWidgets import *
from PyQt6.uic import *
from PyQt6.QtGui import *

from Project1 import *


class Television(QMainWindow, Ui_MainWindow):
    """
    A class representing a basic Television with power, volume, channel, and mute functionality
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 1
    MAX_CHANNEL = 9

    def __init__(self) -> None:
        """
        Initializes a Television objects with default values
        """
        super().__init__()
        self.setupUi(self)
        loadUi("Project1.ui",self)
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__prev_volume = self.__volume
        self.Button_Power.clicked.connect(self.power)
        self.Button_Mute.clicked.connect(self.mute)
        self.Channel_UP.clicked.connect(self.channel_up)
        self.Channel_Down.clicked.connect(self.channel_down)
        self.Volume_Up.clicked.connect(self.volume_up)
        self.Volume_Down.clicked.connect(self.volume_down)
        self.Channel_1.clicked.connect(lambda: self.visual_channel(1))
        self.Channel_2.clicked.connect(lambda: self.visual_channel(2))
        self.Channel_3.clicked.connect(lambda: self.visual_channel(3))
        self.Channel_4.clicked.connect(lambda: self.visual_channel(4))
        self.Channel_5.clicked.connect(lambda: self.visual_channel(5))
        self.Channel_6.clicked.connect(lambda: self.visual_channel(6))
        self.Channel_7.clicked.connect(lambda: self.visual_channel(7))
        self.Channel_8.clicked.connect(lambda: self.visual_channel(8))
        self.Channel_9.clicked.connect(lambda: self.visual_channel(9))
        image = QPixmap("TV_Images/BLACKSCREEN.png")
        self.imgLabel.setPixmap(image)
        self.Volume_Bar.setVisible(False)

    def power(self) -> None:
        """
        Turns the Television on or off
        """
        self.__status = not self.__status
        if not self.__status:
            image = QPixmap("TV_Images/BLACKSCREEN.png")
            self.imgLabel.setPixmap(image)
            self.Volume_Bar.setVisible(False)

        if self.__status:
            self.visual_channel(self.__channel)
            self.Volume_Bar.setVisible(True)



    def mute(self)-> None:
        """
        Mutes or unmutes the television, but only if the TV is on.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.Volume_Bar.setVisible(False)
            else:
                self.__muted = False
                self.__volume = self.__prev_volume
                self.Volume_Bar.setVisible(True)

    def visual_channel(self, channel_number):
        """
        Displays the channel onto the label.
        AI helped me by describing to me best way to display an image onto a label.
        :param channel_number:
        """
        if self.__status:
            self.__channel = channel_number
            TV_Channels = {1: "TV_Images/ABC.jpg", 2: "TV_Images/CNN.jpg", 3: "TV_Images/ESPN.png",
                           4: "TV_Images/HULU.png", 5: "TV_Images/KETV.jpg", 6: "TV_Images/NBC.png",
                           7: "TV_Images/NETFLIX.png", 8: "TV_Images/NFLNETWORK.jpg", 9: "TV_Images/YouTube.png"}
            image_file = TV_Channels.get(channel_number)
            if image_file:
                image = QPixmap(image_file)
                resized_image = image.scaled(161,71)
                self.imgLabel.setPixmap(resized_image)



    def channel_up(self)-> None:
        """
        Brings the channel up in increments of 1
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
            self.visual_channel(self.__channel)

    def channel_down(self)-> None:
        """
        Brings the channel down in increments of 1
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
            self.visual_channel(self.__channel)

    def volume_up(self)-> None:
        """
        Brings the volume up in increments of 1
        """
        if self.__status:
            if not self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1
                    self.Volume_Bar.setProperty("value", self.__volume)
                    self.__prev_volume = self.__volume
                else:
                    self.__volume = Television.MAX_VOLUME


    def volume_down(self)-> None:
        """
        Brings the volume down in increments of 1
        """
        if self.__status:
            if not self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1
                    self.Volume_Bar.setProperty("value", self.__volume)
                    self.__prev_volume = self.__volume
                else:
                    self.__volume = Television.MIN_VOLUME






