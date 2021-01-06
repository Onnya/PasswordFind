from xkcdpass import xkcd_password as xp

import rsa


def check_pswrd(pswrd):
    if len(pswrd) < 8:
        return "Your password is too short"
    if len(pswrd) > 32:
        return "Your password is too long"
    if pswrd == "".join([e for e in pswrd if e.isalnum()]):
        return "There are no special characters in the password"
    if pswrd == pswrd.upper():
        return "Password does not contain lowercase letters"
    if pswrd == pswrd.lower():
        return "Password does not contain uppercase letters"
    return True


def gen_pswrd():
    word_file = xp.locate_wordfile()
    my_words = xp.generate_wordlist(wordfile=word_file, min_length=5, max_length=7)
    return xp.generate_xkcdpassword(my_words, numwords=4, delimiter="-", case='random')


def encrypt_pswrd(password, pubkey):
    crypto = rsa.encrypt(bytes(password, encoding="utf-8"), pubkey)
    return crypto


def decrypt_pswrd(crypto, prkey):
    password = rsa.decrypt(crypto, prkey)
    return password.decode("utf-8")


def make_key():
    (pub, pr) = rsa.newkeys(512)
    pem_pub = pub.save_pkcs1('PEM')
    pem_pr = pr.save_pkcs1('PEM')
    with open('public.pem', 'wb') as key_file:
        key_file.write(pem_pub)
    with open('private.pem', 'wb') as key_file:
        key_file.write(pem_pr)


def take_pr_key():
    with open('private.pem', 'rb') as key_file:
        return rsa.PrivateKey.load_pkcs1(key_file.read(), 'PEM')


def take_pub_key():
    with open('public.pem', 'rb') as key_file:
        return rsa.PublicKey.load_pkcs1(key_file.read(), 'PEM')
