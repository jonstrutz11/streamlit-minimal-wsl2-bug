# streamlit-minimal-wsl2-bug
Minimal example for issue where streamlit does not detect file changes in WSL2

Steps to reproduce:
1. Clone this repo into a WSL2 environment running Ubuntu 20.04 and with Streamlit 1.11.0 installed
2. Make sure your PYTHONPATH includes this repo such that utils_module is recognized by python
3. `streamlit run Home.py`
4. Make a change to Home.py
5. See if changes are detected in app on Home page (they were for me)
6. Make a change to 1_Page_1.py
7. See if changes are detected in app on Page 1 (they weren't for me)
8. Press button on page 1
9. Make a change to the message in the function in utils_module/utils.py
10. Press the button again, see if message is different (it wasn't for me)
