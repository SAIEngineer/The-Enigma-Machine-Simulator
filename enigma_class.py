from string import ascii_uppercase

class Enigma:

    # NAPRAW Reflector

    # CZY mogę przyjąć założenie, że użytkownik nie przygotuje sam pliki z błędnymi ustawieniami?
    # WHEN YOU IMPORT SETTINGS TO ENIGMA, PROGRAM ASSUMES THAT YOU WANT TO READ CIPHERED TEXT,
    # so there's no need to save this settings again to external file, because you already have
    # settings file for that encryption

    def __init__(self, alpha = 1, beta = 1, gama = 1, steckerbrett = {}, reflector = 'A'):
        '''
        Class Enigma. Contains attributes:

        :param alpha: initial alpha setting of the rotor
        :type alphat: int
        :default alpha: 1

        :param beta: initial beta setting of the rotor
        :type beta: int
        :default beta: 1

        :param gama: initial gama setting of the rotor
        :type gama: int
        :default gama: 1

        :param steckerbrett: Steckerbrett shows which letters should replace each other
        :type steckerbrett: dict
        :default steckerbrett: {}

        :param reflector: initial reflector setting of the rotor
        :type reflector: str
        :default reflector: 'A'
        '''

        '''
        ascii_uppercase is a string holding "abcdefgh..."
        Atribute is holding list consisting of ascii_uppercase values
        '''
        self._alphabet = [letter for letter in ascii_uppercase]
        self._alpha = int(alpha)
        self._beta = int(beta)
        self._gama = int(gama)
        self._steckerbrett = steckerbrett
        self._reflector = reflector
        # initiate reflector attribute
        self._reflector_alphabet = self.initaite_reflector()

    '''
    SET: alpha, beta, gama, steckerbrett, reflector
    chyba nie są potrzebne, skoro nigdzie w programie
    się do nich nie odwołuje
    '''
    def alpha(self):
        return self._alpha

    def beta(self):
        return self._beta

    def gama(self):
        return self._gama

    def steckerbrett(self):
        return self._steckerbrett

    def reflector(self):
        return self._reflector

    def initial_settings(self):
        '''
        This method saves initial settings of the machine, before values (like each rotor)
        are changed due to the iteration.
        It returns dictionary with keys as name, and values as a value of the setting.
        '''
        # Creating dictionary to store initial settings
        enigma_settings = {}
        enigma_settings['rotors'] = self.group_rotors()
        enigma_settings['steckenbrett'] = self._steckerbrett
        enigma_settings['reflector'] = self._reflector
        return enigma_settings
    
    def group_rotors(self):
        '''
        Returns list grouped values of each rotor.
        First index indicates the rotor which is the first to receive ciphered text.
        '''
        return [self._alpha, self._beta, self._gama]

    def shift(self, seq, n):
        '''
        Shifts inserted sequence n times. If n > 0, it shifts it to the left.
        If n < 0, it shifts it to the right. If n = 0, function returns entered
        sequence.
        '''
        return seq[n:] + seq[:n]

    def initaite_reflector(self):
        '''
        Initiates value of reflector based on the choosing of the reflector
        '''
        '''
        Each of the specific reflector has defined alphabet,
        that must not be changed
        '''
        if self._reflector == "A":
            # holds ascii alphabet shifted 5 letters to the right
            return self.shift(self._alphabet, -5)
        if self._reflector == "B":
            # holds ascii alphabet shifted 2 letters to the left
            return self.shift(self._alphabet, 2)
        if self._reflector == "C":
            # holds ascii alphabet shifted 7 letters to the left
            return self.shift(self._alphabet, 7)

    def reflect_letter(self, index):
        '''
        Returns letter corresponding to the index of a letter 
        in an alphabet hardcoded to the specific reflector.
        '''

        return self._reflector_alphabet[index]

    """def remove_interspace(self, text):
        '''
        This method allows to use interspace in cyphered text.
        It removes the interspace from the text, at the same time remembering
        the index of it
        index_of_interspace is an attribute so it can be acessible later
        '''
        new_text = ''
        self._index_of_interspace = []
        index = 0
        for letter in text:
            if letter != " ":
                index += 1
                new_text += letter
            else:
                index += 1
                self._index_of_interspace.append(index-1)
        return new_text"""

    """    # chyba to nie jest potrzebne do algorytmu
        def Remove_steckerbrett_connections_from_alphabet(self):
            '''
            Letters that are connected in steckerbrett need to be removed
            from alphabet, since they will not be used to assign them to rottor

            '''
            for letter in list(self._steckerbrett.keys()):
                if letter in self._alphabet:
                    self._alphabet.remove(letter)
                    self._alphabet.remove(self._steckerbrett[letter])
                    # from now on, the steckerbrett will be interchangeable - tuple
                    self._steckerbrett.update({self._steckerbrett[letter]: letter})"""

    """def get_rotor_setting(self):
        '''
        This method is not necessary, since it is implemented in the __init__ that rotor value must be 0 <= rotor <= 26
        TO MODIFY LATER: automatically assing each of the rotor new value, not manually at the end
        '''
        for rotor in self._rotors:
            if rotor != 0:
                index = self._rotors.index(rotor)
                rotor = rotor % 26  # rotor makes turn after 26 letters
                self._rotors[index] = rotor  # replace element on the same index

        self.set_new_alpha(self._rotors[0])
        self.set_new_beta(self._rotors[1])
        self.set_new_gama(self._rotors[2])"""

    '''
    Heart of an algorythm.
    '''

    def turn_rotors(self):
        '''Turn the rotors'''

        # All rotors are in border position (26,26,26) 
        if self._gama % 26 == 0 and self._beta % 26 == 0 and self._alpha % 26 == 0:
            self._alpha = 1
            self._beta = 1
            self._gama = 1
        # Rotor A and B are in border position (26,26,x) x < 26
        elif self._beta % 26 == 0 and self._alpha % 26 == 0:
            self._alpha = 1
            self._beta = 1
            self._gama += 1
        # Rotor A is in border position (26,x,x) x < 26
        elif self._alpha % 26 == 0:
            self._alpha = 1
            self._beta += 1
        # None of rotors is in border position (x,x,x) x < 26
        else:
            self._alpha += 1

    def permutation(self, rotor):
        '''Shifts the alphabet to the right by the value of a rotor setting'''
        shifted_alphabet = self._alphabet[-rotor:] + self._alphabet[:-rotor]
        return shifted_alphabet

    def inverse_permutation(self, rotor):
        '''Shifts the alphabet to the left by the value of a rotor setting'''
        shifted_alphabet = self._alphabet[rotor:] + self._alphabet[:rotor]
        return shifted_alphabet

    def steckerbrett_change_letters(self, letter):
        '''
        If letter is in steckerbrett, switch it for the coressponding one
        '''
        for key, value in self._steckerbrett.items():
            if letter == key: 
                letter = value
            elif letter == value:
                letter = key
            else:
                continue
            # if no matches have been found, letter will not be changed
        return letter

    def encryptingCodec(self, inserted_text):
        '''
        Returns modified ciphered_text.
        '''
        ciphered_text = []
        for letter in inserted_text:
            
            # if steckerbrett holds values
            if self._steckerbrett:
                letter = self.steckerbrett_change_letters(letter)

            '''Encrypt by the rotors'''
            self.turn_rotors()
            next_letter = self.permutation(self._alpha)[self._alphabet.index(letter)]
            next_letter = self.permutation(self._beta)[self._alphabet.index(next_letter)]
            next_letter = self.permutation(self._gama)[self._alphabet.index(next_letter)]

            # self._alphabet.index(next_letter)
            # index litery alfabetu ascii wchodzącej do alfabetu reflektora
            next_letter = self.reflect_letter(self._reflector_alphabet[::-1].index(next_letter))

            next_letter = self.inverse_permutation(self._gama)[self._alphabet.index(next_letter)]
            next_letter = self.inverse_permutation(self._beta)[self._alphabet.index(next_letter)]
            next_letter = self.inverse_permutation(self._alpha)[self._alphabet.index(next_letter)]

            # Once again conjugated letters need to be checked 
            if self._steckerbrett:
                next_letter = self.steckerbrett_change_letters(next_letter)

            # append encripted letter to ciphered_text
            ciphered_text.append(next_letter)
        
        '''Return Modified'''
        return("".join(ciphered_text))