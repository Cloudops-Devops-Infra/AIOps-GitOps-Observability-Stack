import ollama
import requests

# 🔹 Local Infrastructure Identity Control Blocks
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "Website-Deployment-Pipeline"
USER_NAME = "admin"  # 🧠 Changed back to your actual Jenkins User ID
API_TOKEN = "112bada7e4c0ee292ea0a207ca45835227"  # Keeping your fresh token intact

print(f"🔍 [AIOps Engine]: Connecting to local server stream at {JENKINS_URL}...")

try:
    # 1. Target the raw plain-text telemetry log of the last build execution
    log_endpoint = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"
    
    # 2. Fire an authenticated request payload 
    response = requests.get(log_endpoint, auth=(USER_NAME, API_TOKEN))
    
    if response.status_code in [401, 403]:
        print("❌ Authentication failed. Double-check your Jenkins API Token string.")
        exit(1)
    elif response.status_code != 200:
        print(f"❌ Server communication dropped. Job might not exist yet. (HTTP {response.status_code})")
        exit(1)
        
    # 3. Isolate the final 60 lines of text (where the fatal runtime failures settle)
    full_log_dump = response.text.splitlines()
    failed_log_slice = "\n".join(full_log_dump[-60:])
    
    # 4. Formulate an SRE-grade operational prompt system frame
    system_instruction = (
        "You are an elite Site Reliability Engineer (SRE). Analyze this live local Jenkins log failure. "
        "State the exact root cause in one bold sentence, then list actionable terminal commands to fix it."
    )
    
    print("🤖 [Local AI Agent]: Extracting logs and running local trace evaluation...")
    print("-" * 70)
    
    # 5. Pipeline payload directly into your local running Llama 3.2 database
    ai_response = ollama.generate(
        model='llama3.2:1b',
        prompt=f"Context:\n{system_instruction}\n\nLive Jenkins Logs:\n{failed_log_slice}"
    )
    
    # 6. Output the diagnosis output block
    print("\n🚨 AUTOMATED AI FAILURE RECONCILIATION REPORT:\n")
    print(ai_response['response'])
    print("-" * 70)

except Exception as e:
    print(f"❌ Critical system connection breakdown: {e}")