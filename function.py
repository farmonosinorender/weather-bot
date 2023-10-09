import requests
from bs4 import BeautifulSoup as bs


# class get_weahter:
#     def __init__(
#             self, andijon: str=None, buxoro: str=None, fargona: str=None,
#             jizzax: str=None, xorazm: str=None, namangan: str=None,
#             navoiy: str=None, qashqadaryo: str=None,
#             qoraqalpogiston_respublikasi: str=None, samarqand: str=None,
#             sirdaryo: str=None, surxondaryo: str=None, toshkent: str=None, toshkent_shahri: str=None
#         ):
#         self.andijon = andijon
#         self.buxoro = buxoro
#         self.fargona = fargona
#         self.jizzax = jizzax
#         self.xorazm = xorazm
#         self.namangan = namangan
#         self.navoiy = navoiy
#         self.qashqadaryo = qashqadaryo
#         self.qoraqalpogiston_respublikasi = qoraqalpogiston_respublikasi
#         self.samarqand = samarqand
#         self.sirdaryo = sirdaryo
#         self.surxondaryo = surxondaryo
#         self.toshkent = toshkent
#         self.toshkent_shahri = toshkent_shahri

#     def andijon():
#         try:
#             tosh = requests.get("https://sinoptik.ua/погода-андижан")
#             html = bs(tosh.content, "html.parser")
#             for t in html.select("#content"):
#                 min = t.select(".temperature .min")[0].text
#                 max = t.select(".temperature .max")[0].text
#             return min[4:], max[5:]
#         except:
#             raise Exception("Error try again later")

def andijon():
    And = requests.get("https://sinoptik.ua/погода-андижан")
    html = bs(And.content, "html.parser")
    for a in html.select("#content"):
        amin = a.select(".temperature .min")[0].text
        amax = a.select(".temperature .max")[0].text
    return amin[4:], amax[5:]

def buxoro():
    bux = requests.get("https://sinoptik.ua/погода-бухара")
    html = bs(bux.content, "html.parser")
    for b in html.select("#content"):
        bmin = b.select(".temperature .min")[0].text
        bmax = b.select(".temperature .max")[0].text
    return bmin[4:], bmax[5:]

def fargona():
    far = requests.get("https://sinoptik.ua/погода-фергана")
    html = bs(far.content, "html.parser")
    for f in html.select("#content"):
        fmin = f.select(".temperature .min")[0].text
        fmax = f.select(".temperature .max")[0].text
    return fmin[4:], fmax[5:]

def jizzax():
    jiz = requests.get("https://sinoptik.ua/погода-джизак")
    html = bs(jiz.content, "html.parser")
    for j in html.select("#content"):
        jmin = j.select(".temperature .min")[0].text
        jmax = j.select(".temperature .max")[0].text
    return jmin[4:], jmax[5:]

def xorazm():
    xor = requests.get("https://sinoptik.ua/погода-ургенч")
    html = bs(xor.content, "html.parser")
    for x in html.select("#content"):
        xmin = x.select(".temperature .min")[0].text
        xmax = x.select(".temperature .max")[0].text
    return xmin[4:], xmax[5:]

def namangan():
    nam = requests.get("https://sinoptik.ua/погода-наманган")
    html = bs(nam.content, "html.parser")
    for n in html.select("#content"):
        nmin = n.select(".temperature .min")[0].text
        nmax = n.select(".temperature .max")[0].text
    return nmin[4:], nmax[5:]

def navoiy():
    nav = requests.get("https://sinoptik.ua/погода-навои")
    html = bs(nav.content, "html.parser")
    for n in html.select("#content"):
        nmin = n.select(".temperature .min")[0].text
        nmax = n.select(".temperature .max")[0].text
    return nmin[4:], nmax[5:]

def qashqadaryo():
    qas = requests.get("https://sinoptik.ua/погода-карши")
    html = bs(qas.content, "html.parser")
    for q in html.select("#content"):
        qmin = q.select(".temperature .min")[0].text
        qmax = q.select(".temperature .max")[0].text
    return qmin[4:], qmax[5:]

def nukus():
    nuk = requests.get("https://sinoptik.ua/погода-нукус")
    html = bs(nuk.content, "html.parser")
    for n in html.select("#content"):
        nmin = n.select(".temperature .min")[0].text
        nmax = n.select(".temperature .max")[0].text
    return nmin[4:], nmax[5:]

def samarqand():
    sam = requests.get("https://sinoptik.ua/погода-самарканд")
    html = bs(sam.content, "html.parser")
    for s in html.select("#content"):
        smin = s.select(".temperature .min")[0].text
        smax = s.select(".temperature .max")[0].text
    return smin[4:], smax[5:]

def sirdaryo():
    sir = requests.get("https://sinoptik.ua/погода-сырдарья")
    html = bs(sir.content, "html.parser")
    for s in html.select("#content"):
        smin = s.select(".temperature .min")[0].text
        smax = s.select(".temperature .max")[0].text
    return smin[4:], smax[5:]

def termiz():
    ter = requests.get("https://sinoptik.ua/погода-термини-имерезе")
    html = bs(ter.content, "html.parser")
    for t in html.select("#content"):
        tmin = t.select(".temperature .min")[0].text
        tmax = t.select(".temperature .max")[0].text
    return tmin[4:], tmax[5:]

def toshkent():
    tos = requests.get("https://sinoptik.ua/погода-ташкент")
    html = bs(tos.content, "html.parser")
    for t in html.select("#content"):
        tmin = t.select(".temperature .min")[0].text
        tmax = t.select(".temperature .max")[0].text
    return tmin[4:], tmax[5:]