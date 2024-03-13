# Test-1-Modbus

## 簡介

本專案為一個模擬 Modbus 通訊的測試程式，一個客戶端程式 (client.py)和借助由ICDT開發的模擬伺服端程式進行模擬。

## 執行方法

**環境需求**

* Python 3.8 或更高版本

* 安裝 MODBUS TCP Server 模擬程式 [ModbusTcpServerSetupV2005.zip](https://github.com/PenguinTWCoding/Test-1-Modbus/blob/main/ICDT%20Modbus%20TCP%20Server%20Setting.png?raw=true)

**安裝套件**

* `socket`
* `struct`
* `pymodbus`

您可以使用以下命令來安裝套件：
* `pip install -r requirements.txt`

**執行步驟**

1. 啟動 ICDT Modbus TCP Server 程式並按照下圖進行設定：
![image](https://github.com/PenguinTWCoding/Test-1-Modbus/blob/main/ICDT%20Modbus%20TCP%20Server%20Setting.png?raw=true)

2. 啟動客戶端程式：
* `python client.py`

**注意事項**

* 請先啟動伺服器端程式，再啟動客戶端程式。

## 程式說明

### 客戶端程式 (client.py)

客戶端程式模擬一個檢測站，會定期向伺服器端詢問 Modbus 資料並進行統計並輸出至畫面上。

## 待處理問題

目前專案面臨以下問題：

- **伺服端回應速度不穩定：** 目前伺服端回應速度大於1秒，無法穩定地達到1秒一次更新。目前使用比對上次實際詢問時間計算延遲。