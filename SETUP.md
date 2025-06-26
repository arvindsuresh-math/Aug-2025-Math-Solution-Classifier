# Practical Git Guide for Mathematicians (“Erdős-DL” Project)

> *Goal: give every member a repeatable recipe for getting the code, running it, and contributing changes without trampling on colleagues’ work.*

---

## 0. Prerequisites

| Tool | Why you need it | Where to get it |
|------|-----------------|-----------------|
| **Anaconda** | Manages Python + dependencies in an isolated environment. | <https://www.anaconda.com/download> |
| **GitHub Desktop** | Simple graphical app for cloning & pushing. | <https://desktop.github.com> |
| **Visual Studio Code** | Code editor; integrates nicely with Git, Python & Conda. | <https://code.visualstudio.com> |

All three are free and work on macOS **and** Windows.

---

## 1. Install Anaconda

### macOS  

1. Download **“macOS x86_64”** (Intel) *or* **“macOS arm64”** (Apple Silicon).  
2. Run the `.pkg`, accept defaults.  
3. Open **Terminal** → run `conda --version`; a version string should appear.

### Windows  

1. Download **“64-bit Graphical Installer”** (`Anaconda3-….exe`).  
2. Run installer → choose **Just Me** → tick **Add Anaconda to PATH** (ignore the warning).  
3. Open **Anaconda Prompt** → `conda --version` should work.

---

## 2. Clone the repository with GitHub Desktop

> **Clone** = make a local copy of the project’s files **and** its Git history.

1. Launch **GitHub Desktop** and sign in.  
2. **File ▷ Clone Repository…**  
3. **URL tab** → paste `https://github.com/your-org/erdos-dl.git`.  
4. Choose a local folder (e.g. `~/Projects/erdos-dl`) → **Clone**.  
5. You now have a **local repository** linked to the **remote** on GitHub.com.

---

## 3. Open the repo in VS Code

1. In GitHub Desktop: **Repository ▷ Open in Visual Studio Code**  
   (or launch VS Code → **File ▷ Open Folder…** and pick the cloned directory).  
2. Accept the prompt *“Install Python extension?”*.

---

## 4. Branches—what & why

* **`main` branch** – authoritative, deployable version.  
* **Feature branch** – your private draft.

Think of branches like separate drafts of a paper. You write in your draft, then merge approved edits back into the master copy.

### Create *your* branch in GitHub Desktop

1. Top bar **Current Branch** → **New Branch**.  
2. Name it after yourself, e.g. `alice`, `bob_spectral`, `carol-experiments`.  
3. Base branch = `main` → **Create Branch**.  
4. Click **Publish Branch** (first-time push).

---

## 5. Set up the Conda environment (first-time only)

1. Install Anaconda or Miniconda on your system if you haven't already.
2. Open a terminal or command prompt.
3. Clone the repo and open it in VS Code.
4. Navigate to the directory where you cloned the repo.
5. Open a terminal and run the following command:

    ```bash
    conda env create -f environment.yml
    ```

6. Activate the conda environment:

    ```bash
    conda activate erdos-dl
    ```

7. The environment is now set up. When you open Jupyter notebooks, make sure to select the `erdos-dl` kernel.

## 6. Instructions for getting and securely using the OpenAI API key

1. Get the OpenAI API key from the [OpenAI website](https://platform.openai.com/signup).
2. Create a `.env` file in the same directory as this readme and add your API key to it by writing the following line:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

3. Make sure to add `.env` to your `.gitignore` file to prevent it from being committed to version control.

---

If VS Code doesn’t auto-select it: press *Cmd/Ctrl ⇧ P* → **Python: Select Interpreter** → choose `erdos-dl`.

---

## 7. Daily workflow checklist 🚦

Best practices for working with the `Erdős-DL` repo:

1. **Open your repo in VS Code**: one way to do this is to open your cloned repo and select `Open in Visual Studio Code` (or whichever editor you prefer).
2. **In VS Code**: open a terminal window. Then, do the following:
    * *Check you branch*: `git branch` (should show your branch name `my_name`).
    * *Switch to your branch*: `git checkout my_name` (if not already on it). You should always do this in the beginning to make sure you only ever make changes direclty to your own branch.
    * *Pull latest changes*: `git pull origin main` (to get any updates from `main`).
3. **Do whatever work you want**: make your changes in the code or notebooks.
4. **Commit your changes**: as you complete a block of work with similar tasks, you should periodically "commit" your changes. This basically amounts to making them public with a note about what you did. The easiest way to do this is to add the github extension to VS Code, which will allow you to commit changes directly from the editor.
5. **Push your changes**: after committing, push your changes to your branch on GitHub. This makes them available for others to see and review. You can do this by using the github extension in VS Code. Alternatively, you can open a terminal in VS Code and run `git push my_name`.

---

## 8. Gitignore

To prevent certain files from being tracked by Git, you can create a `.gitignore` file in the root of your repository. Here’s a basic example:

```plaintext
# Ignore .DS_Store files
.DS_Store

# Ignore Python bytecode files
*.pyc
__pycache__/

# Ignore the .env file
.env
```

This file tells Git to ignore `.DS_Store` files (macOS), Python bytecode files, and the `.env` file where you store your OpenAI API key.

---
