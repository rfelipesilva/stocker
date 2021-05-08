mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = '#011f4b'
backgroundColor = '#FFFFFF'
secondaryBackgroundColor = '#b3cde0'
textColor = '#262730'
font = 'sans serif'
[server]
port = $PORT
enableCORS = false
headless = true
" > ~/.streamlit/config.toml