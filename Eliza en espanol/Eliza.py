import string
import re
import random

euro = unichr(0x20ac)

class Eliza(object):
    def __init__(self):
        self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),gPats)
        self.values = map(lambda x:x[1],gPats)

    # translate: take a string, replace any words found in dict.keys()
    #  with the corresponding dict.values()
    def translate(self,str,dict):
        words = string.split(string.lower(str))
        keys = dict.keys();
        for i in range(0,len(words)):
            if words[i] in keys:
                words[i] = dict[words[i]]
        return string.join(words)

    # respond: take a string, a set of regexps, and a corresponding
    #    set of response lists; find a match, and return a randomly
    #    chosen response from the corresponding list.
    def respond(self,str):
        # find a match among keys
        for i in range(len(self.keys)):
            match = self.keys[i].match(str)
            if match:
                # found a match ... stuff with corresponding value
                # chosen randomly from among the available options
                resp = random.choice(self.values[i])
                # we've got a response... stuff in reflected text where indicated
                pos = string.find(resp,'%')
                while pos > -1:
                    num = string.atoi(resp[pos+1:pos+2])
                    resp = resp[:pos] + \
                        self.translate(match.group(num),gReflections) + \
                        resp[pos+2:]
                    pos = string.find(resp,'%')
                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

gReflections = {
    "yo" : "tu",
    "tu" : "yo",
    "mi"  : "tu",

    "yo podria"  : "tu podrias",
    "yo tendria"  : "tu tendrias",
    "yo creo"  : "tu crees",
    "yo creeria"  : "tu creerias",

    'a mi' : 'a ti',
    'a ti' : 'a mi',
    "para mi"  : "para ti",
    "para ti" : "para mi",
    "por mi" : "por ti",
    "por ti" : "por mi",
    "desde mi" : "desde tu",

    "tu crees": "yo creo",
    "tu podrias": "yo podria",

    "tuyo"  : "mio",
    'mio' : 'tuyo',
    "me"  : "te",
    'te' : 'me',

    #verbos
    "soy"   : "eres",
    "eres"  : "soy",
    "fui"  : "fuiste",
    "fuiste" : "fui",
    "has" : "he",
    'estoy' : 'estas',
    'era' : 'eras',
    'estaba' : 'estabas',
    'dije' : 'dijiste',
    'seras' : 'sere',
    'puedo' : 'puedes',
    'quiero' :  'quieres'
    }

gPats = [
    [r'.*?(encienda|encender|enciende) la luz',
    ["A que luz te refieres?"]],
     
    [r'.*?(abra|abre) la puerta',
    ["A que puerta te refieres?"]]
    
    [r'',
    [""]]
    ]

def command_interface():
    print "Habla al programa escribiendo en espanol plano-"
    print 'No uses la letra enhe, abrir pregunta ni tildes.  Escribe "salir" para finalizar.'
    print '='*72
    print "Hola. Que deseas hacer hoy?"
    s = ""
    therapist = Eliza();
    while s != "salir":
        s = raw_input(">")
        while s[-1] in "!.": s = s[:-1]
        print therapist.respond(s)

if __name__ == "__main__":
    command_interface()