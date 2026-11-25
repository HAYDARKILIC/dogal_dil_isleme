# Veri Kümeleri

Ders boyunca başvurulan veri kümelerinin seçilmiş bir kaydı.

> **Önemli:** 1–12. hafta not defterleri, çevrimdışı ve tekrarlanabilir çalışabilmeleri için **kendi içlerinde tanımlanmış küçük oyuncak derlemler** kullanır; aşağıdaki veri kümelerinin hiçbiri not defterlerini çalıştırmak için gerekli değildir. Bu veri kümeleri alıştırmalar ve bitirme projesi içindir. Depoda hiçbir veri kümesi dosyası bulunmaz.

| Hafta | Veri kümesi | Kaynak | Amaç |
|------|---------|--------|---------|
| 01 | Reuters-21578, Brown Derlemi | NLTK | İngilizcenin deneysel entropisi |
| 02 | WikiText-103 | HF `wikitext` | BPE / WordPiece / Unigram eğitimi |
| 03 | 20 Newsgroups, IMDb | sklearn / HF `imdb` | Sözcük torbası / TF-IDF sınıflandırması |
| 04 | text8, Wikipedia dökümü (küçük) | mattmahoney.net | word2vec / GloVe / fastText eğitimi |
| 05 | Penn Treebank | HF `ptb_text_only` | Sinirsel dil modelleme |
| 06 | Tiny Shakespeare | char-rnn sürümü | Karakter düzeyinde dil modeli |
| 07 | Multi30K | HF `bentrevett/multi30k` | İngilizce ↔ Almanca çeviri |
| 08 | Multi30K | (aynı) | Transformer ile çeviri |
| 09 | GLUE, SQuAD | HF `glue`, HF `squad` | Önceden eğitilmiş kodlayıcıları sondalama |
| 10 | Alpaca, OpenAssistant (örneklem) | HF | Talimat ayarı, DPO |
| 11 | Natural Questions, MS MARCO (örneklem) | HF | RAG değerlendirmesi |
| 12 | Projeye özgü | — | Bitirme projesi |

Türkçe çalışmak isteyenler için bazı başlangıç noktaları: TS Corpus, OSCAR ve CulturaX'in Türkçe alt kümeleri, Türkçe Wikipedia dökümü.

## Yükleme kuralları

```python
from datasets import load_dataset

ds = load_dataset("wikitext", "wikitext-103-raw-v1")
```

Elle indirme gerektiren veri kümeleri için (ör. Multi30K yansıları zaman zaman değişir) güncel kaynağı Hugging Face Hub'da veri kümesinin sayfasından kontrol edin.

## Önerilen depolama düzeni

İndirdiğiniz verileri şu düzende tutmanız önerilir (bu klasörler `.gitignore` ile sürüm kontrolünün dışında tutulur):

```
datasets/
├── raw/        # indirilen kaynak dosyalar
├── cache/      # HF datasets önbelleği
└── samples/    # not defterlerinde kullanmak isteyebileceğiniz küçük örnekler
```
