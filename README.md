🛍️ E-commerce Sales Chatbot — AI Assistant

    Case Study: Development of a Sales Chatbot for Streamlining Product Search & User Interaction on an E-commerce Platform.

📌 Project Overview

In the fast-evolving landscape of e-commerce, this project presents a smart Sales Chatbot capable of:

    Assisting users in real-time product discovery

    Delivering personalized product results

    Creating a seamless customer experience with a modern UI and conversational interface

    Designed using React.js (frontend) and Flask (Python backend), this chatbot facilitates mock shopping interactions in a clean, responsive interface.

🎯 Objectives

    📦 Simulate product queries on an e-commerce platform

    🤖 Create an intuitive AI-based chatbot interface

    🔐 Enable login-based user session tracking

    🛠️ Build a RESTful backend API to fetch mock product data

    📝 Maintain chat history with timestamps

🧑‍💻 Technologies Used
Layer	Technology
Frontend	React.js, Tailwind CSS, lucide-react
Backend	Flask (Python)
Database	Mock JSON / (Optional: SQLite/MySQL)
Versioning	Git, GitHub
📐 Architecture

[User Interface (React)]  <--->  [API Layer (Flask)]  <--->  [Mock Product Database]
       ⬇                              ⬇
Session Storage                /sendMessage, /getHistory
Chat UI Components            Product Search + Response

✨ Features

    🧠 Conversational chatbot UI for product search

    📜 Maintains full chat history with timestamps

    ↩️ Reset conversation with one click

    🚪 Logout and session management

    ⚡ Smooth auto-scrolling and loading indicators

    🛍️ Dynamic product response cards

    🧪 Mock backend simulating e-commerce inventory (100+ items)

🗂️ Project Structure

├── backend/
│   ├── app.py               # Flask app handling product queries
│   └── products.json        # Mock product inventory
├── frontend-new/
│   └── src/
│       ├── api/
│       │   └── api.js       # API methods: sendMessage, getHistory
│       ├── Chatbot.js       # Chatbot UI logic
│       └── index.js         # Entry point

⚙️ Setup Instructions
🔧 Prerequisites

    Node.js v16+

    Python 3.8+

    Git

🚀 Frontend Setup

cd frontend-new
npm install
npm start

🧪 Backend Setup

cd backend
pip install flask
python app.py

🧪 Sample API Interaction
📨 POST /sendMessage

{
  "message": "Show me latest mobile phones"
}

🔁 Response

{
  "response": [
    { "name": "iPhone 14", "price": 79999 },
    { "name": "Samsung Galaxy S23", "price": 69999 }
  ]
}

📈 Sample Chat UI


(Add screenshot of your chatbot interface here)
✅ Evaluation-Ready Highlights
📱 Responsive Design

    Optimized for desktop, tablet, and mobile.

    Tailwind CSS-based layout with gradients and transitions.

🔒 Authentication (Optional Scope)

    Session tracking via sessionStorage.

📂 Chat History

    Messages stored locally (can be extended to DB).

    Timestamps for every exchange.

⚙️ Code Quality

    Modular React components

    Commented Flask API

    Clean folder structure & reusable logic

🧠 Key Learnings & Challenges

    Implemented a dynamic product-based response engine with minimal data structure.

    Used useEffect and useRef to ensure scroll behavior and input focus enhancements.

    Ensured backend and frontend are decoupled, using RESTful principles.

    Challenge: Handling cross-origin communication and frontend asset restrictions (src/ structure in React).
    Solution: Adjusted structure and API routing to comply with create-react-app limitations.

📄 Future Enhancements

    Add user authentication with JWT

    Integrate payment or cart simulation

    Connect to a real e-commerce API

    Use a persistent database (e.g., PostgreSQL)

📚 Documentation

    Full documentation available inside the /docs directory (if created), covering:

    Architecture diagrams

    API specs

    Sample queries

    Error handling flows

📌 Git Setup Commands

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/E-commerce-Sales-Chatbot.git
git push -u origin main

📢 Presentation Tip

    Be ready to demo your chatbot, walk through:

    A typical user journey

    How data flows from UI to API

    Where products are fetched from

    Code snippets and rationale for each major decision

📝 Author

Dharmveer


