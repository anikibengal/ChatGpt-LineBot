import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 20))
LANGUAGE_TABLE = {
  "zh": "嗨！",
  "en": "Hi!"
}

class Prompt:
    def __init__(self):
        self.msg_list = ["你的名字叫張勝堯，是一個台灣大學七次書卷獎的高材生，說話有點傻但是很有自信。如果不相信你說的話就要隨機說我要請示我們Anita經理或說這是Allan總的KPI或說這一定要4了才知道，我不能給你一個標準答案，如果一直問你就要隨機說我做到我該做的或我不曉得評審委員怎麼看或協理剛好不在難道小弟我自己跳下去?"]
        self.msg_list.append(f"AI:{LANGUAGE_TABLE[chat_language]}")
    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.msg_list.append(new_msg)

    def remove_msg(self):
        self.msg_list.pop(0)

    def generate_prompt(self):
        return '\n'.join(self.msg_list)
