#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from w3bsite.classes.config import *
from w3bsite.classes import utils

# the deployment object class.
class Deployment(syst3m.objects.Object):
	# does not use Defaults so also accessable without Website init.
	# deploy the website on a local ubuntu machine.
	def __init__(self,
		# the root path.
		root=None,
		# the library path.
		library=None,
		# the website name.
		name=None,
		# the domain.
		domain=None,
		# the database path.
		database=None,
		# the remote.
		remote=None,
		# the vps ip (if remote is vps else leave default).
		vps_ip=None,
		vps_username=None,
		# the organization's email.
		email=None,
		country_code="NL",
		province="Amsterdam",
		city="Amsterdam",
		organization=None,
		organization_unit="IT",
		# the organization info.
		# objects.
		namecheap=None,
	):	

		# defaults.
		syst3m.objects.Object.__init__(self, traceback="w3bsite.Website.deployment",)

		# attributes.
		self.vps_ip = vps_ip
		self.vps_username = vps_username
		self.root = root
		self.library = library
		self.domain = domain
		self.database = database
		self.remote = remote
		self.name = name

		self.country_code = country_code
		self.province = province
		self.city = city
		self.organization = organization
		self.organization_unit = organization_unit
		self.email = email

		# vars.
		self.live = gfp.clean(self.library, remove_double_slash=True, remove_last_slash=True) in gfp.clean(self.root, remove_double_slash=True, remove_last_slash=True)

		# objects.
		self.namecheap = namecheap

		#
	# live functions.
	def start(self):

		# execute.
		command = ""
		for i in ["gunicorn.socket", "gunicorn", "nginx"]:
			command += f"sudo systemctl start {i} &&"
		command = command[:-3]
		output = syst3m.utils.__execute_script__(command)
		if output in ["", "\n"]:
			return r3sponse.success(f"Successfully started {self.name}")
		else:
			return r3sponse.error(f"Failed to started {self.name};\n{output}")

		#
	def stop(self):

		# execute.
		command = ""
		for i in ["gunicorn.socket", "gunicorn", "nginx"]:
			command += f"sudo systemctl stop {i} &&"
		command = command[:-3]
		output = syst3m.utils.__execute_script__(command)
		if output in ["", "\n"]:
			return r3sponse.success(f"Successfully stopped {self.name}")
		else:
			return r3sponse.error(f"Failed to stopped {self.name};\n{output}")

		#
	def restart(self):

		# execute.
		command = ""
		for i in ["gunicorn.socket", "gunicorn", "nginx"]:
			command += f"sudo systemctl restart {i} &&"
		command = command[:-3]
		output = syst3m.utils.__execute_script__(command)
		if output in ["", "\n"]:
			return r3sponse.success(f"Successfully restarted {self.name}")
		else:
			return r3sponse.error(f"Failed to restarted {self.name};\n{output}")

		#
	def status(self):

		# execute.
		response = syst3m.console.execute("sudo systemctl status gunicorn > /tmp/status && cat /tmp/status && rm -fr /tmp/status")
		if not response.success: return response
		status = response.output
		return r3sponse.success(f"Successfully parsed the status of {self.name}.", {
			"status":data,
		})

		#
	def reset_logs(self):

		# execute.
		Files.save(f"{self.database}/logs/logs", "")
		Files.save(f"{self.database}/logs/errors", "")
		Files.save(f"{self.database}/logs/nginx", "")
		Files.save(f"{self.database}/logs/nginx.debug", "")
		return r3sponse.success("Successfully resetted the logs.")

		#
	def tail(self, nginx=False, debug=False):
		
		# execute.
		if nginx:
			if debug:
				data = Files.load(f"/{self.database}/logs/nginx.debug")
			else:
				data = Files.load(f"/{self.database}/logs/nginx")
		else:
			if debug:
				data = Files.load(f"{self.database}/logs/logs")
			else:
				data = Files.load(f"{self.database}/logs/errors")
		
		# handler.
		return r3sponse.success(f"Successfully tailed the {self.name} logs.", {
			"logs":data,
		})

		#

	# configure also for remove:vps & remote:local.
	def configure(self, reinstall=False, log_level=0, loader=None):
		
		# check arguments.
		if self.remote in ["vps"]:
			response = r3sponse.parameters.check(
				traceback=self.__traceback__(function="configure"),
				parameters={
					"vps_ip":self.vps_ip,
					"vps_username":self.vps_username,
				})
			if not response.success: return response
			username = self.vps_username
		else:
			username = syst3m.defaults.vars.user
		
		# configure before loader.
		if self.live:
			if reinstall:
				os.system(f"rm -fr {self.database}/tls/dhparam.pem")
			if not Files.exists(f"{self.database}/tls/dhparam.pem"):
				if loader != None: loader.hold()
				tmp = "/tmp/dhparam.pem"
				os.system(f"sudo openssl dhparam -out {tmp} 4096 && sudo chown {syst3m.defaults.vars.user}:{syst3m.defaults.vars.group} {tmp} && mv {tmp} {self.database}/tls/dhparam.pem && sudo chown {syst3m.defaults.vars.user}:{syst3m.defaults.vars.group} {self.database}/tls/dhparam.pem")
				if loader != None: loader.release()

		# loader.
		if log_level >= 0: loader = syst3m.console.Loader(f"Configuring deployment of website {self.domain} ...")

		# check remote.
		if self.remote in ["heroku"]:
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error(f"You can not execute function <Website.deployment.configure> with remote [{self.remote}].")

		# os.
		if OS not in ["macos", "linux"]: 
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error(f"Unsupported operating system [{OS}].")

		# requirements.
		if not Files.exists(f"{self.root}/requirements"): os.mkdir(f"{self.root}/requirements")
		if not Files.exists(f"{self.root}/requirements/requirements.pip"): 
			Files.save(f"{self.root}/requirements/requirements.pip", "wheel\nuwsgi\ngunicorn\nwhitenoise\ndjango\npsycopg2-binary\nsyst3m\nw3bsite\ncl1")
		if not Files.exists(f"{self.root}/requirements/installer"): 
			os.system(f"cp {SOURCE_PATH}/example/requirements/installer {self.root}/requirements/installer && chmod +x {self.root}/requirements/installer")

		# favicon.
		if not Files.exists(f"{self.root}/static/favicon.ico"):
			output = syst3m.utils.__execute_script__(f"curl https://raw.githubusercontent.com/vandenberghinc/public-storage/master/w3bsite/favicon.ico -o {self.root}/static/favicon.ico")

		# tls.
		if self.live:
			if not Files.exists(f"{self.database}/tls/server.key") and not Files.exists(f"{self.database}/tls/server.crt"):
				response = self.generate_tls(log_level=log_level)
				if not response.success: 
					if log_level >= 0: loader.stop(success=False)
					return response

		# database.
		if self.live:
			if not Files.exists(self.database): 
				os.system(f"sudo mkdir -p {self.database} && sudo chown {syst3m.defaults.vars.user}:{syst3m.defaults.vars.group} {self.database} && sudo chmod 770 {self.database}")
			if not Files.exists(f"{self.database}/logs"): os.mkdir(f"{self.database}/logs")

		# deployment.
		if not Files.exists(f"{self.root}/deployment"): os.mkdir(f"{self.root}/deployment")
		clean_root = gfp.clean(self.library, remove_last_slash=True, remove_double_slash=True) # <== note the library change instead of root.
		replacements = {
			"***ROOT***":clean_root, 
			"***USER***":username, 
			"***DOMAIN***":self.domain,
			"***DATABASE***":self.database,
			"***USER***":syst3m.defaults.vars.user,
			"***WEBSITE_BASE***":gfp.base(SOURCE_PATH),
		}
		for path in Files.Directory(path=f"{SOURCE_PATH}/classes/deployment/lib/").paths():
			name = FilePath(path).name()
			try:
				data = Files.load(path)
			except FileNotFoundError:
				data = ""
			new_data = str(data)
			for key,value in replacements.items():
				new_data = new_data.replace(key, value)
			Files.save(f"{self.root}/deployment/{name}", new_data)
		
		# success.
		if log_level >= 0: loader.stop()
		return r3sponse.success(f"Successfully configured the deployment of domain {self.domain}.")

		#
	# deploy is for remote:local only. 
	def deploy(self, code_update=False, reinstall=False, log_level=0):
			
		# loader.
		loader = None
		if log_level >= 0: loader = syst3m.console.Loader(f"Deploying domain {self.domain} ...")

		# check namecheap domain.
		if not (self.remote in ["vps"] and self.live):
			response = self.namecheap.check_domain(self.namecheap.post_domain)
			if response.error != None: 
				if log_level >= 0: loader.stop(success=False)
				r3sponse.log(response=response, log_level=log_level)
				return response
			elif not response["exists"]:
				if log_level >= 0: loader.stop(success=False)
				return r3sponse.error(f"Specified domain [{self.namecheap.post_domain}] is not owned by namecheap user [{self.namecheap.username}].", log_level=log_level)

		# check remote.
		if self.remote in ["vps"] and not self.live:
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error(f"You can not execute function <Website.deployment.deploy> with remote [{self.remote}].")

		# os.
		if OS not in ["linux"]: 
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error(f"Unsupported operating system [{OS}].")
		
		# configure.
		response = self.configure(reinstall=reinstall, log_level=log_level, loader=loader)
		if not response.success: 
			if log_level >= 0: loader.stop(quiet=True)
			return response

		# check tls domain.
		if not Files.exists(f"{self.database}/tls/.domain"): Files.save(f"{self.database}/tls/.domain", self.domain)
		tls_domain = Files.load(f"{self.database}/tls/.domain").replace('\n',"")
		if tls_domain != self.domain:
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error(f"TLS Certificate mis match. Installed tls certificate [{self.database}/tls] is linked to domain {tls_domain}, not specified domain {self.domain}.", log_level=0)
		
		# checks.
		if not Files.exists(f"{self.database}/tls/server.key") or not Files.exists(f"{self.database}/tls/server.crt"):
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error("No tls certificate exists.\nExecute the following command to generate a tls certificate:\n$ ./website.py --generate-tls", log_level=log_level)
		#if not Files.exists(f"{self.database}/tls/signed.server.crt"):
		#	if log_level >= 0: loader.stop(success=False)
		#	return r3sponse.error("No activated tls certificate exists. \nExecute the following command to activate the generated tls certificate:\n$ ./website.py --activate-tls", log_level=log_level)
		#if not Files.exists(f"{self.database}/tls/server.ca-bundle"):
		#	if log_level >= 0: loader.stop(success=False)
		#	return r3sponse.error("No bundled tls certificate exists. \nDownload the signed certificate send to your email, extr the zip to a directory and execute \n$ ./website.py --bundle-tls /path/to/extracted/directory/", log_level=log_level)
		
		# arguments.
		arguments = ""
		if code_update: arguments += " --code-update"
		if reinstall: arguments += " --reinstall"
		
		# execute & handle.
		os.system(f"chmod +x {self.root}/deployment/installer")
		output = syst3m.utils.__execute_script__(f"bash {self.root}/deployment/installer{arguments}").replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')
		if "Error:" in output or ("nginx: the configuration file /etc/nginx/nginx.conf syntax is ok" not in output and "nginx: configuration file /etc/nginx/nginx.conf test is successful" not in output): #"Successfully deployed domain " not in output
			print(output)
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error(f"Failed to deploy website {self.domain}.", log_level=log_level)
		else:
			if log_level >= 0: loader.stop()
			return r3sponse.success(f"Successfully deployed domain https://{self.domain}.", log_level=log_level)

		#
	def generate_tls(self, log_level=0):
		# https://devcenter.heroku.com/articles/acquiring-an-ssl-certificate

		# check base.
		base = f"{self.root}/__defaults__/"
		if not Files.exists(base): os.mkdir(base)
		base = f"{self.database}/tls"
		if not Files.exists(base): os.mkdir(base)

		# check duplicate.
		if Files.exists(f"{self.database}/tls/server.key") or Files.exists(f"{self.database}/tls/server.crt"):
			return r3sponse.error("The tls certificate already exists.", log_level=log_level)

		# generate.
		if log_level >= 0: loader = syst3m.console.Loader("Generating a tls certificate ...")
		output = syst3m.utils.__execute_script__(f"""
			cd {base}

			# Generate a passphrase
			openssl rand -base64 48 > passphrase.txt

			# Generate a Private Key
			openssl genrsa -aes128 -passout file:passphrase.txt -out server.key 4096 # 2048

			# Generate a CSR (Certificate Signing Request)
			openssl req -new -passin file:passphrase.txt -key server.key -out server.csr \
			    -subj "/C={self.country_code}/ST={self.province}/L={self.city}/O={self.organization}/OU={self.organization_unit}/CN={self.domain}/emailAddress={self.email}"

			# Remove Passphrase from Key
			cp server.key server.pass.key
			openssl rsa -in server.pass.key -passin file:passphrase.txt -out server.key

			# Do not self sign.
			# Generating a Self-Signed Certificate for 100 years
			openssl x509 -req -sha256 -days 36500 -in server.csr -signkey server.key -out server.crt

		""")

		# handler.
		if not Files.exists(f"{self.database}/tls/server.key") or not Files.exists(f"{self.database}/tls/server.crt"):
			if log_level >= 0: loader.stop(success=False)
			os.system(f"rm -fr {base}")
			return r3sponse.error(f"Failed to generate a tls certificate.", log_level=log_level)
		else:
			if log_level >= 0: loader.stop()
			Files.save(f"{self.database}/tls/.domain", self.domain)
			return r3sponse.success(f"Successfully generated a tls certificate.", log_level=log_level)

		#
	def activate_tls(self, log_level=0):

		# check existsance.
		if not Files.exists(f"{self.database}/tls/server.key") or not Files.exists(f"{self.database}/tls/server.crt"):
			return r3sponse.error("No generated tls certificate exists.", log_level=log_level)

		# check duplicate.
		if Files.exists(f"{self.database}/tls/signed.server.key"):
			return r3sponse.error("A signed tls certificate already exists.", log_level=log_level)

		response = self.namecheap.get_tls()
		if response.error != None: 
			r3sponse.log(response=response, log_level=log_level)
			return response
		tls, certificates = response["tls"], response["certificates"]
		
		# check no certificates.
		if certificates == 0:

			# create tls.
			loader = syst3m.console.Loader("Purchasing a namecheap tls certificate ...")
			response = self.namecheap.create_tls(
				# the expiration years.
				years=2,
				# the tls type.
				type="PositiveSSL",)
			r3sponse.log(response=response, log_level=log_level)
			if response.error != None: 
				loader.stop(success=False)
				return response	
			loader.stop()
			
			# get tls again.
			response = self.namecheap.get_tls()
			if response.error != None: 
				loader.stop(success=False)
				r3sponse.log(response=response, log_level=log_level)
				return response
			loader.stop()
			tls, certificates = response["tls"], response["certificates"]

		# check root domain tls.
		tls_activated = False
		for certificate_id, info in tls.items():
			if info["host_name"] == self.domain:
				tls_activated = True
				break
		if not tls_activated:

			# get new purchase certficiate.
			id = None
			for certificate_id, info in tls.items():
				if info["status"] == "newpurchase":
					id = certificate_id
					break

			# create certficiate on no new purchase found.
			if id == None:
				loader = syst3m.console.Loader("Purchasing a namecheap tls certificate ...")
				response = self.namecheap.create_tls(
					# the expiration years.
					years=2,
					# the tls type.
					type="PositiveSSL",)
				r3sponse.log(response=response, log_level=log_level)
				if response.error != None: 
					loader.stop(success=False)
					return response	
				loader.stop()
				id = response["certificate_id"]

			# activate tls for root domain.
			loader = syst3m.console.Loader("Activating tls certificate ...")
			response = self.namecheap.activate_tls(
				# the certificate's id.
				certificate_id=id,)
			loader.stop(success=response["success"])
			r3sponse.log(response=response, log_level=log_level)
			if response.error != None: return response
			
		# handlers.
		return r3sponse.success(f"Successfully activated the tls certificate of domain [{self.domain}]. Wait for the CA to send you a .zip file with your signed certificate. Extract the zip & bundle the certificate with: $ ./website.py --bundle-tls /path/to/extracted/directory/certificate/", log_level=log_level)

		#
	def bundle_tls(self, directory, log_level=0):
		
		# check dir.
		if not Files.exists(directory):
			return r3sponse.error(f"Specified directory [{directory}] does not exist.", log_level=log_level)
		if ".zip" in directory:
			return r3sponse.error(f"Specified directory [{directory}] is zip format, extract the zip first.", log_level=log_level)
		if not os.path.isdir(directory):
			return r3sponse.error(f"Specified directory [{directory}] is not a directory.", log_level=log_level)
		
		# move x.crt to server.crt
		if not Files.exists(f"{directory}/server.crt") and not Files.exists(f'{directory}/{self.domain.replace(".","_")}.crt'):
			return r3sponse.success(f'You must rename the [{directory}/{self.domain.replace(".","_")}.crt] file manually to [{directory}/server.crt] in order to proceed.', log_level=log_level)
		if not Files.exists(f"{directory}/server.crt") and Files.exists(f'{directory}/{self.domain.replace(".","_")}.crt'):
			os.system(f'mv {directory}/{self.domain.replace(".","_")}.crt {directory}/server.crt')
		if not Files.exists(f"{directory}/server.crt"):
			return r3sponse.success(f'Failed to rename the [{directory}/{self.domain.replace(".","_")}.crt] file to [{directory}/server.crt].', log_level=log_level)

		# bundle ca.
		syst3m.utils.__execute_script__(f"""
			cat {directory}/AAACertificateServices.crt {directory}/SectigoRSADomainValidationSecureServerCA.crt {directory}/syst3m.defaults.vars.userTrustRSAAAACA.crt > {self.database}/tls/server.ca-bundle
			cat {directory}/server.crt {self.database}/tls/server.ca-bundle > {self.database}/tls/signed.server.crt
			mv {self.database}/tls/server.crt {self.database}/tls/original.server.crt
			cp {self.database}/tls/signed.server.crt {self.database}/tls/server.crt
			""")
		if Files.exists(f"{self.database}/tls/signed.server.crt"):
			return r3sponse.success(f"Successfully bundled ssl certificate [{directory}].", log_level=log_level)
		else:
			return r3sponse.error(f"Failed to bundle ssl certificate [{directory}].", log_level=log_level)
	def check_dns(self, log_level=0):

		# loader.
		if log_level >= 0: loader = syst3m.console.Loader(f"Checking dns settings of domain {self.domain} ...")

		# check namecheap domain.
		response = self.namecheap.check_domain(self.namecheap.post_domain)
		if response.error != None: 
			if log_level >= 0: loader.stop(success=False)
			r3sponse.log(response=response, log_level=log_level)
			return response
		elif not response["exists"]:
			if log_level >= 0: loader.stop(success=False)
			return r3sponse.error(f"Specified domain [{self.namecheap.post_domain}] is not owned by namecheap user [{self.namecheap.username}].", log_level=log_level)

		# add dns records.
		ip = NETWORK_INFO["public_ip"]
		if self.remote in ["vps"]: ip = self.vps_ip
		host = "@"
		www_host = "www"
		if self.namecheap.pre_domain != "":
			host = self.namecheap.pre_domain
			www_host = f"www.{self.namecheap.pre_domain}"
		response = self.namecheap.add_dns(
			# the domain.
			domain=self.namecheap.post_domain,
			# the dns record type,
			type="A",
			# the dns record host,
			host=www_host,
			# the dns record value/address,
			value=ip,)
		if response.error != None and "] already exists." not in response.error: 
			r3sponse.log(response=response, log_level=log_level)
			if log_level >= 0: loader.stop(success=False)
			return response
		elif response.error == None: 
			r3sponse.log(response=response, log_level=log_level)
		response = self.namecheap.add_dns(
			# the domain.
			domain=self.namecheap.post_domain,
			# the dns record type,
			type="A",
			# the dns record host,
			host=host,
			# the dns record value/address,
			value=ip,)
		if response.error != None and "] already exists." not in response.error: 
			r3sponse.log(response=response, log_level=log_level)
			if log_level >= 0: loader.stop(success=False)
			return response
		elif response.error == None: 
			r3sponse.log(response=response, log_level=log_level)
		
		# handlers.
		if log_level >= 0: loader.stop()
		return r3sponse.success(f"Successfully checked the deployment dns settings for domain {self.domain}.", log_level=log_level)

		#

