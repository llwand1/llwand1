#!/usr/bin/env bash
# 逐个探活 README 里用到的每一个徽章 URL —— 死图不能进交付物。
# 清单必须与 README.md 当前实际引用保持一致（改 README 后同步这里）。
set -u
PROBE=(
  "https://img.shields.io/badge/%E7%BA%BF%E4%B8%8A%E5%AE%9E%E4%BE%8B-11wand.com-007AFF?style=for-the-badge&logo=googlechrome&logoColor=white"
  "https://img.shields.io/badge/SOURCE-studentbuddy--v2-181717?style=for-the-badge&logo=github&logoColor=white"
  "https://komarev.com/ghpvc/?username=llwand1&label=VIEWS&color=007aff&style=for-the-badge"
  "https://img.shields.io/github/v/release/llwand1/studentbuddy-v2?label=release&color=8a63f6&style=flat-square"
  "https://img.shields.io/github/last-commit/llwand1/studentbuddy-v2?label=last+commit&color=007aff&style=flat-square"
  "https://img.shields.io/github/license/llwand1/studentbuddy-v2?label=license&color=0f9d58&style=flat-square"
  "https://img.shields.io/github/stars/llwand1/studentbuddy-v2?label=stars&color=f5a623&style=flat-square"
  "https://img.shields.io/github/issues/llwand1/studentbuddy-v2?label=open+issues&color=8a63f6&style=flat-square"
  "https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"
  "https://img.shields.io/badge/Node.js%2022%2B-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white"
  "https://img.shields.io/badge/React%2018-087EA4?style=flat-square&logo=react&logoColor=white"
  "https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white"
  "https://img.shields.io/badge/SQLite%20WAL-003B57?style=flat-square&logo=sqlite&logoColor=white"
  "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"
)
fail=0
for u in "${PROBE[@]}"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 20 "$u")
  if [ "$code" = "200" ]; then
    echo "OK   $code  ${u:0:58}..."
  else
    echo "FAIL $code  $u"
    fail=$((fail + 1))
  fi
done
echo "-----"
echo "失败数: $fail / ${#PROBE[@]}"
