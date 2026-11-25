# Hafta 5 — Dil Modelleme: n-gramlardan Sinirsel Modellere

> Dil modelleme görevini biçimselleştiriyor, perpleksiteyi tanımlıyor ve sayım tabanlı n-gramlardan ileri beslemeli sinirsel dil modellerine (Bengio vd., 2003) uzanan mimari evrimi izliyoruz.

## Öğrenme Hedefleri

- Bir dil modelini biçimsel olarak tanımlamak ve olasılığın zincir kuralıyla ilişkilendirmek.
- Perpleksiteyi çapraz entropiden türetmek ve yorumlama ölçeğini açıklamak.
- Kneser–Ney yumuşatmalı bir n-gram dil modeli uygulamak.
- Bengio (2003) sinirsel dil modelini PyTorch ile uygulamak, aynı test akışında n-gram modeliyle karşılaştırmak ve sinirsel modelin üstünlüğünün hangi koşullarda ortaya çıktığını tartışmak.

## Zorunlu Okumalar

- Bengio, Y., Ducharme, R., Vincent, P. ve Jauvin, C. (2003). *A Neural Probabilistic Language Model*.
- Jurafsky ve Martin, Bölüm 3 ve 7.

## Not Defteri

[`05_language_models.ipynb`](05_language_models.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
