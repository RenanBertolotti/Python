import subprocess

# Windows - ping 192.168.0.1
# Linux   - ping 192.168.0.1 -c 4


# proc = subprocess.run(["ping", 'www.google.com.br'])
proc = subprocess.run(["ping", "192.168.15.4"])


# comandos para ver monitoramento
print(proc.stderr)
print(proc.stdout)
print(proc.returncode)
print(proc.args)