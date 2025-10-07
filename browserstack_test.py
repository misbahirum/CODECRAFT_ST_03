from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ====== Replace these with your BrowserStack credentials ======
USERNAME = "misbahirum_S04xLo"
ACCESS_KEY = "sFL7jLMk7oqY8qK8jkzU"
# =============================================================

# Define browser configurations
browsers = [
    {
        "os": "Windows",
        "osVersion": "11",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "sessionName": "Chrome Test",
    },
    {
        "os": "Windows",
        "osVersion": "10",
        "browserName": "Firefox",
        "browserVersion": "latest",
        "sessionName": "Firefox Test",
    },
    {
        "os": "OS X",
        "osVersion": "Monterey",
        "browserName": "Safari",
        "browserVersion": "latest",
        "sessionName": "Safari Test",
    },
    {
        "os": "Windows",
        "osVersion": "10",
        "browserName": "Edge",
        "browserVersion": "latest",
        "sessionName": "Edge Test",
    },
]

for config in browsers:
    print(f"🚀 Starting test on {config['browserName']}...")

    # Create an Options object
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", config["browserName"])
    options.set_capability("browserVersion", config["browserVersion"])
    options.set_capability("bstack:options", {
        "os": config["os"],
        "osVersion": config["osVersion"],
        "sessionName": config["sessionName"],
        "userName": USERNAME,
        "accessKey": ACCESS_KEY,
    })

    # Connect to BrowserStack
    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(3)
        current_url = driver.current_url

        if "inventory" in current_url:
            print(f"✅ Login Test Passed on {config['browserName']}")
        else:
            print(f"⚠️ Login Test Failed on {config['browserName']}")

    except Exception as e:
        print(f"❌ Error on {config['browserName']}: {e}")

    finally:
        driver.quit()
