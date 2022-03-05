from pickle import TRUE
import telebot
chave_api='api'
bot=telebot.TeleBot(chave_api)
@bot.message_handler(commands=['ver_o_cardapio'])
def cardapio(mensagem):
    vercardapio='''Bloomin' Onion (R$49.90)
Aussie Cheese Fries (R$59.90)
Firecracker Shrimp Nachos (R$69.90)
Alice Springs Chicken (R$59.90)
Ribs on the Barbie (R$79.90)
Jr. Ribs for two (R$99.90)
Havana Thunder (R$34.90)
/voltar'''
    bot.send_message(mensagem.chat.id,vercardapio)
@bot.message_handler(commands=['fazer_o_pedido'])
def fazerpedido(mensagem):
    texto='''ola,digite o que voce quer e o seu endereco de entrega
    /voltar'''
    bot.send_message(mensagem.chat.id,texto)
def verificar(mensagem):
    return True
@bot.message_handler(func=verificar)
@bot.message_handler(commands=['voltar'])
def respostapadrao(mensagem):
    texto='''escolha uma das opcoes abaixo(clique nas opcoes):
    /ver_o_cardapio 
    /fazer_o_pedido'''
    bot.send_message(mensagem.chat.id,texto)
bot.polling()#bot looping