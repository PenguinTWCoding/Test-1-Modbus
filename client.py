import time
import socket
import random

def simulate_detection_machine(client_socket, station_address):
    # 模擬檢測站狀態的變化
    detection_state = random.randint(0, 2)

    # 將模擬的狀態和檢測站位址發送到伺服器
    data = station_address.to_bytes(2, 'big') + detection_state.to_bytes(1, 'big')
    client_socket.send(data)

    time.sleep(0.05)

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345

    # 為每個檢測站設定 Modbus 位址
    STATION_ADDRESSES = [40001, 40003, 40005, 40007, 40009, 40011]

    # 創建6個 client 並模擬各自的檢測機
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sockets:
        client_sockets.connect((HOST, PORT))

        while True:
            for station_address in STATION_ADDRESSES:
                simulate_detection_machine(client_sockets, station_address)
            time.sleep(1)
