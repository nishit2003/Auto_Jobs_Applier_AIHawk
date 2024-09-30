<<<<<<< HEAD
import os
import random
import time

from selenium import webdriver
=======
import logging
import os
import random
import sys
import time

from selenium import webdriver
from loguru import logger

from app_config import MINIMUM_LOG_LEVEL

log_file = "app_log.log"


if MINIMUM_LOG_LEVEL in ["DEBUG", "TRACE", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    logger.remove()
    logger.add(sys.stderr, level=MINIMUM_LOG_LEVEL)
else:
    logger.warning(f"Invalid log level: {MINIMUM_LOG_LEVEL}. Defaulting to DEBUG.")
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")
>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4

chromeProfilePath = os.path.join(os.getcwd(), "chrome_profile", "linkedin_profile")

def ensure_chrome_profile():
<<<<<<< HEAD
    profile_dir = os.path.dirname(chromeProfilePath)
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
    if not os.path.exists(chromeProfilePath):
        os.makedirs(chromeProfilePath)
    return chromeProfilePath

def is_scrollable(element):
    scroll_height = element.get_attribute("scrollHeight")
    client_height = element.get_attribute("clientHeight")
    return int(scroll_height) > int(client_height)

def scroll_slow(driver, scrollable_element, start=0, end=3600, step=100, reverse=False):
    if reverse:
        start, end = end, start
        step = -step
    if step == 0:
        raise ValueError("Step cannot be zero.")
    script_scroll_to = "arguments[0].scrollTop = arguments[1];"
    try:
        if scrollable_element.is_displayed():
            if not is_scrollable(scrollable_element):
                print("The element is not scrollable.")
                return
            if (step > 0 and start >= end) or (step < 0 and start <= end):
                print("No scrolling will occur due to incorrect start/end values.")
                return        
            for position in range(start, end, step):
                try:
                    driver.execute_script(script_scroll_to, scrollable_element, position)
                except Exception as e:
                    print(f"Error during scrolling: {e}")
                time.sleep(random.uniform(1.0, 2.6))
            driver.execute_script(script_scroll_to, scrollable_element, end)
            time.sleep(1)
        else:
            print("The element is not visible.")
    except Exception as e:
        print(f"Exception occurred: {e}")

def chromeBrowserOptions():
    ensure_chrome_profile()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Avvia il browser a schermo intero
    options.add_argument("--no-sandbox")  # Disabilita la sandboxing per migliorare le prestazioni
    options.add_argument("--disable-dev-shm-usage")  # Utilizza una directory temporanea per la memoria condivisa
    options.add_argument("--ignore-certificate-errors")  # Ignora gli errori dei certificati SSL
    options.add_argument("--disable-extensions")  # Disabilita le estensioni del browser
    options.add_argument("--disable-gpu")  # Disabilita l'accelerazione GPU
    options.add_argument("window-size=1200x800")  # Imposta la dimensione della finestra del browser
    options.add_argument("--disable-background-timer-throttling")  # Disabilita il throttling dei timer in background
    options.add_argument("--disable-backgrounding-occluded-windows")  # Disabilita la sospensione delle finestre occluse
    options.add_argument("--disable-translate")  # Disabilita il traduttore automatico
    options.add_argument("--disable-popup-blocking")  # Disabilita il blocco dei popup
    options.add_argument("--no-first-run")  # Disabilita la configurazione iniziale del browser
    options.add_argument("--no-default-browser-check")  # Disabilita il controllo del browser predefinito
    options.add_argument("--disable-logging")  # Disabilita il logging
    options.add_argument("--disable-autofill")  # Disabilita l'autocompletamento dei moduli
    options.add_argument("--disable-plugins")  # Disabilita i plugin del browser
    options.add_argument("--disable-animations")  # Disabilita le animazioni
    options.add_argument("--disable-cache")  # Disabilita la cache 
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])  # Esclude switch della modalità automatica e logging

    # Preferenze per contenuti
    prefs = {
        "profile.default_content_setting_values.images": 2,  # Disabilita il caricamento delle immagini
        "profile.managed_default_content_settings.stylesheets": 2,  # Disabilita il caricamento dei fogli di stile
=======
    logger.debug(f"Ensuring Chrome profile exists at path: {chromeProfilePath}")
    profile_dir = os.path.dirname(chromeProfilePath)
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
        logger.debug(f"Created directory for Chrome profile: {profile_dir}")
    if not os.path.exists(chromeProfilePath):
        os.makedirs(chromeProfilePath)
        logger.debug(f"Created Chrome profile directory: {chromeProfilePath}")
    return chromeProfilePath


def is_scrollable(element):
    scroll_height = element.get_attribute("scrollHeight")
    client_height = element.get_attribute("clientHeight")
    scrollable = int(scroll_height) > int(client_height)
    logger.debug(f"Element scrollable check: scrollHeight={scroll_height}, clientHeight={client_height}, scrollable={scrollable}")
    return scrollable


def scroll_slow(driver, scrollable_element, start=0, end=3600, step=300, reverse=False):
    logger.debug(f"Starting slow scroll: start={start}, end={end}, step={step}, reverse={reverse}")

    if reverse:
        start, end = end, start
        step = -step

    if step == 0:
        logger.error("Step value cannot be zero.")
        raise ValueError("Step cannot be zero.")

    max_scroll_height = int(scrollable_element.get_attribute("scrollHeight"))
    current_scroll_position = int(float(scrollable_element.get_attribute("scrollTop")))
    logger.debug(f"Max scroll height of the element: {max_scroll_height}")
    logger.debug(f"Current scroll position: {current_scroll_position}")

    if reverse:
        if current_scroll_position < start:
            start = current_scroll_position
        logger.debug(f"Adjusted start position for upward scroll: {start}")
    else:
        if end > max_scroll_height:
            logger.warning(f"End value exceeds the scroll height. Adjusting end to {max_scroll_height}")
            end = max_scroll_height

    script_scroll_to = "arguments[0].scrollTop = arguments[1];"

    try:
        if scrollable_element.is_displayed():
            if not is_scrollable(scrollable_element):
                logger.warning("The element is not scrollable.")
                return

            if (step > 0 and start >= end) or (step < 0 and start <= end):
                logger.warning("No scrolling will occur due to incorrect start/end values.")
                return

            position = start
            previous_position = None  # Tracking the previous position to avoid duplicate scrolls
            while (step > 0 and position < end) or (step < 0 and position > end):
                if position == previous_position:
                    # Avoid re-scrolling to the same position
                    logger.debug(f"Stopping scroll as position hasn't changed: {position}")
                    break

                try:
                    driver.execute_script(script_scroll_to, scrollable_element, position)
                    logger.debug(f"Scrolled to position: {position}")
                except Exception as e:
                    logger.error(f"Error during scrolling: {e}")

                previous_position = position
                position += step

                # Decrease the step but ensure it doesn't reverse direction
                step = max(10, abs(step) - 10) * (-1 if reverse else 1)

                time.sleep(random.uniform(0.6, 1.5))

            # Ensure the final scroll position is correct
            driver.execute_script(script_scroll_to, scrollable_element, end)
            logger.debug(f"Scrolled to final position: {end}")
            time.sleep(0.5)
        else:
            logger.warning("The element is not visible.")
    except Exception as e:
        logger.error(f"Exception occurred during scrolling: {e}")


def chrome_browser_options():
    logger.debug("Setting Chrome browser options")
    ensure_chrome_profile()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1200x800")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-autofill")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-cache")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

    prefs = {
        "profile.default_content_setting_values.images": 2,
        "profile.managed_default_content_settings.stylesheets": 2,
>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4
    }
    options.add_experimental_option("prefs", prefs)

    if len(chromeProfilePath) > 0:
