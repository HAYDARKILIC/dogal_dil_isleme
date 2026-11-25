# Hafta 8 — Uçtan Uca Kurulan Transformer

> Her şeyi değiştiren mimari. Vaswani vd. (2017) Transformer'ının tamamını — çok başlı dikkat, konumsal kodlama, artık bağlantılar, katman normalizasyonu, hepsini — `nn.Transformer` kullanmadan PyTorch ile uyguluyoruz.

## Öğrenme Hedefleri

- Ölçekli nokta çarpımı dikkatini türetmek ve $\sqrt{d_k}$ ölçeklemesini açıklamak.
- Çok başlı dikkati PyTorch ile sıfırdan uygulamak.
- Sinüzoidal konumsal kodlamayı uygulamak ve modern alternatifler olarak RoPE ile ALiBi'yi tartışmak.
- Tam bir kodlayıcı–kod çözücü Transformer'ı bir araya getirip eğitmek.

## Zorunlu Okumalar

- Vaswani, A. vd. (2017). *Attention Is All You Need*.
- Su, J. vd. (2021). *RoFormer: Enhanced Transformer with Rotary Position Embedding*.
- Press, O., Smith, N. A. ve Lewis, M. (2022). *Train Short, Test Long: Attention with Linear Biases*.

## Not Defteri

[`08_transformer.ipynb`](08_transformer.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
