#======================================================
# Just try it! :)
#======================================================

class Televisao:
    def __init__(self):
        self.volume = 0
        self.canal = 0
 
    def Mudar_volume(self, volume):
        if volume > 40:
            return 'vol.max = 40'
        if volume < 0:
            return 'vol.min = 0'
        else:
            self.volume = volume
        return self.volume

    def Mudar_canal(self, canal):
        if canal > 100:
            return 'Ultimo canal = 100'
        if canal < 1:
            return 'Ultimo canal = 1'
        else:
            self.canal = canal
        return self.canal

    def imagem(self):
        s = ''
        for x in range(5):
            s += (' '*(x) + '+' + ' '*(10-2*x) + '+') + '\n'
        if self.volume < 10:
            if self.canal == 100:
                s += '+' + '-'*30 + '+' +'\n'
                s += '+' + ' canal:' + str(self.canal) + ' '*20 + '+' + '\n'
                for x in range(10):
                    s += ('+' + ' '*30 + '+') + '\n'
                s += '+' + '  volume:' + str(self.volume) + ' '*20 + '+' + '\n'
                s += '+' + '-'*30 + '+'
            if self.canal < 10 :
                s += '+' + '-'*30 + '+' +'\n'
                s += '+' + '  canal:' + str(self.canal) + ' '*21 + '+' + '\n'
                for x in range(10):
                    s += ('+' + ' '*30 + '+') + '\n'
                s += '+' + '  volume:' + str(self.volume) + ' '*20 + '+' + '\n'
                s += '+' + '-'*30 + '+'
            else:
                s += '+' + '-'*30 + '+' +'\n'
                s += '+' + ' canal:' + str(self.canal) + ' '*21 + '+' + '\n'
                for x in range(10):
                    s += ('+' + ' '*30 + '+') + '\n'
                s += '+' + '  volume:' + str(self.volume) + ' '*20 + '+' + '\n'
                s += '+' + '-'*30 + '+'
        else:
            if self.canal == 100:
                s += '+' + '-'*30 + '+' +'\n'
                s += '+' + ' canal:' + str(self.canal) + ' '*20 + '+' + '\n'
                for x in range(10):
                    s += ('+' + ' '*30 + '+') + '\n'
                s += '+' + ' volume:' + str(self.volume) + ' '*20 + '+' + '\n'
                s += '+' + '-'*30 + '+'
            if self.canal < 10 :
                s += '+' + '-'*30 + '+' +'\n'
                s += '+' + '  canal:' + str(self.canal) + ' '*21 + '+' + '\n'
                for x in range(10):
                    s += ('+' + ' '*30 + '+') + '\n'
                s += '+' + ' volume:' + str(self.volume) + ' '*20 + '+' + '\n'
                s += '+' + '-'*30 + '+'
            else:
                s += '+' + '-'*30 + '+' +'\n'
                s += '+' + ' canal:' + str(self.canal) + ' '*21 + '+' + '\n'
                for x in range(10):
                    s += ('+' + ' '*30 + '+') + '\n'
                s += '+' + ' volume:' + str(self.volume) + ' '*20 + '+' + '\n'
                s += '+' + '-'*30 + '+'
            
        return s
    
tv = Televisao()
p = 'k'
while p == 'k':
    print 'Programa'
    print
    print 'Canal: 1 ~ 100'
    print 'Volume: 0 ~ 40'
    print
    n = input('Digite um canal: ')
    m = input('Regule o volume: ')
    tv.Mudar_canal(n)
    tv.Mudar_volume(m)
    print tv.imagem()


        
        
