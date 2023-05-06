import tkinter as tk
from assets.icon import icon
from bdsm_typer import BDSMTyper
import webbrowser

__version__ = "0.1.0"
bdsm_typer = BDSMTyper(mode=1)

root = tk.Tk()
root.title("BDSM Typer")
root.geometry("500x300")
root.resizable(False, False)

img = tk.PhotoImage(data=icon)
root.tk.call('wm', 'iconphoto', root._w, img)


tk.Label(root, text="BDSM Typer", font=("Courier", 30, "bold")).pack()

link_to_profile = tk.Label(root, text="this ugly thing is created by viperadnan", fg="blue", cursor="hand2")
link_to_profile.pack()
link_to_profile.bind("<Button-1>", lambda e: webbrowser.open_new("https://viperadnan-git.github.io"))


updates_label = tk.Label(root, text="v0.1.0 click here to see updates", cursor="hand2")
updates_label.pack()
updates_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/viperadnan-git/bdsm-typer/releases"))


tk.Label(
    root, text="Press right CTRL key to paste from clipboard", font=("Arial", 12)
).pack()


is_enabled = tk.StringVar()
is_enabled.set("START")


tk.Label(root, text="Mode:", font=("Arial", 12)).pack(anchor=tk.W)
for mode in bdsm_typer.modes:
    radio = tk.Radiobutton(
        root,
        text=mode.capitalize(),
        value=mode,
        font=("Arial", 12),
        command=lambda mode=mode: bdsm_typer.set_mode(mode),
    )
    radio.pack(anchor=tk.W)
    if mode == bdsm_typer.mode:
        radio.select()

ruuning_label = tk.Label(
    root, text="BDSM Typer is running...", font=("Courier", 10, "bold"), fg="green"
)


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
