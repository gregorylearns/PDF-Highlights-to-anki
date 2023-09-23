# Get the directory of the script
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Define the URL of the zip file you want to download
$zipUrl = "https://github.com/gregorylearns/PDF-Highlights-to-anki/archive/refs/heads/main.zip"

# Download the latest release from the GitHub repository
$zipFile = Join-Path -Path $scriptDirectory -ChildPath "main.zip"

# Use Invoke-WebRequest to download the zip file
Invoke-WebRequest -Uri $zipUrl -OutFile $zipFile

# Check if the download was successful
if (Test-Path $localPath) {
    Write-Host "Download complete. The zip file is saved at: $localPath"
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
