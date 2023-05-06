import pyperclip
from pynput.keyboard import Controller, Key, Listener


class BDSMTyper:
    def __init__(self, mode="normal") -> None:
        self.typer = Controller()
        self.listener = None
        self.__modes = ["normal", "ace-editor"]
        self.set_mode(mode)

    def on_release(self, key):
        if key == Key.ctrl_r:
            self.paste_from_clipboard()

    def paste_from_clipboard(self):
        print("Pasting from clipboard using mode:", self.__mode)
        text = pyperclip.paste()
        if self.__mode == "ace-editor":
            textlines = text.split("\n")
            for line in textlines:
                with self.typer.pressed(Key.alt):
                    self.typer.press(Key.backspace)
                    self.typer.release(Key.backspace)
                self.typer.type(line)
        else:
            self.typer.type(text)

    def set_mode(self, mode):
        if mode in self.__modes or type(mode) == int and mode < len(self.__modes):
            if type(mode) == int:
                mode = self.__modes[mode]
            self.__mode = mode
            print("Mode set to:", mode)
        else:
            raise Exception("Invalid mode:", mode)

    def start(self):
        if self.listener:
            self.listener.stop()

        self.listener = Listener(on_release=self.on_release)
        self.listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
    

    @property
    def mode(self):
        return self.__mode

    @property
    def modes(self):
        return self.__modes