# DevOps Demo – Assignment 6
### Jenkins Integration with GitHub

A minimal demo project used to demonstrate Continuous Integration using **Jenkins** and **GitHub**.

---

## 📁 Project Structure

```
devopsass6/
├── README.md        ← This file
├── index.html       ← Web dashboard / project overview page
├── app.py           ← Python application with inline tests
└── Jenkinsfile      ← Declarative CI/CD pipeline definition
```

---

## 🚀 Quick Start (Local)

```bash
# 1. Clone the repository
git clone https://github.com/Strix33/devops-assignment.git
cd devops-assignment

# 2. Run the application
python app.py

# 3. Open the dashboard
start index.html     # Windows
open index.html      # macOS
```

---

## 🤖 Jenkins Setup

| Step | Action |
|------|--------|
| 1 | Install **Git Plugin**, **GitHub Plugin**, **Pipeline Plugin** |
| 2 | Create a new **Pipeline** job named `GitHub-Jenkins-Demo` |
| 3 | Under *Pipeline Definition* choose **Pipeline script from SCM** |
| 4 | Select **Git**, paste URL `https://github.com/Strix33/devops-assignment.git`, set branch to `*/main` |
| 5 | Set *Script Path* to `Jenkinsfile` |
| 6 | Click **Build Now** |

---

## 🔄 CI/CD Workflow

```
Developer → git push → GitHub → (Webhook) → Jenkins → Build → Test → Result
```

---

## 📋 Pipeline Stages

| Stage | Description |
|-------|-------------|
| **Checkout** | Clones the latest code from GitHub `main` branch |
| **Build** | Runs `python app.py` to verify the application executes |
| **Test** | Executes inline test suite (pytest-compatible) |
| **Archive** | Saves `.py`, `.html`, and `README.md` as build artifacts |

---

## ✅ Expected Console Output

```
[Pipeline] stage (Checkout)
📥 Cloning repository from GitHub (branch: main)...
✅ Repository checked out successfully.

[Pipeline] stage (Build)
🔨 Building devops-demo...
===================================================
  DevOps Jenkins Demo
  Version : 1.0.0
===================================================

[Pipeline] stage (Test)
🧪 Running test suite...
  ✅ Test 1 PASSED: greet() default
  ✅ Test 2 PASSED: greet('Jenkins')
  ✅ Test 3 PASSED: get_build_info() keys
  Results: 3 passed, 0 failed

[Pipeline] stage (Archive)
📦 Archiving build artifacts...

[Pipeline] End of Pipeline
🎉 Pipeline SUCCEEDED – Build #1 completed.
```

---

## 📚 Key Concepts

- **Jenkins** – Open-source automation server for CI/CD
- **Git Plugin** – Enables Jenkins to connect to Git repositories
- **Webhook** – GitHub notifies Jenkins on every push (optional)
- **Workspace** – Jenkins clones code here before each build
- **Pipeline as Code** – `Jenkinsfile` stored in the repository

---

*Assignment 6 · DevOps Lab*
