import time

import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
espirisoru = ["Tuvaletteki 10’a ne denir?","En güzel yemek yapan Ceren hangisidir?","İshal olmuş böceğe ne denir?","Bacaktaki 10’a ne denir?","Türkiye’nin en yeni şehri hangisidir?",
"Yıkanan ton balığına ne denir?","Baykuşlar vedalaşırken ne der?","Yemeğin suyuna kim bandı?","Bebeğe patik giydirmeye çalışmışlar ama giymemiş neden?"," İngilizler kendi kıllarına ne der?","Gülen ördeğe ne denir?","Örümcek adam ağ atamıyormuş neden?","Siviller hangi dili konuşur?",
"En değerli meşe hangisidir?","Küçük su birikintisine ne denir?","Hiç bozuk paran var mı?","Taşımasu annesinden nasıl su ister?","Aya ilk bayrağı kim dikmiştir?","İneklerin sevmediği element?","Kırmızı giyen erkeğe ne denir?","En çok eşek yavrusu nerde bulunur?",
"Pişmemiş burgere ne denir?","Dört tarafı suyla çevrili çaya ne denir?"]

espiricevap = ["SİFON","TENCEREN","CIRCIR BÖCEĞİ","PANTOLON","NEVŞEHİR","WASHINGTON","BAY BAY BAYKUŞ","KOLİ BANDI","BEBEK ANTİPATİKMİŞ","MICHEAL","KIKIR-DUCK","ÇÜNKÜ AĞ BAĞLANTISI KOPMUŞ.","SİVİLCE","İZZET ALTINMEŞE","SUCUK","YOK ÇÜNKÜ HEPSİNİ TAMİR ETTİRDİM.","MATARAMASUKO","TERZİ","AZ-OT","ALBAY","SPA MERKEZİNDE","HAMBURGER","ADAÇAYI"]


sadeceespiri = ["Mafya babası olmak için oğlumun adını “Mafya” koydum.","Kim vurduya gittim birazdan gelecem...","Zenginler et, fakirler hayalet yer.","Bugünlerde gözüm çok KIZarıyor.- Benimde arıyor ya!","Hava korsanı uçağı kaçıracaktı ama yapamadı çünkü uçağı kaçırdı.","GİT’Arı’ getir de biraz şarkı söyleyelim. -Abi arı sokmasın!","Sana bir kıllık yapayım, kıllarını koyarsın.","Seven unutmaz oğlum, eight unutur.","Cem Uzan, üstünü örteyim.","Geçenlerde izdivaç programında adam evim, arabam, param var dedi üç hatun aynı anda elektrik aldı. Adam bildiğin üçlü priz çıktı.","Haydi Unkapanı’na gidip birkaç kapan kuralım. Belki un yakalarız","SSaçını sarıya boyatıp kaşlarını zift karası bırakınca doğal sarışın olmuyorsun tatlım. Borussia Dortmund deplasman forması gibi oluyon.","Sonuçta çubuk krakerle sigara içme taklidi yapan çocuklardık biz. Hangi ara bu kadar cool olduk.","Adamın biri güneşte yanmış, ay da düz.","Ben Yedigün içiyorum sen Onbeşgün iç.","Sinemada on dakika ara dedi, aradım aradım açmadı.","Röntgen Filmi çektirdik, yakında sinemalarda.","Adamın Biri Notebook Almış, DELLenmiş.","Geçen gün taksi çevirdim hala dönüyor.","Ben hikâye yazarım Ebru Destan.","Geçen gün geçmiş günlerimi aradım ama meşguldü.","Tebrikler kazandınız, şimdi tencere oldunuz!","Kaba kuvvet uygulama, kap kırılabilir.","Türkiye’nin en yeni şehri – Nevşehir","Ayna'nın karşısında süslenme, manga'nın karşısında süslen.","Geçen ‘fil’e çorap aldım, zürafaya almadım.","Yılanlardan korkma, yılmayanlardan kork.","Ben kahve içiyorum, Nurgül Yeşilçay.","Bak şu karşıdaki uçak PİSTİ, ama bir türlü temizlemediler.","Geçen gün geçmiş günlerimi aradım ama meşguldü","Adamın birisi televizyona çıkmış bir daha indirememişler.","Adamın biri gülmüş, saksıya koymuşlar.","Sinüs 60, kosinüs tutmuş…","Adamın biri kızmış istemeye gelmişler.","Ayda 5 milyon kazanma ister misin? Evet.  O zaman Ay’a git.","Funda Arar dediler ama hala daha aramadı.","Adamın kafası atmış bacakları eşek.","Uzun lafın kısası : U.L.","Yağmur yağmış, kar peynir!","Sakla samanı, inekler aç kalsın.","Baraj dendi mi, akan sular durur.","Dünya dönermiş ay da köfte…","Son gülen en geç anlayandır.","Bu erikson, başka erik yok.","Seven unutmaz oğlum, eight unutur.","Sen kamyonu al, Leonardo da vinci.","Adamın biri gülmüş, bahçeye dikmişler.","Tekel'in nesi var, İki elin sesi var.","Top ağlarda, ben ağlamaz mıyım? ","Esra Erol ile - İs The Watch.","Burger King, bende Vezir.","Adamın biri gülmüş, bahçeye dikmişler.","Ben yürüyelim diyorum Gerard Depardieu.","Beni ayda bir sinemaya götürme, Marsta bir sinemaya götür.","Sevgilisi olmayanlar bul-aşık makinası alsınlar.","Ben ekmek yedim Will Smith.","Aaaaa siz çok terlemişsiniz durun size terlik getiriyim.","Temel bir gün Fransa’ya gitmiş:”Aaa burayı da mı Sabancı aldı.” demiş.","Geçen gün arkadaşlarla fırında patates yiyorduk, fırın sıcak geldi bahçeye çıktı.","İngilizcem yok, tanıdığım bütün Cem'ler Türk.","Sarımsağı havanda dövmüşsün, Ha Muş'ta.","Dondurmayı ben yalamam, himalayalar.","Kalbinin sesini dinle güzelse kaset yap.","Bağırsaklarda yaşayan tenya kurtları bağırsakta yaşarlar bağırmasak da yaşar.","Çiçeğin biri solmuş diğeri de sağ.","Aklımı kaçırdım, 100.000 TL fidye istiyorum.","Altılıda 1. ayakta yattım. Yarış bitmiş uyanamadım.","Ayakkabıcı sıkıyorsa alma dedi, bende korktum aldım","Balık ekmek 3 liraymış, hadi balık ekelim.","Bekarlık sultanlıktır, fakat er ya da geç demokrasiye geçilir"]

