# 🛡️ Phishing Detection Tool (AI Cyber Security Project)

![Tool UI Screenshot](Screenshot%202025-09-01%20004139.png)
![Scan Result Example](Screenshot%202025-09-01%20004238.png)

This project is a **real-time phishing URL detection tool** that combines **heuristic analysis** and the **PhishTank API** to help identify potentially malicious websites.

---

## 🚀 Features
- Detects suspicious patterns in URLs (`@` symbols, long URLs, IP-based domains, missing HTTPS).
- Integrates with **PhishTank database** for community-driven phishing detection.
- Provides a **risk score** and a clear **verdict**:  
  - **Legitimate (0–2)**  
  - **Suspicious (3–5)**  
  - **Phishing Likely (6+)**
- Real-time analysis with a **Streamlit web interface**.

---

## 📂 Project Structure
```
.
├── app.py                # Main Streamlit app
├── heuristics.py         # Heuristic-based detection logic
├── requirements.txt      # Dependencies
├── Screenshot 2025-09-01 004139.png   # UI screenshot
├── Screenshot 2025-09-01 004238.png   # Scan example screenshot
└── README.md             # Project documentation
```

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phishtank-exploration.git
   cd phishtank-exploration
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Usage
Run the Streamlit app:
```bash
streamlit run app.py
```
Then open the local URL shown in your terminal (usually `http://localhost:8501`).

Paste a suspicious URL and click **Scan**. The tool will:
1. Perform **heuristic analysis**.
2. Query the **PhishTank database**.
3. Display a **risk score, verdict, and reasons**.

---

## 🔍 Example
Input:
```
http://example.com@phish.test/login
```
Output:
- **Verdict**: Phishing Likely  
- **Risk Score**: 6  
- **Reasons**: Contains '@', No HTTPS, Long URL

---

## 📦 Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`:
  ```
  streamlit
  requests
  ```

---

## 📜 License
This project is for educational and cybersecurity research purposes only.  
Use responsibly — **do not use it for malicious activities**.
