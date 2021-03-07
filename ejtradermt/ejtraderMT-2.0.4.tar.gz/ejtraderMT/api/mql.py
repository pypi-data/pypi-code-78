import json
import zmq
import pandas as pd
from datetime import datetime, timedelta, date
import time
from pytz import timezone
from tzlocal import get_localzone
from queue import Queue
from ejtraderTH import start
from ejtraderDB import DictSQLite
from tqdm import tqdm
import os
class Functions:
    def __init__(self, host=None, debug=None):
        self.HOST = host or 'localhost'
        self.SYS_PORT = 15555       # REP/REQ port
        self.DATA_PORT = 15556      # PUSH/PULL port
        self.LIVE_PORT = 15557      # PUSH/PULL port
        self.EVENTS_PORT = 15558    # PUSH/PULL port
        self.INDICATOR_DATA_PORT = 15559  # REP/REQ port
        self.CHART_DATA_PORT = 15560  # PUSH 
        self.debug = debug or True

        # ZeroMQ timeout in seconds
        sys_timeout = 100
        data_timeout = 1000

        # initialise ZMQ context
        context = zmq.Context()

        # connect to server sockets
        try:
            self.sys_socket = context.socket(zmq.REQ)
            # set port timeout
            self.sys_socket.RCVTIMEO = sys_timeout * 1000
            self.sys_socket.connect(
                'tcp://{}:{}'.format(self.HOST, self.SYS_PORT))

            self.data_socket = context.socket(zmq.PULL)
            # set port timeout
            self.data_socket.RCVTIMEO = data_timeout * 1000
            self.data_socket.connect(
                'tcp://{}:{}'.format(self.HOST, self.DATA_PORT))

            self.indicator_data_socket = context.socket(zmq.PULL)
            # set port timeout
            self.indicator_data_socket.RCVTIMEO = data_timeout * 1000
            self.indicator_data_socket.connect(
                "tcp://{}:{}".format(self.HOST, self.INDICATOR_DATA_PORT)
            )
            self.chart_data_socket = context.socket(zmq.PUSH)
            # set port timeout
            # TODO check if port is listening and error handling
            self.chart_data_socket.connect(
                "tcp://{}:{}".format(self.HOST, self.CHART_DATA_PORT)
            )

        except zmq.ZMQError:
            raise zmq.ZMQBindError("Binding ports ERROR")

    def _send_request(self, data: dict) -> None:
        """Send request to server via ZeroMQ System socket"""
        try:
            self.sys_socket.send_json(data)
            msg = self.sys_socket.recv_string()
            # terminal received the request
            assert msg == 'OK', 'Something wrong on server side'
        except AssertionError as err:
            raise zmq.NotDone(err)
        except zmq.ZMQError:
            raise zmq.NotDone("Sending request ERROR")

    def _pull_reply(self):
        """Get reply from server via Data socket with timeout"""
        try:
            msg = self.data_socket.recv_json()
        except zmq.ZMQError:
            raise zmq.NotDone('Data socket timeout ERROR')
        return msg

    def _indicator_pull_reply(self):
        """Get reply from server via Data socket with timeout"""
        try:
            msg = self.indicator_data_socket.recv_json()
        except zmq.ZMQError:
            raise zmq.NotDone("Indicator Data socket timeout ERROR")
        if self.debug:
            print("ZMQ INDICATOR DATA REPLY: ", msg)
        return msg

    def live_socket(self, context=None):
        """Connect to socket in a ZMQ context"""
        try:
            context = context or zmq.Context.instance()
            socket = context.socket(zmq.PULL)
            socket.connect('tcp://{}:{}'.format(self.HOST, self.LIVE_PORT))
        except zmq.ZMQError:
            raise zmq.ZMQBindError("Live port connection ERROR")
        return socket

    def streaming_socket(self, context=None):
        """Connect to socket in a ZMQ context"""
        try:
            context = context or zmq.Context.instance()
            socket = context.socket(zmq.PULL)
            socket.connect('tcp://{}:{}'.format(self.HOST, self.EVENTS_PORT))
        except zmq.ZMQError:
            raise zmq.ZMQBindError("Data port connection ERROR")
        return socket

    def _push_chart_data(self, data: dict) -> None:
        """Send message for chart control to server via ZeroMQ chart data socket"""
        try:
            if self.debug:
                print("ZMQ PUSH CHART DATA: ", data, " -> ", data)
            self.chart_data_socket.send_json(data)
        except zmq.ZMQError:
            raise zmq.NotDone("Sending request ERROR")

    def Command(self, **kwargs) -> dict:
        """Construct a request dictionary from default and send it to server"""

        # default dictionary
        request = {
            "action": None,
            "actionType": None,
            "symbol": None,
            "chartTF": None,
            "fromDate": None,
            "toDate": None,
            "id": None,
            "magic": None,
            "volume": None,
            "price": None,
            "stoploss": None,
            "takeprofit": None,
            "expiration": None,
            "deviation": None,
            "comment": None,
            "chartId": None,
            "indicatorChartId": None,
            "chartIndicatorSubWindow": None,
            "style": None,
        }

        # update dict values if exist
        for key, value in kwargs.items():
            if key in request:
                request[key] = value
            else:
                raise KeyError('Unknown key in **kwargs ERROR')

        # send dict to server
        self._send_request(request)

        # return server reply
        return self._pull_reply()

    def indicator_construct_and_send(self, **kwargs) -> dict:
        """Construct a request dictionary from default and send it to server"""

        # default dictionary
        request = {
            "action": None,
            "actionType": None,
            "id": None,
            "symbol": None,
            "chartTF": None,
            "fromDate": None,
            "toDate": None,
            "name": None,
            "params": None,
            "linecount": None,
        }

        # update dict values if exist
        for key, value in kwargs.items():
            if key in request:
                request[key] = value
            else:
                raise KeyError("Unknown key in **kwargs ERROR")

        # send dict to server
        self._send_request(request)

        # return server reply
        return self._indicator_pull_reply()

    def chart_data_construct_and_send(self, **kwargs) -> dict:
        """Construct a request dictionary from default and send it to server"""

        # default dictionary
        message = {
            "action": None,
            "actionType": None,
            "chartId": None,
            "indicatorChartId": None,
            "data": None,
        }

        # update dict values if exist
        for key, value in kwargs.items():
            if key in message:
                message[key] = value
            else:
                raise KeyError("Unknown key in **kwargs ERROR")

        # send dict to server
        self._push_chart_data(message)


