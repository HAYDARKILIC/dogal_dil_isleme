# Hafta 4 — Dağıtık Sözcük Temsilleri

> Seyrek sayımlardan yoğun vektörlere. word2vec'i (negatif örneklemeli skip-gram), GloVe'u ve fastText'i her birini sıfırdan uyguluyoruz.

## Öğrenme Hedefleri

- Negatif örneklemeli skip-gram (SGNS) hedefini türetmek ve bunun kaydırılmış bir PMI matrisini çarpanlarına ayırmaya eşdeğer olduğunu kanıtlamak (Levy ve Goldberg, 2014).
- SGNS'yi elle gradyan hesaplayarak NumPy ile uygulamak.
- GloVe'u uygulamak ve hedefinin neden ağırlıklı en küçük kareler matris çarpanlarına ayırma olduğunu açıklamak.
- Gömmeleri içsel (analoji, benzerlik) ve dışsal (sınıflandırma) olarak değerlendirmek.

## Zorunlu Okumalar

- Mikolov, T. vd. (2013). *Distributed Representations of Words and Phrases and Their Compositionality*.
- Pennington, J., Socher, R. ve Manning, C. D. (2014). *GloVe: Global Vectors for Word Representation*.
- Levy, O. ve Goldberg, Y. (2014). *Neural Word Embedding as Implicit Matrix Factorization*.
- Bojanowski, P. vd. (2017). *Enriching Word Vectors with Subword Information*.

## Not Defteri

[`04_word_embeddings.ipynb`](04_word_embeddings.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
