```markdown
# 🤖 AI Chatbot UI

A sleek and modern user interface for a chatbot using HTML, CSS, and JavaScript — designed to interact with a backend powered by Python (NLTK, FastAPI, or Flask).

---

## 📸 Preview
![<img width="740" height="814" alt="{00F2C251-C803-43F2-A7DD-09DABD5176AB}" src="https://github.com/user-attachments/assets/03e1b406-3604-42b7-9378-629e1c317e2d" />]

<img src="preview.png" alt="AI Chatbot UI Preview" width="100%">

---

## 🧠 Features

- 🟢 Clean, AI-inspired design
- 🧾 Chat bubbles (user & bot format)
- 📱 Mobile responsive
- ⚡ Instant message display
- 🔌 Easy backend integration via `/chat` endpoint (POST)
- 🔄 Supports Enter key and button click

---

## 🚀 Technologies Used

| Layer       | Tech              |
|-------------|-------------------|
| UI          | HTML5, CSS3, JavaScript |
| Backend     | NLTK / FastAPI (your custom chatbot) |
| Hosting     | Local / GitHub Pages / any static server |

---

## 🔧 Folder Structure

```

chatbot-ui/
├── index.html       # Main UI
├── style.css        # Custom styling (optional if inline)
├── preview\.png      # Screenshot for GitHub preview
└── README.md        # Project details

````

---

## 📦 How to Use

1. Clone this repository:

```bash
git clone https://github.com/Harsha-nani75/chatbot-ui.git
````

2. Open `index.html` in your browser.
3. Connect your Python backend at `/chat` (POST).

Example Python backend:

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from chatbot import get_bot_response  # your logic

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(req: Request):
    data = await req.json()
    user_input = data["message"]
    reply = get_bot_response(user_input)
    return JSONResponse({"response": reply})
```

---

## 💬 Example Commands (For NLTK)

* `hi`, `hello` → "Hi there!"
* `what is your name?` → "I'm a chatbot."
* `thank you`, `tq` → "You're welcome!"
* ...and hundreds more...

---

## 📢 Contribute

Want to improve the design or expand the commands?
Feel free to fork and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. Free to use and modify.

---

## 🌐 Author

**Harsha Vardhan**
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile)
🔗 [GitHub](https://github.com/Harsha-nani75)

```

