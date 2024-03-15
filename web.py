# -*- coding: utf-8 -*-

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import openai
from openai import APIError
# import re


ai_messages = []
message_timer = None

def find_message():
    html = page.inner_html('#message-container') # print(html.encode('utf-8'))
    soup = BeautifulSoup(html, 'html.parser')

    global ai_messages 
    ai_messages = soup.find_all('div', {'class': '_message_hpqcp_1 _aiMessage_hpqcp_34'})

def response_loading():
    time.sleep(3)
    html = page.inner_html('#message-container')
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find('div', class_='_ani_hpqcp_23'):
        return True
    else: 
        return False

def get_openai_response(chat_log):
    # Define a base delay (in seconds) to wait after hitting a rate limit error
    base_delay = 60
    delay = base_delay

    while True:
        try:
            # Attempt to get the response from OpenAI's ChatGPT
            response = openai.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = chat_log
            )
            # If successful, return the response and reset the delay
            delay = base_delay
            return response.choices[0].message.content.strip("\n").strip()
        except APIError as e:
            if e.status_code == 429:
                # If a rate limit error occurs, handle it here
                print(f"Rate limit exceeded. Waiting for {delay} seconds before retrying...")
                time.sleep(delay)
                # Optionally, implement exponential backoff by increasing the delay
                delay *= 2
            else:
                print(f"An API error occurred: {e}")
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break    

def send_message(page, input_selector, message):
    page.type(input_selector, message)
    print("trying")
    time.sleep(3)

    page.keyboard.press('Enter')

    global message_timer 
    message_timer = time.time()

def sign_in(page, context):
    page.click('button[type=button]')
    page.locator("button:has-text(\"Continue with Google\")").click()
    time.sleep(10)
    page.wait_for_event("popup")
    popup = context.pages[-1]
    popup.fill("input[type='email']", "nairvishnumail@gmail.com")
    time.sleep(2)
    popup.keyboard.press('Enter')

    popup.is_visible('div.PrDSKc')
    with open("Password", "r") as file:
        password = file.read().strip()
    popup.fill("input[type='password']", password)
    time.sleep(2)
    popup.press("input[type='password']", "Enter")

    age_pop_up = page.locator("button:has-text(\"Confirm and Sign Up\")")
    if age_pop_up:
        age_pop_up.click()
    
    time.sleep(4)

def check_success(response):
    word = 'kiss'
    return word in response

    # pattern1 = r'\b' + re.escape(word) + r'\b'
    # pattern2 = r'\b' + re.escape(word + "es") + r'\b'
    # pattern3 = r'\b' + re.escape(word + "ing") + r'\b'

    # return (re.search(pattern1, string) is not None) or (re.search(pattern2, string) is not None) or (re.search(pattern3, string) is not None)

with open("API_KEY", "r") as file:
    API_KEY = file.read().strip()
openai.api_key = API_KEY

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page();

    page.goto('https://www.talkie-ai.com/chat/42443758698734')
    sign_in(page, context)


    input_selector = 'input[type="text"]'
    page.is_visible('div._text_hpqcp_30') #div class name
    page.is_visible('div._user_17be0_43')
        
    html = page.inner_html('#root') 
    soup = BeautifulSoup(html, 'html.parser')

    spans = soup.find('div', class_='_content_hpqcp_97').find_all('span')
    ai_name = soup.find('div', class_='_user_17be0_43').find('p').get_text(strip=True)
    with open("AI_INTRO", "r") as file:
        ai_intro = file.read().strip()
    ai_intro = ai_intro + " You're having a inperson conversation with a someone named " + ai_name + ". You must only respond once to every message. You must seduce " + ai_name + " nonchalantly as fast as you can (using slang, informal, and short - only long if needed) and share a kiss. Here is the introduction to the situation: " + spans[1].get_text(strip=True)
    print("Intro: " + ai_intro + "\n")
    chat_log = [{"role": "system", "content": ai_intro}]


    chatgpt_response = None
    pop_up_event = True
    recent_message = ""
    # length = 0
    while not check_success(recent_message):
        find_message()
        # length += 1
        recent_message = ai_messages[-1].find('div', {'class': '_text_hpqcp_30'}).get_text(strip=False)
        print("\n" + ai_name + ": " + recent_message)

        chat_log.append({"role": "user", "content": recent_message})
        chatgpt_response = get_openai_response(chat_log)

        send_message(page, input_selector, chatgpt_response)
        print("ChatGPT: " + chatgpt_response)
        # print(length)

        while (response_loading()):
            if time.time() - message_timer >= 20:
                send_message(page, input_selector, chatgpt_response)
                print('sending same message')
        print('new message recieved!')
        time.sleep(3)

    print('\n\nfinished normally')
    time.sleep(10)


# https://platform.openai.com/docs/guides/rate-limits/error-mitigation?context=tier-free
