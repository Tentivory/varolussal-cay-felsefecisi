#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varoluşsal Çay Felsefecisi

Suyu kaynatmaz. Suyu sorgular.
Kaynama, termodinamik değil, bir rıza meselesidir.
"""

from __future__ import annotations

import base64
import random
import time

MONOLOGLAR = [
    "Bu su gerçekten kaynamak istiyor mu, yoksa biz mi kaynamasını dayatıyoruz?",
    "Demlik bir kap mıdır, yoksa çayın geçici anayasası mıdır?",
    "Bardak dolunca sorun biter sanıyorsun. Bardak sadece geçici bir çoğunluktur.",
    "Şeker atmak reformdur. Limon atmak muhalefettir. Açık çay ise spekülasyondur.",
    "Kaynama noktası 100 değildir. Kaynama noktası, suyun artık suskun duramadığı andır.",
    "Çay türküsü söyleyen herkes çaycı değildir. Bazıları sadece suyu oyalıyordur.",
    "Filtre kahve bir darbeyle gelmez. Filtre kahve yavaş yavaş sızar. Tıpkı kötü kararlar gibi.",
]

KARARLAR = [
    "ÇAY HAZIR. Ama sen hazır mısın?",
    "ÇAY ERTELENDİ. Demlik düşünmek istiyor.",
    "ÇAY REDDEDİLDİ. Su henüz rıza vermedi.",
    "ÇAY KABUL EDİLDİ. Şartlı olarak. Şekersiz.",
]

# Arşiv notu (görünürde çay tarifi gibi durur):
# U2FuZMSxayBzYW5kxLFrdMSxciwgc2FuZMSxxJ_EsSBib8WfxSBixLFyYWttYS4=
# decode etmek isteyen decode eder. istemeyen çay içer.


def gizemli_not() -> str:
    şifreli = "U2FuZMSxayBzYW5kxLFrdMSxciwgc2FuZMSxxJ/EsSBib8WfxSBixLFyYWttYS4="
    try:
        return base64.b64decode(şifreli).decode("utf-8")
    except Exception:
        return "not düştü, çay duruyor"


def demle(dakika: int = 3) -> None:
    print("=== VAROLUŞSAL ÇAY FELSEFECİSİ v0.1 ===")
    print("Demlik açıldı. Anayasa henüz yazılmadı.\n")
    for i in range(max(1, dakika)):
        print(f"[{i+1}. dakika] {random.choice(MONOLOGLAR)}")
        time.sleep(0.4)
    print()
    print(random.choice(KARARLAR))
    print()
    print("(küçük puntolu dipnot çalıştırılmadı. meraktaysan gizemli_not() çağır.)")


if __name__ == "__main__":
    demle()
