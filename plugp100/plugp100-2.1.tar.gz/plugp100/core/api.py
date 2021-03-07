import dataclasses
import logging
from time import time
from typing import Any, Dict

import jsons

from plugp100 import helpers
from plugp100.core.methods.set_device_info_method import SetDeviceInfoMethod
from plugp100.core.params.device_info_params import DeviceInfoParams
from plugp100.encryption import Encryption
from plugp100.http_client import Http
from plugp100.core.exceptions import TapoException
from plugp100.core.key_pair import KeyPair
from plugp100.core.methods import GetDeviceInfoMethod
from plugp100.core.methods import HandshakeMethod
from plugp100.core.methods import LoginDeviceMethod
from plugp100.core.methods import SecurePassthroughMethod
from plugp100.core.params import HandshakeParams
from plugp100.core.params import LoginDeviceParams
from plugp100.tp_link_cipher import TpLinkCipher
from plugp100.core.exceptions.TapoException import TapoException

logger = logging.getLogger(__name__)


class TapoApi:

    def __init__(self, address: str):
        self.address = address
        self.url = f"http://{address}/app"
        logger.debug(f"Device url is: {self.url}")

        self.encryption = Encryption()
        self.key_pair: KeyPair
        self.cookie_token: str = ""
        self.token: str = ""

        self.tp_link_cipher: TpLinkCipher = None

    def handshake(self):
        logger.debug("Will perform handshaking...")

        logger.debug("Generating keypair")
        self.__generate_keypair()

        handshake_params = HandshakeParams(self.key_pair.get_public_key())
        logger.debug(f"Handshake params: {jsons.dumps(handshake_params)}")

        handshake_method = HandshakeMethod(handshake_params)
        logger.debug(f"Handshake method: {jsons.dumps(handshake_method)}")

        request_body = jsons.dump(handshake_method)
        logger.debug(f"Request body: {request_body}")

        response = Http.make_post(self.url, request_body)
        resp_dict: dict = response.json()

        logger.debug(f"Device responded with: {resp_dict}")

        self.__validate_response(resp_dict)
        self.cookie_token = response.cookies.get('TP_SESSIONID')
        logger.debug(f"Got TP_SESSIONID token: ...{self.cookie_token[5:]}")

        logger.debug("Decoding handshake key...")
        self.tp_link_cipher = self.encryption.decode_handshake_key(resp_dict['result']['key'], self.key_pair)

    def login_request(self, username: str, password: str):
        logger.debug(f"Will login using username '{username[5:]}...'")
        digest_username = self.encryption.sha_digest_username(username)
        logger.debug(f"Username digest: ...{digest_username[:5]}")

        login_device_params = LoginDeviceParams(
            helpers.mime_encoder(password.encode("UTF-8")),
            helpers.mime_encoder(digest_username.encode("UTF-8"))
        )

        l_ldp = jsons.dumps(login_device_params).replace(helpers.mime_encoder(password.encode("UTF-8")),
                                                         "PASSWORD_REMOVED")
        logger.debug(f"Login device params: {l_ldp}")

        login_device_method = LoginDeviceMethod(login_device_params)
        l_ldm = jsons.dumps(login_device_method).replace(helpers.mime_encoder(password.encode("UTF-8")),
                                                         "PASSWORD_REMOVED")
        logger.debug(f"Login device method: {l_ldm}")

        ldm_encrypted = self.tp_link_cipher.encrypt(jsons.dumps(login_device_method))
        logger.debug(f"Login device method encrypted: {ldm_encrypted}")

        secure_passthrough_method = SecurePassthroughMethod(ldm_encrypted)
        logger.debug(f"Secure passthrough method: {jsons.dumps(secure_passthrough_method)}")
        request_body = jsons.loads(jsons.dumps(secure_passthrough_method))
        logger.debug(f"Request body: {request_body}")

        response = Http.make_post_cookie(self.url, request_body, {'TP_SESSIONID': self.cookie_token})
        resp_dict: dict = response.json()
        logger.debug(f"Device responded with: {resp_dict}")

        self.__validate_response(resp_dict)

        decrypted_inner_response = jsons.loads(
            self.tp_link_cipher.decrypt(
                resp_dict['result']['response']
            )
        )

        logger.debug(f"Device inner response: {decrypted_inner_response}")

        self.token = decrypted_inner_response['result']['token']

    def get_state(self) -> Dict[str, Any]:
        device_info_method = GetDeviceInfoMethod(None)
        logger.debug(f"Device info method: {jsons.dumps(device_info_method)}")
        dim_encrypted = self.tp_link_cipher.encrypt(jsons.dumps(device_info_method))
        logger.debug(f"Device info method encrypted: {dim_encrypted}")

        secure_passthrough_method = SecurePassthroughMethod(dim_encrypted)
        logger.debug(f"Secure passthrough method: {secure_passthrough_method}")
        request_body = jsons.loads(jsons.dumps(secure_passthrough_method))
        logger.debug(f"Request body: {request_body}")

        response = Http.make_post_cookie(f"{self.url}?token={self.token}", request_body,
                                         {'TP_SESSIONID': self.cookie_token})
        resp_dict: dict = response.json()
        logger.debug(f"Device responded with: {resp_dict}")

        self.__validate_response(resp_dict)

        decrypted_inner_response = jsons.loads(
            self.tp_link_cipher.decrypt(
                resp_dict['result']['response']
            ))
        logger.debug(f"Device inner response: {decrypted_inner_response}")
        self.__validate_response(decrypted_inner_response)

        return decrypted_inner_response['result']

    def set_device_info(self, device_params: DeviceInfoParams, terminal_uuid: str):
        logger.debug(f"Device info will change to: {device_params}")

        device_info_method = SetDeviceInfoMethod(device_params.as_dict())
        device_info_method.set_request_time_milis(time())
        device_info_method.set_terminal_uuid(terminal_uuid)
        logger.debug(f"Device info method: {jsons.dumps(device_info_method)}")

        dim_encrypted = self.tp_link_cipher.encrypt(jsons.dumps(device_info_method))
        logger.debug(f"Device info method encrypted: {dim_encrypted}")

        secure_passthrough_method = SecurePassthroughMethod(dim_encrypted)
        logger.debug(f"Secure passthrough method: {secure_passthrough_method}")
        request_body = jsons.loads(jsons.dumps(secure_passthrough_method))
        logger.debug(f"Request body: {request_body}")

        response = Http.make_post_cookie(f"{self.url}?token={self.token}", request_body,
                                         {'TP_SESSIONID': self.cookie_token})
        resp_dict: dict = response.json()
        logger.debug(f"Device responded with: {resp_dict}")
        self.__validate_response(resp_dict)

        decrypted_inner_response = jsons.loads(
            self.tp_link_cipher.decrypt(
                resp_dict['result']['response']
            ))
        logger.debug(f"Device inner response: {decrypted_inner_response}")
        self.__validate_response(decrypted_inner_response)

    def __generate_keypair(self):
        self.key_pair = self.encryption.generate_key_pair()

    def __validate_response(self, resp: dict):
        if 'error_code' not in resp:
            logger.warning("No error_code in the response!")
        else:
            if resp['error_code'] != 0:
                raise TapoException.from_error_code(resp['error_code'])
