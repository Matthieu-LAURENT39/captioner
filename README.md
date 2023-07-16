[![Build](https://github.com/Matthieu-LAURENT39/captioner/actions/workflows/build.yml/badge.svg?branch=main&event=push)](https://github.com/Matthieu-LAURENT39/captioner/actions/workflows/build.yml)

# Captioner
A simple GUI program written in Qt and PySide6 to help caption images.

## Features
- Add text next to any side of the image.
- Live rendering, the changes you made immediately appear on the preview.
- Ability to use Markdown in the text.
- Easily change the border size and margin to adapt to any text length.
- Automatic text wrapping.
- Easy customisation of font, text color and background color.
- Standalone, no need to install anything.

## Installing

### Regular releases
Simply download the latest release for you operating system from the [release tab](https://github.com/Matthieu-LAURENT39/captioner/releases)

### Automatic builds
Builds are generated automatically with every commit, simply head to the [build action in the actions tab](https://github.com/Matthieu-LAURENT39/captioner/actions/workflows/build.yml), select the latest workflow run, and download the artifact for your OS.  
Do note that due to restrictions with github actions, this will download a zip file. The standalone executable will be in that zip.

### Running without compiling
You will need to have the following installed:
- Qt 6
- Python 3.11 or above
- The requirements from the `requirements.txt` file (you can install them with `pip install -r requirements.txt`)
- The source code of this repository to be downloaded on your PC

Once this is all setup, simply run the program by starting `run.py`

### Building it yourself
You will need to have setup everything from the [Running without compiling](#running-without-compiling) section.  
In addition, you must also setup the following:
- PyInstaller (You can install it with `pip install pyinstaller`.)

Once this is setup, you can use the following command to build the program:
`python -m PyInstaller --onefile --noconsole -n "Captioner" "./run.py"`


## License
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.