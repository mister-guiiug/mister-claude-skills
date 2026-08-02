# Installe les skills du dépôt dans le dossier utilisateur Claude.
# Usage : powershell -ExecutionPolicy Bypass -File scripts/install.ps1 [-Destination <chemin>]
param(
    [string]$Destination = (Join-Path $env:USERPROFILE ".claude\skills")
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceDir = Join-Path $repoRoot ".claude\skills"

if (-not (Test-Path $sourceDir)) {
    Write-Error "Dossier source introuvable : $sourceDir"
    exit 1
}

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

$count = 0
Get-ChildItem -Path $sourceDir -Directory | ForEach-Object {
    $target = Join-Path $Destination $_.Name
    if (Test-Path $target) {
        Remove-Item -Recurse -Force $target
    }
    Copy-Item -Recurse -Path $_.FullName -Destination $target
    Write-Host "installee : $($_.Name)"
    $count++
}

Write-Host ""
Write-Host "$count skills installees dans $Destination"
Write-Host "Redemarrer Claude Code pour les charger."
