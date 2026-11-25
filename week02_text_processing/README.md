# Hafta 2 — Metin İşleme ve Tokenizasyon

> Bir dize nasıl tamsayı dizisine dönüşür? Boşluğa göre bölmeyle başlıyor, ardından her modern alt sözcük algoritmasını adım adım yeniden kuruyoruz: BPE, WordPiece, Unigram (SentencePiece).

## Öğrenme Hedefleri

- Karakter, sözcük ve alt sözcük düzeyinde tokenizasyon arasındaki ödünleşimleri açıklamak.
- BPE'yi sıfırdan uygulamak ve gerçek bir derlem üzerinde eğitmek.
- WordPiece'i (olabilirlik tabanlı birleştirme ölçütü) ve EM ile Unigram dil modelini uygulamak.
- Sıfırdan yazılmış bir tokenizer'ı hız ve sıkıştırma oranı açısından `tokenizers` ile kıyaslamak.

## Zorunlu Okumalar

- Sennrich, R., Haddow, B. ve Birch, A. (2016). *Neural Machine Translation of Rare Words with Subword Units*.
- Kudo, T. (2018). *Subword Regularization*.
- Schuster, M. ve Nakajima, K. (2012). *Japanese and Korean Voice Search*.

## Not Defteri

[`02_tokenization.ipynb`](02_tokenization.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
