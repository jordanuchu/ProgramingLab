class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    lista_dati=[]
    lista_linea=[]

    def __init__(self, name ):
        self.name=name

    def get_data(self):

        count=0

        my_file=open(self.name,'r')

        for line in my_file:

            if count>=1:
                elementi = line.split(',')

                try:
                    if type(int(elementi[0])) == int:
                        self.lista_linea.append(int(elementi[0]))
                        if type(float(elementi[1]) == float):
                            self.lista_linea.append(float(elementi[1]))
                            self.lista_dati.append(self.lista_linea)
                            self.lista_linea = []
                except ExamException:
                    pass

            count = count + 1
        my_file.close()
        return self.lista_dati

#--------------------------------------------------------------------------------------------------------
def compute_daily_max_difference(mylist):
    lista_ListEpochGiorno = []
    primo_epoch = 1551398400
    lista_EpochGiorno =[]
    lista_AllEpoch = []
    dico_EpochTemp ={}
    lista_finale =[]

    to=0
    x=0
    while x < len(lista_AllEpoch):
        if (lista_AllEpoch[x] < lista_AllEpoch[x - 1]):
            to = 1
        x = x + 1

    if (to == 1):
        raise ExamException("la nostra lista non è ordinata")
    if len(lista_AllEpoch) != len(set(lista_AllEpoch)):
        raise ExamException('la nostra lista contiene duplicati')

        
    for y in mylist:
        lista_AllEpoch.append(y[0])
        dico_EpochTemp[y[0]] =y[1]


    while primo_epoch<=1554073200:

        for w in lista_AllEpoch:

            if (w - (w % 86400)) == primo_epoch:
                lista_EpochGiorno.append(w)

            else:
                primo_epoch = primo_epoch + 86400
                lista_ListEpochGiorno.append(lista_EpochGiorno)
                lista_EpochGiorno = []
                lista_EpochGiorno.append(w)

    lista_listepochgiornoModif = []

    for i in lista_ListEpochGiorno:
        if i not in lista_listepochgiornoModif:
            lista_listepochgiornoModif.append(i)


    count =0
    for a in lista_listepochgiornoModif:
        if len(a )==1:
            count=count +1

    while count >0:
        for b in lista_listepochgiornoModif:
            if len(b )==1:
                lista_listepochgiornoModif.remove(b)
        count =count -1

    def differenza(e):
        lista_dif=[]
        for i in e:
            a=dico_EpochTemp[i]
            lista_dif.append(a)
        mx=max(lista_dif)-min(lista_dif)
        return mx


    for q in lista_listepochgiornoModif:
        if len(q)==1:
            lista_listepochgiornoModif.append(None)
        else:
            val = differenza(q)
            lista_finale.append(val)

    return lista_finale
#----------------------------------------------------------------------------------------------------------


try:
    time_series_file = CSVTimeSeriesFile(name='data.csv')
    time_series = time_series_file.get_data()
except Exception:
    print("errore nella lettura del file")

lista_escurzione_termica=compute_daily_max_difference(time_series)
print(lista_escurzione_termica)

