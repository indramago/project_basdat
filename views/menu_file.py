from views import acc_hp_view
from views import jenis_acc_view
from views import merk_acc_view
from views import transaction_view
from views import type_hp_view


class MenuView:
    def __init__(self):
        self.accView = acc_hp_view.AccHpView()
        self.jenisView = jenis_acc_view.JenisAccView()
        self.merkView = merk_acc_view.MerkAccView()
        self.typeView = type_hp_view.TypeHpView()
        self.transactionView = transaction_view.TransactionView()

    def menu(self):
        while True:
            print("")
            print("Menu")
            print("1. Acc Hp")
            print("2. Jenis Acc Hp")
            print("3. Merk Acc Hp")
            print("4. Type Hp")
            print("5. Transaksi")
            print("6. Exit")
            match int(input("Masukkan Pilihan Anda : ")):
                case 1:
                    self.accView.display()
                case 2:
                    self.jenisView.display()
                case 3:
                    self.merkView.display()
                case 4:
                    self.typeView.display()
                case 5:
                    self.transactionView.display()
                case 6:
                    break
                case _:
                    print("Masukkan Tidak Benar")
