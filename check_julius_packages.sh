#!/bin/bash

# 公式ドキュメントのインストール方法に記載のライブラリが入っているか確認
# https://github.com/julius-speech/julius#1-build-latest-julius

packages=("build-essential" "zlib1g-dev" "libsdl2-dev" "libasound2-dev")

for package in "${packages[@]}"; do
  if dpkg-query -W -f='${Status}' $package 2>/dev/null | grep -q "ok installed"; then
    echo "$package is installed."
  else
    echo "$package is NOT installed."
  fi
done