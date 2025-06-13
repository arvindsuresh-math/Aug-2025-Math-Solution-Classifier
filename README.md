# Erdos-DL-June25-Math

#### Instructions for setting up the conda environment to run Jupyter notebooks

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

#### Instructions for getting and securely using the OpenAI API key

1. Get the OpenAI API key from the [OpenAI website](https://platform.openai.com/signup).
2. Create a `.env` file in the same directory as this readme and add your API key to it by writing the following line:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
3. Make sure to add `.env` to your `.gitignore` file to prevent it from being committed to version control.