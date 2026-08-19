from pyngrok import ngrok
import time

ngrok.set_auth_token('3Ceim6UOoxxcS6aWR3bXlDDEssU_4is5jXvZSoPhkrgt3Ppdm')
tunnel = ngrok.connect(5000)
print("ngrok tunnel URL:", tunnel.public_url)
print("Keep this window open!")
print("Press Ctrl+C to stop")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping ngrok...")
    ngrok.kill()