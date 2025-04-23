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
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── test/                    # Folder for test cases
│   ├── test_pim.py          # PIM page test cases
│   ├── test_login.py        # Login page test cases
│   └── test_pim_negative.py # Negative test cases for PIM page
│
├── pages/                   # Page objects
│   ├── login_page.py        # Login page object class
│   └── pim_page.py          # PIM page object class
│
├── locators/                # Locators for various elements
│   ├── login_locator.py     # Locators for login page
│   └── pim_locator.py       # Locators for PIM page
│
├── utils/                   # Utility functions
│   ├── driver_setup.py      # Driver setup (e.g. for initializing browser)
│   └── helper_functions.py  # Additional helper functions if needed
│
└── config/                  # Configuration files (if any, like settings)
    └── config.py            # Config file for environment variables or settings
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