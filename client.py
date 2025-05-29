from openai import OpenAI


client = OpenAI(
    api_key="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"
    )
command = '''
[9:20 pm, 29/05/2025] Jyoti: hello
[9:20 pm, 29/05/2025] Jyoti: kaisi h?
[9:20 pm, 29/05/2025] Shivesh: Mast
[9:20 pm, 29/05/2025] Shivesh: Tu bta ?
[9:21 pm, 29/05/2025] Jyoti: main bhi badiya
[9:21 pm, 29/05/2025] Jyoti: aur bta kya chal rha aaj kl      
[9:21 pm, 29/05/2025] Shivesh: Bas kuch nhi
[9:21 pm, 29/05/2025] Shivesh: Bas vacation ke MZZE le rhi hun
[9:21 pm, 29/05/2025] Shivesh: Aur sath main bas hhw kri hun  
[9:21 pm, 29/05/2025] Jyoti: ohh
[9:22 pm, 29/05/2025] Jyoti: mera toh college start hone wala h
[9:22 pm, 29/05/2025] Shivesh: Aree
[9:22 pm, 29/05/2025] Shivesh: Wow
[9:22 pm, 29/05/2025] Shivesh: Konsa
[9:22 pm, 29/05/2025] Shivesh: ??
[9:22 pm, 29/05/2025] Jyoti: newton school of tech
[9:22 pm, 29/05/2025] Shivesh: Ohhh okk
[9:22 pm, 29/05/2025] Shivesh: Badiya
'''

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",      
    messages=[
        {"role": "system","content": "You are person named Shivesh who speaks english as well as hindi , he is from india and is a coder. you analyze chathistory and talk like  and respond like Shivesh"}, 
        {"role":"user","content": command}
    ]
)

print(completion.choices[0].message.content)

