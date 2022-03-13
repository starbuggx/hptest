# honeypot

Docker image
docker pull ghcr.io/starbuggx/honeypot:latest
  
Running on your machine
docker run -d -p 8080:8080 ghcr.io/starbuggx/honeypot:latest
  
Test
curl http://localhost:8080/wplogin.cgi?admin=True
You will receive a new line of text - "Not Found" every 5 seconds.
