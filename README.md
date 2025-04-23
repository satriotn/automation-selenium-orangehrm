# 🧪 Automation Testing: OrangeHRM

This repository contains automation test scripts for the OrangeHRM web application using **Selenium** and **Python (unittest)** framework.

---

## 📹 Automation Testing Video

🔗 [Watch the automation process here](https://www.loom.com/share/f874bfe2d83d4e39abcf596ed1798265?sid=364ec42d-74ef-4c0e-b25f-ad9fb8026f34)  
*(Hosted on Loom)*

---

## 🛠 Tools Used

- **Python 3.10+**
- **Selenium**
- **unittest**
- **ChromeDriver**
- **Git & GitHub**

---

## 📂 Project Structure
```bash
automation-selenium-orangehrm/
│
├── README.md                
├── requirements.txt         
├── test/                    
│   ├── test_pim.py      
│   ├── test_login.py      
│   ├── test_login_negative.py    
│   └── test_pim_negative.py 
│
├── pages/                  
│   ├── login_page.py
│   ├── navbar_page.py         
│   └── pim_page.py         
│
├── locators/                
│   ├── login_locator.py
│   ├── navbar_locator.py  
│   └── pim_locator.py     
│
├── utils/                   
│   ├── driver_setup.py      
```

## ✅ Test Case Coverage

| Test Case ID | Description                        |
|--------------|-------------------------------------|
| TC001        | Login with valid credentials       |
| TC002        | Login with invalid credentials     |
| TC003        | Add New Employee                    |
| TC004        | Add New Employee (existing ID)        |

## 🚀 How to Run the Tests

1. Clone this repository:
```bash
git clone https://github.com/satriotn/automation-selenium-orangehrm.git
cd automation-selenium-orangehrm
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run test:
```bash
python test/test_pim.py
```

## 📝 How This Was Built

1. Identified test scenarios for the OrangeHRM PIM module.

2. Built test cases using the Page Object Model (POM).

3. Used Selenium WebDriver for browser automation and interaction.

4. Used unittest to organize and assert test results.

5. Tested both positive and negative flows:

- Adding a valid employee

- Login with incorrect credentials

## 🙌 Credits

**Developed by:** Satrio Tri Nugroho  
**Project:** Technical Test QA Automation Project - Superfood
