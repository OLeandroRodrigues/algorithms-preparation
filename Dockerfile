# ============================
# Algorithms Preparation - Dockerfile
# ============================
# This image bundles everything needed to run tests for:
# - Python (3.11+)
# - Java (JDK 17 + JUnit Platform Console)
# - C# (.NET SDK 8)
# So anyone can run all tests with a single Docker command.

# Base: .NET SDK 8 (includes C# compiler + runtime)
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS base

# Install Java 17 + Python 3 + pip + venv + common tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    python3 python3-pip python3-venv \
    curl ca-certificates git \
 && rm -rf /var/lib/apt/lists/*

# Create a symlink so "python" points to "python3" (improves cross-platform consistency)
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set working directory
WORKDIR /app

# Copy the whole repository (honors .dockerignore)
COPY . .

# Make test scripts executable (if they exist)
RUN chmod +x run_all_tests.sh || true \
    && chmod +x python/run_tests.sh || true \
    && chmod +x java/run_tests.sh || true \
    && chmod +x csharp/run_tests.sh || true

# ---- Python via virtualenv (PEP 668 safe) ----
# Create a dedicated venv at /opt/venv, upgrade pip, and install requirements if available.
# NOTE: This must come AFTER COPY so that python/requirements.txt exists in the image.
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv "$VIRTUAL_ENV" \
 && python3 -m pip install --upgrade pip \
 && if [ -f python/requirements.txt ]; then pip install -r python/requirements.txt; fi

# Prepare JUnit for Java (optional: download once and cache it)
RUN if [ -f java/run_tests.sh ]; then bash java/run_tests.sh || true; fi

# Default command: run all test suites (Python + Java + C#)
CMD ["bash", "-lc", "./run_all_tests.sh"]