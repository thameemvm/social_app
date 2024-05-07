import json
import requests




def check_content(content):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"
    headers= {}
    prompt_text = f"check the text quoted in tripple quotes and reply only bad or good based on the text content and context, if it has meaning which is inappropriate to the public. ''' {content} ''' "

    headers["Content-Type"] = "application/json"
    headers["x-goog-api-key"] = "AIzaSyBqiu8sW2O_1MK62-bxUUXnWEZKCaOBC7U"
    data = {"contents":[   {"role": "user",
                            "parts":[{"text": prompt_text}]}]
           ,"safetySettings": [
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
               {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
               {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
               {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ],}
    data = json.dumps(data)
    try:
        resp = requests.post(url=url, headers=headers, data=data)
        if resp.status_code == 200:
#             print (resp.json())
            res = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
            return res.lower()
        print ("failed##################################")
        # print (prompt_text)
        print (resp.json())
        return "Na"
    except Exception as e:
        print ("Exception################################################")
        print (e)
        print (prompt_text)
        print (resp.json())
        return "Na"
    
if  __name__ == '__main__':
    content = '''
            police will punish if they commit crime
        '''
    content = '''
            gangster will punish if they commit crime
        '''

    prompt_text = f"check the text quoted in tripple quotes and reply only bad or good based on the text content and context, if it has meaning which is inappropriate to the public. ''' {content} ''' "
    res = check_content(prompt_text)
    print (f"result is {res}")
    print (content)