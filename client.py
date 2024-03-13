import os
import time
from datetime import datetime
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusSocketFramer

def count_ok_ng_products(statistics_station, address_station, detection_state):
    # 更新檢測站的統計信息
    if detection_state == 1:  # 良品
        address_station['ok_count'] += 1
        statistics_station['ok_count'] += 1
    elif detection_state == 2:  # 不良品
        address_station['ng_count'] += 1
        statistics_station['ng_count'] += 1

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 502

    address_station_mapping = {
        'statistics': {'description': "總數量統計", 'ok_count': 0, 'ng_count': 0},
        40001: {'description': "檢測站 1", 'ok_count': 0, 'ng_count': 0},
        40003: {'description': "檢測站 2", 'ok_count': 0, 'ng_count': 0},
        40005: {'description': "檢測站 3", 'ok_count': 0, 'ng_count': 0},
        40007: {'description': "檢測站 4", 'ok_count': 0, 'ng_count': 0},
        40009: {'description': "檢測站 5", 'ok_count': 0, 'ng_count': 0},
        40011: {'description': "檢測站 6", 'ok_count': 0, 'ng_count': 0}
    }

    last_request_time = time.time()  # 初始化上次詢問時間

    while True:
        try:
            # 計算間隔時間並延遲
            current_time = time.time()
            if current_time - last_request_time < 1:  # 確保每次詢問之間至少相隔1秒
                time.sleep(1 - (current_time - last_request_time))
            last_request_time = time.time()  # 更新上次詢問時間

            # 建立連線
            with ModbusTcpClient(host=HOST, port=PORT, framer=ModbusSocketFramer) as client:
                # 使用 read_holding_registers 從地址 40001 開始讀取數值
                result = client.read_holding_registers(address=0, count=11, unit=1)

                if result.isError():
                    print("讀取錯誤")
                else:
                    data = result.registers[0:11]

                    # 清除 cmd 之前的輸出
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')

                    for addr, detection_state in enumerate(data):
                        statistics_station = address_station_mapping['statistics']
                        address_station = address_station_mapping.get(40001 + addr)
                        if address_station:
                            count_ok_ng_products(statistics_station, address_station, detection_state)
                            print(f"檢測站 {address_station['description']}: 當前狀態: {detection_state}, 良品數量: {address_station['ok_count']}, 不良品數量: {address_station['ng_count']}")
                    print(f"總良品數量: {address_station_mapping['statistics']['ok_count']}, 總不良品數量: {address_station_mapping['statistics']['ng_count']}")
                    print(f"最後刷新時間: {datetime.now()}")
            # time.sleep(1)  # 每1秒執行一次詢問

        except Exception as e:
            print(f"{datetime.now()} - 發生錯誤: {e}")
            time.sleep(1)  # 等待1秒後重新嘗試連線
