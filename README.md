---
title: "Multi-Agent Customer Support Automation"
emoji: "📞"
colorFrom: "blue"
colorTo: "green"
sdk: "streamlit"
sdk_version: "1.47.0"
app_file: "app.py"
pinned: true
---

# 📞 Multi-Agent Customer Support Automation

An intelligent multi-agent customer support system powered by [CrewAI](https://github.com/joaomdmoura/crewai) and [Streamlit](https://streamlit.io/). This application simulates how AI agents can collaboratively handle customer inquiries with high quality, empathy, and accuracy.

<div align="center">
  <img src="images/demo_screenshot.png" width="80%" alt="App Demo Screenshot">
</div>

---

## 🚀 Features

- 🤖 **Multi-Agent Collaboration**: AI agents perform specialized tasks such as resolving support inquiries and reviewing responses.
- 🔍 **Web Scraping Integration**: Automatically pulls info from trusted sources like [CrewAI Docs](https://crewai.com/docs/introduction).
- 💬 **Natural, Friendly Tone**: Outputs are helpful, casual yet professional — ideal for real-world support environments.
- 🧠 **Memory-Enabled CrewAI**: Agents can retain shared memory to improve task performance.
- 🧩 **Modular Architecture**: Easily extend or modify the system to include more agents or tools.

---

## 🏗️ Architecture Overview

### 🧠 Agents
- **Support Agent**: Responds directly to customer queries with researched answers.
- **QA Agent**: Reviews the support agent’s reply to ensure tone, accuracy, and completeness.

### 📋 Tasks
1. **Inquiry Resolution**: Resolves user inquiry with research and clarity.
2. **QA Review**: Reviews and polishes the initial response for final output.

### 🛠️ Tools Used
- `WebsiteSearchTool` – for general web searches  
- `ScrapeWebsiteTool` – scrapes content from specific URLs  
- Preconfigured doc scraper for CrewAI docs

---

## 📁 Project Structure

```
multi-agent-customer-support/
├── app.py                 # 🚀 Streamlit app interface
├── agents.py              # 🤖 Agent definitions (not shared yet)
├── tasks.py               # 📋 Task definitions
├── tools.py               # 🛠️ Tool configurations
├── utils.py               # 🔑 API key handling
├── requirements.txt       # 📦 Dependencies
├── README.md              # 📖 Documentation
└── images/
    └── demo_screenshot.png  # 🖼️ App UI screenshot (optional)
```

---

## 🛠️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/saadtoorx/multi-agent-customer-support.git
cd multi-agent-customer-support
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add your OpenAI API key**
- Create a `.env` file:
```env
OPENAI_API_KEY=your-api-key-here
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

- 📝 App simulates a support inquiry from a fictional customer.
- 🧠 CrewAI kicks off task execution between agents.
- 📋 Final, polished response is displayed in Streamlit UI.

---

## 📦 Tech Stack

- **Python 3.8+**
- [Streamlit](https://streamlit.io/)
- [CrewAI](https://github.com/joaomdmoura/crewai)
- [crewAI-tools](https://github.com/joaomdmoura/crewai-tools)
- [OpenAI API](https://platform.openai.com/)
- `python-dotenv`

---

## 🤖 Agent Summary

| Agent              | Responsibility                                              |
|--------------------|-------------------------------------------------------------|
| **Support Agent**  | Researches and writes a helpful reply to customer inquiry.  |
| **QA Agent**       | Reviews the reply, improves tone, and ensures completeness. |

---

## 🔮 Future Improvements

- 🧠 Add more agents (e.g., Sentiment Analyst, Follow-up Manager)
- 🌐 Use live customer chat input instead of static prompt
- 🧾 Export final replies to email or ticketing system
- 🧩 Add memory visualization or trace logs

---

## 📄 License

Licensed under the MIT License. See [`LICENSE`](LICENSE) for full terms.

---

## ✨ Built By

> Created with ❤️ by [Saad Toor](https://www.linkedin.com/in/saadtoorx/) (`@saadtoorx`)  
> Powered by CrewAI, Streamlit, and OpenAI
