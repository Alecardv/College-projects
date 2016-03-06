## Graphic eliza using Iron Python

﻿import wpf
import sys
import string
import re
import random

from System.Windows import Input
from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        self.s = ""
        self.therapist = Eliza()
        wpf.LoadComponent(self, 'Graphic_Eliza.xaml')
    
    def button_Send_Click(self, sender, e):
        if self.textBox.Text == 'salir':
            sys.exit()
        else:
            self.s = self.textBox.Text
            self.textBlock.Text += '\n'
            self.textBlock.Text += 'You: '
            self.textBlock.Text += self.textBox.Text
            self.textBox.Text = ''
            self.textBlock.Text += '\n'
            self.textBlock.Text += 'Eliza: '
            self.textBlock.Text += self.therapist.respond(self.s)


    def textBox_KeyDown(self, sender, e):
        if e.Key == Input.Key.Enter:
            if self.textBox.Text == 'salir':
                sys.exit()
            else:
                self.s = sender.Text
                self.textBlock.Text += '\n'
                self.textBlock.Text += 'You: '
                self.textBlock.Text += sender.Text
                sender.Text = ''
                self.textBlock.Text += '\n'
                self.textBlock.Text += 'Eliza: '
                self.textBlock.Text += self.therapist.respond(self.s)

class Eliza(object):
    def __init__(self):
        self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),gPats)
        self.values = map(lambda x:x[1],gPats)
  
    def translate(self,str,dict):
        words = string.split(string.lower(str))
        keys = dict.keys();
        for i in range(0,len(words)):
            if words[i] in keys:
                words[i] = dict[words[i]]
        return string.join(words)

    def respond(self,str):
        for i in range(0,len(self.keys)):
            match = self.keys[i].match(str)
            if match:
                resp = random.choice(self.values[i])
                pos = string.find(resp,'%')
                while pos > -1:
                    num = string.atoi(resp[pos+1:pos+2])
                    resp = resp[:pos] + \
                        self.translate(match.group(num),gReflections) + \
                        resp[pos+2:]
                    pos = string.find(resp,'%')
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

