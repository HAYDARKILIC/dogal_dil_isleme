# Hafta 6 — Yinelemeli Mimariler: RNN, LSTM, GRU

> Temel ilkelerden sıralı modeller. Zaman içinde geri yayılımı türetiyor, kaybolan gradyan problemini analitik olarak teşhis ediyor ve LSTM ile GRU hücrelerini sıfırdan kuruyoruz.

## Öğrenme Hedefleri

- Basit bir RNN için BPTT'yi elle türetmek ve kaybolan gradyanların kaynağını belirlemek.
- Kaybolan gradyan teoremini ifade etmek ve göstermek (Bengio, Simard, Frasconi, 1994).
- Bir LSTM hücresini elle türetilmiş gradyanlarla NumPy'da sıfırdan uygulamak.
- Shakespeare üzerinde karakter düzeyinde bir RNN eğitmek ve örnekler üretmek.

## Zorunlu Okumalar

- Hochreiter, S. ve Schmidhuber, J. (1997). *Long Short-Term Memory*.
- Bengio, Y., Simard, P. ve Frasconi, P. (1994). *Learning Long-Term Dependencies with Gradient Descent Is Difficult*.
- Cho, K. vd. (2014). *Learning Phrase Representations using RNN Encoder–Decoder*.

## Not Defteri

[`06_rnn_lstm.ipynb`](06_rnn_lstm.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
