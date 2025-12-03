from groq import Groq
import os
import json
from src.core.config import settings
from src.utils.mixin import CSVMixin, JsonMixin
from src.utils.prompts import Prompt
from src.utils.constants import ResponseMessage, Coversation, Roles, AnswerType

client = Groq()

sessions = {}

async def generate_insight(input):
    try:
        if input.query.lower() == "quit":
            if input.session_id in sessions:
                del sessions[input.session_id]
            return {"message": ResponseMessage.CHAT_END}

        if input.session_id not in sessions:
            file = os.path.join(os.getcwd(),"src","data",settings.FILE)
            data = CSVMixin.load(file)

            if input.answer_type:
                if input.answer_type == AnswerType.TECHNICAL:
                    system_prompt = Prompt.TECHNICAL_SYSTEM_PROMPT.format(CSV_DATA=data)
                    ai_model = settings.TECHNICAL_MODEL
                else:
                    system_prompt = Prompt.TEXTUAL_SYSTEM_PROMPT.format(CSV_DATA=data)
                    ai_model = settings.TEXTUAL_MODEL
            else:
                system_prompt = Prompt.DEFAULT_SYSTEM_PROMPT.format(CSV_DATA=data)
                ai_model = settings.TECHNICAL_MODEL

            sessions[input.session_id] = {
                    "messages": [{"role": Roles.SYSTEM, "content": system_prompt}],
                    "model": ai_model }

        else:
            ai_model = sessions[input.session_id]["model"]

        user_input = {"role": Roles.USER, "content": f"Question: {input.query}"}
        sessions[input.session_id]["messages"].append(user_input)

        response = client.chat.completions.create(
            messages=sessions[input.session_id]["messages"],
            model=ai_model,
            temperature=0
        )

        assistant_response = response.choices[0].message.content
        assistant_input = {"role": Roles.ASSISTANT, "content": assistant_response}
        sessions[input.session_id]["messages"].append(assistant_input)
        
        result_json = json.loads(assistant_response)
        return result_json
    
    except FileNotFoundError as e:
           raise FileNotFoundError(f"{e}: JSON file not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"{e}: Invalid JSON format in the file.")
    except Exception as e:
        raise Exception(e)
        