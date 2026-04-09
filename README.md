<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">SUPPLYCHAIN-AI-ASSISTANT</h1></p>
<p align="center">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/HighOnKeys/supplychain-ai-assistant?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/HighOnKeys/supplychain-ai-assistant?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/HighOnKeys/supplychain-ai-assistant?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-Overview)
- [ System Architecture](#-system-architecture)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Tech Stack](#-tech-stack)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
  - [ Example Queries](#-example-queries)
- [ Key Learnings](#-key-learnings)
- [ Future Improvements](#-future-improvements)
- [ Contributing](#-contributing)

---

##  Overview

<code>❯SupplyChain AI Assistant is an intelligent multi-agent system designed to answer both analytical and conceptual queries related to supply chain and inventory management.

The system integrates structured retail data with document-based knowledge using a hybrid architecture that combines:
- Data-driven analytics
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)

It dynamically routes user queries to the most appropriate agent, enabling accurate and context-aware responses.
The application is deployed using Streamlit and optimized for real-world production constraints.</code>

---

## System Architecture

**<code>❯- 
User Query  
↓  
Smart Router  
↓  
--------------------------- ** 
|                         |  
Data Agent          RAG Agent  
(Structured Data)   (Documents + LLM)  
↓                         ↓  
Final Response (LLM Enhanced)</code>

---

##  Features

<code>❯- 🔀 **Smart Query Routing**
  - Classifies queries into data-based or knowledge-based using a lightweight router

- 📊 **Data Agent (Analytics Engine)**
  - Handles structured queries using retail dataset
  - Supports aggregations like total revenue, averages, and trends

- 📚 **RAG Agent (Knowledge Retrieval)**
  - Retrieves relevant documents from unstructured data (PDFs)
  - Generates contextual explanations using LLM

- 🤖 **LLM Integration (Gemini)**
  - Generates human-like explanations and reasoning

- ⚙️ **Hybrid Architecture**
  - Combines structured data + unstructured documents

- 🚀 **Deployed Application**
  - Built using Streamlit Cloud
  - Optimized for dependency constraints and performance

- 🧠 **Production Optimization**
  - Adapted architecture to handle deployment limitations (Python version, FAISS, etc.)</code>
  
---

##  Project Structure

```sh
└── supplychain-ai-assistant/
    ├── agents
    │   ├── rag_agent.py
    │   ├── smart_data_agent.py
    │   └── smart_router.py
    ├── app.py
    ├── data
    │   ├── docs
    │   ├── processed
    │   └── structured
    ├── ingestion
    │   └── load_structured_data.py
    ├── rag
    │   ├── llm_pipeline.py
    │   └── rag_pipeline.py
    └── requirements.txt
```


###  Project Index
<details open>
	<summary><b><code>SUPPLYCHAIN-AI-ASSISTANT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/app.py'>app.py</a></b></td>
				<td><code>❯ Acts as the main entry point of the application. 
Handles user interaction through Streamlit UI, routes queries using the smart router, 
and displays responses from data or RAG agents.</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ Defines project dependencies including Streamlit, pandas, numpy, 
sentence-transformers, and Gemini API integration.
Optimized for cloud deployment compatibility.</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- rag Submodule -->
		<summary><b>rag</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/rag/llm_pipeline.py'>llm_pipeline.py</a></b></td>
				<td><code>❯ Implements LLM-based response generation using prompt engineering.
Processes retrieved context and generates structured explanations.</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/rag/rag_pipeline.py'>rag_pipeline.py</a></b></td>
				<td><code>❯ Handles document loading, text splitting, and retrieval logic.
Implements the core Retrieval-Augmented Generation (RAG) pipeline.</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- agents Submodule -->
		<summary><b>agents</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/agents/rag_agent.py'>rag_agent.py</a></b></td>
				<td><code>❯ Coordinates retrieval and generation by combining document context 
with LLM-based reasoning to answer conceptual queries.</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/agents/smart_router.py'>smart_router.py</a></b></td>
				<td><code>❯ Classifies user queries into:
- Data queries → routed to data agent
- Knowledge queries → routed to RAG agent</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/agents/smart_data_agent.py'>smart_data_agent.py</a></b></td>
				<td><code>❯ Processes analytical queries using structured retail dataset.
Performs aggregations, filtering, and statistical computations.</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- ingestion Submodule -->
		<summary><b>ingestion</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/ingestion/load_structured_data.py'>load_structured_data.py</a></b></td>
				<td><code>❯ Loads and preprocesses structured retail dataset.
Prepares data for analytical queries.</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Tech Stack

<code>| Category            | Tools / Technologies                          |
|--------------------|-----------------------------------------------|
| Programming Language | Python                                       |
| UI Framework        | Streamlit                                    |
| Data Processing     | Pandas, NumPy                                |
| Machine Learning    | Sentence Transformers                        |
| LLM Integration     | Google Gemini API                            |
| Retrieval System    | Retrieval-Augmented Generation (RAG)         |
| Architecture        | Multi-Agent System (Router + Agents)         |
| Data Storage        | CSV Dataset (Retail Inventory Data)          |
| Document Handling   | PyPDF (PDF Processing)                       |
| Deployment          | Streamlit Cloud                             |</code>

###  Installation

Install supplychain-ai-assistant using one of the following methods:

**Build from source:**

1. Clone the supplychain-ai-assistant repository:
```sh
❯ git clone https://github.com/HighOnKeys/supplychain-ai-assistant
```

2. Navigate to the project directory:
```sh
❯ cd supplychain-ai-assistant
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

4. Add API key:
   Create .env file:
```sh
❯ GEMINI_API_KEY="your_api_key_here"
```

###  Usage
Run supplychain-ai-assistant using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ streamlit run app.py
```

###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

### Example Queries:
```sh
- What is demand forecasting?
- Which region has highest sales?
- Average demand forecast by category
- Total revenue
```

---

## Key Learnings:
- Multi-agent AI system design
- RAG pipeline implementation
- LLM integration (Gemini)
- Debugging real-world deployment issues
- Optimizing ML systems for production

---

##  Future Improvements:
- Chat-style conversational UI
- Data visualisation dashboard
- Upload custom datasets
- Faster retrieval with caching

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/HighOnKeys/supplychain-ai-assistant/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/HighOnKeys/supplychain-ai-assistant/issues)**: Submit bugs found or log feature requests for the `supplychain-ai-assistant` project.
- **💡 [Submit Pull Requests](https://github.com/HighOnKeys/supplychain-ai-assistant/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/HighOnKeys/supplychain-ai-assistant
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/HighOnKeys/supplychain-ai-assistant/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=HighOnKeys/supplychain-ai-assistant">
   </a>
</p>
</details>

---

If you found this useful, consider giving a ⭐ on GitHub!

---
