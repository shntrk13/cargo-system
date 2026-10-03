total_gain = 0
total_post = 0
post_list = []


def new_post():  # fonksiyonların yanına () koymayı unutma!!
    global total_post  # dışarıda oluşturulan total post değişkenini kullanmak için
    global total_gain
    name = input("Adınız: ")
    city = input("Şehir: ")
    package_weight = int(input("Paket ağırlığı: "))
    package_lenght = int(input("Paket uzunluğu: "))
    package_width = int(input("Paket genişliği: "))
    package_height = int(input("Paket yüksekliği: "))
    delivery_type = input("Teslimat Tipi(Standart Teslimat/Hızlı Teslimat): ")
    package_type = ""
    volume = package_lenght * package_width * package_height

    if volume >= 0 and volume <= 10000:
        package_type = "Küçük Paket"
    elif volume >= 10001 and volume <= 30000:
        package_type = "Orta Paket"
    elif volume < 0:
        print("That's not possible")
    else:
        package_type = "Büyük Paket"

    package_price = 0

    if package_type == "Küçük Paket":
        package_price = 0
    elif package_type == "Orta Paket":
        package_price = 40
    elif package_type == "Büyük Paket":
        package_price = 80

    cargo_price = 0

    if package_weight < 0:
        print("That's not possible!")
    elif package_weight >= 0 and package_weight <= 2:
        cargo_price = 100
    elif package_weight <= 5:
        cargo_price = 150
    elif package_weight <= 10:
        cargo_price = 220
    else:
        cargo_price = 300 + (package_weight - 10) * 20

    city_price = 0
    if city == "Ankara":
        city_price = 0
    elif city == "İstanbul":
        city_price = 50
    elif city == "İzmir":
        city_price = 70
    elif city == "Antalya":
        city_price = 80
    elif city == "Trabzon":
        city_price = 100
    else:
        city_price = 120

    total = package_price + cargo_price + city_price
    delivery_price = 0
    if delivery_type == "Hızlı Teslimat":
        delivery_price = total * 0.3
        total += total * 0.3

    discount = 0
    if total >= 500:
        discount = total * 0.1
        total -= total * 0.1
    elif total > 300:
        discount = total * 0.05
        total -= total * 0.05

    info = {
        "customer": name,
        "city": city,
        "weight": package_weight,
        "package": package_type,
        "delivery": delivery_type,
        "total price": total,
    }

    post_list.append(info)
    total_post += 1
    total_gain += total

    return print(
        f"============================== \nGönderi Özeti \n=============================="
        + f"\nMüsteri : {name} \nŞehir: {city} \nAğırlık: {package_weight} \nPaket: {package_type} \nTeslimat :{delivery_type}"
        + f"\nTemel Ücret: {cargo_price}TL \nMesafe Ücreti: {city_price}TL \nPaket Ücreti: {package_price}TL \nHızlı Teslimat: {delivery_price}TL \nİndirim:{discount}TL"
        + f"\nToplam: {total} TL"
    )


def list_post():
    if total_post == 0 or total_post < 0:
        print("There is not post!")
    else:
        for i, post in enumerate(post_list, start=1):
            print(f"{i}. Gönderi")
            print(f"Müşteri: {post['customer']}")
            print(f"Şehir: {post['city']}")
            print(f"Paket: {post['package']}")
            print(f"Ücret: {post['total price']} TL")
            print("--------------------")


def rapor():
    print("==============================")
    print("Gün Sonu Raporu")
    print("==============================")
    print(f"Toplam Gönderi: {total_post}")
    print(f"Toplam Kazanç: {total_gain} TL")

    standart = 0
    fast = 0
    small = 0
    medium = 0
    large = 0
    for i, post in enumerate(post_list, start=1):
        if post["delivery"] == "Standart Teslimat":
            standart += 1
        else:
            fast += 1

        if post["package"] == "Küçük Paket":
            small += 1
        elif post["package"] == "Orta Paket":
            medium += 1
        elif post["package"] == "Büyük Paket":
            large += 1

    print(f"Standart Teslimat: {standart}")
    print(f"Hızlı Teslimat: {fast}")
    print(f"Küçük Paket: {small}")
    print(f"Orta Paket: {medium}")
    print(f"Büyük Paket: {large}")
    average_post_price = 0
    if total_gain <= 0:
        average_post_price = 0
    else:
        average_post_price = total_gain / total_post

    print(f"Ortalama Gönderi Ücreti:{average_post_price} ")

    max = 0
    for post in post_list:
        if post["total price"] > max:
            max = post["total price"]

    print(f"En Pahalı Gönderi: {max} ")


while True:
    print("==============================")
    print("         HIZLI KARGO")
    print("==============================")

    print("1-Yeni Gönderi Oluştur.")
    print("2-Gönderileri Listele")
    print("3-Gün Sonu Raporu")
    print("4- Çıkış")
    choose = int(input("Seçiminiz: "))
    if choose == 1:
        new_post()
    elif choose == 2:
        list_post()
    elif choose == 3:
        rapor()
    elif choose == 4:
        break
    else:
        print("There are not this option")
