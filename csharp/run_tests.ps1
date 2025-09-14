Write-Host "=== Setup for C# Algorithms Project ==="

# 1) Check dotnet
$dotnet = Get-Command dotnet -ErrorAction SilentlyContinue
if (-not $dotnet) {
    Write-Host ".NET SDK not found."
    Write-Host "Please install .NET SDK (8.0+ recommended) from:"
    Write-Host "   https://dotnet.microsoft.com/download"
    exit 1
}
$version = dotnet --version
Write-Host ".NET SDK found: $version"

# 2) Find .sln or .csproj
$solutions = Get-ChildItem -Recurse -Filter *.sln | Select-Object -ExpandProperty FullName
$projects  = @()

if (-not $solutions -or $solutions.Count -eq 0) {
    $projects = Get-ChildItem -Recurse -Filter *.csproj | Select-Object -ExpandProperty FullName
    if (-not $projects -or $projects.Count -eq 0) {
        Write-Host "No .sln or .csproj found in the current directory or subfolders."
        Write-Host "Run this script from your repository root."
        exit 1
    }
}

# 3) Restore
if ($solutions -and $solutions.Count -gt 0) {
    Write-Host "Restoring solutions..."
    foreach ($sln in $solutions) {
        Write-Host "dotnet restore `"$sln`""
        dotnet restore "$sln"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Failed to restore: $sln"
            exit 1
        }
    }
    Write-Host "Restore completed."
} else {
    Write-Host "Restoring projects..."
    foreach ($proj in $projects) {
        Write-Host "dotnet restore `"$proj`""
        dotnet restore "$proj"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Failed to restore: $proj"
            exit 1
        }
    }
    Write-Host "Restore completed."
}

# 4) Run tests
# Prefer testing by solution if available; otherwise test projects that look like test projects
if ($solutions -and $solutions.Count -gt 0) {
    Write-Host "Running tests by solution..."
    foreach ($sln in $solutions) {
        Write-Host "dotnet test --nologo `"$sln`""
        dotnet test --nologo "$sln"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Some tests failed in solution: $sln"
            exit 1
        }
    }
    Write-Host "All solution tests passed."
} else {
    # Heurística: arquivos com 'Test' ou 'Tests' no nome/caminho
    $testProjects = $projects | Where-Object { $_ -match '(\\|/)?Tests?(\\|/)?' -or $_ -match 'Tests?\.csproj$' -or $_ -match 'Test\.csproj$' }
    if (-not $testProjects -or $testProjects.Count -eq 0) {
        Write-Host "No test projects detected. Skipping test run."
        exit 0
    }

    Write-Host "Running tests by project..."
    foreach ($tp in $testProjects) {
        Write-Host "dotnet test --nologo `"$tp`""
        dotnet test --nologo "$tp"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Some tests failed in project: $tp"
            exit 1
        }
    }
    Write-Host "All project tests passed."
}