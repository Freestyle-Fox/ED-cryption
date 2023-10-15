def encrypter(string, special_chars_dict):
    encripted_msg = ''
    print(encripted_msg)
    for i in string:
        encripted_msg += special_chars_dict[i]
    return encripted_msg


def encrypter001(string):
    encryption001 = {}
    for char in range(32, 127):  # ASCII codes for printable characters (space to tilde)
        current_char = chr(char)
        # Circular mapping for printable characters
        next_char = chr((char - 32 + 1) % 94 + 32)
        encryption001[current_char] = next_char
    return encrypter(string, encryption001)


def encrypter002(string):
    
    encryption002 = {
    ' ': 'Q^9', '!': '@c1', '"': 'Pz!', '#': '*k6', '$': '$o)', '%': 'Lq2', '&': 'Hx+', "'": 'Jm5', '(': 'N!w', ')': 'Ry3', '*': 'Ku@', '+': 'Vn1', ',': 'Gt$', '-': 'Iv7', '.': 'Aa%', '/': 'Bb*', '0': 'Xf4', '1': 'Yp6', '2': 'Ws)', '3': 'Uz#', '4': 'Dc8', '5': 'Ml0', '6': 'Zj(', '7': 'Sd7', '8': 'Fo3', '9': 'Tr%', ':': 'Hg*', ';': 'Eq@', '<': 'Ny1', '=': 'Pu)', '>': 'Ov5', '?': 'It$', '@': 'Lm7', 'A': 'Wk#', 'B': 'Rx2', 'C': 'Vs%', 'D': 'Gz!', 'E': 'Fn8', 'F': 'Ub*', 'G': 'Qa1', 'H': 'Hp!', 'I': 'Jo9', 'J': 'Yl2', 'K': 'Ts#', 'L': 'Zv(', 'M': 'Rd3', 'N': 'Uy)', 'O': 'Dc6', 'P': 'Bq@', 'Q': 'Xw1', 'R': 'Am)', 'S': 'Go4', 'T': 'Nt#', 'U': 'Js(', 'V': 'Fz8', 'W': 'Ly%', 'X': 'Kb*', 'Y': 'Mh@', 'Z': 'Er5', '[': 'Iu2', '\\': 'Hp6', ']': 'Dx#', '^': 'Pv(', '_': 'Wn9', '`': 'Gs$', 'a': 'Ol2', 'b': 'Xr!', 'c': 'Qu3', 'd': 'Ht@', 'e': 'Bw6', 'f': 'Yz%', 'g': 'Mx*', 'h': 'Np)', 'i': 'Fd8', 'j': 'Sk!', 'k': 'Rb9', 'l': 'Vo$', 'm': 'Pu1', 'n': 'Zc2', 'o': 'It%', 'p': 'Aa*', 'q': 'Gs6', 'r': 'Hd(', 's': 'Ty3', 't': 'Wv@', 'u': 'Lq5', 'v': 'Mj!', 'w': 'Uo9', 'x': 'Fn#', 'y': 'Qg(', 'z': 'Pz8', '{': 'Ky*', '|': 'Er1', '}': 'Bs!', '~': 'Jw7'}
    return encrypter(string, encryption002)