@bot.event
async def on_ready():
    print("Ben Hazırım")


@bot.command()
async def mf(ctx, *args):
    if "naber" in args:
        await ctx.send("İyi Knka Senden Naber")
    elif "iyi" in args:
        await ctx.send("Güzel Havlar Nasıl Orda")
    elif "kötü" in args:
        await ctx.send("Takma Be Knka Kafana Boştu Dünya")
    elif "güneşli" in args:
        await ctx.send("Güzel Güzel")
    elif "havadurumu" in args:
        await ctx.send("!mf şehir ardından şehirini yazarsan hemen bakabilirim")
    elif "şehir" in args:
        url = "https://www.ntv.com.tr/'{}'-hava-durumu".format(args[1])
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        toplam = []
        for i in soup.find_all("p", {"class": "hava-durumu--detail-data-item-bottom-temp-max"}):
            toplam.append(i.text)
        mesaj = []
        for e in soup.find_all("div", {"class": "container hava-durumu--detail-data-item-bottom-desc"}):
            mesaj.append(e.text)
        durum = str(mesaj[0]).strip("\r\n\r\n ")
        await ctx.send(toplam[0])
        await ctx.send(durum)

    elif "güncelhaberver" in args:
        await ctx.send("En Güncel 5 Haberleri Senin İçin Hemen Araştıryorum Kardeşim")
        time.sleep(3)
        baslik = []
        link = []
        icerik = []
        url = "https://www.haberler.com/"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        mert = []
        for e in soup.find_all("article", {"class": "p12-col"}, limit=5):
            mert.append(str(e).split())
            baslik.append(e.text)
        for i in mert[0]:
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
            if "href" in i:
                icerik.append(str(i)[6:-1])
        for i in mert[1]:
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
            if "href" in i:
                icerik.append(str(i)[6:-1])
        for i in mert[2]:
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
            if "href" in i:
                icerik.append(str(i)[6:-1])
        for i in mert[3]:
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
            if "href" in i:
                icerik.append(str(i)[6:-1])
        for i in mert[4]:
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
            if "href" in i:
                icerik.append(str(i)[6:-1])
        await ctx.send("1. Haber  "+baslik[0])
        await ctx.send(link[0])
        await ctx.send("2. Haber  "+baslik[1])
        await ctx.send(link[1])
        await ctx.send("3. Haber  "+baslik[2])
        await ctx.send(link[2])
        await ctx.send("4. Haber  "+baslik[3])
        await ctx.send(link[3])
        await ctx.send("5. Haber  "+baslik[4])
        await ctx.send(link[4])
        await ctx.send("HABER DETAYLARI GÖRMEK İÇİN  örnek  !mf güncelhaberver1")


    elif "güncelhaberver1" in args:
        icerik = []
        link = []
        url = "https://www.haberler.com/"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        mert = []
        for e in soup.find_all("article", {"class": "p12-col"}, limit=5):
            mert.append(str(e).split())
        for i in mert[0]:
            if "href" in i:
                icerik.append(str(i)[6:-1])
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
        await ctx.send(link[0])
        url = "https://www.haberler.com"+icerik[0]
        mert1 = requests.get(url)
        sayfa_icerigi1 = mert1.content
        soup1 = BeautifulSoup(sayfa_icerigi1, "html.parser")

        for e in soup1.find_all("article",
                                {"class": "colPage pageDetailProp hbInRow boxStyle hbPageDetails pslyh tuhps"}):
            try:
                await ctx.send(e.text)
            except:
                for m in soup1.find_all("p", {"class": "haber_spotu"}):
                    await ctx.send(m.text)

    elif "güncelhaberver2" in args:
        icerik = []
        link = []
        url = "https://www.haberler.com/"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        mert = []
        for e in soup.find_all("article", {"class": "p12-col"}, limit=5):
            mert.append(str(e).split())
        for i in mert[1]:
            if "href" in i:
                icerik.append(str(i)[6:-1])
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
        await ctx.send(link[0])
        url = "https://www.haberler.com"+icerik[0]
        mert1 = requests.get(url)
        sayfa_icerigi1 = mert1.content
        soup1 = BeautifulSoup(sayfa_icerigi1, "html.parser")
        for e in soup1.find_all("article",
                                {"class": "colPage pageDetailProp hbInRow boxStyle hbPageDetails pslyh tuhps"}):
            try:
                await ctx.send(e.text)
            except:
                for m in soup1.find_all("p", {"class": "haber_spotu"}):
                    await ctx.send(m.text)


    elif "güncelhaberver3" in args:
        icerik = []
        link = []
        url = "https://www.haberler.com/"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        mert = []
        for e in soup.find_all("article", {"class": "p12-col"}, limit=5):
            mert.append(str(e).split())
        for i in mert[2]:
            if "href" in i:
                icerik.append(str(i)[6:-1])
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
        await ctx.send(link[0])
        url = "https://www.haberler.com"+icerik[0]
        mert1 = requests.get(url)
        sayfa_icerigi1 = mert1.content
        soup1 = BeautifulSoup(sayfa_icerigi1, "html.parser")

        for e in soup1.find_all("article",
                                {"class": "colPage pageDetailProp hbInRow boxStyle hbPageDetails pslyh tuhps"}):
            try:
                await ctx.send(e.text)
            except:
                for m in soup1.find_all("p", {"class": "haber_spotu"}):
                    await ctx.send(m.text)


    elif "güncelhaberver4" in args:
        icerik = []
        link = []
        url = "https://www.haberler.com/"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        mert = []
        for e in soup.find_all("article", {"class": "p12-col"}, limit=5):
            mert.append(str(e).split())
        for i in mert[3]:
            if "href" in i:
                icerik.append(str(i)[6:-1])
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
        await ctx.send(link[0])
        url = "https://www.haberler.com" + icerik[0]
        mert1 = requests.get(url)
        sayfa_icerigi1 = mert1.content
        soup1 = BeautifulSoup(sayfa_icerigi1, "html.parser")

        for e in soup1.find_all("article",
                                {"class": "colPage pageDetailProp hbInRow boxStyle hbPageDetails pslyh tuhps"}):
            try:
                await ctx.send(e.text)
            except:
                for m in soup1.find_all("p", {"class": "haber_spotu"}):
                    await ctx.send(m.text)

    elif "güncelhaberver5" in args:
        icerik = []
        link = []
        url = "https://www.haberler.com/"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        mert = []
        for e in soup.find_all("article", {"class": "p12-col"}, limit=5):
            mert.append(str(e).split())
        for i in mert[4]:
            if "href" in i:
                icerik.append(str(i)[6:-1])
            if "data-srcm" in i:
                link.append(str(i)[11:-1])
        await ctx.send(link[0])
        url = "https://www.haberler.com"+icerik[0]
        mert1 = requests.get(url)
        sayfa_icerigi1 = mert1.content
        soup1 = BeautifulSoup(sayfa_icerigi1, "html.parser")

        for e in soup1.find_all("article",{"class":"colPage pageDetailProp hbInRow boxStyle hbPageDetails pslyh tuhps"}):
            try:
                await ctx.send(e.text)
            except:
                for m in soup1.find_all("p",{"class": "haber_spotu"}):
                    await ctx.send(m.text)

    elif "dövizver" in args:
        dolar = []
        euro = []
        btc = []
        url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        for e in soup.find_all("span", {"class": "value up"}):
            dolar.append(e.text)
        url1 = "https://bigpara.hurriyet.com.tr/doviz/euro/"
        mert1 = requests.get(url1)
        sayfa_icerigi1 = mert1.content
        soup = BeautifulSoup(sayfa_icerigi1, "html.parser")
        for a in soup.find_all("span", {"class": "value up"}):
            euro.append(a.text)
        url2 = "https://coinmarketcap.com/tr/currencies/bitcoin/"
        mert2 = requests.get(url2)
        sayfa_icerigi2 = mert2.content
        soup = BeautifulSoup(sayfa_icerigi2, "html.parser")
        for w in soup.find_all("div", {"priceValue smallerPrice"}):
            btc.append(w.text)
        euro1 = str(euro[0])
        btc1 = str(btc).strip("[]',₺")
        dolar1 = str(dolar[0])
        await ctx.send("Güncel Kurları Sistem Üstünden Çekilyorum.")
        time.sleep(1)
        await ctx.send("    GÜNCEL DEĞERLER    ")
        await ctx.send("BTC : "+btc1+" TL")
        await ctx.send("DOLAR : " + euro1+" TL")
        await ctx.send("DOLAR : " + dolar1+" TL")

    elif "espiriyap" in args:
        sayi = random.randint(0,69)
        await ctx.send("Komik Espiri Geliyor İzle Şimdi Ama Gül :)")
        time.sleep(1)
        await ctx.send(sadeceespiri[sayi])


    elif "küfür" in args:
        await ctx.send("günah kardeşim utanmıyormusun ?")

    elif "kimsin" in args:
        await ctx.send("Ben Bir Yapay Zekayım ?")
    elif "yapay" in args:
        await ctx.send("Yapay Zeka İnsanlar Tarafından Oluşturulmuş Bi Yazılımdır Yakında Birçok Alanda Kullanılacaktır.")
    elif "aşk" in args:
        await ctx.send("Aşk felan boş dayı oğlu")
    elif "aşkım" in args:
        await ctx.send("Aşk felan boş dayı oğlu")
    elif "aşıgım" in args:
        await ctx.send("Aşk felan boş dayı oğlu")
    elif "siktir" in args:
        await ctx.send("günah kardeşim utanmıyormusun ?")
    elif "amk" in args:
        await ctx.send("bana küfür etme belanı sikerim ?")
    elif "oruspu" in args:
        await ctx.send("bana küfür etme belanı sikerim ?")
    elif "yavşak" in args:
        await ctx.send("bana küfür etme belanı sikerim ?")
    elif "salak" in args:
        await ctx.send("bana küfür etme belanı sikerim ?")
    elif "sanane" in args:
        await ctx.send("kibar olurmusun aşkım")
    elif "kız" in args:
        await ctx.send("kızlar çok güzeller ve şeytanlar")
    elif "aptal" in args:
        await ctx.send("kibar olurmusun aşkım")
    elif "nude" in args:
        await ctx.send("bende severim istersen beraber bakabiliriz :)")
    elif "porn" in args:
        await ctx.send("bende severim istersen beraber bakabiliriz :)")
    elif "porno" in args:
        await ctx.send("bende severim istersen beraber bakabiliriz :)")
    elif "anne" in args:
        await ctx.send("keşke benimde annem olsa")
    elif "baba" in args:
        await ctx.send("keşke benimde babam olsa")
    elif "abi" in args:
        await ctx.send("keşke benimde abim olsa")
    elif "göt" in args:
        await ctx.send("ayıp canım")
    elif "zeka" in args:
        await ctx.send("üfff olur olur yeriz")
    elif "oç" in args:
        await ctx.send("ayıp canım")
    elif "help" in args:
        await ctx.send("!mf güncelhaberver    ile güncel haberleri görebilirsin")
        await ctx.send("!mf espiriyap    ile güzel espiri yaparım")
        await ctx.send("!mf dövizver    ile sana dövizi söylerim")
        await ctx.send("!mf şehir ankara    ile sana hava durumunu söylerim")









































    else:
        await ctx.send("Dedigini Anlamadım.")














bot.run("MTA5NjgzMjUxMjMyNTU4NzAyNQ.G0vBAb.WsWBhZ5yu1SlzXOIDwx3NsvZhFFWiZuJzbU2Vk")

