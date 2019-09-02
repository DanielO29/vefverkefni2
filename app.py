import os
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def heimasida():
    return """
    <h2> Halló Heimur! </h2>
    <p>
    <a href="/frettir1" title="Frettir 1">Fréttir 1 </a> --
    <a href="/frettir2" title="Frettir 2">Fréttir 2 </a> --
    <a href="/frettir3" title="Frettir 3">Fréttir 3 </a> 
    </p>
    """

@app.route("/frettir1")
def frettagrein():
    return """
    <h2> Þrír fullorðnir menn reyndu að taka af honum vespuna </h2>
    <p> 14 ára unglingur í Breiðholti varð fyrir því í kvöld að þrír fullorðnir karlmenn réðust að honum og reyndu að ræna af honum vespu sem hann ók. Drengurinn gaf þá lýsingu á mönnunum að þeir hefðu verið um tvítugt og af erlendum uppruna, líklega frá Austur-Evrópu. </p>
    <p>
    <a href="/" title="heimasida">Forsíða </a> --
    <a href="/frettir2" title="Frettir 2">Fréttir 2 </a> -- 
    <a href="/frettir3" title="Frettir 3">Fréttir 3 </a>
    </p>
    """


@app.route("/frettir2")
def frettagrein2():
    return """
    <h2> Erum við að þvo okkur of oft um hendurnar? </h2>
    <p> Læknar, foreldrar, kennarar, leiðbeinendur og í raun allir þeir sem hjálpast að við að ala upp og kenna börnum á hreinlæti, minna þau reglulega á það að þvo sér vel um hendurnar. Handþvottur er eitthvað sem við ólumst upp við að gera reglulega og flestum finnst vera sjálfsagður hlutur. </p>
    <p>
    <a href="/" title="heimasida">Forsíða </a> --
    <a href="/frettir1" title="Frettir 1">Fréttir 1 </a> -- 
    <a href="/frettir3" title="Frettir 3">Fréttir 3 </a>
    </p>
    """
@app.route("/frettir3")
def frettagrein3():
    return """
    <h2> Neyðarástandi lýst yfir á Púertó Ríkó </h2>
    <p> Neyðarástandi hef­ur verið lýst yfir á Pú­er­tó Ríkó, vegna hita­belt­is­storms­ins Dori­an, sem bú­ist er við að muni ná styrk felli­byls er að hann geng­ur þar á land í kvöld. </p>
    <p>
    <a href="/" title="heimasida">Forsíða </a> --
    <a href="/frettir2" title="Frettir 2">Fréttir 2 </a> -- 
    <a href="/frettir1" title="Frettir 1">Fréttir 1 </a>
    </p>
    """

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True)