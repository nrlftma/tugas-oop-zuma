
class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru

    def tembak(self, warna_sama):
        print("Katak menembakkan bola!")
        if warna_sama >= 2:
            self.skor += 50
            print("Skor bertambah 50 poin.")
        else:
            print("Skor tidak bertambah.")

    def info_status(self):
        print("=== STATUS KATAK ZUMA ===")
        print("Warna peluru:", self.warna_peluru)
        print("Skor:", self.skor)
        print("Status aktif:", self.is_active)


# UJI COBA PROGRAM

katak_player = KatakZuma("Kuning")
katak_player.info_status()
katak_player.ganti_warna("Merah")
katak_player.tembak(2)
katak_player.tembak(1)
katak_player.info_status()
