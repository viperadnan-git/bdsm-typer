import tkinter as tk
import webbrowser

from assets.icon import icon
from bdsm_typer import BDSMTyper

__version__ = "0.1.0"
bdsm_typer = BDSMTyper(mode=1)

root = tk.Tk()
root.title("BDSM Typer")
root.geometry("500x300")
root.resizable(False, False)

img = tk.PhotoImage(data=icon)
root.tk.call("wm", "iconphoto", root._w, img)


tk.Label(root, text="BDSM Typer", font=("Courier", 30, "bold")).pack()

link_to_profile = tk.Label(
    root, text="this ugly thing is created by viperadnan", fg="blue", cursor="hand2"
)
link_to_profile.pack()
link_to_profile.bind(
    "<Button-1>", lambda e: webbrowser.open_new("https://viperadnan-git.github.io")
)

updates_label = tk.Label(
    root, text=f"v{__version__} click here to see updates", cursor="hand2"
)
updates_label.pack()
updates_label.bind(
    "<Button-1>",
    lambda e: webbrowser.open_new(
        "https://github.com/viperadnan-git/bdsm-typer/releases"
    ),
)

tk.Label(
    root, text="Press right CTRL key to paste from clipboard", font=("Arial", 12)
).pack(pady=(0, 20))


mode_frame = tk.Frame(root)
mode_frame.pack(anchor=tk.W, padx=20)

tk.Label(mode_frame, text="Mode:", font=("Arial", 12)).pack(side=tk.LEFT)

for mode in bdsm_typer.modes:
    radio = tk.Radiobutton(
        mode_frame,
        text=mode.capitalize(),
        value=mode,
        font=("Arial", 12),
        command=lambda mode=mode: bdsm_typer.set_mode(mode),
    )
    radio.pack(side=tk.LEFT)
    if mode == bdsm_typer.mode:
        radio.select()


shortcut_frame = tk.Frame(root)
shortcut_frame.pack(anchor=tk.W, padx=20)

shortcut_key = tk.StringVar(value="Right Ctrl")

tk.Label(shortcut_frame, text="Shortcut key:", font=("Arial", 12)).pack(side=tk.LEFT)

for key in bdsm_typer.shortcut_keys:
    radio = tk.Radiobutton(
        shortcut_frame,
        text=key,
        value=key,
        font=("Arial", 12),
        command=lambda key=key: bdsm_typer.set_shortcut_key(key),
        variable=shortcut_key,
    )
    radio.pack(side=tk.LEFT)
    if key == bdsm_typer.shortcut_key:
        radio.select()


ruuning_label = tk.Label(
    root, text="BDSM Typer is running...", font=("Courier", 10, "bold"), fg="green"
)


is_enabled = tk.StringVar()
is_enabled.set("START")


def toggle():
    if is_enabled.get() == "START":
        bdsm_typer.start()
        is_enabled.set("STOP")
        ruuning_label.pack()
        print("BDSM Typer is enabled.")
    else:
        bdsm_typer.stop()
        is_enabled.set("START")
        ruuning_label.pack_forget()
        print("BDSM Typer is disabled.")


tk.Button(
    root, textvariable=is_enabled, font=("Arial", 12, "bold"), command=toggle, width=20
).pack(pady=15)


try:
    print("BDSM Typer is running...")
    root.mainloop()
except KeyboardInterrupt:
    pass
print("BDSM Typer is stopped.")
