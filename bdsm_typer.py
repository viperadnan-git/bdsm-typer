import pyperclip
from pynput.keyboard import Controller, Key, Listener


class BDSMTyper:
    def __init__(
        self, mode="normal", shortcut_key="Right Ctrl", line_break=True
    ) -> None:
        self.typer = Controller()
        self.listener = None
        self.__modes = ["normal", "ace-editor"]
        self.__keys_map = {
            "Esc": Key.esc,
            "Right Ctrl": Key.ctrl_r,
            "Right Shift": Key.shift_r,
        }
        self.__line_break = line_break
        self.set_mode(mode)
        self.set_shortcut_key(shortcut_key)

    def on_release(self, key):
        if key == self.__shortcut_key:
            self.paste_from_clipboard()

    def paste_from_clipboard(self):
        print("Pasting from clipboard using mode:", self.__mode)
        text = pyperclip.paste()
        if self.__mode == "ace-editor":
            textlines = text.split("\n")
            for line in textlines:
                with self.typer.pressed(Key.alt):
                    self.typer.tap(Key.backspace)
                self.typer.type(line)
                if self.__line_break:
                    self.typer.tap(Key.enter)
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

    def set_shortcut_key(self, key):
        if key in self.__keys_map.keys():
            self.__shortcut_key = self.__keys_map[key]
            print("Shortcut key set to:", key)
        else:
            raise Exception("Invalid shortcut key:", key)

    def set_line_break(self, line_break):
        self.__line_break = bool(line_break)
        print("Line break set to:", bool(line_break))

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

    @property
    def shortcut_key(self):
        for key, value in self.__keys_map.items():
            if value == self.__shortcut_key:
                return key

    @property
    def shortcut_keys(self):
        return list(self.__keys_map.keys())
