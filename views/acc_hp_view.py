from Models import acc_hp_model


class AccHpView:
    def __init__(self):
        self.model = acc_hp_model.AccHpModel()
        pass

    def display(self):
        while True:
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Show")
            print("5. Back")
            match (int(input("Pilih menu: "))):
                case 1:
                    self._insert()
                case 2:
                    self._update()
                case 3:
                    self._delete()
                case 4:
                    self._show()
                case 5:
                    return
                case _:
                    print("Menu tidak tersedia")

    def _insert(self):
        id_jenis_acc = int(input("Id Jenis Acc: "))
        id_type_hp = int(input("Id Type Hp: "))
        nama_acc = input("Nama Acc: ")
        stok_acc = int(input("Stok Acc: "))
        data = (id_jenis_acc, id_type_hp, nama_acc, stok_acc)
        self.model.insert(data)

    def _update(self):
        id_acc_hp = int(input("ID Acc Hp: "))
        id_jenis_acc = int(input("Id Jenis Acc: "))
        id_type_hp = int(input("Id Type Hp: "))
        nama_acc = input("Nama Acc: ")
        stok_acc = int(input("Stok Acc: "))
        data = (id_acc_hp, id_jenis_acc, id_type_hp, nama_acc, stok_acc)
        self.model.update(data)

    def _delete(self):
        id_acc_hp = int(input("ID Acc Hp: "))
        self.model.delete(id_acc_hp)

    def _show(self):
        for data in self.model.get_data():
            print("|{}.| {} | {} | {} | {} |".format(data[0], data[1], data[2], data[3], data[4]))
