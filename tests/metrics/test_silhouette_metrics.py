from tests.common import *


def test_silhouette(adata_pca):
    score = scib.me.silhouette(
        adata_pca,
        group_key='celltype',
        embed='X_pca',
        scale=True
    )
    LOGGER.info(f"score: {score}")
    assert 0 <= score <= 1


def test_silhouette_batch(adata_pca):
    score = scib.me.silhouette_batch(
        adata_pca,
        batch_key='batch',
        group_key='celltype',
        embed='X_pca',
        scale=True,
        verbose=False
    )
    LOGGER.info(f"score: {score}")
    assert 0 <= score <= 1


def test_isolated_labels_silhouette(adata_pca):
    score = scib.me.isolated_labels(
        adata_pca,
        label_key='celltype',
        batch_key='batch',
        embed='X_pca',
        cluster=False,
        verbose=True
    )
    LOGGER.info(f"score: {score}")
    assert score <= 1
    assert score >= 0
