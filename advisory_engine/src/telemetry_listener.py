import os
import time
from prompt_manager import format_llama_prompt

LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../shared/telemetry_stream.jsonl"))

def listen_telemetry():
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "a").close()

    print("[Advisory] Watching telemetry stream...")
    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            prompt = format_llama_prompt(line)
            print("\n--- NEW OPERATOR ADVISORY PROMPT ---")
            print(prompt)

if __name__ == "__main__":
    listen_telemetry()
