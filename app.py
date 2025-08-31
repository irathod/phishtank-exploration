# app.py
import streamlit as st
from heuristics import heuristic_score_and_reasons
import requests

# PhishTank check endpoint
PHISHTANK_CHECK_URL = "https://checkurl.phishtank.com/checkurl/"

def check_phishtank(url):
    """
    Returns a dict:
      - success: True/False
      - in_database: True/False if found in PhishTank
      - verified: True/False/None
      - message: status message
    """
    try:
        r = requests.post(PHISHTANK_CHECK_URL, data={'url': url}, headers={'format': 'json'}, timeout=10)
        if r.status_code != 200:
            return {"success": False, "message": f"HTTP {r.status_code}"}
        data = r.json()
        res = data.get('results', {})
        in_db = res.get('in_database') if isinstance(res.get('in_database'), bool) else res.get('valid', False)
        verified = res.get('verified') if 'verified' in res else None
        return {"success": True, "in_database": bool(in_db), "verified": verified, "raw": res}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Streamlit UI
st.set_page_config(page_title="Phishing Detection Tool", page_icon="🛡️")
st.title("🛡️ Phishing Detection Tool (Real-time)")

st.markdown("""
Enter a URL below to analyze if it is phishing or safe.  
The tool uses heuristic checks and PhishTank (community phishing database).
**Note:** Do not click on suspicious links — only paste them.
""")

url = st.text_input("Enter URL (with http:// or https://)", value="http://example.com@phish.test/login")

if st.button("Scan"):
    if not url:
        st.error("Please enter a URL.")
    else:
        st.info("Analyzing URL...")
        res = heuristic_score_and_reasons(url)

        st.subheader("Verdict")
        if res["verdict"] == "Invalid URL":
            st.error("Invalid URL format. Add http:// or https://")
        else:
            if res["verdict"] == "Phishing Likely":
                st.error(f"**{res['verdict']}**  — Risk Score: {res['score']}")
            elif res["verdict"] == "Suspicious":
                st.warning(f"**{res['verdict']}**  — Risk Score: {res['score']}")
            else:
                st.success(f"**{res['verdict']}**  — Risk Score: {res['score']}")

            st.subheader("Reasons")
            for level, msg in res["reasons"]:
                if level == "warn":
                    st.warning(msg)
                elif level == "info":
                    st.info(msg)
                else:
                    st.write(msg)

        st.subheader("PhishTank Check")
        ph = check_phishtank(url)
        if not ph["success"]:
            st.info("PhishTank check unavailable: " + ph.get("message", ""))
        else:
            if ph.get("in_database"):
                st.error(f"PhishTank: URL found in database. Verified: {ph.get('verified')}")
            else:
                st.success("PhishTank: URL not found in database.")
