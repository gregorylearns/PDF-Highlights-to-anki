# PDF Highlights to Anki 📚

[![License](https://img.shields.io/badge/License-GNU%20GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0)

**Current Version:** 0.0.4 (Alpha Stage) 🚧

Convert PDF Expert annotations from iOS app into Anki cards. Highlighted text becomes cards, and those with red underlines become cloze deletions. Exports to .apkg format.

## Description

This tool is designed to extract annotations made in the iOS app PDF Expert and convert them into Anki flashcards. It can recognize highlighted text as regular cards and text with red underlines as cloze deletions.

## Features

- Convert PDF Expert annotations to Anki flashcards.
- Supports both highlighted text and red underlines.
- Export your flashcards in .apkg format for easy use in Anki.

## Important Notes

- This project is currently in its alpha stage, so please expect bugs and issues.
- There is no warranty provided with this software.
- Contributions and suggestions for improvements are welcome! Feel free to submit a pull request.

## Instructions

1. **Download PDF Expert**: Get the PDF Expert app on your iOS or Android device.
2. **Annotation Tools**: Use the text highlight tool and text underline tool in PDF Expert. Avoid using the freehand highlight/underline tool, as it may not extract the text effectively.
3. **Export Annotations**: Export your annotations by going to "Annotations Summary" in PDF Expert.
4. **Run the Tool**:
   - Download and run a binary (`.exe`) from the [Releases](https://github.com/gregorylearns/PDF-Highlights-to-anki/releases) page
   - Use `gui.pyw` for a graphical user interface.
   - Alternatively, you can use the [command line](## Command Line Interface (CLI) Usage).
5. **Run with HTML**: Use the exported HTML file with the tool.
6. **Open the .apkg File**: After processing, you can find the generated .apkg file in the "anki_converted" folder.
7. **???**
8. **Profit!** 💰

**Note:** All cloze deletions are enclosed within `c1::`. If you wish to create more cloze cards (e.g., `c2::`, `c3::`, etc.), you can manually edit them in the Anki note editor.

## Disclaimer

- This tool is specifically designed for PDF Expert and has been tested on iOS PDF Expert (Free version) and Windows 10. It has not been tested on MacOS or Linux.
- It does NOT work with GoodNotes because it doesn't have a text highlight feature.
- Javascript/Python web-hosted version so conversion can be done on web browser.

## Future Roadmap

- The future roadmap includes support for exporting annotation summaries from other apps such as Foxit PDF and more.

## Building Instructions 🛠️

To build the PDF Highlights to Anki application from source code, follow these steps:

1. Install the necessary dependencies, including PySimpleGUI, BeautifulSoup4, Genanki, and PSG Compiler:

   ```bash
   pip install psgcompiler beautifulsoup4 genanki pysimplegui
   ```

2. Launch the PSG Compiler:

   ```bash
    psgcompiler
   ```

3. In the PSG Compiler window that pops up:

- In the 'Python Script' field, select the `gui.pyw` file.
- Under `Icon`, select the logo located at `build/icon/icon_128.ico`.
- Press the `Convert` button to build the application.

## Command Line Interface (CLI) Usage

```bash
usage: pdfexperthighlights2anki.py [-h] file_path deck_name

Process file_path and deck_name

positional arguments:
  file_path   Path to the file
  deck_name   Name of the deck

options:
  -h, --help  show this help message and exit
```

## License

This project is licensed under the GNU General Public License v3.0. For more details, please refer to the LICENSE file.

Made with ❤️ by a hobbyist programmer. If you'd like to port this tool to JavaScript or have any suggestions for improvements, please don't hesitate to reach out!

Happy Learning and Flashcard Making! 📖🧠