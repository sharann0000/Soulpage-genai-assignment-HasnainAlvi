# Soulpage-genai-assignment-HasnainAlvi
# Conversational Knowledge Bot (Task 2)

## 🏗 Architecture
This bot uses **LangChain** and a **ReAct Agent** to decide between using its internal knowledge or searching the web for real-time facts.

## 🛠 Features
* [cite_start]**Memory**: Uses `ConversationBufferMemory` to maintain context for follow-up questions[cite: 26, 31].
* [cite_start]**Search Tool**: Integrated with `DuckDuckGo Search` for factual accuracy[cite: 27, 32].
* [cite_start]**UI**: Built with `Streamlit` for a conversational chat experience[cite: 36].

## 🚀 How to Run
1. Clone the repo: `git clone https://github.com/HasnainAlvi/Soulpage-genai-assignment-HasnainAlvi.git`
2. [cite_start]Install dependencies: `pip install -r requirements.txt` 
3. Add your API key to a `.env` file.
4. Run the app: `streamlit run app.py`

## [cite_start]💬 Sample Chat Log [cite: 40]
**User:** Who is the CEO of OpenAI?
**Bot:** The CEO of OpenAI is Sam Altman.
**User:** Where did he study?
**Bot:** Sam Altman attended Stanford University but dropped out after one year.
