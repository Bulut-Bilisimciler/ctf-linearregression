### Scikit-Learn Kütüphanesi ile Lineer Regresyon Modeli Oluşturma

Bu CTF senaryosunda sizlerden Makine Öğrenmesi alanında en yaygın kullanılan Python kütüphanelerinden biri olan Scikit-Learn kütüphanesini kullanarak, sizlere sağladığımız verilerle eğitilmiş bir Lineer Regresyon modeli oluşturmanız beklenmektedir. 

Senaryo kapsamında sizlerden;
* atanan makinelere gerekli kurulumları yapmanızı,
* Sizler için hazırladığımız veri setini indirmenizi,
* Scikit-Learn kütüphanesini kullanarak bu veriler ile bir Lineer regresyon modeli eğitmenizi ve 
* Teste hazır hale gelen modelinizi export etmenizi bekliyoruz.

### Talimatlar 


- Sizlere atanan [Alpine Linux](https://alpinelinux.org/) makinesi üzerine apk komutları ile Python kurulumu yapmalısınız.
- Python kurulumu sonrasında, en yaygın kullanılan ve Python yüklemeniz sonrası aktive olan 'pip' paket yöneticisinin komutları ile çalışma boyunca ihtiyaç duyacağınız Python kütüphanelerini yüklemelisiniz. Gerekli kütüphaneler aşağıdaki gibidir.
  - scikit-learn
  - pickle
  - numpy
  - pandas
  - json
  - requests
  
- Eğitim için sizlere sağladığımız verisetlerini 'git clone' komutu ile **https://github.com/Bulut-Bilisimciler/ctf-regression-traindata.git** adresinden **/home** dizininize klonlamalısınız.

<!---
Servisle alakalı yapılacak dönüşe göre burası düzenlenecek. Train datasını makinenin içinde kurulu verip test scriptini verify.json ile ayağa kaldırırsak test datasının klonlanma kısmını direkt olarak servisin içine de gömebiliriz.
-->

- Git clone ile download ettiğiniz 'train.csv' dosyasını kullanarak model eğitiminizi tamamlayınız.
  

```bash
# İPUCU: Verinin ve değişken isimlerinin incelenmesi

import pandas as pd
data = pd.read_csv('example_data.csv')
data.head()
```

- Model eğitimi için yazacağınız Python scripti/app'inde eğittiğiniz modeli 'Pickle' kütüphanesini kullanarak home dizininize Export etmeyi unutmamalısınız.


```bash
# İPUCU: Pickle ile modelin kayıt işlemi

import pickle
with open('/home/linear_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)
```
- Bütün işlemleri yerine getirdikten sonra kontrol işlemleri için "Kontrol Et" butonuna basınız ve senaryoyu tamamlayınız.


### Yardımcı Kaynaklar  

- [apk](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management)  
- [pip](https://pip.pypa.io/en/stable/getting-started/)
- [Scikit-Learn](https://scikit-learn.org/stable/index.html)  