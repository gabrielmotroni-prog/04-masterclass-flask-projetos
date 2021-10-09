# arquivo que contem meus filtros personalizados

#ja eh esperado nessa funcao um value tipo date time por isso o retorno ja retorna 
#usando a funcao return ja usar datime
def format_date(value):
    return value.strftime("%d-%m-%Y %H:%M:%S")