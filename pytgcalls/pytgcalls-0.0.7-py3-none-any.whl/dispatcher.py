#  tgcalls - Python binding for tgcalls (c++ lib by Telegram)
#  pytgcalls - Library connecting python binding for tgcalls and Pyrogram
#  Copyright (C) 2020-2021 Il`ya (Marshal) <https://github.com/MarshalX>
#
#  This file is part of tgcalls and pytgcalls.
#
#  tgcalls and pytgcalls is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  tgcalls and pytgcalls is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License v3
#  along with tgcalls. If not, see <http://www.gnu.org/licenses/>.

import asyncio
import logging

logger = logging.getLogger(__name__)


class Dispatcher:

    def __init__(self, available_actions):
        self.actions = available_actions
        self.__action_to_handlers = self.__build_handler_storage()

    def __build_handler_storage(self):
        logger.debug('Build storage of handlers for dispatcher.')
        return {action: [] for action in self.actions}

    def add_handler(self, callback, action):
        logger.debug('Add handler..')
        if not asyncio.iscoroutinefunction(callback):
            raise RuntimeError('Sync callback does not supported')

        try:
            handlers = self.__action_to_handlers[action]
            if callback in handlers:
                logger.debug('Handler already exists.')
                return callback

            handlers.append(callback)
        except KeyError:
            raise RuntimeError('Invalid action')

        logger.debug('Handler added.')
        return callback

    def remove_handler(self, callback, action) -> bool:
        logger.debug('Remove handler..')
        try:
            handlers = self.__action_to_handlers[action]
            for i in range(len(handlers)):
                if handlers[i] == callback:
                    del handlers[i]
                    return True
        except KeyError:
            raise RuntimeError('Invalid action')

        return False

    def remove_all(self):
        self.__action_to_handlers = self.__build_handler_storage()

    def get_handlers(self, action):
        try:
            logger.debug(f'Get handlers of {action}')
            return self.__action_to_handlers[action]
        except KeyError:
            raise RuntimeError('Invalid action')

    def trigger_handlers(self, action, instance, *args, **kwargs):
        logger.debug(f'Trigger handlers of {action}')

        for handler in self.get_handlers(action):
            asyncio.ensure_future(handler(instance, *args, **kwargs), loop=instance.client.loop)
