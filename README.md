# ✨ Building WittyBit: A Sarcastic AI Fine-tuned on Gemma 3 ✨

This repository contains the code and resources "**[Building WittyBit: Crafting an AI with Unmatched Wit and Sarcasm](#)**". It chronicles the process of developing "WittyBit", a fine-tuned Large Language Model (LLM) designed to deliver sharp humor, clever comebacks, and a delightfully snarky attitude.

We explore an end-to-end pipeline using accessible tools:
1.  **Generating diverse questions** using Llama 3.2 2B.
2.  **Crafting responses** in WittyBit's persona, again with Llama 3.2 2B.
3.  **Filtering for quality** using an LLM-as-a-Judge approach.
4.  **Fine-tuning** Google's Gemma 3 4B model using Unsloth for peak efficiency on consumer hardware.
5.  **Demonstrating** the final model with a Streamlit app.

---

## 🚀 WittyBit in Action!

Check out WittyBit's unique brand of helpfulness:

**Example 1:**

![Example of WittyBit answering a simple question](assets/WittyBit_example_1.png)

**Example 2:**

![Example of WittyBit "helping" with code](assets/WittyBit_example_2.png)

***Video Demo:**

Watch a short interaction with the fine-tuned WittyBit model:

![WittyBit Interaction Demo](assets/WittyBit.gif)

---

## 💡 Key Features & Technologies

*   **Custom AI Persona:** Fine-tuned model embodying the "WittyBit" sarcastic personality.
*   **AI-Powered Data Generation:** Leveraged **Llama 3.2 3B** to create the training dataset (questions and responses).
*   **LLM-as-a-Judge:** Used **Llama 3.2 3B** to automatically score generated responses for persona consistency, enabling efficient data filtering.
*   **State-of-the-Art Base Model:** Fine-tuned Google's efficient and powerful **Gemma 3 4B**.
*   **Memory-Efficient Training:** Utilized **Unsloth** for significantly faster fine-tuning (~2x) and reduced memory usage (~70%), enabling training on consumer GPUs.
*   **Quantization:** Employed 4-bit quantization during loading to further reduce memory requirements.
*   **PEFT (LoRA):** Used Low-Rank Adaptation for parameter-efficient fine-tuning, drastically reducing the computational cost.
*   **Streamlit Demo:** Interactive demonstration of the fine-tuned model.

---
## 📂 Repository Structure
```plaintext
WittyBitAI-Finetune/
│
├── assets/ # Images and videos for README
│ ├── WittyBit_example_1.png
│ ├── WittyBit_example_2.png
│ └── video.mp4
│
├── notebooks/ # Jupyter notebooks for the workflow
│ ├── 01_generate_questions.ipynb
│ ├── 02_generate_responses.ipynb
│ ├── 03_score_responses.ipynb
│ ├── 04_finetune_WittyBit.ipynb # <--(Colab recommended)
│ └── 05_streamlit_demo.ipynb # <--(Colab recommended)
│
├── prompts/ # Text files containing the system prompts used
│ ├── prompt_generate_questions_*.txt
│ ├── prompt_generate_WittyBit_response.txt
│ └── prompt_score_WittyBit_response.txt
│
├── data/ # Sample data and placeholder for generated files
│ ├── sample_scored_responses.csv # Example output after scoring
│ └── README.md # Explains data generation and .gitignore usage
│
├── .gitignore # Specifies intentionally untracked files (like large data)
├── README.md # This file!
```

*   **`notebooks/`**: Contains the step-by-step Jupyter notebooks for the entire process.
*   **`prompts/`**: Holds the detailed system prompts used to guide the LLMs during data generation and scoring.
*   **`data/`**: Intended location for the generated data files (questions, responses, scores). A sample is included. 
*   **`assets/`**: Stores images and videos used in this README.

---
## ▶️ Running the Pipeline

Follow the notebooks in the `notebooks/` directory in numerical order.

**Note:** Steps 1-3 can likely be run on a local machine (GPU preferred). Steps 4 and 5 are best run on **Google Colab** 

1.  **Generate Questions (`generate_questions.ipynb`)**
    *   **What it does:** Uses Llama 3.2 3B (via Transformers) and the prompts in `prompts/` to generate diverse questions (conversational, coding, help).
    *   **Output:** Saves question files (e.g., `conversational_questions.csv`, `coding_questions.csv`, etc.) to the `data/` directory.

2.  **Generate WittyBit's Responses (`generate_responses.ipynb`)**
    *   **What it does:** Takes the generated questions from Step 1 and uses Llama 3.2 3B with the WittyBit persona prompt (`prompts/prompt_generate_WittyBit_response.txt`) to generate sarcastic answers.
    *   **Input:** Question files from the `data/` directory.
    *   **Output:** A file containing questions and their corresponding generated WittyBit responses (e.g., `generated_responses.csv`) in the `data/` directory.

3.  **Score Responses (`score_responses.ipynb`)**
    *   **What it does:** Implements the LLM-as-a-Judge technique. Uses Llama 3.2 3B and the scoring prompt (`prompts/prompt_score_WittyBit_response.txt`) to rate each generated response on a scale of 1-5 based on how well it matches the WittyBit persona.
    *   **Input:** The response file from Step 2 (`data/generated_responses.csv`).
    *   **Output:** A file containing questions, responses, and their scores (e.g., `scored_responses.csv`) in the `data/` directory. A sample (`sample_scored_responses.csv`) is provided.

4.  **Fine-tune WittyBit (`finetune_WittyBit.ipynb`)** - **(Run on Colab!)**
    *   **What it does:** Filters the scored responses (keeping scores >= 4) and uses this high-quality dataset to fine-tune the Gemma 3 4B model using Unsloth and PEFT (LoRA).
    *   **Input:** The scored response file from Step 3 (`data/scored_responses.csv`).
    *   **Output:** Saves the fine-tuned LoRA adapter weights locally within the Colab environment (or potentially to Google Drive / Hugging Face Hub if configured). Make sure to save these weights!

5.  **Run Streamlit Demo (`streamlit_demo.ipynb`)** - **(Run on Colab!)**
    *   **What it does:** Loads the base Gemma 3 4B model and merges the fine-tuned LoRA adapter weights saved in Step 4. It then launches a simple Streamlit application within the notebook environment to interactively chat with your fine-tuned WittyBit AI.
    *   **Input:** Path to the saved LoRA adapter weights from Step 4.

---

## 📝 Blog Post

For a detailed explanation of the process, motivation, and learnings, please read the accompanying Medium article:

[**Building WittyBit: My Journey of Creating a Hilariously Sarcastic AI with LLMs**](https://medium.com/@Revanth_Regeti/building-WittyBit-my-journey-of-creating-a-hilariously-sarcastic-ai-with-llms-0e9e52cb715d)

---

## 📜 License

The code in this repository is licensed under the [MIT License](LICENSE)

Note that the base models used (Llama 3.2, Gemma 3) have their own licenses that must be adhered to. Please refer to their official documentation for details.

---

## 📞 Contact

Feel free to connect if you have questions or want to discuss AI fine-tuning!

*   **LinkedIn:** [[LinkedIn Profile](https://www.linkedin.com/in/masoob/)]
---

Happy Fine-tuning! Let me know if WittyBit gives you too much sass. 😉
