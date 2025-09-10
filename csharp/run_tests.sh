#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/tests"

# Restaura dependências do .NET (NuGet packages)
dotnet restore

# Executa os testes com saída mais limpa
dotnet test --nologo --verbosity minimal