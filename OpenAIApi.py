from openai import OpenAI

class OpenAIAPI:
    def __init__(self):
        API_KEY = open("G:\Learning\Python\Workspace\ScrumAnswers\API_KEY", "r").read()
        global client
        client = OpenAI(api_key=API_KEY)
        #openai.api_key = API_KEY
            
    def getApiResp(self, req: str) -> str:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[{"role": "system", "content": "You are a helpful Scrum assistant designed to output JSON."},
                      {"role": "user", "content": req}
                      ]
            )
        return response.choices[0].message.content
        #return "we have response"
    