gReflections = {
    "yo" : "tu",
    "tu" : "yo",
    "mi"  : "tu", #Ej: Mi amor, Tu amor

    "yo podria"  : "tu podrias",
    "yo tendria"  : "tu tendrias",
    "yo creo"  : "tu crees",
    "yo creeria"  : "tu creerias",

    'a mi' : 'a ti',
    'a ti' : 'a mi',
    "para mi"  : "para ti", #Ej: Es importante para mi, Es importante para ti
    "para ti" : "para mi",
    "por mi" : "por ti",
    "por ti" : "por mi",
    "desde mi" : "desde tu",

    "tu crees": "yo creo",
    "tu podrias": "yo podria",

    "tuyo"  : "mio",
    'mio' : 'tuyo',
    "me"  : "te", #Me pertenece, Te pertenece
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
[r'Yo necesito (.*)',
["¿Por que tu necesitas %1?",
"¿Eso realmente te ayuda a obtener %1?",
"¿Estas seguro que necesitas %1?"]],

[r'¿Por que tu no ([^\?]*)\??',
["¿Tu realmente crees que yo no %1?",
"Tal vez algun dia tu %1.",
"¿Realmente me quieres para %1?"]],

[r'Porque no puedo ([^\?]*)\??',
["Tu crees que estas capacitado para %1?",
"Si tu pudieras %1, que crees que harias?",
"No se -- porque tu no puedes%1?",
"Realmente lo has intentado?"]],

[r'Yo no puedo (.*)',
["Como sabes que no puedes %1?",
"Sin embargo tu podrias %1 si tu lo intentas.",
"Que haria falta para que usted pudiera %1?"]],

[r'Yo soy (.*)',
["Viniste a mi por que eres %1?",
"Hace cuanto eres %1?",
"Como te sientes siendo %1?"]],

[r'I\'?m (.*)',
["How does being %1 make you feel?",
"Do you enjoy being %1?",
"Why do you tell me you're %1?",
"Why do you think you're %1?"]],

[r'Tu eres ([^\?]*)\??',
["Por que importa lo que sea %1?",
"Te gustaria que no fuera %1?",
"Pero piensas que soy %1.",]],

[r'Que es (.*)',
["Por que lo preguntas?",
"No tengo respuesta para eso, quizas siri si :p",
"Ya buscaste en Google?"]],

[r'Como es (.*)',
["Como supones que es %1?",
"Quizas tu puedas contestar tu pregunta",
"Por que me preguntas eso?"]],

[r'Porque (.*)',
["Esa es la razon?",
"Que otras razones te vienen a la mente?",
"Estas seguro que %1?",
"Estoy de acuerdo"]],

[r'(.*) perdon|perdoname (.*)',
["En muchos casos una disculpa no es suficiente.",
"Prometes no volver a hacerlo?"]],

[r'Hola(.*)',
["Hola!, no sabes lo feliz que estoy de verte de nuevo :D",
"Hola, Como estas?",
"Hola, Como te sientes hoy?"]],

[r'yo creo (.*)',
["dudas %1?",
"Realmente crees eso?",
"No estoy de acuerdo"]],

[r'(.*) amigo?s (.*)',
["Dime a cerca de tus amigos?",
"Cuando piensas en un amigo, que viene a tu cabeza?",
"Cuentame de tus amigos de infancia?"]],

[r'Si',
["Luces muy seguro",
"Bueno",
"Podrias decirme por que?"]],

[r'No',
["Luces muy seguro",
"Bueno",
"Podrias decirme por que?"]],

[r'(.*) computador(.*)',
["Estas hablando a cerca de mi?",
"Te parece extraño hablar conmigo?",
"Como te hace sentir hablar con computadores?",
"Te sientes amenazado por las computadoras?"]],

[r'Is it (.*)',
["Do you think it is %1?",
"Perhaps it's %1 -- what do you think?",
"If it were %1, what would you do?",
"It could well be that %1."]],

[r'It is (.*)',
["You seem very certain.",
"If I told you that it probably isn't %1, what would you feel?"]],

[r'Podrias ([^\?]*)\??',
["Que te hace pensar que no podria %1?",
"Si podria %1, entonces que?",
"Por que preguntas si puedo %1?"]],

[r'Podria ([^\?]*)\??',
["Quizas no quieres %1.",
"Realmete crees que podrias %1?",
"Si puedes %1, por que no lo haces?"]],

[r'Tu eres (.*)',
["Por que crees que soy %1?",
"No te gusta que sea %1?",
"Tambien quieres ser %1.",
"Te ves reflejado en mi?"]],

[r'(.*) eres (.*)',
["Por que dices que soy %1?",
"Por que piensas que soy %1?",
"Estamos hablando de ti o de mi?"]],

[r'Tu ?no (.*)',
["Por  que no %1?",
"Realmente %1?",
"Deberiamos hablar de ti, no de mi."]],

[r'Yo ?me siento (.*)',
["Es bueno que te expreses, cuentame mas.",
"Usualmente te sientes %1?",
"Cuando te sientes %1?",
"Cuando te sientes %1, que haces?"]],

[r'Yo tengo(.*)',
["Por que dices que tienes %1?",
"Realmente tienes %1?",
"Ahora tu tienes %1, que tendras despues?"]],

[r'I would (.*)',
["Could you explain why you would %1?",
"Why would you %1?",
"Who else knows that you would %1?"]],

[r'Is there (.*)',
["Do you think there is %1?",
"It's likely that there is %1.",
"Would you like there to be %1?"]],

[r'Mi (.*)',
["Ya veo tu %1.",
"Por que dices que es tuyo?"]],

[r'Por que (.*)',
["Por que no me dices tu?",
"Tu crees que %1?" ]],

[r'Yo quiero (.*)',
["Que harias si consigues %1?",
"Por que lo quieres%1?",
"Que harias si no consigues %1?",]],

[r'(.*) madre|mamá(.*)',
["Dime más acerca de tu madre.",
"Como es la relación con tu madre?",
"Como te hace sentir tu madre?",
"Amas a tu madre?",
"Buenas relaciones familiares son importantes."]],

[r'(.*) padre|papá(.*)',
["Dime mas acerca de tu padre.",
"Como es la relación con tu padre?",
"Como te hace sentir tu padre?",
"Amas a tu padre?",
"Buenas relaciones familiares son importantes."]],

[r'(.*) niñez(.*)',
["Tienes amigos de la niñez?",
"Cual es tu mejor recuerdo de pequeño?",
"Recuerdas algun sueño que tenias cuando eras pequeño?",
"De niño se burlaban de ti?",
"Crees que tus vivencias de niño fueron significativas?"]],

[r'(.*) bien(.*) tu\?',
["Igual que tu",
]],

[r'(.*)\?',
["Por que preguntas eso?",
"Por favor considera que podrias responder tu mismo la pregunta.",
"Quizas la respuesta esta en tu corazón?",
"Por que me preguntas si sabes que no se la respuesta?"]],

[r'Salir',
["Gracias por hablar conmigo!",
"Adios, ten un gran día!",
"Gracias son $100.000, Ten un gran día!"]],

[r'(.*)',
["Por favor cuentame más.",
"Cambiemos de tema, no quiero hablar de eso.",
"Can you elaborate on that?",
"Por que dices que %1?",
"Ya veo.",
"Muy interesante.",
"%1.",
"OK, y eso que te dice?",
"Y eso como te hace sentir?",
"Como te sientes cuando dices eso?"]]
]


if __name__ == '__main__':
    Application().Run(MyWindow())