class Metatrader:

    def __init__(self, host=None, real_volume=None, localtime=True):
        self.api = Functions(host)
        self.real_volume = real_volume or False
        self.localtime = localtime 
        self.utc_timezone = timezone('UTC')
        self.my_timezone = get_localzone()
        self.utc_brocker_offset = self._utc_brocker_offset()
        self._priceQ = Queue()
        self._eventQ = Queue()
        self._historyQ = Queue()
       
    
       
        
       
    def balance(self):
        return self.api.Command(action="BALANCE")

    def accountInfo(self):
        return self.api.Command(action="ACCOUNT")

    def positions(self):
        return self.api.Command(action="POSITIONS")

    def orders(self):
        return self.api.Command(action="ORDERS")

    def trade(self, symbol, actionType, volume, stoploss, takeprofit, price, deviation):
        self.api.Command(
            action="TRADE",
            actionType=actionType,
            symbol=symbol,
            volume=volume,
            stoploss=stoploss,
            takeprofit=takeprofit,
            price=price,
            deviation=deviation
        )

    def buy(self, symbol, volume, stoploss, takeprofit, deviation=5):
        price = 0
        self.trade(symbol, "ORDER_TYPE_BUY", volume,
                   stoploss, takeprofit, price, deviation)

    def sell(self, symbol, volume, stoploss, takeprofit, deviation=5):
        price = 0
        self.trade(symbol, "ORDER_TYPE_SELL", volume,
                   stoploss, takeprofit, price, deviation)

    def buyLimit(self, symbol, volume, stoploss, takeprofit, price=0, deviation=5):
        self.trade(symbol, "ORDER_TYPE_BUY_LIMIT", volume,
                   stoploss, takeprofit, price, deviation)

    def sellLimit(self, symbol, volume, stoploss, takeprofit, price=0, deviation=5):
        self.trade(symbol, "ORDER_TYPE_SELL_LIMIT", volume,
                   stoploss, takeprofit, price, deviation)

    def buyStop(self, symbol, volume, stoploss, takeprofit, price=0, deviation=5):
        self.trade(symbol, "ORDER_TYPE_BUY_STOP", volume,
                   stoploss, takeprofit, price, deviation)

    def sellStop(self, symbol, volume, stoploss, takeprofit, price=0, deviation=5):
        self.trade(symbol, "ORDER_TYPE_SELL_LIMIT", volume,
                   stoploss, takeprofit, price, deviation)

    def cancel_all(self):
        orders = self.orders()

        if 'orders' in orders:
            for order in orders['orders']:
                self.CancelById(order['id'])

    def close_all(self):
        positions = self.positions()

        if 'positions' in positions:
            for position in positions['positions']:
                self.CloseById(position['id'])

    def positionModify(self, id, stoploss, takeprofit):
        self.api.Command(
            action="TRADE",
            actionType="POSITION_MODIFY",
            id=id,
            stoploss=stoploss,
            takeprofit=takeprofit
        )

    def ClosePartial(self, id, volume):
        self.api.Command(
            action="TRADE",
            actionType="POSITION_PARTIAL",
            id=id,
            volume=volume
        )

    def CloseById(self, id):
        self.api.Command(
            action="TRADE",
            actionType="POSITION_CLOSE_ID",
            id=id
        )

    def CloseBySymbol(self, symbol):
        self.api.Command(
            action="TRADE",
            actionType="POSITION_CLOSE_SYMBOL",
            symbol=symbol
        )

    def orderModify(self, id, stoploss, takeprofit, price):
        self.api.Command(
            action="TRADE",
            actionType="ORDER_MODIFY",
            id=id,
            stoploss=stoploss,
            takeprofit=takeprofit,
            price=price
        )

    def CancelById(self, id):
        self.api.Command(
            action="TRADE",
            actionType="ORDER_CANCEL",
            id=id
        )

    def _utc_brocker_offset(self):
        utc = datetime.now(self.utc_timezone).strftime('%Y-%m-%d %H:%M:%S')
        try:
            broker = self.accountInfo()
            broker = datetime.strptime(broker['time'], '%Y.%m.%d %H:%M:%S')
        except KeyError:
            raise "Metatrader 5 Server is disconnect"
        utc = datetime.strptime(utc, '%Y-%m-%d %H:%M:%S')

        duration = broker - utc
        duration_in_s = duration.total_seconds()
        hour = divmod(duration_in_s, 60)[0]
        seconds = int(hour)*60
        return seconds

    
    def _price(self):
        connect = self.api.live_socket()
        while True:
            price = connect.recv_json()
            try:
                price = price['data']
                price = pd.DataFrame([price]) 
                price = price.set_index([0])
                price.index.name = 'date'
                if self.allchartTF == 'TICK':
                    price.index = pd.to_datetime(price.index, unit='ms')
                    price.columns = ['bid', 'ask']
                    self._priceQ.put(price)
                else:
                    if self.real_volume:
                        del price[5]
                    else:
                        del price[6]
                    price.index = pd.to_datetime(price.index, unit='s')
                    price.columns = ['open', 'high', 'low','close', 'volume','spread']
                    
                    self._priceQ.put(price)
            except KeyError:
                  pass
            
           

    def _event(self):
        connect = self.api.streaming_socket()
        while True:
            event = connect.recv_json()
            try:
                event = event['request']
                event = pd.DataFrame(event, index=[0])
                self._eventQ.put(event)
            except KeyError:
                pass

    def price(self, symbol, chartTF):
        self.api.Command(action="RESET")
        self.allsymbol = symbol
        self.allchartTF = chartTF
        for active in symbol:
            self.api.Command(action="CONFIG",  symbol=active, chartTF=chartTF)  
        try:
            start(self._price, max_threads=20)
        except:
             print("Error: unable to start Price thread")
      
        return  self._priceQ.get()
       


    def event(self, symbol, chartTF):
        self.api.Command(action="RESET")
        self.allsymbol = symbol
        self.allchartTF = chartTF
        for active in symbol:
            self.api.Command(action="CONFIG",  symbol=active, chartTF=chartTF)          
       
        try:
            start(self._event,max_threads=20)
        except:
            print("Error: unable to start Event thread")
      
        return  self._eventQ.get()
        

    
      

    # convert datestamp to dia/mes/ano
    def date_to_timestamp(self, s):
        return time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple())
    # convert datestamp to dia/mes/ano
    def datetime_to_timestamp(self, s):
        return time.mktime(s.timetuple())

    def date_to_timestamp_broker(self):
        brokertime = time.mktime(datetime.strptime(self.accountInfo()['time'], '%Y.%m.%d %H:%M:%S').timetuple())
        return round(brokertime)

    def brokerTimeCalculation(self,s):
        delta = timedelta(seconds = s)
        broker = datetime.strptime(self.accountInfo()['time'], '%Y.%m.%d %H:%M:%S')
        result = broker - delta
        return result
  

    


    def timeframe_to_sec(self, timeframe):
        # Timeframe dictionary
        TIMECANDLE = {
            "M1": 60,
            "M2": 120,
            "M3": 180,
            "M4": 240,
            "M5": 300,
            "M15": 900,
            "M30": 1800,
            "H1": 3600,
            "H4": 14400,
            "D1": 86400,
            "W1": 604800,
            "MN": 2629746,

        }
        return TIMECANDLE[timeframe]

    def setlocaltime_dataframe(self, df):
        df.index = df.index.tz_localize(self.utc_brocker_offset)
        df.index = df.index.tz_convert(self.my_timezone)
        df.index = df.index.tz_localize(None)
        return df
   


    def history(self,symbol,chartTF=None,fromDate=None,toDate=None,database=None):
        self.chartTF = chartTF
        self.fromDate = fromDate
        self.toDate = toDate
        if isinstance(symbol, tuple):
            for symbols in symbol:
                self.symbol = symbols
        else:
            self.symbol = symbol
        if chartTF:
            if database:
                try:
                    start(self.historyThread_save,repeat=1, max_threads=2000)
                except:
                    print("Error: unable to start History thread")
            else:
                try:
                    start(self.historyThread, max_threads=20)
                except:
                    print("Error: unable to start History thread")
                return self._historyQ.get()
        else:
            q = DictSQLite('history')
            if isinstance(symbol, list):
                try:
                    df = q[f'{self.symbol[0]}']
                except KeyError:
                    df = f" {self.symbol[0]}  isn't on database"
                    pass 
            else:
                try:
                    df = q[f'{self.symbol}']
                except KeyError:
                    df = f" {self.symbol}  isn't on database"
                    pass
            return df
    
       


    def historyThread(self):
        actives = self.symbol
        chartTF = self.chartTF
        fromDate = self.fromDate
        toDate  = self.toDate
        main = pd.DataFrame()
        current = pd.DataFrame()
        if(chartTF == 'TICK'):
            chartConvert = 60
        else:
            chartConvert = self.timeframe_to_sec(chartTF)
        for active in actives:
            # the first symbol on list is the main and the rest will merge
            if active == actives[0]:
                # get data
                if fromDate and toDate:
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.date_to_timestamp(fromDate), toDate=self.date_to_timestamp(toDate))
                elif isinstance(fromDate, int):
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + fromDate * chartConvert - chartConvert) ))
                elif isinstance(fromDate, str) and toDate==None:
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.date_to_timestamp(fromDate),toDate=self.date_to_timestamp_broker())
                else:
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + 100 * chartConvert - chartConvert) ))
                self.api.Command(action="RESET")
                try:
                    main = pd.DataFrame(data['data'])
                    main = main.set_index([0])
                    main.index.name = 'date'
                    

                    # TICK DATA
                    if(chartTF == 'TICK'):
                        main.columns = ['bid', 'ask']
                        main.index = pd.to_datetime(main.index, unit='ms')
                    else:
                        main.index = pd.to_datetime(main.index, unit='s')
                        if self.real_volume:
                            del main[5]
                        else:
                            del main[6]
                        main.columns = ['open', 'high', 'low',
                                        'close', 'volume', 'spread']
                except KeyError:
                    pass
            else:
                 # get data
                if fromDate and toDate:
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.date_to_timestamp(fromDate), toDate=self.date_to_timestamp(toDate))
                elif isinstance(fromDate, int):
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + fromDate * chartConvert - chartConvert) ))
                elif isinstance(fromDate, str) and toDate==None:
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.date_to_timestamp(fromDate),toDate=self.date_to_timestamp_broker())
                else:
                    data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                        fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + 100 * chartConvert - chartConvert) ))

                self.api.Command(action="RESET")
                try:
                    current = pd.DataFrame(data['data'])
                    current = current.set_index([0])
                    current.index.name = 'date'
                    active = active.lower()
                    # TICK DATA
                    if(chartTF == 'TICK'):
                        current.index = pd.to_datetime(current.index, unit='ms')
                        current.columns = [f'{active}_bid', f'{active}_ask']
                    else:
                        current.index = pd.to_datetime(current.index, unit='s')
                        if self.real_volume:
                            del current[5]
                        else:
                            del current[6]
            
                        current.columns = [f'{active}_open', f'{active}_high',
                                        f'{active}_low', f'{active}_close', f'{active}_volume', f'{active}_spread']

                    main = pd.merge(main, current, how='inner',
                                    left_index=True, right_index=True)
                except KeyError:
                    pass
        try:
            if self.localtime:
                self.setlocaltime_dataframe(main)
        except AttributeError:
            pass
        main = main.loc[~main.index.duplicated(keep='first')]
        self._historyQ.put(main)

    def save_to_csv_first(self,df):
        df.to_csv(f'DataBase/{self.active_file}.csv', header=True)

    def save_to_csv_second(self,df):
        df.to_csv(f'DataBase/{self.active_file}.csv',  mode='a', header=False)
    

    def historyThread_save(self,data):
            actives = self.symbol
            chartTF = self.chartTF
            fromDate = self.fromDate
            toDate  = self.toDate
            main = pd.DataFrame()
            current = pd.DataFrame()
            header = True
            self.count = 0
            try:
                os.makedirs('DataBase')
            except OSError:
                pass
            # count data
            start_date = datetime.strptime(fromDate, "%d/%m/%Y")

            end_date = datetime.strptime(toDate, "%d/%m/%Y") or date.today() #date(2021, 1, 1)

            delta = timedelta(days=1)
            delta2 = timedelta(days=1)
            diff_days = start_date - end_date
            days_count = diff_days.days
            pbar = tqdm(total=abs(days_count))
            while start_date <= end_date:
                pbar.update(delta.days)
                fromDate = start_date.strftime("%d/%m/%Y")
                toDate = start_date
                toDate +=  delta2
                toDate = toDate.strftime("%d/%m/%Y")  

                if(chartTF == 'TICK'):
                    chartConvert = 60
                else:
                    chartConvert = self.timeframe_to_sec(chartTF)
                for active in actives:
                    self.count += 1 
                   
                    # the first symbol on list is the main and the rest will merge
                    if active == actives[0]:
                        self.active_file = active
                        # get data
                        if fromDate and toDate:
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.date_to_timestamp(fromDate), toDate=self.date_to_timestamp(toDate))
                        elif isinstance(fromDate, int):
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + fromDate * chartConvert - chartConvert) ))
                        elif isinstance(fromDate, str) and toDate==None:
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.date_to_timestamp(fromDate),toDate=self.date_to_timestamp_broker())
                        else:
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + 100 * chartConvert - chartConvert) ))
                        self.api.Command(action="RESET")
                        try:
                            main = pd.DataFrame(data['data'])
                            main = main.set_index([0])
                            main.index.name = 'date'
                            

                            # TICK DATA
                            if(chartTF == 'TICK'):
                                main.columns = ['bid', 'ask']
                                main.index = pd.to_datetime(main.index, unit='ms')
                            else:
                                main.index = pd.to_datetime(main.index, unit='s')
                                if self.real_volume:
                                    del main[5]
                                else:
                                    del main[6]
                                main.columns = ['open', 'high', 'low',
                                                'close', 'volume', 'spread']
                        except KeyError:
                            pass
                    else:
                        # get data
                        if fromDate and toDate:
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.date_to_timestamp(fromDate), toDate=self.date_to_timestamp(toDate))
                        elif isinstance(fromDate, int):
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + fromDate * chartConvert - chartConvert) ))
                        elif isinstance(fromDate, str) and toDate==None:
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.date_to_timestamp(fromDate),toDate=self.date_to_timestamp_broker())
                        else:
                            data = self.api.Command(action="HISTORY", actionType="DATA", symbol=active, chartTF=chartTF,
                                                fromDate=self.datetime_to_timestamp(self.brokerTimeCalculation((10800 + chartConvert) + 100 * chartConvert - chartConvert) ))

                        self.api.Command(action="RESET")
                        try:
                            current = pd.DataFrame(data['data'])
                            current = current.set_index([0])
                            current.index.name = 'date'
                            active = active.lower()
                            # TICK DATA
                            if(chartTF == 'TICK'):
                                current.index = pd.to_datetime(current.index, unit='ms')
                                current.columns = [f'{active}_bid', f'{active}_ask']
                            else:
                                current.index = pd.to_datetime(current.index, unit='s')
                                if self.real_volume:
                                    del current[5]
                                else:
                                    del current[6]
                    
                                current.columns = [f'{active}_open', f'{active}_high',
                                                f'{active}_low', f'{active}_close', f'{active}_volume', f'{active}_spread']

                            main = pd.merge(main, current, how='inner',
                                            left_index=True, right_index=True)
                        except KeyError:
                            pass
                try:
                    if self.localtime:
                        self.setlocaltime_dataframe(main)
                except AttributeError:
                    pass
                main = main.loc[~main.index.duplicated(keep='first')]
                if self.count == 1:
                    start(self.save_to_csv_first,data=[main],repeat=1, max_threads=20)
                else:
                    start(self.save_to_csv_second,data=[main],repeat=1, max_threads=20)
             
                start_date += delta
            pbar.close()
            start(self.save_to_db,repeat=1, max_threads=20)



    def save_to_db(self,data):
        q = DictSQLite('history')
        df = pd.read_csv(f'DataBase/{self.active_file}.csv', low_memory=False)
        q[f"{self.active_file}"] = df
        # Get directory name
        MODELFILE = f'DataBase/{self.active_file}.csv'
        try:
            os.remove(MODELFILE)
        except OSError:
            pass
            




    

    
   