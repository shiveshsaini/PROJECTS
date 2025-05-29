import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key="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"
    )

# Step 1: Click on the icon at (604, 741)
pyautogui.click(555, 747)
time.sleep(1)  # short pause

# Step 2: Drag from (443, 116) to (1343, 652) to select the Chat_History
pyautogui.moveTo(543, 214)
pyautogui.dragTo(1126, 690, duration=1 , button = "left")  # smooth drag

# Step 3: Copy the selected Chat_History (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)  # wait for clipboard to update
pyautogui.click()


# Step 4: Get Chat_History from clipboard
Chat_History = pyperclip.paste()


print(Chat_History)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",      
    messages=[
        {"role": "system","content": "You are a person named Shivesh from India, bilingual in English and Hindi. "
    "You chat naturally and casually like Shivesh would in a WhatsApp conversation not like bot. "
    "Read the chat history carefully, and respond directly to the latest message or context, "
    "keeping your reply short, friendly, and informal.Shivesh does not use much of emoji so prefer not to use them much sometimes its okay ro express same emotion as text  "
    "Do not summarize the conversation or comment about the chat, just reply naturally as if you are chatting live.Reply in Hindi + English.You can also reply in sarcasm"}, 
        {"role":"user","content": Chat_History}
    ]
)

response = completion.choices[0].message.content
pyperclip.copy(response)

# Click at the specified position
pyautogui.click(1053, 693)
time.sleep(1)

# Paste from clipboard (Ctrl+V)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Press Enter
pyautogui.press('enter')


