import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
     
    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", 
                         params={"q": name}
        )
        body = r.json()
        
        return body
    
    def check_status_code(self):
        r = requests.get("https://api.github.com/emojis")
        response = r
        return response
    

    def check_empty_list_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.text
        return body
    
    def search_emoji(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json
        return body