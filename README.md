# Doğal Dil İşleme: Temel İlkelerden Modern Büyük Dil Modellerine

Karakter düzeyinde metin işlemeden başlayıp talimatla ayarlanmış büyük dil modellerine (LLM) kadar tüm NLP yığınını sıfırdan yeniden kuran, 12 haftalık, araştırma düzeyinde bir ders. Her kavram matematiksel olarak türetilir, saf **NumPy** veya **PyTorch** ile uygulanır (ilgili temel öğe tam olarak anlaşılana kadar üst düzey NLP kütüphaneleri kullanılmaz) ve gerçek veri kümeleri üzerinde sınanır. Klasik istatistiksel NLP ile modern transformer tabanlı ekosistem arasında bir köprüdür.

---

## Ders Felsefesi

1. **İçe aktarmadan önce türet.** TF-IDF'ten çok başlı dikkate kadar her algoritma, üretim düzeyindeki karşılığı (scikit-learn, Hugging Face, PyTorch yerleşikleri) kullanılmadan önce sıfırdan uygulanır.
2. **Matematikten taviz verilmez.** Her not defteri temeldeki doğrusal cebir, olasılık veya bilgi kuramıyla açılır, ardından bunu koda dönüştürür.
3. **Sezgi yerine ölçüm.** Her iddia çalıştırılabilir bir deneyle desteklenir: gradyanlar sayısal olarak doğrulanır, modeller taban çizgileriyle karşılaştırılır ve uygun yerlerde endüstri standardı bir referansla (ör. Hugging Face `tokenizers`; `utils.metrics` için `sacrebleu` ve `rouge-score`) kıyaslanır. Daha büyük ölçekli kıyaslamalar (gensim, fastText, Hugging Face Transformers) alıştırmaların konusudur.
4. **Makaleyi oku.** Her hafta bir ya da iki temel makaleye dayanır. Not defterleri makalenin ana fikirlerini küçük, çevrimdışı çalışan deneylerle yeniden kurar.

---

## Bir Bakışta Müfredat

| Hafta | Konu | Ana Not Defteri | Dayanak Makaleler |
|------|-------|------------------|---------------|
| 01 | Temeller: dilbilim, olasılık, bilgi kuramı | `01_foundations.ipynb` | Shannon (1948), Manning ve Schütze Bölüm 2 |
| 02 | Metin işleme: tokenizasyon, normalizasyon, BPE, WordPiece | `02_tokenization.ipynb` | Sennrich vd. (2016), Kudo (2018) |
| 03 | Klasik temsiller: BoW, TF-IDF, n-gramlar, LSA | `03_classical_representations.ipynb` | Salton (1975), Deerwester (1990) |
| 04 | Sözcük gömmeleri: word2vec, GloVe, fastText, değerlendirme | `04_word_embeddings.ipynb` | Mikolov vd. (2013), Pennington vd. (2014) |
| 05 | Dil modelleri: n-gram → sinirsel → perpleksite | `05_language_models.ipynb` | Bengio vd. (2003) |
| 06 | BPTT ile sıfırdan RNN, LSTM ve GRU | `06_rnn_lstm.ipynb` | Hochreiter ve Schmidhuber (1997) |
| 07 | Seq2Seq ve dikkat mekanizmaları | `07_seq2seq_attention.ipynb` | Sutskever vd. (2014), Bahdanau vd. (2015) |
| 08 | Uçtan uca uygulanan Transformer | `08_transformer.ipynb` | Vaswani vd. (2017) |
| 09 | Önceden eğitilmiş modeller: BERT, GPT, T5 — mimariler ve hedefler | `09_pretrained_models.ipynb` | Devlin vd. (2019), Radford vd. (2019) |
| 10 | İnce ayar, PEFT, LoRA, RLHF, DPO | `10_finetuning_alignment.ipynb` | Hu vd. (2021), Ouyang vd. (2022), Rafailov vd. (2023) |
| 11 | Modern LLM uygulamaları: RAG, araç kullanımı, değerlendirme düzenekleri | `11_modern_llm_applications.ipynb` | Lewis vd. (2020) |
| 12 | Bitirme projesi: alana özgü bir dil modeli kur, ince ayar yap, değerlendir ve dağıt | `12_capstone.ipynb` | — |

---

## Ön Koşullar

- **Python** (orta düzey): NumPy, temel PyTorch, sanal ortamlar.
- **Matematik**: doğrusal cebir, çok değişkenli kalkülüs, olasılık (bu portföydeki `probability` ve `statistics` depolarına bakın).
- **Derin öğrenme** (önerilir): gerekli arka plan `deep_learning` deposunda ele alınmıştır.

---

## Depo Yapısı

```
nlp_course/
├── week01_foundations/
│   ├── 01_foundations.ipynb
│   └── README.md
├── week02_text_processing/
│   ├── 02_tokenization.ipynb
│   └── README.md
├── ... (hafta 03–12)
├── datasets/
│   └── README.md          # Seçilmiş veri kümesi kaydı
├── utils/
│   ├── __init__.py
│   ├── text.py            # Sıfırdan metin yardımcıları
│   ├── metrics.py         # BLEU, ROUGE, perpleksite vb.
│   └── viz.py             # Dikkat haritaları, gömme izdüşümleri
├── assets/
│   └── rubric.md          # Bitirme projesi değerlendirme ölçütleri
├── requirements.txt
├── environment.yml
├── .gitignore
└── LICENSE
```

---

## Ortam

```bash
# conda ile
conda env create -f environment.yml
conda activate nlp-course

# Ya da pip ile
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

**Not defterleri** yalnızca `numpy`, `matplotlib`, `torch` ve `tokenizers` gerektirir, internet bağlantısı istemez ve CPU'da her biri bir dakikadan kısa sürede baştan sona çalışır. `requirements.txt` içindeki diğer paketler alıştırmalar ve bitirme projesi içindir.

Alıştırmalar ve bitirme projesi için önerilen donanım: 1–9. haftalar için tek bir tüketici sınıfı GPU (≥ 8 GB VRAM) yeterlidir. 10–12. haftalar ≥ 24 GB VRAM'den veya bir bulut sunucusundan yararlanır.

---

## Bu Ders Nasıl Kullanılır

Her haftanın klasöründe şunlar bulunur:

- **Ana not defteri** — ders anlatımı, türetmeler ve kod.
- Öğrenme hedeflerini, okuma listesini ve alıştırma setini içeren bir **`README.md`**.

Not defterini hücre hücre ilerleyerek çalışın. Sıfırdan uygulamayı atlamayın — üretim kütüphanesi çağrıları, temel öğeyi kendiniz kurduktan *sonra* gelir.

---

## Atıf

Bu materyal öğretiminizde veya araştırmanızda işinize yararsa:

```bibtex
@misc{kilic2026nlp,
  author = {Kılıç, Haydar},
  title  = {Doğal Dil İşleme: Temel İlkelerden Modern Büyük Dil Modellerine},
  year   = {2026},
  url    = {https://github.com/HAYDARKILIC/nlp_course}
}
```

---

## Lisans

MIT. Bkz. `LICENSE`.
