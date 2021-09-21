
#!/usr/bin/python3

import os
from script import *

def main():
	print("1 Assign ip address")
	print("2 delete ip address")
	print("3 display ip address")
	print("4 display all interfaces")
	print("5 configure routing")
	print("6 Turn on/off interfaces")
	print("7 add ARP entry ")
	print("8 Delete ARP entry")
	print("9 restart Network")
	print("10 change hostname")
	print("11 Add DNS server entry")
	print("12 exit ")


while True:
	main()
	ch = int(input("Enter the choice"))
	if ch==1:
		ip_cmd()
	elif ch==2:
		ip_del()
	elif ch==3:
		ip_display()
	elif ch==4:
		display_all_interface()
	elif ch==5:
		configure_routing()
	elif ch==6:
		on_off_interface()
	elif ch==7:
		add_arp_entry()
	elif ch==8:
		del_erp_entry()
	elif ch==9:
		restart_network()
	elif ch==10:
		change_host_name()
	elif ch==11:
		add_dns_server()
	elif ch==12:
		break
	else:
		print("wrong choice")
