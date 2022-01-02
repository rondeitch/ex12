import tkinter as tk
from gui_style import *


class Clock:

    def __init__(self, parent, time, callback, **kwargs):
        # callback #
        self.__callback = callback  # input function.
        # clock #
        self.__clock_frame = tk.Frame(parent)  # TODO: check if need to add **kwargs as param.
        self.__time = time  # time of the game.
        self.__time_minute = time // 60  # minute that left.
        self.__time_second = time % 60  # seconds left for specific minutes.
        self.__clock = self.create_clock(self.__time_minute, self.__time_second)  # create the clock
        # time_label #
        self.__time_label = self.create_time_label()  # label of 'Time: '
        # packing clock #
        self.__clock_frame.pack(**kwargs)  # Packing the clock. Gets the **kwargs as params.

    def create_time_label(self):
        """
        Label of the text- 'Time: '
        :return: Tk.Label (time_label)
        """
        time_label = tk.Label(self.__clock_frame, text='Time: ', **STYLES["clock"]["default"])
        time_label.pack(side=tk.LEFT, fill=tk.BOTH)
        return time_label

    def create_clock(self, minute, second):
        """
        Creat a clock for the game.
        :param minute: int
        :param second: int
        :return: clock (Tk.Label)
        """
        clock = self._init_clock(minute, second)
        clock.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        return clock

    def _init_clock(self, minute, second):
        """
        Initial the clock.
        :param minute: int
        :param second: int
        :return: Tk.Label (clock)
        """
        if self.__time_second >= 10:
            if self.__time_minute >= 10:
                clock = tk.Label(self.__clock_frame, text=str(minute) + ':' + str(second), **STYLES["clock"]["default"])
            else:
                clock = tk.Label(self.__clock_frame, text="0" + str(minute) + ':' + str(second),
                                 **STYLES["clock"]["default"])
        else:
            if self.__time_minute >= 10:
                clock = tk.Label(self.__clock_frame, text=str(minute) + ':0' + str(second),
                                 **STYLES["clock"]["default"])
            else:
                clock = tk.Label(self.__clock_frame, text="0" + str(minute) + ':0' + str(second),
                                 **STYLES["clock"]["default"])
        return clock

    def _clock_runner(self):
        """
        Run the time left for the game. If time ends the function operates the callback.
        :return: None
        """
        if self.__time == 0:
            self.__callback()
        self._clock_text_manage()
        if self._time_going_to_end():
            self._change_clock_color()
        self._run_clock()

    def _clock_text_manage(self):
        """
        Manage the text of the clock according to the time that left.
        :return: None
        """
        if self.__time_second >= 10:
            if self.__time_minute >= 10:
                self.__clock['text'] = str(self.__time_minute) + ':' + str(self.__time_second)
            else:
                self.__clock['text'] = "0" + str(self.__time_minute) + ':' + str(self.__time_second)
        else:
            if self.__time_minute >= 10:
                self.__clock['text'] = str(self.__time_minute) + ':0' + str(self.__time_second)
            else:
                self.__clock['text'] = "0" + str(self.__time_minute) + ':0' + str(self.__time_second)

    def _run_clock(self):
        """
        Run the clock time, and update it in __init__.
        :return: None
        """
        self.__time -= 1
        if self.__time_second > 0:
            self.__time_second -= 1
            self.__clock.after(1000, self._clock_runner)
        elif self.__time_minute > 0 and self.__time_second == 0:
            self.__time_minute -= 1
            self.__time_second = 59
            self.__clock.after(1000, self._clock_runner)

    def _time_going_to_end(self):
        """
        Checks if the time is before ending- the time we are determined.
        :return: bool
        """
        if self.__time_minute == 0 and self.__time_second <= 30:
            return True
        return False

    def _change_clock_color(self):
        self.__clock.configure(**STYLES['clock']['before_end'])
        self.__time_label.configure(**STYLES['clock']['before_end'])

    @property
    def time_left(self):
        """
        Return how much seconds left for the game.
        :return: int
        """
        return self.__time

    def start(self):
        """
        Operate _clock_runner that run the time, and at end operates callback.
        :return: None
        """
        self._clock_runner()


# TODO: delete this at end (debug helper).
def foo():
    print('hello world')


def main_root():
    root = tk.Tk()
    clo = Clock(root, 3, foo)
    clo.start()
    root.mainloop()


if __name__ == '__main__':
    main_root()
