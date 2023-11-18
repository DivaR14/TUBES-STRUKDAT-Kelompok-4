import streamlit as st

class Node:
    def __init__(self, key, terjemahan, gimmick, gimmick2):
        self.key = key
        self.terjemahan = terjemahan
        self.gimmick = gimmick
        self.gimmick2 = gimmick2
        self.parent = None
        self.right = None
        self.left = None
        self.color = 0

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, None, None, None)
        self.nil.color = 1
        self.root = self.nil
        self.number_of_nodes = 0

    def search(self, key):
        # Implementasi metode pencarian seperti sebelumnya
        node = self.root

        while node != self.nil:  # as long as we didn't reach the end of the tree
            if node.key == key:
                return node.terjemahan
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def search1(self, key):
        # Implementasi metode pencarian seperti sebelumnya
        key_lower = str(key).lower()
        node = self.root

        while node != self.nil:  # as long as we didn't reach the end of the tree
            if node.terjemahan.lower() == key.lower():
                return node.key
            elif key < node.terjemahan:
                node = node.left
            else:
                node = node.right
        return False

    def search2(self, key):
        # Implementasi metode pencarian seperti sebelumnya
        node = self.root

        while node != self.nil:  # as long as we didn't reach the end of the tree
            if node.key == key:
                return node.gimmick
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def search3(self, key):
        # Implementasi metode pencarian seperti sebelumnya
        node = self.root

        while node != self.nil:  # as long as we didn't reach the end of the tree
            if node.terjemahan == key:
                return node.gimmick2
            elif key < node.terjemahan:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, key, terjemahan, gimmick, gimmick2):
        # Implementasi metode insert seperti sebelumnya
            newNode = Node(str(key).lower(), str(terjemahan).lower(), str(gimmick).lower(), str(gimmick2).lower())
            newNode.left = self.nil
            newNode.right = self.nil
            node = self.root
            parent = None

            while node != self.nil:
                parent = node
                if newNode.key < node.key:
                    node = node.left
                else:
                    node = node.right
            newNode.parent = parent

            if parent is None:
                newNode.color = 1
                self.root = newNode
                self.number_of_nodes += 1
                return
            elif newNode.key < parent.key:
                parent.left = newNode
            else:
                parent.right = newNode

            if newNode.parent.parent is None:
                self.number_of_nodes += 1
                return

            self.insertFix(newNode)
            self.number_of_nodes += 1

    def insertFix(self, newNode):
        # Implementasi metode insertFix seperti sebelumnya
        while newNode != self.root and newNode.parent.color == 0:  # Loop until we reach the root or parent is black

            parentIsLeft = False  # Parent is considered left child by default

            # Assign uncle to appropriate node
            if newNode.parent == newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                parentIsLeft = True
            else:
                uncle = newNode.parent.parent.left

            # Case 1: Uncle is red -> Reverse colors of uncle, parent and grandparent
            if uncle.color == 0:
                newNode.parent.color = 1
                uncle.color = 1
                newNode.parent.parent.color = 0
                newNode = newNode.parent.parent

            # Case 2: Uncle is black -> check triangular or linear and rotate accordingly
            else:
                # Left-right condition (triangular)
                if parentIsLeft and newNode == newNode.parent.right:
                    newNode = newNode.parent  # Take care as we made the new node the parent
                    self.leftRotate(newNode)
                # Right-Left condition (triangular)
                elif not parentIsLeft and newNode == newNode.parent.left:
                    newNode = newNode.parent
                    self.rightRotate(newNode)
                # Left-left condition (linear)
                if parentIsLeft:
                    newNode.parent.color = 1  # the new parent
                    newNode.parent.parent.color = 0  # the new grandparent will be red
                    self.rightRotate(newNode.parent.parent)
                # Right-right condition (linear)
                else:
                    newNode.parent.color = 1
                    newNode.parent.parent.color = 0
                    self.leftRotate(newNode.parent.parent)

        self.root.color = 1  # Set root to black

    def leftRotate(self, node):
        # Implementasi metode leftRotate seperti sebelumnya
        y = node.right
        node.right = y.left  # connect node to c
        if y.left != self.nil:  # connect c to node
            y.left.parent = node

        y.parent = node.parent  # connect y to node's parent

        if node.parent is None:  # connect node's parent to y
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node  # connect y to node
        node.parent = y  # connect node to y

    def rightRotate(self, node):
        # Implementasi metode rightRotate seperti sebelumnya

        y = node.left
        node.left = y.right  # connect node to d
        if y.right != self.nil:  # connect d to node
            y.right.parent = node
        y.parent = node.parent  # connect y to node's parent

        if node.parent is None:  # connect b parent to a's parent
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node  # connect y to node
        node.parent = y  # connect node to y

