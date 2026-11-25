# Hafta 10 — İnce Ayar, PEFT ve Hizalama

> Önceden eğitilmiş bir model, verimli biçimde ve insan tercihleriyle hizalı olarak nasıl işe yarar bir şeye dönüştürülür? Tam ince ayarı, LoRA'yı, talimat ayarını, RLHF'yi ve DPO'yu ele alıyoruz.

## Öğrenme Hedefleri

- Küçük bir Transformer'a bir sınıflandırma görevinde ince ayar yapmak ve felaket boyutunda unutmayı (catastrophic forgetting) ölçmek.
- Düşük Ranklı Uyarlamayı (LoRA) türetmek, sıfırdan bir modül olarak uygulamak ve aynı görevde tam ince ayarla karşılaştırmak.
- Talimat ayarı için veri hattını kurmak (eğitim döngüsü 4. haftadakiyle aynıdır).
- RLHF hedefini ve DPO kaybını türetmek; DPO'yu oyuncak bir politika üzerinde uçtan uca eğitmek.

## Zorunlu Okumalar

- Hu, E. vd. (2021). *LoRA: Low-Rank Adaptation of Large Language Models*.
- Ouyang, L. vd. (2022). *Training Language Models to Follow Instructions with Human Feedback*.
- Rafailov, R. vd. (2023). *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*.
- Christiano, P. vd. (2017). *Deep Reinforcement Learning from Human Preferences*.

## Not Defteri

[`10_finetuning_alignment.ipynb`](10_finetuning_alignment.ipynb) dosyasını açın.

## Alıştırmalar

Alıştırma seti not defterinin son bölümündedir. Önerilen süre: 4–6 saat.

## Daha İleri

- Derste kullanılan değerlendirme ölçütleri için depo kökündeki `assets/` klasörüne göz atın.
- `utils/` paketi ortak metin, metrik ve görselleştirme yardımcılarını içerir.
