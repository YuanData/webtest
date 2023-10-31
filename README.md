# Web 測試專案

這是一個使用 **Page Object Model (POM)** 方法的 web 測試專案。專案目錄結構如下：

```
webtest/
│
├── conftest.py
├── config_manager.py
├── README.md
│
├── drivers/
│   └── chromedriver
├── setting/
│   └── config.ini
├── data/
│   └── daten.py
│
├── locators/
│   └── register_loc.py
├── pages/
│   └── register_page.py
│
└── test/
    └── test_register.py
```

## Page Object Model (POM)

在這個專案中，我們選擇使用 **Page Object Model** 作為我們的測試設計模式。POM 的主要目的是為了抽象化測試和業務邏輯之間的界面，將 web 頁面的每個頁面視為一個物件，並在該物件中封裝該頁面的行為。

### Locators

我們將所有的定位器（例如：Xpath、CSS selectors、element IDs 等）獨立放置在 `locators` 資料夾中。這樣的組織方式有以下好處：

1. **維護容易**：當 web 頁面的某些元素更改時，我們只需修改 `locators` 資料夾下的相應檔案，而不必修改測試邏輯。
2. **提高可讀性**：把測試邏輯與定位器分開可以使測試腳本更簡潔、有組織，提高整體的可讀性。
3. **重用性**：如果有多個測試需要相同的定位器，我們只需定義一次即可。

## 初始設定

在執行測試前，請確保進行以下初始設定：

### 下載 chromedriver

1. 根據您的作業系統和安裝的Chrome版本，前往 [ChromeDriver官方網站](https://sites.google.com/a/chromium.org/chromedriver/) 下載相對應版本的ChromeDriver。
2. 下載完成後，請將 `chromedriver` 放入 `drivers` 目錄下。確保其路徑為：`drivers/chromedriver`。

### 設定config

1. 將 `setting/config.ini.example` 重新命名為 `setting/config.ini`。
2. 打開 `setting/config.ini`，找到網址示例的部分，替換成您想要測試的真實網址。

## 執行測試

如果您想要執行測試，可以使用以下的指令：

```bash
pytest test/test_register.py
```
目前有以下三個測試用例：
1. **成功註冊**: 確認當使用有效的註冊資料時，可以成功註冊。
2. **無效的Email註冊**: 測試當用戶輸入的Email格式不正確時的情況。
3. **確認密碼不匹配**: 測試當輸入的密碼和確認密碼不一致時的情況。

這三個測試用例只是範例。還有其他測試用例，例如：密碼太短、註冊資料有缺、Email已經被註冊過等等，這些都需要進一步的補充。

## 測試用例詳細說明

### 成功註冊

- **描述**: 確認使用有效的註冊資料可以成功註冊，且系統會跳出相對應的提示訊息。
- **預期結果**: 
  1. 會看到提示 "請至Email信箱 收驗證信! 謝謝！"。
  2. 用戶會被導向登入頁面。

### 無效的Email註冊

- **描述**: 確認當輸入不合法的Email格式時，系統會跳出錯誤提示。
- **預期結果**: 系統會顯示 "不符合email格式" 的錯誤提示。

### 確認密碼不匹配

- **描述**: 測試當用戶輸入的密碼和確認密碼不一致時，系統會跳出錯誤提示。
- **預期結果**: 系統會顯示 "密碼與確認密碼不符" 的錯誤提示。

## 待補充測試用例

1. **密碼太短**: 測試密碼小於指定的字符數時的情況。
2. **註冊資料有缺**: 測試當註冊資料不完整，例如: 必填欄位沒填寫時的情況。
3. **Email已註冊過**: 測試使用已被註冊過的Email來註冊時的情況。

## 進一步建議

為了使測試更完整，我們可能還需要考慮以下測試用例：

1. **特殊字符的密碼**: 測試當用戶使用特殊字符作為密碼時的情況。
2. **Email格式驗證**: 測試不同的無效Email格式，如: "test@@example.com"。
3. **忘記密碼功能**: 測試忘記密碼功能是否正常運作。
4. **驗證登入功能**: 測試登入功能是否正常運作。
