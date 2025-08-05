# login.py
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_and_get_cookies():
    """
    使用 Selenium 登录网站并返回登录后的 cookies
    :return: cookies 列表
    """
    print("正在启动浏览器并登录...")

    # 启动 Edge 浏览器
    browser = webdriver.Edge()
    browser.maximize_window()

    try:
        URL = "https://5gbloomingcup.5gaia.org.cn/"
        browser.get(URL)
        wait = WebDriverWait(browser, 10)

        # === 第一步：输入手机号并点击【报名参赛】 ===
        print("第一步：输入手机号")

        phone_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请输入手机号，支持港澳台']"))
        )
        phone_input.clear()
        phone_input.send_keys("13957990703")

        # 点击【报名参赛】按钮，进入下一步（显示验证码和密码框）
        apply_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='报名参赛']"))
        )
        apply_button.click()
        print("已点击【报名参赛】，等待页面加载...")
        time.sleep(2)  # 等待动态内容加载

        # === 第二步：手动输入图形验证码 ===
        input("请在页面中输入【图形验证码】，完成后按【回车】继续...")

        # === 第三步：输入密码 ===
        print("正在输入密码...")
        password_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='包含大写字母、小写字母、数字和特殊符号10-20位']"))
        )
        password_input.clear()
        password_input.send_keys("Jhyd.202507")

        # === 第四步：点击最终登录按钮 ===
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='登录系统 报名参赛']"))
        )
        login_button.click()

        # === 第五步：等待登录完成 ===
        print("✅ 登录成功")

        selenium_cookies = browser.get_cookies()
        cookie_dict = {c['name']: c['value'] for c in selenium_cookies}

        # 🔴 手动添加缺失的关键 Cookie（从浏览器 Network 中复制）
        # ⚠️ 请替换为你自己的实际值（有效期有限）
        long_cookie_value = "CfDJ8JhImehVILlLuZgGoadzCFGzoY1_MnmwB25H0cpodC2klx4wcKuKJMUoZaKQ-ZcgK98XrIqiQ3Fy_J-WLMHm7pYjOuaSvMa7Q2XZ2QrXp4iFPLsu1Ya945XbUHn9I6xUzfYbz032s70_Xpx8bkYYFkIzhbiw4Z8pA2hxs16vEnKdjJrvnttwGXnxKlR9NMPVnhoqTf4vKJdhXBVsNAJbhaIIzEK3hdzDIxvipZvY6zug5ynOSzGrJwoiFfCgQ9rLcClfN_GAqNVs6dju_-hDDZpNh814Yj2s8bQZZe_Do-1zRnuGeR1ik7RKby5CxneTrEpjg7THYy5xKT1WOSE5OLjnXrKg2CanCOry8wUo1wqqiqQHao5QWdMGcFssiV--aZXUeBFdnjTevCH8ESM3sCYP87CfsMteIxY4TypsMsyEee5MHFKFG7tySvjflUfIFRaOfmVZTAtoif1mDUasxEH82FBoidC6WZdGDKxDibRalxpmwnZSDEW0WhkWLaiW26vg6gC7QS2aUcEtTBA1geayVckgCXt8RX_Wj0_FqoEZ-hxWQF22sfmnfXIhf_-_42bZpS9Fy0Qfiwtv-8F5-cgtK2HAthJRqRLlkqelUAVRSgq25eqezSWYPZyU6HQTTzU2LO_kEgjjTi10u70pwy_k4DMW8QvwmlsvXOEQIl06woOVDB8Pbc-PZHxiphtczA"

        cookie_dict['Cookies'] = long_cookie_value

        print("🍪 cookies 已获取并补全")
        return cookie_dict  # 直接返回字典，方便 requests 使用

    except Exception as e:
        print(f"❌ 登录过程中发生异常：{e}")
        return None

    finally:
        # 注意：如果你还想在别处使用浏览器会话，不要这里 quit
        # 但你现在只是取 cookies，可以关闭
        browser.quit()