<<<<<<< HEAD
        initialPath = os.path.dirname(chromeProfilePath)
        profileDir = os.path.basename(chromeProfilePath)
        options.add_argument('--user-data-dir=' + initialPath)
        options.add_argument("--profile-directory=" + profileDir)
    else:
        options.add_argument("--incognito")
=======
        initial_path = os.path.dirname(chromeProfilePath)
        profile_dir = os.path.basename(chromeProfilePath)
        options.add_argument('--user-data-dir=' + initial_path)
        options.add_argument("--profile-directory=" + profile_dir)
        logger.debug(f"Using Chrome profile directory: {chromeProfilePath}")
    else:
        options.add_argument("--incognito")
        logger.debug("Using Chrome in incognito mode")
>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4

    return options


def printred(text):
<<<<<<< HEAD
    # Codice colore ANSI per il rosso
    RED = "\033[91m"
    RESET = "\033[0m"
    # Stampa il testo in rosso
    print(f"{RED}{text}{RESET}")

def printyellow(text):
    # Codice colore ANSI per il giallo
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    # Stampa il testo in giallo
    print(f"{YELLOW}{text}{RESET}")
=======
    red = "\033[91m"
    reset = "\033[0m"
    logger.debug("Printing text in red: %s", text)
    print(f"{red}{text}{reset}")


def printyellow(text):
    yellow = "\033[93m"
    reset = "\033[0m"
    logger.debug("Printing text in yellow: %s", text)
    print(f"{yellow}{text}{reset}")

def stringWidth(text, font, font_size):
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]
>>>>>>> e1d1ea8534f538bd20053e26f4f379adeef0eca4
