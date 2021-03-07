#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from netw0rk.classes.config import *
from netw0rk.classes import utils

# the firewall class.
class FireWall(object):
	def __init__(self):	
		a=1
		#
	def enable(self):

		# check os.
		response = self.__check_os__()
		if response["error"] != None: return response

		# do.
		output = utils.__execute_script__("printf 'y\\ny\\ny\\ny\\ny\\ny\\n' | sudo ufw enable")
		if "Firewall is active and enabled on system startup" in output:
			return r3sponse.success(f"Successfully enabled the firewall.")
		else:
			return r3sponse.error(f"Failed to enable the firewall.")

		#
	def disable(self):
		
		# check os.
		response = self.__check_os__()
		if response["error"] != None: return response

		# do.
		output = utils.__execute_script__("printf 'y\\ny\\ny\\ny\\ny\\ny\\n' | sudo ufw disable")
		if "Firewall stopped and disabled on system startup" in output:
			return r3sponse.success(f"Successfully disabled the firewall.")
		else:
			return r3sponse.error(f"Failed to disable the firewall.")

		#
	def allow(self, port):
		

		# check os.
		response = self.__check_os__()
		if response["error"] != None: return response

		# do.
		output = utils.__execute__(["sudo", "ufw", "allow", str(port)])
		if "Rule updated" in output or "Rules updated" in output or "Skipping adding existing rule" in output:
			return r3sponse.success(f"Successfully allowed port [{port}].")
		else:
			return r3sponse.error(f"Failed to allow port [{port}], output: [{output}].")

		#
	def deny(self, port):
		

		# check os.
		response = self.__check_os__()
		if response["error"] != None: return response

		# do.
		output = utils.__execute__(["sudo", "ufw", "deny", str(port)])
		if "Rule updated" in output or "Rules updated" in output or "Skipping adding existing rule" in output:
			return r3sponse.success(f"Successfully denied port [{port}].")
		else:
			return r3sponse.error(f"Failed to deny port [{port}], output: [{output}].")

		#
	def allow_all(self):
		response = self.info()
		if response["error"] != None: return response
		response = self.set_default(deny=True)
		if response["error"] != None: return response
		ports = response["ports"]
		for port, info in ports.items():
			response = self.allow(port)
			if response["error"] != None: return response
		return r3sponse.success(f"Successfully allowed all {len(ports)} ports.")
	def deny_all(self):
		response = self.info()
		if response["error"] != None: return response
		response = self.set_default(deny=False)
		if response["error"] != None: return response
		ports = response["ports"]
		for port, info in ports.items():
			response = self.allow(port)
			if response["error"] != None: return response
		return r3sponse.success(f"Successfully allowed all {len(ports)} ports.")
	def set_default(self, deny=True):
		

		# check os.
		response = self.__check_os__()
		if response["error"] != None: return response

		# do.
		option = None
		if deny: option = "deny"
		else: option = "allow"
		output = utils.__execute__(["sudo", "ufw", "default", option])
		if "Default incoming policy changed to " in output:
			return r3sponse.success(f"Successfully set the default action to [{option}].")
		else:
			return r3sponse.error(f"Failed set the default action to [{option}].")

		#
	def info(self):
		def __handle_port_line__(line):
			new = []
			for i in line.split("  "):
				if i not in ["", " "]:
					new.append(i)
			_new_ = []
			for i in new:
				for a in range(101):
					if len(i) > 0 and i[0] == " ": i = i[1:]
					elif len(i) > 0 and i[len(i)-1] == " ": i = i[:-1]
					else: break
				_new_.append(i)
			return {
				"port":_new_[0],
				"status":_new_[1],
				"from":_new_[2],
			}

		# check os.
		response = self.__check_os__()
		if response["error"] != None: return response

		# retrieve.
		output = utils.__execute__(["sudo", "ufw", "status"])
		#print(f"Output: [{output}].")

		# get status.
		status = "unkown"
		if "Status: " in output: 
			try: status = output.split("Status: ")[1].split("\n")[0].replace(" ","")
			except IndexError: status = "unkown"

		# iterate ports.
		ports = {}
		output = output.split('\n')
		if len(output) > 1:
			c, set = 0, 0
			for i in output:
				if 'To' in i and 'Action' in i and 'From' in i:
					set += 1
				elif set >= 2:
					if i not in ["", " "]:
						info = __handle_port_line__(i)
						ports[info["port"]] = info
				elif set != 0: set += 1
				c += 1

		# success.
		return r3sponse.success("Successfully retrieved the firewall info.", {
			"status":status,
			"ports":ports,
		})

		#
	# system functions.
	def __check_os__(self):
		if OS not in ["linux"]:
			return r3sponse.error(f"Unsupported operating system: [{OS}].")
		return r3sponse.success(f"Supported operating system: [{OS}].")

# initialized classes.
firewall = FireWall()

"""

# retrieve the firewall information.
response = firewall.info()

# disable the firewall.
response = firewall.disable()

# enable the firewall.
response = firewall.enable()

# set the default port action.
response = set_default(deny=True)

# allow a port.
response = firewall.allow(2200)

# deny a port.
response = firewall.deny(2200)

"""