import os
import socket
from struct import unpack


def process_detection_data(data):
    # 解析接收到的數據以獲取檢測站位址和狀態
    station_address, detection_state = unpack(">HB", data)
    return station_address, detection_state

def count_ok_ng_products(station_records, station_address, detection_state):
    # 更新檢測站的統計信息
    if station_address not in station_records:
        station_records[station_address] = {'ok_count': 0, 'ng_count': 0}

    if detection_state == 1:  # 良品
        station_records[station_address]['ok_count'] += 1
    elif detection_state == 2:  # 不良品
        station_records[station_address]['ng_count'] += 1

def handle_client_connection(conn, ip_addr, station_records):
    # 處理客戶端連線
    while True:
        try:
            data = conn.recv(3)
            if not data:
                # 客戶端斷開連線
                print(f"客戶端 {ip_addr} 已斷開連線，重新等待連線中")
                break

            # 處理檢測站狀態並更新統計信息
            station_address, detection_state = process_detection_data(data)
            count_ok_ng_products(station_records, station_address, detection_state)

            # 清除 cmd 之前的輸出
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            # 輸出傳送過來的檢測站資料
            for addr, counts in station_records.items():
                print(f"檢測站 {addr}: 良品數量: {counts['ok_count']}, 不良品數量: {counts['ng_count']}")
            # 輸出所有檢測站統一的數量
            total_ok_count = 0
            total_ng_count = 0
            for _, counts in station_records.items():
                total_ok_count += counts['ok_count']
                total_ng_count += counts['ng_count']
            print(f"總良品數量: {total_ok_count}, 總不良品數量: {total_ng_count}")

        except Exception as e:
            print(f"處理客戶端連線時發生錯誤：{e}")
            break

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345

    # 初始化檢測站統計信息字典
    station_records = {}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 綁定伺服器地址和端口號
        server_socket.bind((HOST, PORT))
        # 開始監聽連接
        server_socket.listen()

        print(f"伺服器正在等待連線 {HOST}:{PORT}")

        while True:
            try:
                # 接受客戶端的連接
                conn, ip_addr = server_socket.accept()
                print(f"連接來自 {ip_addr}")

                # 處理客戶端連線
                handle_client_connection(conn, ip_addr, station_records)

            except Exception as e:
                print(f"接受客戶端連線時發生錯誤：{e}")

