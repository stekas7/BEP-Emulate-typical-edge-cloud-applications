import subprocess

# Base command and parameters
base_command = [
    "wrk", "-t", "2", "-c", "2", "-d", "10", "-L", 
    "-s", "./wrk2/scripts/hotel-reservation/mixed-workload_type_1.lua",
    "http://frontend.default.svc.cluster.local:5000"
]

# Iterate from 1 to 10 for the requests per second
for rps in range(1, 11):
    # Construct the command with the current RPS
    command = base_command + ["-R", str(rps)]
    print(f"Running: {' '.join(command)}")
    
    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Print the output
    print(result.stdout)
    print(result.stderr)
