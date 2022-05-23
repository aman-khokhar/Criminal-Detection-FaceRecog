from pyngrok import ngrok

print("Hello")
url = ngrok.connect(5000)
print(url)