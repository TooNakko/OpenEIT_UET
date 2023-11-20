
import threading
import subprocess

def run_script(script):
    subprocess.run(['python', script])

# Create threads for each script
thread1 = threading.Thread(target=run_script, args=('plot.py',))
thread2 = threading.Thread(target=run_script, args=('WriteIntoCom.py',))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

