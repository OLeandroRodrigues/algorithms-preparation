# ============================
# Java Tests Runner (PowerShell)
# ============================

# Ensure UTF-8 output to avoid garbled characters
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$baseDir = $PSScriptRoot
$libDir  = Join-Path $baseDir "lib"
if (!(Test-Path $libDir)) { New-Item -ItemType Directory -Path $libDir | Out-Null }

# JUnit Console JAR
$version = "1.10.2"
$jar     = "junit-platform-console-standalone-$version.jar"
$jarPath = Join-Path $libDir $jar
$url     = "https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/$version/$jar"

# Download JUnit Console if missing
if (!(Test-Path $jarPath)) {
    Write-Host "Downloading JUnit Console $version..."
    Invoke-WebRequest -Uri $url -OutFile $jarPath
}

# Clean old .class files (ignore lib/)
Write-Host "Cleaning old .class files..."
Get-ChildItem -Recurse -Filter *.class |
    Where-Object { $_.DirectoryName -notlike "*\lib*" } |
    Remove-Item -Force

# Compile all Java sources (including tests)
Write-Host "Compiling sources and tests..."
$javaFiles = Get-ChildItem -Recurse -Filter *.java | ForEach-Object { $_.FullName }
if ($javaFiles.Count -eq 0) {
    Write-Host "No .java files found."
    exit 1
}

# -d $baseDir => writes .class into the correct package folder tree rooted at $baseDir
javac -cp ".;$jarPath" -d $baseDir $javaFiles

# Build explicit selectors from package + class name (no guessing)
$testFiles = Get-ChildItem -Recurse -Filter *Test.java
if ($testFiles.Count -eq 0) {
    Write-Host "No *Test.java files found."
    exit 1
}

Write-Host "Collecting test classes..."
$selectors = @()
foreach ($f in $testFiles) {
    $text = Get-Content -Raw $f.FullName
    $pkgMatch = [regex]::Match($text, '^\s*package\s+([A-Za-z0-9_.]+)\s*;', 'Multiline')
    $cls = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    if ($pkgMatch.Success) {
        $fqn = "$($pkgMatch.Groups[1].Value).$cls"
    } else {
        # No package declared: default package
        $fqn = $cls
    }
    Write-Host " - $fqn"
    $selectors += ('--select-class=' + $fqn)
}

# Run tests with explicit class selectors; ASCII details for Windows; disable ANSI colors
Write-Host "Running tests..."
$args = @(
    '-cp', $baseDir,
    '--details=tree',
    '--details-theme=ascii',
    '--disable-ansi-colors'
) + $selectors

# Use 'execute' explicitly (as the deprecation warning suggests)
& java -jar $jarPath execute @args