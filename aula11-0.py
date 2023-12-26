#cores no terminal
#Padrão ANSI = padrão de normalização internacional
#ANSI escape sequence
#tudo começa com contrabarra (caracter de escape) e é seguido por um código (o que funciona melhor p Python é o 033)
#exemplo: \033[style;text;back;m
#\033[0;33;44m
#código pra style: 0 (nenhum - none), 1(negrito - bold), 4(sublinhado - underline) e 7(inverter - negative)
#para text: de 30 a 37
#para back: de 40 a 47

print('\033[7;35;41mteste')

print('\033[4;36;43mManuela\033[m')