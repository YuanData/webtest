# 測試註冊功能
這份文件說明註冊功能測試，請參考以下詳細資訊。

## 1. 初始設定

在執行測試前，請確保進行以下初始設定：

### 1.1. 下載 chromedriver

1. 根據您的作業系統和安裝的Chrome版本，前往 [ChromeDriver官方網站](https://sites.google.com/a/chromium.org/chromedriver/) 下載相對應版本的ChromeDriver。
2. 下載完成後，請將 `chromedriver` 放入 `drivers` 目錄下。確保其路徑為：`drivers/chromedriver`。

### 1.2. 設定檔案

1. 將 `setting/config.ini.example` 重新命名為 `setting/config.ini`。
2. 打開 `setting/config.ini`，找到網址示例的部分，替換成您想要測試的真實網址。

## 2. 測試案例概述

目前有以下三個測試用例：
1. **成功註冊**: 確認當使用有效的註冊資料時，可以成功註冊。
2. **無效的Email註冊**: 測試當用戶輸入的Email格式不正確時的情況。
3. **確認密碼不匹配**: 測試當輸入的密碼和確認密碼不一致時的情況。

這三個測試用例只是範例。還有其他測試用例，例如：密碼太短、註冊資料有缺、Email已經被註冊過等等，這些都需要進一步的補充。

## 3. 測試用例詳細說明

### 3.1. 成功註冊

- **描述**: 確認使用有效的註冊資料可以成功註冊，且系統會跳出相對應的提示訊息。
- **預期結果**: 
  1. 會看到提示 "請至Email信箱 收驗證信! 謝謝！"。
  2. 用戶會被導向登入頁面。

### 3.2. 無效的Email註冊

- **描述**: 確認當輸入不合法的Email格式時，系統會跳出錯誤提示。
- **預期結果**: 系統會顯示 "不符合email格式" 的錯誤提示。

### 3.3. 確認密碼不匹配

- **描述**: 測試當用戶輸入的密碼和確認密碼不一致時，系統會跳出錯誤提示。
- **預期結果**: 系統會顯示 "密碼與確認密碼不符" 的錯誤提示。

## 4. 待補充測試用例

1. **密碼太短**: 測試密碼小於指定的字符數時的情況。
2. **註冊資料有缺**: 測試當註冊資料不完整，例如: 必填欄位沒填寫時的情況。
3. **Email已註冊過**: 測試使用已被註冊過的Email來註冊時的情況。

## 5. 進一步建議

為了使測試更完整，我們可能還需要考慮以下測試用例：

1. **特殊字符的密碼**: 測試當用戶使用特殊字符作為密碼時的情況。
2. **Email格式驗證**: 測試不同的無效Email格式，如: "test@@example.com"。
3. **忘記密碼功能**: 測試忘記密碼功能是否正常運作。
4. **驗證登入功能**: 測試登入功能是否正常運作。