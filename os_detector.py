import subprocess

def detect_os(target):
    output = subprocess.check_output(['ping', target])
    if "ttl" in output.lower().decode():
        ttl = int(output.lower().decode().split("ttl=")[1].split()[0])
        if ttl <= 64:
            return 'Linux'
        elif ttl <= 128:
            return 'windows'

    return 'unknown'

print(detect_os('45.33.32.156'))
