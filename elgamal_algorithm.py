from elgamal.elgamal import Elgamal, PublicKey, PrivateKey, CipherText
from algorithm import Algorithm


# self.private_key = PrivateKey(
# 22763364761752953499026581212788555278960115429036559359008266034809244953613445346099559800203421465023198696515011456216983906912540855829748849985504680955686758319183123469098642497912279066928820225677280437400965215613642029762121710699272627595608213571195042757435653822268173513032123061816835414358606371708059281001644311399894096755888648610475759920709784815080149187393529880347379238509950062912420612352960851772927061255678641760429569099975421238093889460074159155408386923334998490183741962433866252635460188243039431437723720973865481584323106766117621977920270406863606367168428324584755243764643
# 5475428716348260836333346743859471632711378924268004419322474704628451444724258993166470462506743517718535830782187837807220102017170971620051388274196458629635186024267535322644046777928886513621467648819218807646975570372363322134906985730900282095003422879840065690733133184404026730175896315059258981017647190898742763966022211100940915643654935585556223408884095654521622694202841887892046340203707429224541209337379145869760140481891654033822927902259689177823740806905446788917703737968078498719423064260020372871021476438334953582200779738767913577769467297221698969161986852240448535126267280170024002740030

# self.public_key = PublicKey(
# 22763364761752953499026581212788555278960115429036559359008266034809244953613445346099559800203421465023198696515011456216983906912540855829748849985504680955686758319183123469098642497912279066928820225677280437400965215613642029762121710699272627595608213571195042757435653822268173513032123061816835414358606371708059281001644311399894096755888648610475759920709784815080149187393529880347379238509950062912420612352960851772927061255678641760429569099975421238093889460074159155408386923334998490183741962433866252635460188243039431437723720973865481584323106766117621977920270406863606367168428324584755243764643
# 2
# 84192645185195124817074892167373367175867067212311358887657880171055051745589728335546792594868290177801287656291870529141006021963110432815708343212274523170226568831800949958914818182072423278708401010295347394105013417792484583235939792970669713806753823434372705178874457182127978818935143528598161420269516828379480001959291416902263473384029449654429255112864595283697137557092450310661757668528071064045593691157903299547167084372271978486231219469184602085399418574779982285037124578405259995198700419879634607091149167250550254686456706261153063724173889922895941321035332916917804580368647554875806557513897329909048647496208351382310971177967443798018833572494096478342960171749963287076716978404805790285966843120245247107377116753656221248504596363785337973252683679426985885989119786834056730150731031848451241518075690442918262070760475578784232824239077677274509482175350715842522731523271894166337378266575047590401048438831235347641153021246767112441106511191167690317218047072615420866046647775731417430135591329666193655832239087748158837953828161799013216197301163496519065645150587437505525369575831617655961116219256126498685942888225668419582445977884126316862255714467008535634351271596286845216405118928529

# CipherText(
# 273023277698901928717167850450805295997892558483655181116481933232426458459796088527415405654285348492538011762403739224120985512896123607534039475463397578990087804077976656437085820711233331950905903917862649630898090280376930220189801697663601096259079775007359807507997827530487538796802221542136891402564290269951564886067679437508558073078817869628964846261321835322920577465823092937836602271112342740193716003782879771607788230254245466219325596952903378441072599555084442288098741795393303506720347221432648688237350136162416538427862051152322120509044454987946696636028125829215332517221598727576464233576677053460472657379841848395578860219923229770910862270299302780019281092176236138824826461298993885989488324226892223506765119876766268378854013467762203847032908483269129845964782064530547593850553479570131091818168771454478529267967092955723066275041407172871404216429711070634383723503716247657227807671319881663465056655576119739096017544167407546975327506377579908119859677333257152895707179320508202541149185838574846889599422196955674807078024131734920356985083391245756799649833766785670391365332979672941354443006146806583660884097452698784424849185274862179254307108510226627897609666144953141647420107318336
# 12815918601298631721245245315050438532666015673231935727012934933223526184353977196735179923963805928324907057211534134373303632337724002064339885086336342592531632083636907329186595067736015331811817195334435728651185167221463782737928849696772590151803011803065137627017325671346722534636229078258810111999859968233419531536614586215794934220843999485198736053125411723672847071063712753056069618885525502292954635739257603876828301286409802279174699380789637845325325288427356346680421280622128482560120308601002384120870661082677329896121880557450171944033104435141703391201300986030092382649053618160650193556951)


class ElgamalAlgorithm(Algorithm):
    def __init__(self, p=None, x=None, g=None, y=None):
        if x:
            self.private_key = PrivateKey(p, x)
            # print(self.private_key)
        if g and y:
            self.public_key = PublicKey(p, g, y)
            # print(self.public_key)

    def encrypt(self, data):
        data_bytes = bytearray(data, 'utf-8')
        encrypted_message = Elgamal.encrypt(data_bytes, self.public_key)
        return encrypted_message

    def decrypt(self, data):
        a, b = data
        cipher_text = CipherText(a,b)
        decrypted_message = Elgamal.decrypt(cipher_text, self.private_key)

        return decrypted_message.decode('utf-8')