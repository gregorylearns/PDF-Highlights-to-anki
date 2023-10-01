import PySimpleGUI as sg
import os
import subprocess
import webbrowser
import pdfexperthighlights2anki as h2anki


# Define the output folder
output_folder = "anki_converted"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the GUI layout
layout = [
    [sg.Text("Select an HTML file:")],
    [sg.InputText(key="file_path", size=(40, 1)), sg.FileBrowse(file_types=(("HTML Files", "*.html"),))],
    [sg.Text("Enter Deck Name:"), sg.InputText(key="deck_name")],
    [sg.Checkbox("Edit File Before Conversion (.apkg)", key='-EDIT-')],
    [sg.Button("Run Script"), sg.Button("Check for Updates"), sg.Button("Exit")],
]

# Create the window
window = sg.Window("PDF Expert Highlights to Anki v0.0.4", layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Check for Updates":
        # Define the URL to the update page
        update_url = "https://github.com/gregorylearns/PDF-Highlights-to-anki/releases"
        # Open the URL in the default web browser
        webbrowser.open(update_url)


    elif event == "Run Script":
        file_path = values["file_path"]
        deck_name = values["deck_name"]
        edit_file = values['-EDIT-']
        print(f"edit file value: {edit_file}")

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
        # subprocess.run(["h2anki.py", file_path, deck_name])
        # Simulate script completion by copying the file to the output folder
        output_folder = "anki_converted"
        output_path = os.path.join(output_folder, f"{deck_name}.apkg")

        try:
            os.makedirs(output_folder, exist_ok=True)
            with open(file_path, "rb") as source_file, open(output_path, "wb") as destination_file:
                final_clozed_list = h2anki.main(file_path, deck_name, edit_file)

                if edit_file == False:
                    h2anki.generate_from_final_clozed_list(final_clozed_list,deck_name)

                else:
                    clozed_list_w_edits = h2anki.list_to_text(final_clozed_list, deck_name)
                    h2anki.open_in_notepad(clozed_list_w_edits)

                    ch = sg.popup_ok_cancel("Done with editing the file in notepad?", 
                        "Save the file in notepad, exit file, then click OK",  
                        title="OkCancel")
                   
                    if ch=="OK":
                       print ("You pressed OK")
                       final_clozed_list_w_edits = h2anki.textfile_to_list(clozed_list_w_edits)
                       h2anki.generate_from_final_clozed_list(final_clozed_list_w_edits,deck_name)
                   
                    if ch=="Cancel":
                       print ("You pressed Cancel")


            sg.popup(f"Script completed! Processed file saved in '{output_folder}' folder")
            h2anki.cleanup_temp_files()

        except Exception as e:
            sg.popup_error(f"An error occurred: {e}")

window.close()
