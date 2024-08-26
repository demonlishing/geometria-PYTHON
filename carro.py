#acessar um objeto no método público

#livro01 = livro("A Metarmorfose", "Franz Kafka", etc....) Adicionando atributos ao livro

# livro01.titulo() - Acessar os atributos públicos
#@property
#def titulo(self):                  Acessar atributos privados
#    return self.__titulo

def set_titulo(self, texto):
    self.__titulo = texto
