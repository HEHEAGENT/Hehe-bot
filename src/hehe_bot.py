import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def hehe_chat(message, personality="hehe-basic"):
    try:
        with open(f"personalities/{personality}.txt", "r", encoding="utf-8") as f:
            prompt = f.read()
    except FileNotFoundError:
  

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ],
        temperature=1.2
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("hehe～来送吗？输入 exit 退出")
    while True:
        msg = input("你: ")
        if msg.lower() == "exit": break
        print("hehe:", hehe_chat(msg))
