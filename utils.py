from models import Pessoas

def insere_pessoa():
    pessoa = Pessoas(nome='Douphing',idade=34)
    print(pessoa)
    pessoa.save()



def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Douphing').first()
    print(pessoa.idadge)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Douphing').first()
    pessoa.nome = 'Campos'
    pessoa.save()

def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Douglas').firts()
    pessoa.delete()

if __name__ == '__main__':
   #insere_pessoa()
   consulta_pessoa()
   #altera_pessoa()
    #exclui_pessoas()