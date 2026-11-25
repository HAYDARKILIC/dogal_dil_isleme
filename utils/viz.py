"""Ders not defterlerinde kullanılan çizim yardımcıları."""
from __future__ import annotations

from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np


def plot_attention(matrix: np.ndarray, x_labels: Sequence[str], y_labels: Sequence[str], title: str = "Dikkat") -> plt.Figure:
    """Bir dikkat ağırlık matrisini ısı haritası olarak görselleştirir."""
    fig, ax = plt.subplots(figsize=(max(6, len(x_labels) * 0.6), max(4, len(y_labels) * 0.5)))
    im = ax.imshow(matrix, aspect="auto", cmap="viridis")
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels, rotation=45, ha="right")
    ax.set_yticks(range(len(y_labels)))
    ax.set_yticklabels(y_labels)
    ax.set_title(title)
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    return fig


def plot_training_curves(history: dict[str, list[float]], title: str = "Eğitim") -> plt.Figure:
    """`history` içindeki her anahtar için bir eğri çizer."""
    fig, ax = plt.subplots(figsize=(10, 5))
    for name, values in history.items():
        ax.plot(values, label=name)
    ax.set_xlabel("adım")
    ax.set_ylabel("değer")
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    return fig


def project_embeddings_2d(emb: np.ndarray, method: str = "pca") -> np.ndarray:
    """Görselleştirme için (N, d) boyutlu bir gömme matrisini 2B'ye izdüşürür.

    Varsayılan PCA'dır (ucuz, deterministik). İlgili kütüphane kurulu olduğunda
    doğrusal olmayan görselleştirme için `t-SNE` veya `UMAP`'e geçin.
    """
    if method == "pca":
        x = emb - emb.mean(axis=0, keepdims=True)
        u, s, vt = np.linalg.svd(x, full_matrices=False)
        return (u[:, :2] * s[:2])
    raise ValueError(f"Desteklenmeyen yöntem: {method!r}")
