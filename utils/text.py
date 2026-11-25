"""Ders boyunca kullanılan, sıfırdan yazılmış metin işleme yardımcıları."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from typing import Iterable, Iterator

# Türkçe büyük/küçük harf eşlemesi: Python'un str.lower() yöntemi dile duyarlı değildir.
# "I".lower() Türkçedeki gibi "ı" değil "i" verir; "İ".lower() ise "i" + birleşen nokta (U+0307) üretir.
_TR_LOWER = str.maketrans({"I": "ı", "İ": "i"})


def normalize(text: str, lower: bool = True, form: str = "NFC", lang: str | None = None) -> str:
    """Metni Unicode'a göre normalize eder ve isteğe bağlı olarak küçük harfe çevirir.

    Parametreler
    ------------
    text : str
        Girdi dizesi.
    lower : bool, varsayılan True
        Küçük harfe çevirme uygulanıp uygulanmayacağı. Büyük/küçük harfe duyarlı
        görevler (NER, sözcük türü etiketleme, kod) için False yapın.
    form : str
        Unicode normalizasyon biçimi. Çoğu metin için ``NFC`` kullanın; uyumluluk
        ayrıştırması istiyorsanız (ör. tam genişlikli karakterler → ASCII) ``NFKC``.
    lang : str veya None
        ``"tr"`` (veya ``"az"``) verilirse Türkçe kuralları uygulanır: ``I → ı`` ve
        ``İ → i``. Varsayılan (None) dile duyarsız ``str.lower()`` davranışıdır.

    Örnekler
    --------
    >>> normalize("Iğdır İstanbul", lang="tr")
    'ığdır istanbul'
    """
    text = unicodedata.normalize(form, text)
    if lower:
        if lang in ("tr", "az"):
            text = text.translate(_TR_LOWER)
        text = text.lower()
    return text


_TOKEN_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def whitespace_tokenize(text: str) -> list[str]:
    """Basit taban çizgisi tokenizer'ı. Yalnızca karşılaştırma referansı olarak kullanın."""
    return text.split()


def regex_tokenize(text: str) -> list[str]:
    """Noktalama işaretlerini sözcüklerden ayıran, biraz daha akıllı bir tokenizer."""
    return _TOKEN_RE.findall(text)


def ngrams(tokens: Iterable[str], n: int) -> Iterator[tuple[str, ...]]:
    """Bir token dizisinden ardışık n-gramlar üretir."""
    tokens = list(tokens)
    for i in range(len(tokens) - n + 1):
        yield tuple(tokens[i : i + n])


def vocab_from_counts(counter: Counter, min_count: int = 1, max_size: int | None = None) -> dict[str, int]:
    """Bir Counter'dan deterministik bir token -> kimlik eşlemesi kurar.

    Ders boyunca kullanılan kurala göre ``<pad>``, ``<unk>``, ``<bos>``, ``<eos>``
    özel tokenları 0–3 kimliklerine ayrılmıştır. ``max_size`` özel tokenları da
    içeren toplam sözlük boyutudur; özel tokenlar her zaman korunur.
    """
    specials = ["<pad>", "<unk>", "<bos>", "<eos>"]
    vocab = {tok: i for i, tok in enumerate(specials)}
    items = [(t, c) for t, c in counter.most_common() if c >= min_count]
    if max_size is not None:
        items = items[: max(0, max_size - len(specials))]
    for tok, _ in items:
        if tok not in vocab:
            vocab[tok] = len(vocab)
    return vocab
