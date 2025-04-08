#pyutogui
#RPA
import pyautogui
import time
 
 
#Point(x=482, y=234)
#Tempo de execução após o Sleep
pyautogui.PAUSE = 0.7

#Pegar posiçãoes do mouse e da tela 
print(pyautogui.position())
print(pyautogui.size())

#Função do mouse 


time.sleep(3)
pyautogui.hotkey('alt','tab') #-- Mudando de pagina 
'''pyautogui.moveTo(x=659, y=16, duration=1) # Movendo o mouse ate o  local 
pyautogui.click(x=659, y=16) # Clicando no local 
pyautogui.write('Enviando uma mensagem') # Enviando uma mensagem
pyautogui.press('Enter') # Enviando a mensagem
pyautogui.hotkey('ctrl','v') # Colando algo '''
pyautogui.click(x=482, y=234)
pyautogui.press('Enter') # Enviando o que colou 



