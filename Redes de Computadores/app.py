import socket

hostname = socket.gethostname()
ipv4 = socket.gethostbyname(hostname)

ipv4_bin_list = ipv4.replace("."," ").split()

ipv4_binary = []

for octet in ipv4_bin_list:
  octet_bin = bin(int(octet))[2:]

  ipv4_binary.append(octet_bin)

print(f'Your Computer Name is: {hostname}')
print(f'Your Computer IP Address is: {ipv4}')
print(f'Your Computer IP Address in Binary is: {".".join(ipv4_binary)}')