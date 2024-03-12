# Test-1-Modbus

## 簡介

本專案為一個模擬 Modbus 通訊的測試程式，包含一個伺服器端程式 (server.py) 和一個客戶端程式 (client.py)。

## 執行方法

**環境需求**

* Python 3.8 或更高版本

**安裝套件**

* `socket`
* `struct`

您可以使用以下命令來安裝套件：
* `pip install -r requirements.txt`

**執行步驟**

1. 啟動伺服器端程式：
* `python server.py`

2. 啟動客戶端程式：
* `python client.py`

**注意事項**

* 請先啟動伺服器端程式，再啟動客戶端程式。

## 程式說明

### 伺服器端程式 (server.py)

伺服器端程式負責接收來自客戶端程式的 Modbus 資料，並進行統計和輸出。

### 客戶端程式 (client.py)

客戶端程式模擬一個檢測站，會定期向伺服器端程式傳送 Modbus 資料。
