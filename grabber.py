import requests, hashlib, string, random, uuid, time, calendar, re, json
from sys import platform

class colors:

    ENDC     = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'

def escape(string):
    if platform == "win32" or platform == "win64" or platform == "windows":
        return string.replace('/', '\\')
    else: return string
    
def printc(value, color='', nonewline=None, more=''):

    end = '\n'
    if nonewline: end = ''

    if color: print(color + value + colors.ENDC + more, end=end)
    else: print(value + more, end=end)

def inputc(value, color='', more=''):

    if color: return input(color + value + colors.ENDC + more)
    else: return input(value + more) 

def RandomString(n = 10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringChars(n = 10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result

def printn(args): print(args, end='')
def ClearConsole(): printn("\033[H\033[2J")
def DeleteLine(): printn("\033[F"); print("\033[K")

class account:

    def __init__(self, username: str, password: str, version: str):
        self.fheaders = self.fetch_headers()
        self.username = username
        self.password = password
        self.cookies = dict()
        self.csrftoken = self.fheaders['csrftoken']
        self.mid = self.fheaders['mid']
        self.UserAgent = self.randDevice().replace('(VERSION)', version)
        self.DeviceID = self.generate_device_id(self.hex_digest(username, password))
        self.guid1 = str(uuid.uuid4())
        self.guid2 = str(uuid.uuid4())
        self.guid3 = str(uuid.uuid4())
        self.checkpoint = bool()
        self.loggedIn = bool()
        self.ds_user_id = str()
        self.maxID = str()

        headers = {}
        headers['User-Agent'] = self.UserAgent
        headers['Host'] = 'i.instagram.com'
        headers['x-ig-app-locale'] = 'en_SA'
        headers['x-ig-device-locale'] = 'en_SA' 
        headers['x-ig-mapped-locale'] = 'en_US'
        headers['x-pigeon-session-id'] = '29739560-730e-41dc-a065-eae576baba2c'
        headers['x-pigeon-rawclienttime'] = '1599515404.254'
        headers['x-ig-connection-speed'] = '643kbps'
        headers['x-ig-bandwidth-speed-kbps'] = '1236.889'
        headers['x-ig-bandwidth-totalbytes-b'] = '6672937'
        headers['x-ig-bandwidth-totaltime-ms'] = '7015'
        headers['x-ig-app-startup-country'] = 'SA'
        headers['x-bloks-version-id'] = '85e371bf185c688d008ad58d18c84943f3e6d568c4eecd561eb4b0677b1e4c55'
        headers['x-ig-www-claim'] = '0'
        headers['x-bloks-is-layout-rtl'] = 'false'
        headers['x-ig-device-id'] = 'f4aa25e2-1663-4545-afa4-9b770ae5476d'
        headers['x-ig-android-id'] = self.DeviceID
        headers['x-ig-connection-type'] = 'WIFI'
        headers['x-ig-capabilities'] = '3brTvw8='
        headers['x-ig-app-id'] = '567067343352427'
        headers['accept-language'] = 'en-SA, en-US'
        headers['x-mid'] = self.mid
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8' 
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        self.headers = headers
        self.login()

    def fetch_headers(self) -> dict:
        url = 'https://i.instagram.com/api/v1/si/fetch_headers/'

        headers = {}
        headers['Host'] = 'i.instagram.com'
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:80.0) Gecko/20100101 Firefox/80.0'
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        headers['Accept-Language'] = 'ar,en-US;q=0.7,en;q=0.3'
        headers['Accept-Encoding'] = 'gzip, deflate, br'
        headers['Connection'] = 'close'

        return requests.get(url, headers=headers).cookies.get_dict()

    def hex_digest(self, *args):
        m = hashlib.md5()
        m.update(b''.join([arg.encode('utf-8') for arg in args]))
        return m.hexdigest()

    def generate_device_id(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def randDevice(self) -> str:

        dpi = [
        '480', '320', '640', '515', '120', '160', '240', '800'
        ]
        manufacturer = [
            'HUAWEI', 'Xiaomi', 'samsung', 'OnePlus', 'LGE/lge', 'ZTE', 'HTC',
            'LENOVO', 'MOTOROLA', 'NOKIA', 'OPPO', 'SONY', 'VIVO', 'LAVA'
        ]
        
        randResolution = random.randrange(2, 9) * 180
        lowerResolution = randResolution - 180

        DEVICE = {
            'android_version': random.randrange(18, 25),
            'android_release': f'{random.randrange(1, 7)}.{random.randrange(0, 7)}',
            'dpi': f'{random.choice(dpi)}dpi',
            'resolution': f'{lowerResolution}x{randResolution}',
            'manufacturer': random.choice(manufacturer),
            'device': f'{random.choice(manufacturer)}-{RandomStringUpper(5)}',
            'model': f'{randomStringWithChar(4)}',
            'cpu': f'{RandomStringChars(2)}{random.randrange(1000, 9999)}'
        }

        if random.randrange(0, 2):
            DEVICE['android_release'] = f'{random.randrange(1, 7)}.{random.randrange(0, 7)}.{random.randrange(1, 7)}'

        USER_AGENT_BASE = (
            'Instagram (VERSION) '
            'Android ({android_version}/{android_release}; '
            '{dpi}; {resolution}; {manufacturer}; '
            '{device}; {model}; {cpu}; en_US)'
        )

        return USER_AGENT_BASE.format(**DEVICE)

    def sendCode(self, url, security_code):
        postData = {}
        guid = str(uuid.uuid4())

        postData['security_code'] = security_code
        postData['guid'] = self.guid1
        postData['_csrftoken'] = self.cookies['csrftoken']
        postData['device_id'] = self.DeviceID
        
        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(postData)}'

        response = requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)
        return response

    def sendMethod(self, url, choice):
        postData = {}
        guid = str(uuid.uuid4())

        postData['choice'] = choice # (Phone number = 0, email = 1)
        postData['guid'] = self.guid1
        postData['_csrftoken'] = self.cookies['csrftoken']
        postData['device_id'] = self.DeviceID

        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(postData)}'

        return requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)

    def login(self):

        TimeStamp = calendar.timegm(time.gmtime())

        data = {}
        data['jazoest'] = '22713'
        data['phone_id'] = self.guid1
        data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{TimeStamp}:{self.password}'
        data['_csrftoken'] = self.csrftoken
        data['username'] = self.username
        data['adid'] = self.guid2
        data['guid'] = self.guid3
        data['device_id'] = self.DeviceID
        data['google_tokens'] = '[]'
        data['login_attempt_count'] = '0'

        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(data)}'

        response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=self.headers, cookies=self.fheaders, data=payload, verify=True)
        if 'logged_in_user' in response.text:
            self.loggedIn = True
            self.cookies = response.cookies.get_dict()
            self.csrftoken = self.cookies['csrftoken']
            self.ds_user_id = self.cookies['ds_user_id']
            printc('Logged In Successfully', colors.GREEN2)
        elif 'challenge_required' in response.text:
            self.checkpoint = True
            self.cookies = response.cookies.get_dict()

            checkpoint_path = re.findall(r'"api_path": "(.*?)"', response.text)[0]
            challenge_url = f'https://i.instagram.com/api/v1{checkpoint_path}'

            getMethods = requests.get(challenge_url, headers=self.headers, cookies=self.cookies)

            phone = bool()
            email = bool()

            step_name = getMethods.json()['step_name'] 
            if step_name == "select_verify_method":
                if "phone_number" in getMethods.text:
                    phone = True
                if "email" in getMethods.text:
                    email = True
            elif step_name == "delta_login_review":
                choice = 0
            else:
                print(f'Strange step_name: {step_name}\n Send me this {insta}')
                choice = 0

            printc('Challenge is required', colors.RED)
            if email:
                printc('1', colors.YELLOW, more=') email')
            if phone:
                printc('0', colors.YELLOW, more=') phone number')
            choice = inputc('Choose a method to unlock your account: ', colors.YELLOW)
            
            res = self.sendMethod(challenge_url, choice)
            sendto = res.json()['step_data']['contact_point']
            print(f'A code has been sent to {sendto}')
            
            code = inputc('Enter code: ', colors.YELLOW)
            response = self.sendCode(challenge_url, code)
            if 'logged_in_user' in response.text:
                self.loggedIn = True
                self.cookies = response.cookies.get_dict()
                self.csrftoken = self.cookies['csrftoken']
                self.ds_user_id = self.cookies['ds_user_id']
                printc('Logged In Successfully', colors.GREEN2)
            else: printc('Login failure, try again', colors.GREEN2); exit()

        elif 'Incorrect Username' in response.text:
            printc("The username you entered doesn't appear to belong to an account.", colors.RED)
            exit()
        elif 'active user' in response.text:
            printc('Your account has been disabled.', colors.RED)
            exit()
        elif 'Incorrect password' in response.text:
            printc("The password you entered is incorrect.", colors.RED)
            exit()
        else:
            printc(f'Unknown error: {response.text}', colors.RED)
            exit()

    def getID(self, us):
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0"
        headers["Host"] = "www.instagram.com"
        headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        headers["Accept-Language"] = "ar,en-US;q=0.7,en;q=0.3"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Connection"] = "keep-alive"

        res = requests.get(f'https://www.instagram.com/{us}/?__a=1', headers=headers, cookies=self.cookies)
        return res.json()['graphql']['user']['id'] 

    def getFollowers(self, userID) -> list:
        url = f'https://i.instagram.com/api/v1/friendships/{userID}/followers/?search_surface=follow_list_page&order=default&query=&enable_groups=true&rank_token=missing'
        if self.maxID:
            url += f'&max_id={self.maxID}'

        response = requests.get(url, headers=self.headers, cookies=self.cookies, verify=True)
        res = response.json()
        
        users = []
        
        for i in res['users']:
            users.append(i['username'])

        if res['next_max_id']:
            self.maxID = res['next_max_id']
        else: self.maxID = str()

        return users

ClearConsole()
print()

username = inputc('Username: ', colors.YELLOW)
password = inputc('Password: ', colors.YELLOW)
t = int(inputc('sleep (milliseconds, best: 500): ', colors.YELLOW))
path = escape(inputc('path: (like: /users/ali/Desktop/list.txt): ', colors.YELLOW))
f = open(path, 'a')

version = '155.0.0.37.107'

print()
account = account(username, password, version)

target = inputc('target: ', colors.YELLOW)
print()
ID = account.getID(target)

count = 0
while True:
    users = account.getFollowers(ID)
    for user in users:
        f.write(f'{user}\n')
    count += len(users)
    DeleteLine()
    printc(f'Grabbed: {count}', color=colors.BLUE2, nonewline=True)
    if not account.maxID: break
    time.sleep(t / 1000)

print()
printc('Done saved to: ', color=colors.GREEN, more=path)
