
import os

def ip_cmd():
	ip = input("enter ip addres to add on interface \n")
	if len(ip.split('.'))==4:
		interfaces=os.popen('ls /sys/class/net').read()
		print("Interfaces\n",interfaces)
		interface=input("choose interface :\t")
		command =f'ip address add {ip} dev {interface}'
		res =os.popen(command).read()
		print("ip address assigned\n")
	else:
		print("ip is not valid \n")

def ip_del():
	ip = input("Enter ip address to delete /n")
	if len(ip.split('.'))==4:
		interfaces=os.popen('ls /sys/class/net').read()
		print("Interfaces\n",interfaces)
		interface=input("choose interface :\t")
		command= f'ip address del {ip} dev {interface}'
		res=os.popen(command).read()
		print("ip address deleted\n")
	else:
		print("ip invalid format\n")

def ip_display():
	command =f'ip -c -br address'
	res=os.popen(command).read()
	print(res)

def display_all_interface():
	interfaces=os.popen('ls /sys/class/net').read()
	print("Listing all interfaces\n")
	print(interfaces)

def configure_routing():
	network_addr = input('Enter network Address with /mask : ')
	getway_ip = input('Enter Gateway ip address : ')
	if len(network_addr.split('.')) == 4 and len(getway_ip.split('.')) == 4:
		cmd = f'ip r add {network_addr} via {getway_ip}'
		res = os.popen(cmd).read()
		print(res)
		print('Routing configuration completed !')

def on_off_interface():
	print('1.Turned off interface ')
	print('2.Turned on interface')
	choice = int(input('Enter choice : '))
	interfaces = os.popen('ls /sys/class/net').read()
	print(interfaces)
	interface_choice=input("select interface")
	if choice == 1:
		cmd = f'ip link set dev {interface_choice}  down'
		res = os.popen(cmd).read()
		print(res)
		print(f'{interface_choice} turned off ')
	elif choice == 2:
		cmd = f'ip link set dev {interface_choice}  up'
		res = os.popen(cmd).read()
		print(res)
		print(f'{interface_choice} turned on ')
	else:
		print('Wrong option choosed')

def add_arp_entry():
	ip = input('Enter ip address  : ')
	if len(ip.split('.')) == 4:
		interfaces = os.popen('ls /sys/class/net').read()
		interface_choice = input("Enter Interface : ")
		arp_cache = os.popen('ip n show | cut -d " " -f5').read()
		cmd = f'ip n add {ip} lladdr {arp_cache} dev {interface_choice} nud permanent'
		res = os.popen(cmd).read()
		print('ARP Entry added successfully ')

def del_arp_entry():
	ip = input('Enter ip address : ')
	if len(ip.split('.')) == 4:
		interfaces = os.popen('ls /sys/class/net').read()
		interface_choice =input("Enter Interface : ")
		cmd = f'ip n del {ip} dev {interface_choice}'
		res = os.popen(cmd).read()
		print('ARP Entry deleted successfully')

def restart_network():
	cmd = 'sudo systemctl restart networking'
	cmd2 = 'sudo systemctl status networking'
	os.popen(cmd).read()
	print('Network services restarted ')
	print(os.popen(cmd2).read())

def change_host_name():
	host_name = input("Enter new host name :")
	cmd = f'hostnamectl set-hostname {host_name}'
	os.popen(cmd).read()
	print(f'new host name {host_name} set successfully ')

def add_dns_server():
	print('adding dns server')
	print('first : nameserver 8.8.8.8 write in this format')
	print('second : ctrl + d  to exit ')
	cmd = 'sudo cat  >> /etc/resolv.conf'
	print(os.popen(cmd).read())
	print('Nameserver added successfully')
