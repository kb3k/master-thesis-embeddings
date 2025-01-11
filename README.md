# Setup Instructions

This guide will help you configure your environment to work with specific versions of Python and required dependencies. At the time of writing, there are a few specific requirements for compatibility:

### Python Compatibility:

- **Torch 1.3.1** requires Python **3.10** (not Python 3.11).
- **Gensim 4.30** requires Python **>=3.7**.

### Step 1: Verify Python Versions

To verify the versions of Python installed on your system, run the following command:

```bash
ls -l /usr/local/bin/python*
```

### Step 2: Set Python 3.10 as Default

If you have multiple versions of Python installed, you may need to set Python 3.10 as the default version. Use the following commands:

```bash
# Create symlinks to make Python 3.10 the default
ln -s -f /usr/local/bin/python3.10 /usr/local/bin/python3
ln -s -f /usr/local/bin/python3.10 /usr/local/bin/python
```

### Step 3: Install JupyterLab and Kernel

Next, install the necessary tools for running Jupyter notebooks:

```bash
python -m pip install jupyterlab
python -m pip install ipykernel
python -m ipykernel install --name wine-chatbot-rec
python -m ipykernel install --user
```

### Step 4: Set Up a Virtual Environment

To ensure you have an isolated environment for this project, you’ll need to create a virtual environment.

1. **Install `virtualenv` (if not already installed):**

   ```bash
   python -m pip install --user virtualenv
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv <name>  # For example, wine-chatbot-rec
   ```

### Step 5: Activate the Virtual Environment and Install Dependencies

1. **Activate the virtual environment:**

   On macOS/Linux:

   ```bash
   source <name>/bin/activate  # For example, source wine-chatbot-rec/bin/activate
   ```

   On Windows:

   ```bash
   <name>\Scripts\activate
   ```

2. **Install the required packages:**

   ```bash
   python -m pip install -r requirements.txt
   ```

### Step 6: Run Jupyter Notebook Locally

Once your environment is set up and the dependencies are installed, you can run Jupyter locally:

```bash
jupyter notebook
```

This should open up the Jupyter interface in your default browser.

---

### Reference

For more detailed information on setting Python 3 as the default version on macOS, check out this helpful reference:  
[How to Set Python 3 as a Default Python Version on Mac](https://dev.to/malwarebo/how-to-set-python3-as-a-default-python-version-on-mac-4jjf)

---

### Disclaimer

This README.md was created with the assistance of ChatGPT.

---
