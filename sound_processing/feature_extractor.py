# -*- coding: utf-8 -*-
"""feature_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wpl4nex_ONCaLu3AX6B9spxNBYrO2alD
"""

# Commented out IPython magic to ensure Python compatibility.
import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import os
import sklearn

class FeatureExtractor:
  """
      Extract features such as spectral centroid, spectral rolloff, spectral bandwidth, spectral flatness, rmse, MFCC and chroma feature.

      FeatureExtractor Args:

      sr (int): sampling rate

      Returns:
      array: extracted features
  """

  def __init__(self):
    self.extracted_features = []

  def spectral_centroid(self, x, sr):
    return librosa.feature.spectral_centroid(x, sr=sr)

  def spectral_rolloff(self, x, sr):
    return librosa.feature.spectral_rolloff(x, sr=sr)

  def spectral_bandwidth(self, x, sr):
    return librosa.feature.spectral_bandwidth(x, sr=sr)

  def spectral_flatness(self, x):
    return librosa.feature.spectral_flatness(x)

  def rmse(self, x, hop_length):
    return librosa.feature.rmse(x, hop_length=hop_length, center=True)

  def mfcss(self, x, sr):
    return librosa.feature.mfcc(x, sr=sr)

  def chromas(self, x, sr, hop_length):
    return librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)

  def features(self, x, sr, hop_length):
    self.extracted_features.extend(self.spectral_centroid(x=x, sr=sr))
    self.extracted_features.extend(self.spectral_rolloff(x=x, sr=sr))
    self.extracted_features.extend(self.spectral_bandwidth(x=x, sr=sr))
    self.extracted_features.extend(self.spectral_flatness(x=x))
    self.extracted_features.extend(self.rmse(x=x, hop_length=hop_length))
    self.extracted_features.extend(self.mfcss(x=x, sr=sr))
    self.extracted_features.extend(self.chromas(x=x, sr=sr, hop_length=hop_length))

    return np.asarray(self.extracted_features)