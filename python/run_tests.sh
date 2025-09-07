#!/usr/bin/env bash
set -euo pipefail

# Config
JUNIT_VERSION="1.10.2"
LIB_DIR="$(cd "$(dirname "$0")" && pwd)/lib"
JAR="$LIB_DIR/junit-platform-console-standalone-${JUNIT_VERSION}.jar"

mkdir -p "$LIB_DIR"

# Baixa JUnit Console se não existir
if [ ! -f "$JAR" ]; then
  echo "Downloading JUnit Console ${JUNIT_VERSION}..."
  curl -fsSL -o "$JAR" "https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/${JUNIT_VERSION}/junit-platform-console-standalone-${JUNIT_VERSION}.jar"
fi

# Clear old .class 
find "$(dirname "$0")" -type f -name "*.class" -delete

# Compilling all code and tests (ignore folder lib)
echo "Compiling sources and tests..."
javac -cp ".:${JAR}" $(find "$(dirname "$0")" -path "$(dirname "$0")/lib" -prune -o -name "*.java" -print)

# Run tets scanning the classpath
echo "Running tests..."
java -jar "$JAR" -cp "$(dirname "$0")" --scan-class-path