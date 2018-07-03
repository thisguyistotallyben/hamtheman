

frommorse = {

}

class Morse:
    def __init__(self):
        self.tomorse = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            ' ': ' / '  # this is for spaces
        }

    def translate_text(self, message):
        morsemess = ''
        for i in message:
            if i in self.tomorse:
                morsemess += self.tomorse[i]
                morsemess += ' '
            else:
                morsemess += '<?>'

        return morsemess

if __name__ == '__main__':
    m = Morse()
    print(m.translate_text('words are kool'))
