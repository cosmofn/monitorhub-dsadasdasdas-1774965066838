from flask import Flask
import subprocess
import threading
import os
import sys

app = Flask(__name__)

@app.route('/')
def alive():
    return {'status': 'alive', 'message': 'I am alive! 🟢', 'service': 'python main.py'}

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/api/status')
def status():
    return {'status': 'running', 'uptime': 'active', 'command': 'python main.py'}

def run_user_command():
    try:
        print(f"🚀 Starting: python main.py", flush=True)
        process = subprocess.Popen("python main.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            print(line, end='', flush=True)
        for line in process.stderr:
            print(line, end='', file=sys.stderr, flush=True)
    except Exception as e:
        print(f"❌ Error: {e}", flush=True)

if __name__ == '__main__':
    print("🔮 MonitorHub Wrapper Starting...", flush=True)
    thread = threading.Thread(target=run_user_command, daemon=True)
    thread.start()
    port = int(os.environ.get('PORT', 10000))
    print(f"🌐 Server running on port {port}", flush=True)
    app.run(host='0.0.0.0', port=port, debug=False)
