# Hafta 9 — Önceden Eğitilmiş Modeller: BERT, GPT, T5

> Üç mimari, üç hedef, üç felsefe. Her birini inceliyor, ön eğitim hedeflerini sıfırdan uyguluyor ve modellerin gerçekte ne öğrendiğini görmek için iç temsillerini sorguluyoruz. Gerçek önceden eğitilmiş kontrol noktalarıyla (Hugging Face) çalışmak alıştırmaların konusudur.

## Öğrenme Hedefleri

- Yalnızca kodlayıcı, yalnızca kod çözücü ve kodlayıcı–kod çözücü mimarilerini ve her birinin hangi görevlere uygun olduğunu açıklamak.
- Maskeli dil modellemeyi (MLM) ve nedensel dil modellemeyi uçtan uca uygulamak.
- T5 tarzı span bozmayı (span corruption) uygulamak.
- Bir BERT'i katman katman sorgulamak ve bağlamsal bilginin derinlikle ortaya çıktığı klasik bulguyu yeniden üretmek.

## Zorunlu Okumalar

- Devlin, J. vd. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*.
- Radford, A. vd. (2019). *Language Models are Unsupervised Multitask Learners* (GPT-2).
- Raffel, C. vd. (2020). *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer* (T5).
- Rogers, A., Kovaleva, O. ve Rumshisky, A. (2020). *A Primer in BERTology*.

## Not Defteri

[`09_pretrained_models.ipynb`](09_pretrained_models.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
