# Hafta 7 — Diziden Diziye Modeller ve Dikkat

> Kodlayıcı–kod çözücü paradigması ve onun darboğazını kıran dikkat mekanizması. Bu, Transformer'a giden kavramsal köprüdür.

## Öğrenme Hedefleri

- Oyuncak bir çeviri görevi için LSTM tabanlı bir seq2seq modeli uygulamak.
- Sade seq2seq'in bilgi darboğazı başarısızlığını deneysel olarak belirlemek.
- Bahdanau (toplamsal) ve Luong (çarpımsal) dikkati türetmek ve uygulamak.
- Dikkat ısı haritalarını görselleştirmek ve dilbilimsel olarak yorumlamak.

## Zorunlu Okumalar

- Sutskever, I., Vinyals, O. ve Le, Q. V. (2014). *Sequence to Sequence Learning with Neural Networks*.
- Bahdanau, D., Cho, K. ve Bengio, Y. (2015). *Neural Machine Translation by Jointly Learning to Align and Translate*.
- Luong, M.-T., Pham, H. ve Manning, C. D. (2015). *Effective Approaches to Attention-based Neural Machine Translation*.

## Not Defteri

[`07_seq2seq_attention.ipynb`](07_seq2seq_attention.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
