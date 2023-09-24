Add-Type -AssemblyName PresentationFramework
Add-Type -AssemblyName System.Windows.Forms

# Install PySimpleGUI, beautifulsoup4, and genanki
pip install PySimpleGUI beautifulsoup4 genanki

# Check if the installation was successful
if ($LASTEXITCODE -eq 0) {
    Write-Host "Packages installed successfully!"
    
    # Display a dialog message
    [System.Windows.MessageBox]::Show("Packages installed successfully!", "Success", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
} else {
    Write-Host "Installation failed. Please check for errors."
    
    # Display an error dialog message
    [System.Windows.MessageBox]::Show("Installation failed. Please check for errors.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
}
