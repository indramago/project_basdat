from Models import jenis_acc_model


class JenisAccView:
    def __init__(self):
        self.model = jenis_acc_model.JenisAccModel()
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
        id_merk_hp = int(input("Id Merk Acc: "))
        nama_jenis_acc = input("Nama Jenis Acc: ")
        data = (id_merk_hp, nama_jenis_acc)
        self.model.insert(data)

    def _update(self):
        id_jenis_acc = int(input("Id Jenis Acc"))
        id_merk_acc = int(input("Id Merk Acc: "))
        nama_jenis_acc = input("Nama Jenis Acc: ")
        data = (id_jenis_acc, id_merk_hp, nama_jenis_acc)
        self.model.update(data)

    def _delete(self):
        id_acc_hp = int(input("ID Jenis Acc: "))
        self.model.delete(id_acc_hp)

    def _show(self):
        for data in self.model.get_data():
            print("|{}.| {} | {} | ".format(data[0], data[1], data[2]))
