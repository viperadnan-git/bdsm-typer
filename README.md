# BDSMTyper

BDSMTyper is a software tool that allows you to copy and paste text on websites where pasting is not allowed. Works perfectly on ACE Editor and supports pasting on any website using the right control key of the keyboard. BDSMTyper is a single executable file that can be run with just one click, without any installation.

## Features

-   Copy and paste text on websites where pasting is not allowed
-   Supports pasting on any website using the right control key of the keyboard
-   Works on ACE Editor which is widely used in web-based text editor
-   Single executable file that can be run with just one click, without any installation
-   Additional Features:
    -  Line spacing after each line
    -  Remove auto completion brackets
    -  Purge before pasting
-   Open source and free to use
-   No installation required
-   No admin privileges required


## How to use

1. Download the BDSMTyper executable file from the Releases section of this repository.
2. Run the BDSMTyper executable file.
3. In order to paste text on a website where pasting is not allowed, click on START button to activate the BDSMTyper editor.
4. Copy the text you want to paste on the website to the clipboard.
5. Click on the right control key of your keyboard to paste the copied text on the website.

## Build

To build BDSMTyper from the source code, you will need to have PyInstaller installed. PyInstaller is a Python package that can be used to convert Python scripts into standalone executable files.

To install PyInstaller, run the following command:

```
pip install pyinstaller
```

Once PyInstaller is installed, you can use the build.sh script to build the BDSMTyper executable file. To do so, follow these steps:

1. Open a terminal window and navigate to the root directory of the BDSMTyper project.
2. Run the following command to make the build.sh script executable:

```
chmod +x build.sh
```

3. Run the build.sh script by executing the following command:

```
./build.sh
```

4. The build process will start, and once it's complete, you'll find the BDSMTyper executable file in the `dist` directory.

## License

BDSMTyper is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE) for more information.

## Contributing

Contributions to BDSMTyper are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for more information on how to get started.

## Contact

If you have any questions or comments, please feel free to reach out to us at viperadnan@gmail.com.
