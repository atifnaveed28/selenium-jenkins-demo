# Selenium Login Test with Jenkins CI

## Overview

This project demonstrates a **Selenium-based login test** for a sample web application integrated with **Jenkins CI/CD pipeline**.
The goal is to automate **test execution**, **dependency management**, and **continuous integration** using Python, Git, and Jenkins.

---

## Features

- **Automated login test** using Selenium WebDriver (Chrome).
- **Python virtual environment** (`venv`) setup for reproducible dependencies.
- **Jenkins pipeline** to run tests automatically on code changes.
- **Workspace-relative paths** for cross-machine compatibility.
- **Post-build success/failure notification** in Jenkins console.

---

## Prerequisites

- **Python 3.12+** installed on the Jenkins server or local machine.
- **Git** installed.
- **Google Chrome** installed (or Chromium-based browser).
- **ChromeDriver** compatible with your Chrome version.
- **Jenkins** installed and running.

---

## Project Structure
selenium-jenkins-demo/
│
├─ tests/
│ └─ test_login.py # Selenium login test
├─ requirements.txt # Python dependencies
├─ Jenkinsfile # Jenkins CI/CD pipeline
└─ README.md

---

## Setup and Run Locally
1. **Clone the repository**:
```bash
git clone https://github.com/atifnaveed28/selenium-jenkins-demo.git
cd selenium-jenkins-demo

Jenkins CI/CD Setup:
Create a new Jenkins pipeline job.
Configure Git repository:
https://github.com/atifnaveed28/selenium-jenkins-demo.git
Use the provided Jenkinsfile for the pipeline script.

Pipeline stages:
Checkout: Pulls code from GitHub.
Setup Python Environment: Creates venv, upgrades pip, installs dependencies.
Run Selenium Tests: Executes login test using pytest.
Post Actions: Echoes test result (success/failure).
Run the pipeline and verify tests pass in Jenkins console.