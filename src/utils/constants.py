from enum import Enum

class ResponseMessage:
    CHAT_END = "Chat ended successfully"

class Coversation(str, Enum):
    QUIT = "quit"

class Roles(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class AnswerType(str, Enum):
    TECHNICAL = "technical"
    TEXTUAL = "textual"

