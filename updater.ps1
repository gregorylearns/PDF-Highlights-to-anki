Add-Type -AssemblyName PresentationFramework
Add-Type -AssemblyName System.Windows.Forms

# Get the directory of the script
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Define the URL of the zip file you want to download
$zipUrl = "https://github.com/gregorylearns/PDF-Highlights-to-anki/archive/refs/heads/main.zip"

# Download the latest release from the GitHub repository
$zipFile = Join-Path -Path $scriptDirectory -ChildPath "main.zip"

# Use Invoke-WebRequest to download the zip file
Invoke-WebRequest -Uri $zipUrl -OutFile $zipFile

# Check if the download was successful
if (Test-Path $zipFile) {
    Write-Host "Download complete. The zip file is saved at: $zipFile"
} else {
    Write-Host "Download failed."
}


# Extract the downloaded ZIP archive to the script directory
Expand-Archive -Path $zipFile -DestinationPath $scriptDirectory -Force

# Clean up by removing the ZIP file
Remove-Item -Path $zipFile

# Define the base directory relative to the script
$baseDirectory = Join-Path -Path $PSScriptRoot -ChildPath "PDF-Highlights-to-anki-main"

# Check if the source directory exists
if (Test-Path -Path $baseDirectory -PathType Container) {
    # Get the list of files and subdirectories in the source directory
    $itemsToMove = Get-ChildItem -Path $baseDirectory

    # Move each item to the base directory
    foreach ($item in $itemsToMove) {
        $destinationPath = Join-Path -Path $PSScriptRoot -ChildPath $item.Name
        echo $destinationPath
        Move-Item -Path $item.FullName -Destination $destinationPath -Force
    }

    # Delete the source directory
    Remove-Item -Path $baseDirectory -Force -Recurse

    Write-Host "Contents of 'PDF-Highlights-to-anki-main' moved to the base directory."
} else {
    Write-Host "Source directory 'PDF-Highlights-to-anki-main' does not exist relative to the script."
}



# Output a message indicating that the update is complete
Write-Host "Update complete. The latest code is now in $scriptDirectory"



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
