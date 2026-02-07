from pyngrok import ngrok
import uvicorn

# Open a public URL to your local server
public_url = ngrok.connect(8000)
print(f" * Public URL: {public_url}")

# Run the FastAPI app
uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
