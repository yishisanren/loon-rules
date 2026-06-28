# loon-rules

个人维护的 Loon 远程规则集。

## broker-hk.list

富途 + 老虎证券域名,用于「香港时延优选」分流。

**订阅链接:**

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/broker-hk.list
```

**Loon 引用方式**(`[Remote Rule]` 段):

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/broker-hk.list, policy=香港时延优选, tag=券商, enabled=true
```

## sing-box / homeproxy 订阅

`.list` 改动后,GitHub Actions 会自动把它转换成 sing-box `source` 格式的规则集,
输出到 `srs/`(由 `scripts/loon2singbox.py` 生成,请勿手改 `srs/` 下的文件)。

homeproxy「规则集」可直接远程订阅(类型 `remote`,格式 `source`):

```
https://raw.githubusercontent.com/yishisanren/loon-rules/main/srs/broker-hk.json
```

新增 `.list` 时无需额外配置,工作流会自动为每个 `*.list` 生成同名 `srs/<name>.json`。