rbt = RedBlackTree()
rbt.insert("apel", "apple", "Apel berasal dari pohon buah apel yang dikenal sebagai Malus domestica. Pohon ini berasal dari wilayah Asia Tengah.", "The largest apple production usually comes from countries such as China, the United States, and Poland.")
rbt.insert("mobil", "car", "Mobil tercepat yang pernah dibuat adalah Bugatti Chiron Super Sport 300+, yang mencapai kecepatan 304 mph (sekitar 490 km/jam) pada tahun 2019.", "Karl Benz is considered the inventor of the modern car. In 1886, he built the first gasoline-powered car called the Benz Patent-Motorwagen.")
rbt.insert("buku", "book", "Buku telah menjadi sumber pengetahuan dan informasi utama selama berabad-abad. Mereka menjadi jendela ke dunia pengetahuan dan cerita.","The first books were printed using a printing press by Johannes Gutenberg in the 1440s. Prior to that, books were produced manually.")

# rbt.insert("ikan", "fish", "Cara reproduksi ikan bervariasi. Beberapa ikan bertelur, sementara yang lain melahirkan anak secara langsung. Ada juga ikan yang melakukan migrasi panjang untuk bertelur.","Some fish species communicate through body movements and sounds. This can include fin movements or sounds produced by air bubbles.")
# rbt.insert("kucing", "cat", "Kucing adalah hewan pemakan daging (carnivora). Sistem pencernaannya dirancang khusus untuk mencerna daging, dan kebanyakan nutrisi yang mereka butuhkan berasal dari protein hewani.","Cats have an incredible jumping ability. Some cats can jump up to five times their body height to catch prey or reach higher places")
# rbt.insert("hati", "heart", "Hati berperan dalam detoksifikasi, yaitu membersihkan dan menghilangkan zat-zat beracun dari tubuh.","The liver is a vital organ in the human body, located in the upper abdomen on the right side.")
# rbt.insert("sepatu", "shoes", "Sejarah penggunaan sepatu dapat ditelusuri kembali ribuan tahun. Awalnya, sepatu dibuat sederhana untuk melindungi kaki, dan seiring waktu, desain dan fungsi sepatu berkembang.","Shoes are designed to provide protection for the feet from environmental elements like soil, rocks, and weather, as well as to offer support during walking")
# rbt.insert("bola", "ball", "Bola umumnya terbuat dari berbagai bahan, seperti kulit, karet, PVC, atau bahan sintetis. Jenis bahan dapat memengaruhi kemampuan bola dan kenyamanan pemain.","There are various types of balls used in different sports, including soccer balls, basketballs, volleyballs, tennis balls, and many more, each with different sizes, weights, and textures")
# rbt.insert("meja", "table", "Meja dapat terbuat dari berbagai bahan, termasuk kayu, logam, kaca, atau campuran bahan-bahan tersebut. Pilihan bahan dapat mempengaruhi penampilan, daya tahan, dan harga meja.","Tables are pieces of furniture designed to provide a flat surface and support various activities, such as working, dining, or writing.")
# rbt.insert("awan", "cloud", "Awan memainkan peran penting dalam siklus air. Mereka dapat berkondensasi dan membentuk titik-titik air yang kemudian jatuh sebagai hujan atau salju.","There are various types and shapes of clouds, including cirrus (high and thin clouds), cumulus (puffy and white clouds), and stratus (low, overcast clouds).")


def main():
    st.title("Aplikasi Penerjemah Sederhana")

    menu_option = st.sidebar.radio("Pilih Opsi:", ["Translasi Indonesian -> English", "Translasi English -> Indonesian"])

    if menu_option == "Translasi Indonesian -> English":
        translate_indo_to_eng()
    elif menu_option == "Translasi English -> Indonesian":
        translate_eng_to_indo()
    # elif menu_option == "Tambah Kata Kunci":
    #     add_keyword()

def translate_indo_to_eng():
    kata_kunci = st.text_input("Masukkan kata kunci yang ingin diterjemahkan:").lower()
    if st.button("Terjemahkan"):
        terjemahan = rbt.search(kata_kunci)
        gimmick = rbt.search2(kata_kunci)
        if rbt.search(kata_kunci) is False:
            st.warning("Kata kunci tidak ditemukan dalam kamus.")
        elif terjemahan:
            st.success(f"Terjemahan dari {kata_kunci} adalah {terjemahan}")
            st.write(gimmick)

def translate_eng_to_indo():
    kata_kunci = st.text_input("Masukkan kata kunci yang ingin diterjemahkan:").lower()
    if st.button("Terjemahkan"):
        terjemahan = rbt.search1(kata_kunci)
        gimmick2 = rbt.search3(kata_kunci)
        if rbt.search1(kata_kunci) is False:
            st.warning("Kata kunci tidak ditemukan dalam kamus.")
        elif terjemahan:
            st.success(f"Terjemahan dari {kata_kunci} adalah {terjemahan}")
            st.write(gimmick2)

if __name__ == "__main__":
    main()
