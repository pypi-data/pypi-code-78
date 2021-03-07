from rlgym.communication import Message
from rlgym.communication import communication_exception_handler

import win32file
import win32pipe
from multiprocessing.pool import ThreadPool

class CommunicationHandler(object):
    RLGYM_GLOBAL_PIPE_ID = "RLGYM_GLOBAL_COMM_PIPE"
    RLGYM_GLOBAL_PIPE_NAME = r"\\.\pipe\RLGYM_GLOBAL_COMM_PIPE"
    RLGYM_DEFAULT_PIPE_SIZE = 4096

    def __init__(self):
        self._current_pipe_name = CommunicationHandler.RLGYM_GLOBAL_PIPE_NAME
        self._pipe = None
        self._connected = False

    def receive_message(self, header=None, num_attempts=100):
        #TODO: deal with discarded messages while waiting for a specific header
        if not self.is_connected():
            print("RLGYM ATTEMPTED TO RECEIVE MESSAGE WITH NO CONNECTION")
            return communication_exception_handler.BROKEN_PIPE_ERROR

        m = Message()
        received_message = Message()
        exception_code = None
        for i in range(num_attempts):
            try:
                code, msg_bytes = win32file.ReadFile(self._pipe, CommunicationHandler.RLGYM_DEFAULT_PIPE_SIZE)

            #This is the pywintypes.error object type.
            except BaseException as e:
                exception_code = communication_exception_handler.handle_exception(e)
                break

            msg_str = bytes.decode(msg_bytes)
            m.deserialize(msg_str)

            #Only deserialize valid messages.
            if header is None or header == m.header:
                received_message.deserialize(msg_str)
                # Peek the next message in the pipe to see if we've reached the end of new messages.
                data = win32pipe.PeekNamedPipe(self._pipe, CommunicationHandler.RLGYM_DEFAULT_PIPE_SIZE)
                if data[0] == b'':
                    break

        #TODO: make sure users of this object deal with the null message response
        return received_message, exception_code

    def send_message(self, message=None, header=None, body=None):
        if not self.is_connected():
            print("RLGYM ATTEMPTED TO SEND MESSAGE WITH NO CONNECTION")
            return communication_exception_handler.BROKEN_PIPE_ERROR

        if message is None:
            if header is None:
                header = Message.RLGYM_NULL_MESSAGE_HEADER

            if body is None:
                body = Message.RLGYM_NULL_MESSAGE_BODY

            message = Message(header=header, body=body)

        serialized = message.serialize()
        exception_code = None
        try:
            win32file.WriteFile(self._pipe, str.encode(serialized))

        except BaseException as e:
            exception_code = communication_exception_handler.handle_exception(e)

        return exception_code

    def open_pipe(self, pipe_name=None, num_allowed_instances=1):
        if pipe_name is None:
            pipe_name = CommunicationHandler.RLGYM_GLOBAL_PIPE_NAME

        if self.is_connected():
            self.close_pipe()

        self._connected = False

        pool = ThreadPool(processes=1)
        pool.apply_async(CommunicationHandler.handle_diemwin_potential, args=[self.is_connected])

        #win32pipe.PIPE_UNLIMITED_INSTANCES
        self._pipe = win32pipe.CreateNamedPipe(pipe_name,
                                               win32pipe.PIPE_ACCESS_DUPLEX | win32file.FILE_FLAG_OVERLAPPED,

                                               win32pipe.PIPE_TYPE_MESSAGE |
                                               win32pipe.PIPE_READMODE_MESSAGE |
                                               win32pipe.PIPE_WAIT,

                                               num_allowed_instances,

                                               CommunicationHandler.RLGYM_DEFAULT_PIPE_SIZE,
                                               CommunicationHandler.RLGYM_DEFAULT_PIPE_SIZE, 0, None)

        win32pipe.ConnectNamedPipe(self._pipe)

        self._current_pipe_name = pipe_name
        self._connected = True

        pool.terminate()
        pool.join()

    def close_pipe(self):
        self._connected = False
        win32file.CloseHandle(self._pipe)

    def is_connected(self):
        return self._connected

    @staticmethod
    def format_pipe_id(pipe_id):
        return r"\\.\pipe\{}".format(pipe_id)

    @staticmethod
    def handle_diemwin_potential(connected):
        import time
        import pywinauto

        # Windows Direct Input Emulator (DIEmWin) spawns a window sometimes, so we delete it here.
        while not connected():
            try:
                app = pywinauto.Application().connect(title='DIEmWin', visible_only=True)
                if app.is_process_running():
                    app.window(title='DIEmWin', visible_only=True).close()
                    print("DIEmWin detector successfully closed window")
                    return
            except:
                time.sleep(2)
