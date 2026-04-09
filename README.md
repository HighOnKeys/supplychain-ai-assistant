<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">SUPPLYCHAIN-AI-ASSISTANT</h1></p>
<p align="center">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/HighOnKeys/supplychain-ai-assistant?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
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

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>❯ SupplyChain AI Assistant is an intelligent multi-agent system designed to answer both analytical and conceptual queries related to supply chain and inventory management.

The system integrates structured retail data with document-based knowledge using a hybrid architecture that combines:
- Data-driven analytics
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)

It dynamically routes user queries to the most appropriate agent, enabling accurate and context-aware responses.
The application is deployed using Streamlit and optimized for real-world production constraints.</code>

---

##  Features

<code>❯ - 🔀 **Smart Query Routing**
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
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
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
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/rag/rag_pipeline.py'>rag_pipeline.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
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
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/agents/smart_router.py'>smart_router.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HighOnKeys/supplychain-ai-assistant/blob/master/agents/smart_data_agent.py'>smart_data_agent.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
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
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with supplychain-ai-assistant, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


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




###  Usage
Run supplychain-ai-assistant using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

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

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
