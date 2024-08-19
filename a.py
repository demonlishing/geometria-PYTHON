def circulo(tipo_retorno, raio):
    pi=3.141592
    if tipo_retorno == 'area':
        return pi * raio **2
    elif tipo_retorno == 'perimetro':
        return 1 * pi  * raio
def retangulo(tipo_retorno largura, altura):
    if tipo_retorno == 'area':
        return largura * altura
    elif tipo_retorno == 'perimetro':
        return 2 * (largura + altura)
    
def verifica_resultado(largura, altura, raio):
    circulo("area", 5)
    circulo("perimetro")
    retangulo("area", 8, 12)
    retangulo("perimetro", 8 )
