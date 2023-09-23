import PySimpleGUI as sg
import os
import subprocess
import pdfexperthighlights2anki

# Define the output folder
output_folder = "anki_converted"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the GUI layout
layout = [
    [sg.Text("Select an HTML file:")],
    [sg.InputText(key="file_path", size=(40, 1)), sg.FileBrowse(file_types=(("HTML Files", "*.html"),))],
    [sg.Text("Enter Deck Name:"), sg.InputText(key="deck_name")],
    [sg.Button("Run Script"), sg.Button("Exit")],
]

# Create the window
window = sg.Window("PDF Expert Highlights to Anki v0.0.1", layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Run Script":
        file_path = values["file_path"]
        deck_name = values["deck_name"]

        if not file_path:
            sg.popup_error("Please select an HTML file.")
            continue

        if not deck_name:
            sg.popup_error("Please enter a Deck Name.")
            continue

        if not file_path.endswith(".html"):
            sg.popup_error("Please select an HTML file.")
            continue

        # Run your script here, for example:
        # subprocess.run(["pdfexperthighlights2anki.py", file_path, deck_name])
        # Simulate script completion by copying the file to the output folder
        output_folder = "anki_converted"
        output_path = os.path.join(output_folder, f"{deck_name}.apkg")

        try:
            os.makedirs(output_folder, exist_ok=True)
            with open(file_path, "rb") as source_file, open(output_path, "wb") as destination_file:
                pdfexperthighlights2anki.main(file_path, deck_name)
            sg.popup(f"Script completed! Processed file saved in '{output_folder}' folder")

        except Exception as e:
            sg.popup_error(f"An error occurred: {e}")

window.close()