def encrypter003(string):
    encryption003 = {
    ' ': '2Pz', '!': '9@c', '"': '1Bz', '#': '6*k', '$': '5$o', '%': '4Lq', '&': '8Hx', "'": '3Jm', '(': '7Nw', ')': '0Ry', '*': '@Ku', '+': '1Vn', ',': '$Gt', '-': '7Iv', '.': '%Aa', '/': '*Bb', '0': '4Xf', '1': '6Yp', '2': ')Ws', '3': '#Uz', '4': '8Dc', '5': '0Ml', '6': '2Zj', '7': '7Sd', '8': '3Fo', '9': '%Tr', ':': '*Hg', ';': '@Eq', '<': '1Ny', '=': ')Pu', '>': '5Ov', '?': '$It', '@': '7Lm', 'A': '#Wk', 'B': '2Rx', 'C': '%Vs', 'D': '!Gz', 'E': '8Fn', 'F': '*Ub', 'G': '1Qa', 'H': '!Hp', 'I': '9Jo', 'J': '2Yl', 'K': '#Ts', 'L': '(Zv', 'M': '3Rd', 'N': ')Uy', 'O': '6Dc', 'P': '@Bq', 'Q': '1Xw', 'R': ')Am', 'S': '4Go', 'T': '#Nt', 'U': '(Js', 'V': '8Fz', 'W': '%Ly', 'X': '*Kb', 'Y': '@Mh', 'Z': '5Er', '[': '2Iu', '\\': '6Hp', ']': '#Dx', '^': '(Pv', '_': '9Wn', '`': '$Gs', 'a': '2Ol', 'b': '!Xr', 'c': '3Qu', 'd': '@Ht', 'e': '6Bw', 'f': '%Yz', 'g': '*Mx', 'h': ')Np', 'i': '8Fd', 'j': '!Sk', 'k': '9Rb', 'l': '$Vo', 'm': '1Pu', 'n': '2Zc', 'o': '%It', 'p': '*Aa', 'q': '6Gs', 'r': '(Hd', 's': '3Ty', 't': '@Wv', 'u': '5Lq', 'v': '!Mj', 'w': '9Uo', 'x': '#Fn', 'y': '(Qg', 'z': '8Pz', '{': '*Ky', '|': '1Er', '}': '!Bs', '~': '7Jw' }
    return encrypter(string, encryption003)

def encrypter004(string):
    encryption004 = {
    ' ': '1Az', '!': '2Bx', '"': '3Cq', '#': '4Dw', '$': '5Ev', '%': '6Fu', '&': '7Gt', "'": '8Hs', '(': '9Ir', ')': '0Jp', '*': 'aKo', '+': 'bLn', ',': 'cMm', '-': 'dNl', '.': 'eOk', '/': 'fPi', '0': 'gQh', '1': 'hRg', '2': 'iSf', '3': 'jTt', '4': 'kUe', '5': 'lVd', '6': 'mWc', '7': 'nXb', '8': 'oYa', '9': 'pZz', ':': 'q[{', ';': 'r\\|', '<': 's]}', '=': 't^~', '>': 'u_@', '?': 'v`#', '@': 'w$a', 'A': 'x%b', 'B': 'y&c', 'C': 'z(d', 'D': '(e)', 'E': '*f!', 'F': '+g@', 'G': ',h#', 'H': '-i$', 'I': '.j%', 'J': '/k^', 'K': '0l&', 'L': '1m*', 'M': '2n(', 'N': '3o)', 'O': '4p_', 'P': '5q@', 'Q': '6r#', 'R': '7s$', 'S': '8t%', 'T': '9u^', 'U': '0v&', 'V': '1w*', 'W': '2x(', 'X': '3y)', 'Y': '4z_', 'Z': '5{!', '[': '6|@', '\\': '7}#', ']': '8~$', '^': '9a%', '_': '0b^', '`': '1c&', 'a': '2d*', 'b': '3e(', 'c': '4f)', 'd': '5g_', 'e': '6h!', 'f': '7i@', 'g': '8j#', 'h': '9k$', 'i': '0l%', 'j': '1m^', 'k': '2n&', 'l': '3o*', 'm': '4p(', 'n': '5q)', 'o': '6r_', 'p': '7s!', 'q': '8t@', 'r': '9u#', 's': '0v$', 't': '1w%', 'u': '2x^', 'v': '3y&', 'w': '4z*', 'x': '5{(', 'y': '6|)', 'z': '7}_', '{': '8~!', '|': '9^@', '}': '0_#', '~': '1`$'}
    return encrypter(string, encryption004)

